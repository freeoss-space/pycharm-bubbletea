"""Message types mirroring Bubble Tea v2 Msg types."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from bubbletea.mouse import Mouse
from bubbletea.modifiers import KeyMod

# Base type alias
Msg = Any


# --- Simple signal messages ---

@dataclass(frozen=True)
class QuitMsg:
    """Signals the program to quit."""


@dataclass(frozen=True)
class InterruptMsg:
    """Signals a user interrupt (Ctrl+C)."""


@dataclass(frozen=True)
class SuspendMsg:
    """Signals the program to suspend."""


@dataclass(frozen=True)
class ResumeMsg:
    """Signals the program to resume after suspension."""


@dataclass(frozen=True)
class FocusMsg:
    """Signals the terminal gained focus."""


@dataclass(frozen=True)
class BlurMsg:
    """Signals the terminal lost focus."""


@dataclass(frozen=True)
class ClearScreenMsg:
    """Signals a screen clear."""


@dataclass(frozen=True)
class PasteStartMsg:
    """Signals the start of a bracketed paste."""


@dataclass(frozen=True)
class PasteEndMsg:
    """Signals the end of a bracketed paste."""


# --- Key messages ---

def _format_keystroke(code: int, text: str, mod: int) -> str:
    parts = []
    if mod & KeyMod.CTRL:
        parts.append("ctrl")
    if mod & KeyMod.ALT:
        parts.append("alt")
    if mod & KeyMod.SHIFT:
        parts.append("shift")
    if text:
        parts.append(text)
    elif code:
        parts.append(chr(code))
    return "+".join(parts) if parts else ""


@dataclass(frozen=True)
class KeyPressMsg:
    """A key press event."""

    code: int
    text: str = ""
    mod: int = 0
    shifted_code: int = 0
    base_code: int = 0
    is_repeat: bool = False

    def __str__(self) -> str:
        return self.text if self.text else (chr(self.code) if self.code else "")

    def keystroke(self) -> str:
        return _format_keystroke(self.code, self.text, self.mod)


@dataclass(frozen=True)
class KeyReleaseMsg:
    """A key release event."""

    code: int
    text: str = ""
    mod: int = 0
    shifted_code: int = 0
    base_code: int = 0
    is_repeat: bool = False

    def __str__(self) -> str:
        return self.text if self.text else (chr(self.code) if self.code else "")

    def keystroke(self) -> str:
        return _format_keystroke(self.code, self.text, self.mod)


# --- Mouse messages ---

@dataclass(frozen=True)
class MouseClickMsg:
    """A mouse click event."""
    mouse: Mouse

    def __str__(self) -> str:
        return f"click {self.mouse}"


@dataclass(frozen=True)
class MouseMotionMsg:
    """A mouse motion event."""
    mouse: Mouse

    def __str__(self) -> str:
        return f"motion {self.mouse}"


@dataclass(frozen=True)
class MouseReleaseMsg:
    """A mouse button release event."""
    mouse: Mouse

    def __str__(self) -> str:
        return f"release {self.mouse}"


@dataclass(frozen=True)
class MouseWheelMsg:
    """A mouse wheel event."""
    mouse: Mouse

    def __str__(self) -> str:
        return f"wheel {self.mouse}"


# --- Terminal / window messages ---

@dataclass(frozen=True)
class WindowSizeMsg:
    """Reports the terminal window size."""
    width: int
    height: int


@dataclass(frozen=True)
class CursorPositionMsg:
    """Reports the cursor position."""
    x: int
    y: int


# --- Color messages ---

def _is_dark_hex(color: str) -> bool:
    """Heuristic: parse hex color, check if luminance < 0.5."""
    c = color.lstrip("#")
    if len(c) == 6:
        r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        return luminance < 0.5
    return False


@dataclass(frozen=True)
class ForegroundColorMsg:
    """Reports the terminal foreground color."""
    color: str

    def is_dark(self) -> bool:
        return _is_dark_hex(self.color)

    def __str__(self) -> str:
        return self.color


@dataclass(frozen=True)
class BackgroundColorMsg:
    """Reports the terminal background color."""
    color: str

    def is_dark(self) -> bool:
        return _is_dark_hex(self.color)

    def __str__(self) -> str:
        return self.color


@dataclass(frozen=True)
class CursorColorMsg:
    """Reports the cursor color."""
    color: str

    def is_dark(self) -> bool:
        return _is_dark_hex(self.color)

    def __str__(self) -> str:
        return self.color


@dataclass(frozen=True)
class ColorProfileMsg:
    """Reports the terminal color profile."""
    profile: str


# --- Clipboard ---

@dataclass(frozen=True)
class ClipboardMsg:
    """Reports clipboard content."""
    content: str
    selection: int = 0

    def clipboard(self) -> int:
        return self.selection

    def __str__(self) -> str:
        return self.content


# --- Paste ---

@dataclass(frozen=True)
class PasteMsg:
    """A paste event with content."""
    content: str

    def __str__(self) -> str:
        return self.content


# --- Batch ---

@dataclass
class BatchMsg:
    """A batch of commands."""
    commands: list


# --- Keyboard enhancements ---

@dataclass(frozen=True)
class KeyboardEnhancements:
    """Keyboard enhancement configuration for views."""
    report_event_types: bool = False


@dataclass(frozen=True)
class KeyboardEnhancementsMsg:
    """Reports terminal keyboard enhancement capabilities."""
    flags: int

    def supports_key_disambiguation(self) -> bool:
        return bool(self.flags & 1)

    def supports_event_types(self) -> bool:
        return bool(self.flags & 2)


# --- Misc messages ---

@dataclass(frozen=True)
class CapabilityMsg:
    """Reports a terminal capability."""
    content: str

    def __str__(self) -> str:
        return self.content


@dataclass(frozen=True)
class ModeReportMsg:
    """Reports a terminal mode setting."""
    mode: int
    value: int


@dataclass(frozen=True)
class TerminalVersionMsg:
    """Reports the terminal version string."""
    version: str

    def __str__(self) -> str:
        return self.version


@dataclass(frozen=True)
class EnvMsg:
    """Provides access to environment variables."""
    environ: dict[str, str] = field(default_factory=dict)

    def getenv(self, key: str) -> str:
        return self.environ.get(key, "")

    def lookup_env(self, key: str) -> tuple[str, bool]:
        if key in self.environ:
            return self.environ[key], True
        return "", False


@dataclass(frozen=True)
class RawMsg:
    """A raw byte sequence message."""
    data: bytes
