"""Tests for key modifier constants."""

from bubbletea.modifiers import KeyMod


class TestKeyMod:
    def test_basic_modifiers(self):
        assert KeyMod.SHIFT is not None
        assert KeyMod.ALT is not None
        assert KeyMod.CTRL is not None

    def test_extended_modifiers(self):
        assert KeyMod.META is not None
        assert KeyMod.HYPER is not None
        assert KeyMod.SUPER is not None

    def test_lock_modifiers(self):
        assert KeyMod.CAPS_LOCK is not None
        assert KeyMod.NUM_LOCK is not None
        assert KeyMod.SCROLL_LOCK is not None

    def test_modifiers_are_flags(self):
        combined = KeyMod.SHIFT | KeyMod.CTRL
        assert combined & KeyMod.SHIFT
        assert combined & KeyMod.CTRL
        assert not (combined & KeyMod.ALT)

    def test_all_unique(self):
        all_mods = [m for m in KeyMod]
        assert len(set(m.value for m in all_mods)) == len(all_mods)
