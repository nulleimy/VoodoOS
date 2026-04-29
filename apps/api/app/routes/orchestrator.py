from fastapi import APIRouter

from apps.api.app.schemas.orchestrator import (
    OrchestratorRunRequest,
    OrchestratorRunResponse,
)
from apps.api.app.services.orchestrator_service import OrchestratorService

router = APIRouter(prefix="/orchestrator", tags=["orchestrator"])

service = OrchestratorService()


@router.post("/run", response_model=OrchestratorRunResponse)
def run_orchestrator(payload: OrchestratorRunRequest) -> OrchestratorRunResponse:
    result = service.run(
        prompt=payload.prompt,
        requires_privacy=payload.requires_privacy,
        actor_id=payload.actor_id,
        metadata=payload.metadata,
    )
    return OrchestratorRunResponse(**result)
