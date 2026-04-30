from fastapi import APIRouter, HTTPException

from apps.api.app.schemas.orchestrator import (
    OrchestratorRunDetailResponse,
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


@router.get("/runs/{run_id}", response_model=OrchestratorRunDetailResponse)
def get_orchestrator_run(run_id: str) -> OrchestratorRunDetailResponse:
    result = service.get_run(run_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Orchestrator run not found")
    return OrchestratorRunDetailResponse(**result)
