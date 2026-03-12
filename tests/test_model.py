"""Tests for Model protocol."""

from bubbletea.model import Model
from bubbletea.view import View
from bubbletea.messages import QuitMsg, KeyPressMsg
from bubbletea.modifiers import KeyMod


class Counter(Model):
    def __init__(self, count: int = 0):
        self.count = count

    def init(self):
        return None

    def update(self, msg):
        if isinstance(msg, KeyPressMsg):
            if msg.text == "q":
                from bubbletea.commands import quit_cmd
                return self, quit_cmd
            if msg.text == "+":
                return Counter(self.count + 1), None
        return self, None

    def view(self):
        return View(f"Count: {self.count}")


class TestModel:
    def test_model_init(self):
        m = Counter()
        assert m.init() is None

    def test_model_view(self):
        m = Counter(42)
        v = m.view()
        assert str(v) == "Count: 42"

    def test_model_update_returns_tuple(self):
        m = Counter()
        new_model, cmd = m.update(KeyPressMsg(code=ord("+"), text="+"))
        assert isinstance(new_model, Counter)
        assert new_model.count == 1
        assert cmd is None

    def test_model_update_quit(self):
        m = Counter()
        new_model, cmd = m.update(KeyPressMsg(code=ord("q"), text="q"))
        assert cmd is not None

    def test_model_is_protocol(self):
        assert isinstance(Counter(), Model)

    def test_model_immutable_pattern(self):
        m = Counter(0)
        new_m, _ = m.update(KeyPressMsg(code=ord("+"), text="+"))
        assert m.count == 0
        assert new_m.count == 1
