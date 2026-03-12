# Commands

Commands (`Cmd`) are callables that produce messages. They run asynchronously — the program dispatches them in background threads.

## Type

```python
Cmd = Callable[[], Msg] | None
```

## Message Producers

These return a message directly (use as the `cmd` in `update`'s return):

| Function | Returns | Description |
|----------|---------|-------------|
| `quit_cmd()` | `QuitMsg` | Quit the program |
| `interrupt()` | `InterruptMsg` | Signal interrupt |
| `suspend()` | `SuspendMsg` | Suspend the program |
| `clear_screen()` | `ClearScreenMsg` | Clear the screen |
| `read_clipboard()` | Msg | Request clipboard |
| `read_primary_clipboard()` | Msg | Request primary clipboard |
| `request_window_size()` | Msg | Request window dimensions |
| `request_cursor_position()` | Msg | Request cursor position |
| `request_background_color()` | Msg | Request bg color |
| `request_foreground_color()` | Msg | Request fg color |
| `request_cursor_color()` | Msg | Request cursor color |
| `request_terminal_version()` | Msg | Request terminal version |

```python
def update(self, msg):
    if isinstance(msg, tea.KeyPressMsg) and msg.text == "q":
        return self, tea.quit_cmd  # pass the function itself as Cmd
```

## Command Factories

These return a `Cmd` (a callable):

### `batch(*cmds) -> Cmd`

Run multiple commands concurrently:

```python
cmd = tea.batch(tea.printf("Loading..."), some_async_task)
```

### `sequence(*cmds) -> Cmd`

Run commands sequentially:

```python
cmd = tea.sequence(load_data, render_results)
```

### `tick(duration, fn) -> Cmd`

Fire once after `duration` seconds:

```python
cmd = tea.tick(1.0, lambda t: TickMsg(t))
```

### `every(duration, fn) -> Cmd`

Fire repeatedly every `duration` seconds:

```python
cmd = tea.every(5.0, lambda t: PollMsg(t))
```

### `printf(template, *args) -> Cmd`

Print formatted text:

```python
cmd = tea.printf("Loaded %d items", count)
```

### `println(*args) -> Cmd`

Print a line:

```python
cmd = tea.println("Ready!")
```

### `set_clipboard(s) -> Cmd` / `set_primary_clipboard(s) -> Cmd`

Set clipboard content:

```python
cmd = tea.set_clipboard("copied text")
```

### `request_capability(s) -> Cmd`

Query a terminal capability:

```python
cmd = tea.request_capability("rgb")
```

### `raw(data) -> Cmd`

Send raw data:

```python
cmd = tea.raw(b"\x1b[0m")
```
