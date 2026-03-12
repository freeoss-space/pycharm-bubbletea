"""Key modifier flags mirroring Bubble Tea v2 KeyMod."""

from enum import IntFlag


class KeyMod(IntFlag):
    """Keyboard modifier flags, combinable with bitwise OR."""

    SHIFT = 1
    ALT = 2
    CTRL = 4
    META = 8
    HYPER = 16
    SUPER = 32
    CAPS_LOCK = 64
    NUM_LOCK = 128
    SCROLL_LOCK = 256
