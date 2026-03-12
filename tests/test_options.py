"""Tests for program options."""

import io

from bubbletea.options import (
    with_input, with_output, with_fps, with_filter,
    with_window_size, with_color_profile, with_environment,
    without_renderer, without_signal_handler, without_catch_panics,
    ProgramOption,
)


class TestProgramOptions:
    def test_with_input(self):
        opt = with_input(io.StringIO())
        assert isinstance(opt, ProgramOption)

    def test_with_output(self):
        opt = with_output(io.StringIO())
        assert isinstance(opt, ProgramOption)

    def test_with_fps(self):
        opt = with_fps(60)
        assert isinstance(opt, ProgramOption)

    def test_with_filter(self):
        opt = with_filter(lambda model, msg: msg)
        assert isinstance(opt, ProgramOption)

    def test_with_window_size(self):
        opt = with_window_size(80, 24)
        assert isinstance(opt, ProgramOption)

    def test_with_color_profile(self):
        opt = with_color_profile("truecolor")
        assert isinstance(opt, ProgramOption)

    def test_with_environment(self):
        opt = with_environment(["TERM=xterm"])
        assert isinstance(opt, ProgramOption)

    def test_without_renderer(self):
        opt = without_renderer()
        assert isinstance(opt, ProgramOption)

    def test_without_signal_handler(self):
        opt = without_signal_handler()
        assert isinstance(opt, ProgramOption)

    def test_without_catch_panics(self):
        opt = without_catch_panics()
        assert isinstance(opt, ProgramOption)
