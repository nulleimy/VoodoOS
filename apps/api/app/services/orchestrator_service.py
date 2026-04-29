from typing import Any, Optional

from packages.orchestrator.engine import VoodooOrchestrator
from packages.orchestrator.models import OrchestratorRequest


class OrchestratorService:
    def __init__(self) -> None:
        self.orchestrator = VoodooOrchestrator()

    def run(
        self,
        prompt: str,
        requires_privacy: bool = False,
        actor_id: str = "system",
        metadata: Optional[dict[str, Any]] = None,
    ) -> dict:
        response = self.orchestrator.run(
            OrchestratorRequest(
                prompt=prompt,
                requires_privacy=requires_privacy,
                actor_id=actor_id,
                metadata=metadata or {},
            )
        )

        return {
            "recommendation": response.recommendation,
            "llm_provider": response.llm_provider,
            "workflow_state": response.workflow_state,
            "execution_status": response.execution_status,
            "memory_record_id": response.memory_record_id,
            "requires_human_approval": response.requires_human_approval,
            "routing_mode": response.routing_mode,
            "selected_steps": response.selected_steps,
        }
