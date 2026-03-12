# Model

The `Model` protocol is the heart of every Bubble Tea application. It follows [The Elm Architecture](https://guide.elm-lang.org/architecture/) with three methods: `init`, `update`, and `view`.

## Protocol

```python
class Model(Protocol):
    def init(self) -> Cmd | None: ...
    def update(self, msg: Msg) -> tuple[Model, Cmd | None]: ...
    def view(self) -> View: ...
```

## Methods

### `init() -> Cmd | None`

Called once when the program starts. Return a command to run on startup, or `None`.

### `update(msg) -> (Model, Cmd | None)`

Called whenever a message arrives. Return a new model and an optional command.

### `view() -> View`

Called after every `update`. Return a `View` describing the current UI.

## Example

```python
import bubbletea as tea


class Counter(tea.Model):
    def __init__(self, count=0):
        self.count = count

    def init(self):
        return None

    def update(self, msg):
        if isinstance(msg, tea.KeyPressMsg):
            if msg.text == "+":
                return Counter(self.count + 1), None
            if msg.text == "-":
                return Counter(self.count - 1), None
            if msg.text == "q":
                return self, tea.quit_cmd
        return self, None

    def view(self):
        return tea.View(f"Count: {self.count}\n\n+/- to change, q to quit")
```

## Immutability Pattern

Models should follow an immutable update pattern — return a *new* model instance rather than mutating `self`:

```python
# Good: return new instance
return Counter(self.count + 1), None

# Avoid: mutating in place
self.count += 1
return self, None
```
