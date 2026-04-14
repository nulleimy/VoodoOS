from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class OrchestratorRequest:
    prompt: str
    requires_privacy: bool = False
    actor_id: str = "system"
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class OrchestratorResponse:
    recommendation: str
    llm_provider: str
    workflow_state: str
    execution_status: str
    memory_record_id: str
    requires_human_approval: bool
