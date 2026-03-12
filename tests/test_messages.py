"""Tests for message types."""

from bubbletea.messages import (
    QuitMsg, InterruptMsg, SuspendMsg, ResumeMsg,
    FocusMsg, BlurMsg,
    KeyPressMsg, KeyReleaseMsg,
    MouseClickMsg, MouseMotionMsg, MouseReleaseMsg, MouseWheelMsg,
    WindowSizeMsg, CursorPositionMsg,
    ForegroundColorMsg, BackgroundColorMsg, CursorColorMsg,
    ColorProfileMsg, ClipboardMsg,
    PasteMsg, PasteStartMsg, PasteEndMsg,
    ClearScreenMsg, BatchMsg,
    KeyboardEnhancementsMsg, CapabilityMsg,
    ModeReportMsg, TerminalVersionMsg, EnvMsg, RawMsg,
)
from bubbletea.mouse import Mouse, MouseButton
from bubbletea.modifiers import KeyMod


class TestSimpleMessages:
    def test_quit_msg(self):
        msg = QuitMsg()
        assert isinstance(msg, QuitMsg)

    def test_interrupt_msg(self):
        msg = InterruptMsg()
        assert isinstance(msg, InterruptMsg)

    def test_suspend_resume(self):
        assert SuspendMsg() is not None
        assert ResumeMsg() is not None

    def test_focus_blur(self):
        assert FocusMsg() is not None
        assert BlurMsg() is not None

    def test_paste_messages(self):
        p = PasteMsg(content="hello")
        assert str(p) == "hello"
        assert PasteStartMsg() is not None
        assert PasteEndMsg() is not None

    def test_clear_screen(self):
        assert ClearScreenMsg() is not None


class TestKeyMessages:
    def test_key_press_creation(self):
        k = KeyPressMsg(code=ord("a"), text="a")
        assert k.code == ord("a")
        assert k.text == "a"

    def test_key_press_string(self):
        k = KeyPressMsg(code=ord("a"), text="a")
        assert str(k) == "a"

    def test_key_press_with_modifier(self):
        k = KeyPressMsg(code=ord("c"), text="", mod=KeyMod.CTRL)
        assert k.mod == KeyMod.CTRL
        assert "ctrl" in k.keystroke().lower()

    def test_key_release(self):
        k = KeyReleaseMsg(code=ord("a"), text="a")
        assert k.code == ord("a")
        assert str(k) == "a"

    def test_key_repeat(self):
        k = KeyPressMsg(code=ord("a"), text="a", is_repeat=True)
        assert k.is_repeat is True

    def test_shifted_code(self):
        k = KeyPressMsg(code=ord("a"), text="A", shifted_code=ord("A"))
        assert k.shifted_code == ord("A")

    def test_base_code(self):
        k = KeyPressMsg(code=ord("a"), text="a", base_code=ord("a"))
        assert k.base_code == ord("a")


class TestMouseMessages:
    def test_mouse_click(self):
        m = Mouse(x=1, y=2, button=MouseButton.LEFT)
        msg = MouseClickMsg(mouse=m)
        assert msg.mouse.x == 1
        assert msg.mouse.y == 2

    def test_mouse_motion(self):
        m = Mouse(x=5, y=5, button=MouseButton.NONE)
        msg = MouseMotionMsg(mouse=m)
        assert msg.mouse.x == 5

    def test_mouse_release(self):
        m = Mouse(x=1, y=1, button=MouseButton.LEFT)
        msg = MouseReleaseMsg(mouse=m)
        assert msg.mouse.button == MouseButton.LEFT

    def test_mouse_wheel(self):
        m = Mouse(x=0, y=0, button=MouseButton.WHEEL_UP)
        msg = MouseWheelMsg(mouse=m)
        assert msg.mouse.button == MouseButton.WHEEL_UP

    def test_mouse_msg_string(self):
        m = Mouse(x=1, y=2, button=MouseButton.LEFT)
        msg = MouseClickMsg(mouse=m)
        assert isinstance(str(msg), str)


class TestWindowSizeMsg:
    def test_creation(self):
        msg = WindowSizeMsg(width=80, height=24)
        assert msg.width == 80
        assert msg.height == 24


class TestCursorPositionMsg:
    def test_creation(self):
        msg = CursorPositionMsg(x=10, y=5)
        assert msg.x == 10
        assert msg.y == 5


class TestColorMessages:
    def test_foreground_color(self):
        msg = ForegroundColorMsg(color="#ff0000")
        assert msg.color == "#ff0000"
        assert isinstance(str(msg), str)

    def test_background_color(self):
        msg = BackgroundColorMsg(color="#000000")
        assert msg.color == "#000000"

    def test_cursor_color(self):
        msg = CursorColorMsg(color="#ffffff")
        assert msg.color == "#ffffff"

    def test_is_dark(self):
        dark = ForegroundColorMsg(color="#000000")
        assert dark.is_dark() is True
        light = ForegroundColorMsg(color="#ffffff")
        assert light.is_dark() is False

    def test_color_profile(self):
        msg = ColorProfileMsg(profile="truecolor")
        assert msg.profile == "truecolor"


class TestClipboardMsg:
    def test_creation(self):
        msg = ClipboardMsg(content="text", selection=0)
        assert msg.content == "text"
        assert msg.clipboard() == 0
        assert str(msg) == "text"


class TestBatchMsg:
    def test_creation(self):
        msgs = BatchMsg(commands=[lambda: QuitMsg()])
        assert len(msgs.commands) == 1


class TestKeyboardEnhancementsMsg:
    def test_supports_key_disambiguation(self):
        msg = KeyboardEnhancementsMsg(flags=1)
        assert msg.supports_key_disambiguation() is True

    def test_supports_event_types(self):
        msg = KeyboardEnhancementsMsg(flags=2)
        assert msg.supports_event_types() is True


class TestCapabilityMsg:
    def test_creation(self):
        msg = CapabilityMsg(content="rgb")
        assert str(msg) == "rgb"


class TestModeReportMsg:
    def test_creation(self):
        msg = ModeReportMsg(mode=1, value=1)
        assert msg.mode == 1
        assert msg.value == 1


class TestTerminalVersionMsg:
    def test_creation(self):
        msg = TerminalVersionMsg(version="xterm-256")
        assert str(msg) == "xterm-256"


class TestEnvMsg:
    def test_getenv(self):
        msg = EnvMsg(environ={"HOME": "/home/user", "TERM": "xterm"})
        assert msg.getenv("HOME") == "/home/user"

    def test_getenv_missing(self):
        msg = EnvMsg(environ={})
        assert msg.getenv("MISSING") == ""

    def test_lookup_env(self):
        msg = EnvMsg(environ={"KEY": "val"})
        val, ok = msg.lookup_env("KEY")
        assert val == "val"
        assert ok is True

    def test_lookup_env_missing(self):
        msg = EnvMsg(environ={})
        val, ok = msg.lookup_env("MISSING")
        assert val == ""
        assert ok is False


class TestRawMsg:
    def test_creation(self):
        msg = RawMsg(data=b"\x1b[0m")
        assert msg.data == b"\x1b[0m"
