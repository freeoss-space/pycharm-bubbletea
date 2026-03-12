"""Command functions mirroring Bubble Tea v2 Cmd type and helpers."""

from __future__ import annotations

import time
import threading
from typing import Any, Callable, Optional

from bubbletea.messages import (
    Msg, QuitMsg, InterruptMsg, SuspendMsg, ClearScreenMsg,
    ClipboardMsg, BatchMsg, RawMsg, CapabilityMsg,
)

# Cmd is a callable returning a Msg
Cmd = Optional[Callable[[], Msg]]


# --- Simple msg-producing functions (match Go's func Quit() Msg pattern) ---

def quit_cmd() -> QuitMsg:
    """Return a QuitMsg to exit the program."""
    return QuitMsg()


def interrupt() -> InterruptMsg:
    """Return an InterruptMsg."""
    return InterruptMsg()


def suspend() -> SuspendMsg:
    """Return a SuspendMsg."""
    return SuspendMsg()


def clear_screen() -> ClearScreenMsg:
    """Return a ClearScreenMsg."""
    return ClearScreenMsg()


# --- Request functions (return marker msgs for the runtime) ---

class _RequestMsg:
    """Marker for terminal query requests."""
    def __init__(self, kind: str):
        self.kind = kind


def request_window_size() -> Msg:
    return _RequestMsg("window_size")


def request_cursor_position() -> Msg:
    return _RequestMsg("cursor_position")


def request_background_color() -> Msg:
    return _RequestMsg("background_color")


def request_foreground_color() -> Msg:
    return _RequestMsg("foreground_color")


def request_cursor_color() -> Msg:
    return _RequestMsg("cursor_color")


def request_terminal_version() -> Msg:
    return _RequestMsg("terminal_version")


# --- Clipboard ---

class _ClipboardSetMsg:
    def __init__(self, content: str, primary: bool = False):
        self.content = content
        self.primary = primary


class _ClipboardReadMsg:
    def __init__(self, primary: bool = False):
        self.primary = primary


def set_clipboard(s: str) -> Cmd:
    """Return a Cmd that sets the system clipboard."""
    return lambda: _ClipboardSetMsg(s)


def set_primary_clipboard(s: str) -> Cmd:
    """Return a Cmd that sets the primary clipboard."""
    return lambda: _ClipboardSetMsg(s, primary=True)


def read_clipboard() -> Msg:
    """Return a msg requesting clipboard content."""
    return _ClipboardReadMsg()


def read_primary_clipboard() -> Msg:
    """Return a msg requesting primary clipboard content."""
    return _ClipboardReadMsg(primary=True)


# --- Capability request ---

def request_capability(s: str) -> Cmd:
    """Return a Cmd that requests a terminal capability."""
    return lambda: CapabilityMsg(content=s)


# --- Batch & Sequence ---

def batch(*cmds: Cmd) -> Cmd:
    """Combine multiple commands to run concurrently."""
    def _batch() -> BatchMsg:
        return BatchMsg(commands=list(cmds))
    return _batch


def sequence(*cmds: Cmd) -> Cmd:
    """Chain commands to run sequentially."""
    def _sequence() -> BatchMsg:
        return BatchMsg(commands=list(cmds))
    return _sequence


# --- Timing ---

def tick(duration: float, fn: Callable[[float], Msg]) -> Cmd:
    """Return a Cmd that fires once after *duration* seconds."""
    def _tick() -> Msg:
        time.sleep(duration)
        return fn(time.time())
    return _tick


def every(duration: float, fn: Callable[[float], Msg]) -> Cmd:
    """Return a Cmd that fires repeatedly every *duration* seconds."""
    def _every() -> Msg:
        time.sleep(duration)
        return fn(time.time())
    return _every


# --- Output ---

class _PrintMsg:
    def __init__(self, text: str):
        self.text = text


def printf(template: str, *args: Any) -> Cmd:
    """Return a Cmd that prints formatted text."""
    return lambda: _PrintMsg(template % args)


def println(*args: Any) -> Cmd:
    """Return a Cmd that prints a line."""
    return lambda: _PrintMsg(" ".join(str(a) for a in args) + "\n")


# --- Raw ---

def raw(data: Any) -> Cmd:
    """Return a Cmd that sends raw data."""
    return lambda: RawMsg(data=data)
