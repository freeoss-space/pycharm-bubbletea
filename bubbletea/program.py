"""Program runner mirroring Bubble Tea v2 Program type."""

from __future__ import annotations

import sys
import threading
import queue
from typing import Any, IO, Optional

from bubbletea.model import Model
from bubbletea.view import View
from bubbletea.messages import QuitMsg, InterruptMsg
from bubbletea.options import ProgramOption
from bubbletea.errors import ProgramKilledError, InterruptedError


class Program:
    """Manages the event loop for a Bubble Tea application.

    Create with ``Program(model, *options)`` and call ``run()`` to start.
    """

    def __init__(self, model: Model, *opts: ProgramOption):
        self._model = model
        self._msgs: queue.Queue = queue.Queue()
        self._done = threading.Event()
        self._killed = False

        # Apply options
        self._output: IO = sys.stdout
        self._input: IO = sys.stdin
        self._renderer_enabled = True
        self._fps = 60
        self._filter = None
        self._catch_panics = True

        for opt in opts:
            match opt.key:
                case "input":
                    self._input = opt.value
                case "output":
                    self._output = opt.value
                case "renderer":
                    self._renderer_enabled = opt.value
                case "fps":
                    self._fps = opt.value
                case "filter":
                    self._filter = opt.value
                case "catch_panics":
                    self._catch_panics = opt.value

    def run(self) -> Model:
        """Run the program's event loop, returning the final model."""
        cmd = self._model.init()
        if cmd is not None:
            self._dispatch_cmd(cmd)

        while not self._done.is_set():
            try:
                msg = self._msgs.get(timeout=0.05)
            except queue.Empty:
                continue

            if self._filter:
                msg = self._filter(self._model, msg)

            if isinstance(msg, QuitMsg):
                self._done.set()
                break

            if isinstance(msg, InterruptMsg):
                self._done.set()
                raise InterruptedError("program was interrupted")

            self._model, cmd = self._model.update(msg)

            if self._renderer_enabled:
                view = self._model.view()
                self._output.write(str(view))
                self._output.flush()

            if cmd is not None:
                self._dispatch_cmd(cmd)

        return self._model

    def send(self, msg: Any) -> None:
        """Send a message to the program."""
        self._msgs.put(msg)

    def quit(self) -> None:
        """Send a QuitMsg to stop the program."""
        self.send(QuitMsg())

    def kill(self) -> None:
        """Immediately stop the program."""
        self._killed = True
        self._done.set()

    def wait(self) -> None:
        """Block until the program exits."""
        self._done.wait()

    def release_terminal(self) -> None:
        """Release terminal resources."""

    def restore_terminal(self) -> None:
        """Restore terminal to its previous state."""

    def printf(self, template: str, *args: Any) -> None:
        """Print formatted text to the program's output."""
        self._output.write(template % args)
        self._output.flush()

    def println(self, *args: Any) -> None:
        """Print a line to the program's output."""
        self._output.write(" ".join(str(a) for a in args) + "\n")
        self._output.flush()

    def _dispatch_cmd(self, cmd: Any) -> None:
        """Execute a command in a background thread."""
        if callable(cmd):
            def _run():
                msg = cmd()
                if msg is not None:
                    self.send(msg)
            threading.Thread(target=_run, daemon=True).start()
