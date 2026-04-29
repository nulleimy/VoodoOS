from dataclasses import dataclass, field


@dataclass
class CapabilityPolicy:
    agent_id: str
    allowed_capabilities: list[str] = field(default_factory=list)
    requires_human_approval_for: list[str] = field(default_factory=list)
