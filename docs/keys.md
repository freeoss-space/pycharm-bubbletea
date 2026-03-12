# Key Constants

String constants for key codes, matching Bubble Tea v2's key definitions.

## Arrow / Navigation

```python
tea.KEY_UP, tea.KEY_DOWN, tea.KEY_LEFT, tea.KEY_RIGHT
tea.KEY_HOME, tea.KEY_END, tea.KEY_PG_UP, tea.KEY_PG_DOWN
tea.KEY_BEGIN, tea.KEY_FIND, tea.KEY_INSERT, tea.KEY_DELETE, tea.KEY_SELECT
```

## Whitespace / Control

```python
tea.KEY_BACKSPACE   # "backspace"
tea.KEY_TAB         # "tab"
tea.KEY_ENTER       # "enter"
tea.KEY_RETURN      # alias for KEY_ENTER
tea.KEY_ESCAPE      # "escape"
tea.KEY_ESC         # alias for KEY_ESCAPE
tea.KEY_SPACE       # "space"
```

## Function Keys

```python
tea.KEY_F1 through tea.KEY_F63
```

## Keypad

```python
tea.KEY_KP_0 through tea.KEY_KP_9
tea.KEY_KP_ENTER, tea.KEY_KP_EQUAL, tea.KEY_KP_MULTIPLY
tea.KEY_KP_PLUS, tea.KEY_KP_MINUS, tea.KEY_KP_DIVIDE
tea.KEY_KP_DECIMAL, tea.KEY_KP_COMMA, tea.KEY_KP_SEP
tea.KEY_KP_UP, tea.KEY_KP_DOWN, tea.KEY_KP_LEFT, tea.KEY_KP_RIGHT
tea.KEY_KP_HOME, tea.KEY_KP_END, tea.KEY_KP_PG_UP, tea.KEY_KP_PG_DOWN
tea.KEY_KP_INSERT, tea.KEY_KP_DELETE, tea.KEY_KP_BEGIN
```

## Lock & System Keys

```python
tea.KEY_CAPS_LOCK, tea.KEY_SCROLL_LOCK, tea.KEY_NUM_LOCK
tea.KEY_PRINT_SCREEN, tea.KEY_PAUSE, tea.KEY_MENU
```

## Media Keys

```python
tea.KEY_MEDIA_PLAY, tea.KEY_MEDIA_PAUSE, tea.KEY_MEDIA_PLAY_PAUSE
tea.KEY_MEDIA_STOP, tea.KEY_MEDIA_REVERSE
tea.KEY_MEDIA_FAST_FORWARD, tea.KEY_MEDIA_REWIND
tea.KEY_MEDIA_NEXT, tea.KEY_MEDIA_PREV, tea.KEY_MEDIA_RECORD
```

## Volume Keys

```python
tea.KEY_LOWER_VOL, tea.KEY_RAISE_VOL, tea.KEY_MUTE
```

## Modifier Keys (as key codes)

```python
tea.KEY_LEFT_SHIFT, tea.KEY_LEFT_ALT, tea.KEY_LEFT_CTRL
tea.KEY_LEFT_SUPER, tea.KEY_LEFT_HYPER, tea.KEY_LEFT_META
tea.KEY_RIGHT_SHIFT, tea.KEY_RIGHT_ALT, tea.KEY_RIGHT_CTRL
tea.KEY_RIGHT_SUPER, tea.KEY_RIGHT_HYPER, tea.KEY_RIGHT_META
tea.KEY_ISO_LEVEL3_SHIFT, tea.KEY_ISO_LEVEL5_SHIFT
```

## Example

```python
from bubbletea import KEY_UP, KEY_DOWN, KEY_ENTER

def update(self, msg):
    if isinstance(msg, tea.KeyPressMsg):
        if msg.text == KEY_UP:
            self.cursor -= 1
        elif msg.text == KEY_DOWN:
            self.cursor += 1
```
