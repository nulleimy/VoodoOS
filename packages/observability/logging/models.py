from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class AuditEvent:
    event_type: str
    actor_id: str
    target: str
    status: str
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class DecisionTrace:
    trace_id: str
    steps: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
