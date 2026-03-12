"""Tests for View, Cursor, Position, and CursorShape."""

from bubbletea.view import View, Cursor, CursorShape, Position


class TestPosition:
    def test_creation(self):
        p = Position(x=5, y=10)
        assert p.x == 5
        assert p.y == 10

    def test_defaults(self):
        p = Position()
        assert p.x == 0
        assert p.y == 0


class TestCursorShape:
    def test_shapes(self):
        assert CursorShape.BLOCK is not None
        assert CursorShape.UNDERLINE is not None
        assert CursorShape.BAR is not None

    def test_shapes_are_distinct(self):
        shapes = {CursorShape.BLOCK, CursorShape.UNDERLINE, CursorShape.BAR}
        assert len(shapes) == 3


class TestCursor:
    def test_creation(self):
        c = Cursor(x=5, y=10)
        assert c.position.x == 5
        assert c.position.y == 10

    def test_defaults(self):
        c = Cursor(x=0, y=0)
        assert c.shape == CursorShape.BLOCK
        assert c.blink is False
        assert c.color is None

    def test_with_options(self):
        c = Cursor(x=1, y=2, shape=CursorShape.BAR, blink=True, color="#ff0000")
        assert c.shape == CursorShape.BAR
        assert c.blink is True
        assert c.color == "#ff0000"


class TestView:
    def test_creation_from_string(self):
        v = View("Hello, World!")
        assert str(v) == "Hello, World!"

    def test_new_view(self):
        v = View("test")
        assert str(v) == "test"

    def test_set_content(self):
        v = View("old")
        v.set_content("new")
        assert str(v) == "new"

    def test_cursor(self):
        v = View("test")
        v.cursor = Cursor(x=1, y=2)
        assert v.cursor.position.x == 1

    def test_alt_screen(self):
        v = View("test")
        v.alt_screen = True
        assert v.alt_screen is True

    def test_mouse_tracking(self):
        v = View("test")
        v.mouse_tracking = True
        assert v.mouse_tracking is True

    def test_report_focus(self):
        v = View("test")
        v.report_focus = True
        assert v.report_focus is True

    def test_keyboard_enhancements(self):
        from bubbletea.messages import KeyboardEnhancements
        v = View("test")
        v.keyboard_enhancements = KeyboardEnhancements(report_event_types=True)
        assert v.keyboard_enhancements.report_event_types is True
