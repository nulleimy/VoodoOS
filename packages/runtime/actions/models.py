from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class ActionRequest:
    action_name: str
    payload: Dict[str, Any] = field(default_factory=dict)
    actor_id: str = "system"


@dataclass
class ActionResult:
    action_name: str
    status: str
    output: Dict[str, Any] = field(default_factory=dict)
