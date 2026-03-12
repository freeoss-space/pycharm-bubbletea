# Program

The `Program` class manages the event loop for a Bubble Tea application.

## Creating a Program

```python
import bubbletea as tea

p = tea.Program(model)
p = tea.Program(model, tea.with_fps(30), tea.without_renderer())
```

## Methods

### `run() -> Model`

Start the event loop. Blocks until the program exits. Returns the final model.

```python
final_model = p.run()
```

### `send(msg: Msg) -> None`

Send a message to the program from outside the event loop:

```python
p.send(tea.WindowSizeMsg(width=120, height=40))
```

### `quit() -> None`

Send a `QuitMsg` to gracefully stop the program:

```python
p.quit()
```

### `kill() -> None`

Immediately stop the program:

```python
p.kill()
```

### `wait() -> None`

Block until the program finishes:

```python
p.wait()
```

### `release_terminal() -> None`

Release terminal resources (for spawning subprocesses).

### `restore_terminal() -> None`

Restore terminal after `release_terminal()`.

### `printf(template, *args) -> None`

Print formatted text to the program's output:

```python
p.printf("Status: %s", status)
```

### `println(*args) -> None`

Print a line to the program's output:

```python
p.println("Ready!")
```

## Example

```python
import bubbletea as tea
import threading


class MyModel(tea.Model):
    def __init__(self):
        self.text = "waiting..."

    def init(self):
        return None

    def update(self, msg):
        if isinstance(msg, tea.QuitMsg):
            return self, None
        return self, None

    def view(self):
        return tea.View(self.text)


p = tea.Program(MyModel(), tea.without_renderer())

# Send messages from another thread
def background():
    import time
    time.sleep(1)
    p.quit()

threading.Thread(target=background).start()
final = p.run()
```
