"""Tests for key constants."""

from bubbletea.keys import (
    KEY_UP, KEY_DOWN, KEY_RIGHT, KEY_LEFT, KEY_BEGIN,
    KEY_FIND, KEY_INSERT, KEY_DELETE, KEY_SELECT,
    KEY_PG_UP, KEY_PG_DOWN, KEY_HOME, KEY_END,
    KEY_F1, KEY_F2, KEY_F12, KEY_F63,
    KEY_BACKSPACE, KEY_TAB, KEY_ENTER, KEY_RETURN,
    KEY_ESCAPE, KEY_ESC, KEY_SPACE,
    KEY_CAPS_LOCK, KEY_SCROLL_LOCK, KEY_NUM_LOCK,
    KEY_PRINT_SCREEN, KEY_PAUSE, KEY_MENU,
    KEY_KP_ENTER, KEY_KP_EQUAL, KEY_KP_MULTIPLY, KEY_KP_PLUS,
    KEY_KP_0, KEY_KP_9,
    KEY_MEDIA_PLAY, KEY_MEDIA_PAUSE, KEY_MEDIA_STOP,
    KEY_LOWER_VOL, KEY_RAISE_VOL, KEY_MUTE,
    KEY_LEFT_SHIFT, KEY_LEFT_ALT, KEY_LEFT_CTRL, KEY_LEFT_SUPER,
    KEY_RIGHT_SHIFT, KEY_RIGHT_ALT, KEY_RIGHT_CTRL, KEY_RIGHT_SUPER,
    KEY_EXTENDED,
)


class TestKeyConstants:
    def test_arrow_keys_are_unique(self):
        arrows = {KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT}
        assert len(arrows) == 4

    def test_navigation_keys_exist(self):
        assert KEY_PG_UP is not None
        assert KEY_PG_DOWN is not None
        assert KEY_HOME is not None
        assert KEY_END is not None

    def test_function_keys_range(self):
        assert KEY_F1 != KEY_F2
        assert KEY_F12 != KEY_F63

    def test_enter_return_alias(self):
        assert KEY_ENTER == KEY_RETURN

    def test_escape_esc_alias(self):
        assert KEY_ESCAPE == KEY_ESC

    def test_whitespace_keys(self):
        assert KEY_BACKSPACE is not None
        assert KEY_TAB is not None
        assert KEY_SPACE is not None

    def test_modifier_keys(self):
        assert KEY_LEFT_SHIFT != KEY_RIGHT_SHIFT
        assert KEY_LEFT_ALT != KEY_RIGHT_ALT
        assert KEY_LEFT_CTRL != KEY_RIGHT_CTRL

    def test_keypad_keys(self):
        assert KEY_KP_0 != KEY_KP_9
        assert KEY_KP_ENTER is not None

    def test_media_keys(self):
        assert KEY_MEDIA_PLAY is not None
        assert KEY_MEDIA_STOP is not None

    def test_volume_keys(self):
        assert KEY_LOWER_VOL != KEY_RAISE_VOL
        assert KEY_MUTE is not None

    def test_extended_key(self):
        assert KEY_EXTENDED is not None

    def test_lock_keys(self):
        assert KEY_CAPS_LOCK is not None
        assert KEY_SCROLL_LOCK is not None
        assert KEY_NUM_LOCK is not None
