"""Tests for command functions."""

import time

from bubbletea.commands import (
    batch, sequence, quit_cmd, interrupt, suspend, clear_screen,
    printf, println, set_clipboard, read_clipboard,
    request_window_size, request_cursor_position,
    request_background_color, request_foreground_color,
    request_cursor_color, request_terminal_version,
    request_capability, every, tick, raw,
    set_primary_clipboard, read_primary_clipboard,
)
from bubbletea.messages import (
    QuitMsg, InterruptMsg, SuspendMsg, ClearScreenMsg,
    ClipboardMsg, WindowSizeMsg, RawMsg,
)


class TestSimpleCommands:
    def test_quit_returns_quit_msg(self):
        msg = quit_cmd()
        assert isinstance(msg, QuitMsg)

    def test_interrupt_returns_interrupt_msg(self):
        msg = interrupt()
        assert isinstance(msg, InterruptMsg)

    def test_suspend_returns_suspend_msg(self):
        msg = suspend()
        assert isinstance(msg, SuspendMsg)

    def test_clear_screen_returns_msg(self):
        msg = clear_screen()
        assert isinstance(msg, ClearScreenMsg)


class TestClipboardCommands:
    def test_set_clipboard_returns_cmd(self):
        cmd = set_clipboard("hello")
        assert callable(cmd)

    def test_set_primary_clipboard_returns_cmd(self):
        cmd = set_primary_clipboard("hello")
        assert callable(cmd)

    def test_read_clipboard_returns_msg(self):
        msg = read_clipboard()
        assert msg is not None

    def test_read_primary_clipboard_returns_msg(self):
        msg = read_primary_clipboard()
        assert msg is not None


class TestBatchSequence:
    def test_batch_combines_commands(self):
        cmd = batch(quit_cmd, interrupt)
        assert callable(cmd)

    def test_batch_empty(self):
        cmd = batch()
        result = cmd()
        assert result is not None

    def test_sequence_chains_commands(self):
        cmd = sequence(quit_cmd, interrupt)
        assert callable(cmd)


class TestOutputCommands:
    def test_printf_returns_cmd(self):
        cmd = printf("hello %s", "world")
        assert callable(cmd)

    def test_println_returns_cmd(self):
        cmd = println("hello")
        assert callable(cmd)


class TestTimingCommands:
    def test_tick_returns_cmd(self):
        cmd = tick(1.0, lambda t: QuitMsg())
        assert callable(cmd)

    def test_every_returns_cmd(self):
        cmd = every(1.0, lambda t: QuitMsg())
        assert callable(cmd)


class TestRequestCommands:
    def test_request_window_size(self):
        msg = request_window_size()
        assert msg is not None

    def test_request_cursor_position(self):
        msg = request_cursor_position()
        assert msg is not None

    def test_request_background_color(self):
        msg = request_background_color()
        assert msg is not None

    def test_request_foreground_color(self):
        msg = request_foreground_color()
        assert msg is not None

    def test_request_cursor_color(self):
        msg = request_cursor_color()
        assert msg is not None

    def test_request_terminal_version(self):
        msg = request_terminal_version()
        assert msg is not None

    def test_request_capability(self):
        cmd = request_capability("rgb")
        assert callable(cmd)


class TestRawCommand:
    def test_raw_returns_cmd(self):
        cmd = raw(b"\x1b[0m")
        assert callable(cmd)
