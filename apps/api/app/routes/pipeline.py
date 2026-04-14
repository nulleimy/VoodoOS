from fastapi import APIRouter

from apps.api.app.schemas.pipeline import PipelineRunRequest, PipelineRunResponse
from apps.api.app.services.pipeline_service import PipelineService

router = APIRouter(prefix="/pipeline", tags=["pipeline"])

service = PipelineService()


@router.post("/run", response_model=PipelineRunResponse)
def run_pipeline(payload: PipelineRunRequest) -> PipelineRunResponse:
    result = service.run(
        prompt=payload.prompt,
        requires_privacy=payload.requires_privacy,
    )
    return PipelineRunResponse(**result)
