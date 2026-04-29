from typing import Any

from pydantic import BaseModel, Field


class OrchestratorRunRequest(BaseModel):
    prompt: str = Field(..., min_length=1)
    requires_privacy: bool = False
    actor_id: str = "system"
    metadata: dict[str, Any] = Field(default_factory=dict)


class OrchestratorRunResponse(BaseModel):
    recommendation: str
    llm_provider: str
    workflow_state: str
    execution_status: str
    memory_record_id: str
    requires_human_approval: bool
    routing_mode: str
    selected_steps: list[str]
