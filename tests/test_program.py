"""Tests for Program."""

import io

from bubbletea.program import Program
from bubbletea.model import Model
from bubbletea.view import View
from bubbletea.messages import QuitMsg, KeyPressMsg
from bubbletea.options import with_input, with_output, with_fps, without_renderer


class SimpleModel(Model):
    def __init__(self, done=False):
        self.done = done

    def init(self):
        return None

    def update(self, msg):
        if isinstance(msg, QuitMsg):
            return SimpleModel(done=True), None
        return self, None

    def view(self):
        return View("simple")


class TestProgram:
    def test_create_program(self):
        m = SimpleModel()
        p = Program(m)
        assert p is not None

    def test_create_with_options(self):
        m = SimpleModel()
        inp = io.StringIO()
        out = io.StringIO()
        p = Program(m, with_input(inp), with_output(out), without_renderer())
        assert p is not None

    def test_send_message(self):
        m = SimpleModel()
        p = Program(m, without_renderer())
        p.send(QuitMsg())

    def test_quit(self):
        m = SimpleModel()
        p = Program(m, without_renderer())
        p.quit()

    def test_kill(self):
        m = SimpleModel()
        p = Program(m, without_renderer())
        p.kill()

    def test_printf(self):
        out = io.StringIO()
        m = SimpleModel()
        p = Program(m, with_output(out), without_renderer())
        p.printf("hello %s", "world")

    def test_println(self):
        out = io.StringIO()
        m = SimpleModel()
        p = Program(m, with_output(out), without_renderer())
        p.println("hello")
