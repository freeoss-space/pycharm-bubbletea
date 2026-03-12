"""Tests for error types."""

from bubbletea.errors import ProgramPanicError, ProgramKilledError, InterruptedError


class TestErrors:
    def test_program_panic_error(self):
        err = ProgramPanicError("panic!")
        assert isinstance(err, Exception)
        assert "panic" in str(err).lower()

    def test_program_killed_error(self):
        err = ProgramKilledError()
        assert isinstance(err, Exception)

    def test_interrupted_error(self):
        err = InterruptedError()
        assert isinstance(err, Exception)

    def test_error_hierarchy(self):
        assert issubclass(ProgramPanicError, RuntimeError)
        assert issubclass(ProgramKilledError, RuntimeError)
        assert issubclass(InterruptedError, RuntimeError)
