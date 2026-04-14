from dataclasses import dataclass, field
from typing import List


@dataclass
class CapabilityPolicy:
    agent_id: str
    allowed_capabilities: List[str] = field(default_factory=list)
    requires_human_approval_for: List[str] = field(default_factory=list)
