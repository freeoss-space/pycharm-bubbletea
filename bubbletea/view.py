"""View, Cursor, Position, and CursorShape types mirroring Bubble Tea v2."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum
from typing import Any, Optional


class CursorShape(IntEnum):
    """Cursor shape constants."""

    BLOCK = 0
    UNDERLINE = 1
    BAR = 2


@dataclass
class Position:
    """A 2D position."""

    x: int = 0
    y: int = 0


@dataclass
class Cursor:
    """Terminal cursor with position, shape, color, and blink."""

    position: Position = field(init=False)
    shape: CursorShape = CursorShape.BLOCK
    blink: bool = False
    color: Optional[str] = None

    def __init__(
        self,
        x: int,
        y: int,
        shape: CursorShape = CursorShape.BLOCK,
        blink: bool = False,
        color: Optional[str] = None,
    ):
        self.position = Position(x, y)
        self.shape = shape
        self.blink = blink
        self.color = color


class View:
    """Represents the rendered view content.

    Mirrors Bubble Tea's View type with content, cursor, and display options.
    """

    def __init__(self, content: str = ""):
        self._content = content
        self.cursor: Optional[Cursor] = None
        self.alt_screen: bool = False
        self.mouse_tracking: bool = False
        self.report_focus: bool = False
        self.keyboard_enhancements: Any = None

    def set_content(self, content: str) -> None:
        """Replace the view content."""
        self._content = content

    def __str__(self) -> str:
        return self._content
