from pydantic import BaseModel


class PipelineRunRequest(BaseModel):
    prompt: str
    requires_privacy: bool = False


class PipelineRunResponse(BaseModel):
    recommendation: str
    llm_provider: str
    workflow_state: str
    memory_record_id: str
    requires_human_approval: bool
