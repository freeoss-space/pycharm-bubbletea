"""
Bubble Tea for Python — A TUI framework based on The Elm Architecture.

This is a Python port of the Go library Bubble Tea (charm.land/bubbletea/v2)
by Charmbracelet, Inc. See https://github.com/charmbracelet/bubbletea
"""

from bubbletea.keys import *  # noqa: F401,F403
from bubbletea.mouse import Mouse, MouseButton  # noqa: F401
from bubbletea.modifiers import KeyMod  # noqa: F401
from bubbletea.messages import (  # noqa: F401
    Msg,
    QuitMsg,
    InterruptMsg,
    SuspendMsg,
    ResumeMsg,
    FocusMsg,
    BlurMsg,
    KeyPressMsg,
    KeyReleaseMsg,
    MouseClickMsg,
    MouseMotionMsg,
    MouseReleaseMsg,
    MouseWheelMsg,
    WindowSizeMsg,
    CursorPositionMsg,
    ForegroundColorMsg,
    BackgroundColorMsg,
    CursorColorMsg,
    ColorProfileMsg,
    ClipboardMsg,
    PasteMsg,
    PasteStartMsg,
    PasteEndMsg,
    ClearScreenMsg,
    BatchMsg,
    KeyboardEnhancementsMsg,
    CapabilityMsg,
    ModeReportMsg,
    TerminalVersionMsg,
    EnvMsg,
    RawMsg,
)
from bubbletea.commands import (  # noqa: F401
    Cmd,
    batch,
    sequence,
    every,
    tick,
    quit_cmd,
    interrupt,
    suspend,
    clear_screen,
    printf,
    println,
    set_clipboard,
    set_primary_clipboard,
    read_clipboard,
    read_primary_clipboard,
    request_background_color,
    request_foreground_color,
    request_cursor_color,
    request_cursor_position,
    request_window_size,
    request_terminal_version,
    request_capability,
    raw,
)
from bubbletea.view import View, Cursor, CursorShape, Position  # noqa: F401
from bubbletea.model import Model  # noqa: F401
from bubbletea.program import Program  # noqa: F401
from bubbletea.options import (  # noqa: F401
    ProgramOption,
    with_input,
    with_output,
    with_fps,
    with_filter,
    with_window_size,
    with_color_profile,
    with_environment,
    without_renderer,
    without_signal_handler,
    without_catch_panics,
)
from bubbletea.errors import (  # noqa: F401
    ProgramPanicError,
    ProgramKilledError,
    InterruptedError,
)

Key = KeyPressMsg  # Convenience alias

__version__ = "0.1.0"
