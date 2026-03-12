"""Mouse types and constants mirroring Bubble Tea v2."""

from dataclasses import dataclass, field
from enum import IntEnum


class MouseButton(IntEnum):
    """Mouse button constants."""

    NONE = 0
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3
    WHEEL_UP = 4
    WHEEL_DOWN = 5
    WHEEL_LEFT = 6
    WHEEL_RIGHT = 7
    BACKWARD = 8
    FORWARD = 9
    BUTTON10 = 10
    BUTTON11 = 11


@dataclass(frozen=True)
class Mouse:
    """Represents a mouse event with position, button, and modifiers."""

    x: int
    y: int
    button: MouseButton
    mod: int = 0

    def __str__(self) -> str:
        return f"{self.button.name.lower()} ({self.x}, {self.y})"
