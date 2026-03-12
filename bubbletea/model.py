"""Model protocol mirroring Bubble Tea v2 Model interface."""

from __future__ import annotations

from typing import Any, Optional, Protocol, Tuple, runtime_checkable

from bubbletea.view import View


@runtime_checkable
class Model(Protocol):
    """The Elm Architecture model interface.

    Implement this protocol to create a Bubble Tea application:
    - ``init()`` returns an optional initial command.
    - ``update(msg)`` handles messages, returning ``(new_model, cmd)``.
    - ``view()`` returns a ``View`` describing the UI.
    """

    def init(self) -> Any:
        """Return an initial Cmd (or None)."""
        ...

    def update(self, msg: Any) -> Tuple["Model", Any]:
        """Process a message and return (updated_model, cmd)."""
        ...

    def view(self) -> View:
        """Return the current view."""
        ...
