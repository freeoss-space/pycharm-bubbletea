# Bubble Tea for Python

Python bindings for [Bubble Tea](https://github.com/charmbracelet/bubbletea) — a TUI framework based on [The Elm Architecture](https://guide.elm-lang.org/architecture/).

> **Original project:** [charm.land/bubbletea/v2](https://pkg.go.dev/charm.land/bubbletea/v2)
> by [Charmbracelet, Inc.](https://charm.sh/)
> Licensed under the [MIT License](LICENSE).

This library is a pure-Python port of the Go-based Bubble Tea v2 framework,
providing the same functional, message-driven architecture for building
terminal user interfaces.

## Installation

```bash
pip install pycharm-bubbletea
```

Or install from source:

```bash
git clone https://github.com/charmbracelet/bubbletea-python
cd bubbletea-python
pip install -e .
```

## Quick Start

Every Bubble Tea program is built around a **Model** with three methods:

```python
import bubbletea as tea


class TodoModel(tea.Model):
    def __init__(self, choices=None, cursor=0, selected=None):
        self.choices = choices or ["Buy carrots", "Buy celery", "Buy kohlrabi"]
        self.cursor = cursor
        self.selected = selected or set()

    def init(self):
        return None

    def update(self, msg):
        if isinstance(msg, tea.KeyPressMsg):
            match msg.text:
                case "q":
                    return self, tea.quit_cmd
                case "up" | "k":
                    cursor = max(0, self.cursor - 1)
                    return TodoModel(self.choices, cursor, self.selected), None
                case "down" | "j":
                    cursor = min(len(self.choices) - 1, self.cursor + 1)
                    return TodoModel(self.choices, cursor, self.selected), None
                case " ":
                    selected = self.selected ^ {self.cursor}
                    return TodoModel(self.choices, self.cursor, selected), None
        return self, None

    def view(self):
        lines = ["What should we buy at the market?\n"]
        for i, choice in enumerate(self.choices):
            cur = ">" if i == self.cursor else " "
            chk = "x" if i in self.selected else " "
            lines.append(f"{cur} [{chk}] {choice}")
        lines.append("\nPress q to quit.")
        return tea.View("\n".join(lines))


if __name__ == "__main__":
    p = tea.Program(TodoModel())
    p.run()
```

## The Elm Architecture

Bubble Tea is built around three core concepts:

| Concept | Method | Purpose |
|---------|--------|---------|
| **Init** | `init()` | Return an initial command (or `None`) |
| **Update** | `update(msg)` | Handle a message, return `(model, cmd)` |
| **View** | `view()` | Return a `View` describing the UI |

Messages flow in, the model updates, and the view re-renders — that's it.

## Commands

Commands are functions that produce messages asynchronously:

```python
# Simple message producers
tea.quit_cmd()          # Returns QuitMsg
tea.interrupt()         # Returns InterruptMsg
tea.clear_screen()      # Returns ClearScreenMsg

# Commands returning Cmd (callable)
tea.batch(cmd1, cmd2)   # Run commands concurrently
tea.sequence(cmd1, cmd2)# Run commands sequentially
tea.tick(1.0, handler)  # Fire once after 1 second
tea.every(5.0, handler) # Fire every 5 seconds
tea.printf("hi %s", n)  # Print formatted text
tea.println("hello")    # Print a line
tea.set_clipboard("x")  # Set system clipboard
```

## Program Options

```python
import io
import bubbletea as tea

p = tea.Program(
    model,
    tea.with_output(io.StringIO()),    # Custom output
    tea.with_input(io.StringIO()),     # Custom input
    tea.with_fps(30),                  # Limit FPS
    tea.with_window_size(80, 24),      # Set initial size
    tea.without_renderer(),            # Disable rendering
)
```

## API Reference

Full documentation for each module is in the [docs/](docs/) folder:

- [Model](docs/model.md) — The core protocol
- [Messages](docs/messages.md) — All message types
- [Commands](docs/commands.md) — Command functions
- [View](docs/view.md) — View, Cursor, Position
- [Keys](docs/keys.md) — Key constants
- [Mouse](docs/mouse.md) — Mouse types
- [Program](docs/program.md) — Program runner
- [Options](docs/options.md) — Program configuration

## Running Tests

```bash
pip install pytest
pytest tests/ -v
```

## Attribution

This project is a Python port of [Bubble Tea](https://github.com/charmbracelet/bubbletea)
by [Charmbracelet, Inc.](https://charm.sh/), originally written in Go.
The original project is licensed under the MIT License. All credit for the
design, architecture, and API goes to the Charmbracelet team.

## License

[MIT](LICENSE) — same as the original Bubble Tea project.
