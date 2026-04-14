from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class MemoryScope:
    user_id: str
    project_id: str
    agent_id: str


@dataclass
class EpisodicMemoryRecord:
    record_id: str
    scope: MemoryScope
    summary: str
    tags: List[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
