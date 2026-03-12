# Program Options

Configuration options passed to `Program()`.

## Options

### `with_input(reader: IO) -> ProgramOption`

Set the input source:

```python
import io
p = tea.Program(model, tea.with_input(io.StringIO("input data")))
```

### `with_output(writer: IO) -> ProgramOption`

Set the output destination:

```python
buf = io.StringIO()
p = tea.Program(model, tea.with_output(buf))
```

### `with_fps(fps: int) -> ProgramOption`

Set the maximum frames per second:

```python
p = tea.Program(model, tea.with_fps(30))
```

### `with_filter(fn) -> ProgramOption`

Set a message filter — `fn(model, msg) -> msg`:

```python
def my_filter(model, msg):
    if isinstance(msg, tea.KeyPressMsg) and msg.text == "x":
        return None  # swallow 'x' key
    return msg

p = tea.Program(model, tea.with_filter(my_filter))
```

### `with_window_size(width, height) -> ProgramOption`

Set the initial window dimensions:

```python
p = tea.Program(model, tea.with_window_size(120, 40))
```

### `with_color_profile(profile: str) -> ProgramOption`

Set the color profile:

```python
p = tea.Program(model, tea.with_color_profile("truecolor"))
```

### `with_environment(env: list[str]) -> ProgramOption`

Set environment variables:

```python
p = tea.Program(model, tea.with_environment(["TERM=xterm-256color"]))
```

### `without_renderer() -> ProgramOption`

Disable the renderer (useful for testing):

```python
p = tea.Program(model, tea.without_renderer())
```

### `without_signal_handler() -> ProgramOption`

Disable built-in signal handling:

```python
p = tea.Program(model, tea.without_signal_handler())
```

### `without_catch_panics() -> ProgramOption`

Let exceptions propagate instead of catching them:

```python
p = tea.Program(model, tea.without_catch_panics())
```
