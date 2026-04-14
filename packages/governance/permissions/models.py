from dataclasses import dataclass


@dataclass
class PermissionRequest:
    agent_id: str
    capability: str
    reason: str


@dataclass
class PermissionDecision:
    allowed: bool
    requires_human_approval: bool
    reason: str
