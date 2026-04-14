from dataclasses import dataclass, field
from typing import Any


@dataclass
class DecisionContext:
    intent: str
    constraints: list[str] = field(default_factory=list)
    risk_flags: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class DecisionResult:
    recommendation: str
    reasoning_summary: str
    risk_score: float
    confidence_score: float
    requires_human_approval: bool
