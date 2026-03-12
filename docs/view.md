# View

The `View` class represents the rendered UI content returned by `Model.view()`.

## View

```python
v = tea.View("Hello, World!")
str(v)  # "Hello, World!"

v.set_content("Updated!")
str(v)  # "Updated!"
```

### Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `cursor` | `Cursor \| None` | `None` | Terminal cursor |
| `alt_screen` | `bool` | `False` | Use alternate screen |
| `mouse_tracking` | `bool` | `False` | Enable mouse events |
| `report_focus` | `bool` | `False` | Enable focus events |
| `keyboard_enhancements` | `KeyboardEnhancements \| None` | `None` | Enhanced keyboard |

```python
def view(self):
    v = tea.View(self.render())
    v.alt_screen = True
    v.mouse_tracking = True
    v.cursor = tea.Cursor(x=self.col, y=self.row)
    return v
```

## Position

```python
p = tea.Position(x=5, y=10)
p = tea.Position()  # defaults to (0, 0)
```

## CursorShape

```python
tea.CursorShape.BLOCK      # 0
tea.CursorShape.UNDERLINE   # 1
tea.CursorShape.BAR         # 2
```

## Cursor

```python
c = tea.Cursor(x=10, y=5)
c = tea.Cursor(x=0, y=0, shape=tea.CursorShape.BAR, blink=True, color="#ff0000")
```

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `position` | `Position` | — | Set via `x`, `y` args |
| `shape` | `CursorShape` | `BLOCK` | Cursor appearance |
| `blink` | `bool` | `False` | Blinking cursor |
| `color` | `str \| None` | `None` | Cursor color (hex) |

## KeyboardEnhancements

```python
from bubbletea.messages import KeyboardEnhancements

v = tea.View("content")
v.keyboard_enhancements = KeyboardEnhancements(report_event_types=True)
```
