# Mouse

Mouse types and button constants.

## MouseButton

An `IntEnum` of all mouse button constants:

| Constant | Value | Description |
|----------|-------|-------------|
| `MouseButton.NONE` | 0 | No button |
| `MouseButton.LEFT` | 1 | Left button |
| `MouseButton.MIDDLE` | 2 | Middle button |
| `MouseButton.RIGHT` | 3 | Right button |
| `MouseButton.WHEEL_UP` | 4 | Scroll up |
| `MouseButton.WHEEL_DOWN` | 5 | Scroll down |
| `MouseButton.WHEEL_LEFT` | 6 | Scroll left |
| `MouseButton.WHEEL_RIGHT` | 7 | Scroll right |
| `MouseButton.BACKWARD` | 8 | Back button |
| `MouseButton.FORWARD` | 9 | Forward button |
| `MouseButton.BUTTON10` | 10 | Extra button |
| `MouseButton.BUTTON11` | 11 | Extra button |

## Mouse

A frozen dataclass representing a mouse event:

```python
m = tea.Mouse(x=10, y=5, button=tea.MouseButton.LEFT, mod=0)
m.x       # 10
m.y       # 5
m.button  # MouseButton.LEFT
m.mod     # 0 (KeyMod flags)
str(m)    # "left (10, 5)"
```

## Example

```python
def update(self, msg):
    if isinstance(msg, tea.MouseClickMsg):
        x, y = msg.mouse.x, msg.mouse.y
        if msg.mouse.button == tea.MouseButton.LEFT:
            return self.handle_click(x, y), None
    return self, None
```
