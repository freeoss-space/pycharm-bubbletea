"""Error types mirroring Bubble Tea v2 error variables."""


class ProgramPanicError(RuntimeError):
    """Raised when the program experiences a panic."""


class ProgramKilledError(RuntimeError):
    """Raised when the program is killed."""


class InterruptedError(RuntimeError):
    """Raised when the program is interrupted (e.g. Ctrl+C)."""
