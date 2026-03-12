"""Program options mirroring Bubble Tea v2 ProgramOption type."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, IO, Optional


@dataclass(frozen=True)
class ProgramOption:
    """A configuration option for Program."""

    key: str
    value: Any


def with_input(reader: IO) -> ProgramOption:
    """Set the input reader."""
    return ProgramOption("input", reader)


def with_output(writer: IO) -> ProgramOption:
    """Set the output writer."""
    return ProgramOption("output", writer)


def with_fps(fps: int) -> ProgramOption:
    """Set the maximum frames per second."""
    return ProgramOption("fps", fps)


def with_filter(fn: Callable) -> ProgramOption:
    """Set a message filter function ``fn(model, msg) -> msg``."""
    return ProgramOption("filter", fn)


def with_window_size(width: int, height: int) -> ProgramOption:
    """Set the initial window size."""
    return ProgramOption("window_size", (width, height))


def with_color_profile(profile: str) -> ProgramOption:
    """Set the color profile (e.g. 'truecolor', 'ansi256')."""
    return ProgramOption("color_profile", profile)


def with_environment(env: list[str]) -> ProgramOption:
    """Set environment variables."""
    return ProgramOption("environment", env)


def without_renderer() -> ProgramOption:
    """Disable the renderer."""
    return ProgramOption("renderer", False)


def without_signal_handler() -> ProgramOption:
    """Disable the signal handler."""
    return ProgramOption("signal_handler", False)


def without_catch_panics() -> ProgramOption:
    """Disable panic catching."""
    return ProgramOption("catch_panics", False)
