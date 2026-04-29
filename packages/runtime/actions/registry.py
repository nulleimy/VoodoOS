from typing import Callable

from packages.runtime.actions.models import ActionRequest, ActionResult


class ActionRegistry:
    def __init__(self) -> None:
        self._actions: dict[str, Callable[[ActionRequest], ActionResult]] = {}

    def register(self, name: str, handler: Callable[[ActionRequest], ActionResult]) -> None:
        self._actions[name] = handler

    def get(self, name: str) -> Callable[[ActionRequest], ActionResult]:
        if name not in self._actions:
            raise KeyError(f"Unknown action: {name}")
        return self._actions[name]
