# Messages

Messages (`Msg`) are the events that drive a Bubble Tea application. They are passed to `Model.update()`.

## Signal Messages

| Message | Description |
|---------|-------------|
| `QuitMsg` | Signals the program to quit |
| `InterruptMsg` | User interrupt (Ctrl+C) |
| `SuspendMsg` | Suspend the program |
| `ResumeMsg` | Resume after suspension |
| `FocusMsg` | Terminal gained focus |
| `BlurMsg` | Terminal lost focus |
| `ClearScreenMsg` | Clear the screen |

```python
if isinstance(msg, tea.QuitMsg):
    print("Goodbye!")
```

## Key Messages

### `KeyPressMsg` / `KeyReleaseMsg`

```python
KeyPressMsg(code=ord("a"), text="a", mod=0, is_repeat=False)
```

| Field | Type | Description |
|-------|------|-------------|
| `code` | `int` | Key code (Unicode codepoint) |
| `text` | `str` | Printable character(s) |
| `mod` | `int` | Modifier flags (`KeyMod`) |
| `shifted_code` | `int` | Shifted key variant |
| `base_code` | `int` | US layout equivalent |
| `is_repeat` | `bool` | Whether this is a key repeat |

**Methods:** `str(msg)` returns the text, `msg.keystroke()` returns a string like `"ctrl+c"`.

```python
if isinstance(msg, tea.KeyPressMsg):
    if msg.keystroke() == "ctrl+c":
        return model, tea.quit_cmd
```

## Mouse Messages

All mouse messages carry a `Mouse` object via `msg.mouse`:

| Message | Trigger |
|---------|---------|
| `MouseClickMsg` | Button pressed |
| `MouseMotionMsg` | Pointer moved |
| `MouseReleaseMsg` | Button released |
| `MouseWheelMsg` | Scroll wheel |

```python
if isinstance(msg, tea.MouseClickMsg):
    x, y = msg.mouse.x, msg.mouse.y
```

## Terminal Messages

| Message | Fields | Description |
|---------|--------|-------------|
| `WindowSizeMsg` | `width`, `height` | Terminal resized |
| `CursorPositionMsg` | `x`, `y` | Cursor position report |
| `ForegroundColorMsg` | `color` | Terminal fg color |
| `BackgroundColorMsg` | `color` | Terminal bg color |
| `CursorColorMsg` | `color` | Cursor color |
| `ColorProfileMsg` | `profile` | Color profile name |
| `TerminalVersionMsg` | `version` | Terminal version string |

Color messages support `is_dark()`:

```python
if isinstance(msg, tea.BackgroundColorMsg):
    if msg.is_dark():
        # Use light theme
```

## Clipboard & Paste Messages

```python
# ClipboardMsg: reports clipboard content
msg.content   # The text
msg.clipboard()  # Selection index

# PasteMsg: bracketed paste content
msg.content   # The pasted text

# PasteStartMsg / PasteEndMsg: paste boundaries
```

## Other Messages

| Message | Fields | Description |
|---------|--------|-------------|
| `BatchMsg` | `commands` | A batch of commands |
| `KeyboardEnhancementsMsg` | `flags` | Terminal keyboard capabilities |
| `CapabilityMsg` | `content` | Terminal capability report |
| `ModeReportMsg` | `mode`, `value` | Terminal mode report |
| `EnvMsg` | `environ` | Environment variables |
| `RawMsg` | `data` | Raw byte data |

```python
# EnvMsg
msg = tea.EnvMsg(environ={"TERM": "xterm"})
msg.getenv("TERM")          # "xterm"
msg.lookup_env("MISSING")   # ("", False)
```
