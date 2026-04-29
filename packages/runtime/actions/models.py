from dataclasses import dataclass, field
from typing import Any


@dataclass
class ActionRequest:
    action_name: str
    payload: dict[str, Any] = field(default_factory=dict)
    actor_id: str = "system"


@dataclass
class ActionResult:
    action_name: str
    status: str
    output: dict[str, Any] = field(default_factory=dict)
