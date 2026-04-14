from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List


@dataclass
class AuditEvent:
    event_type: str
    actor_id: str
    target: str
    status: str
    details: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DecisionTrace:
    trace_id: str
    steps: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
