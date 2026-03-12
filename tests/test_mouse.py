"""Tests for mouse types and constants."""

from bubbletea.mouse import Mouse, MouseButton


class TestMouseButton:
    def test_standard_buttons(self):
        assert MouseButton.NONE is not None
        assert MouseButton.LEFT is not None
        assert MouseButton.MIDDLE is not None
        assert MouseButton.RIGHT is not None

    def test_wheel_buttons(self):
        assert MouseButton.WHEEL_UP is not None
        assert MouseButton.WHEEL_DOWN is not None
        assert MouseButton.WHEEL_LEFT is not None
        assert MouseButton.WHEEL_RIGHT is not None

    def test_extra_buttons(self):
        assert MouseButton.BACKWARD is not None
        assert MouseButton.FORWARD is not None
        assert MouseButton.BUTTON10 is not None
        assert MouseButton.BUTTON11 is not None

    def test_buttons_are_unique(self):
        all_buttons = [b for b in MouseButton]
        assert len(set(all_buttons)) == len(all_buttons)


class TestMouse:
    def test_creation(self):
        m = Mouse(x=10, y=20, button=MouseButton.LEFT)
        assert m.x == 10
        assert m.y == 20
        assert m.button == MouseButton.LEFT

    def test_default_mod(self):
        m = Mouse(x=0, y=0, button=MouseButton.NONE)
        assert m.mod == 0

    def test_string_representation(self):
        m = Mouse(x=5, y=3, button=MouseButton.LEFT)
        s = str(m)
        assert "left" in s.lower() or "LEFT" in s

    def test_with_modifier(self):
        m = Mouse(x=0, y=0, button=MouseButton.LEFT, mod=1)
        assert m.mod == 1
