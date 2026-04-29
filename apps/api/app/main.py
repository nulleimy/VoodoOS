from fastapi import FastAPI

from apps.api.app.routes.health import router as health_router
from apps.api.app.routes.orchestrator import router as orchestrator_router
from apps.api.app.routes.pipeline import router as pipeline_router

app = FastAPI(title="VoodoOS API", version="0.1.0")

app.include_router(health_router)
app.include_router(orchestrator_router)
app.include_router(pipeline_router)
