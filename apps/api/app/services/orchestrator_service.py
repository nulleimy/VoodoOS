from typing import Any, Optional

from packages.orchestrator.engine import VoodooOrchestrator
from packages.orchestrator.models import OrchestratorRequest
from packages.orchestrator.run_store import OrchestratorRunRecord, OrchestratorRunStore


class OrchestratorService:
    def __init__(self) -> None:
        self.orchestrator = VoodooOrchestrator()
        self.run_store = OrchestratorRunStore()

    def run(
        self,
        prompt: str,
        requires_privacy: bool = False,
        actor_id: str = "system",
        metadata: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        resolved_metadata = metadata or {}

        response = self.orchestrator.run(
            OrchestratorRequest(
                prompt=prompt,
                requires_privacy=requires_privacy,
                actor_id=actor_id,
                metadata=resolved_metadata,
            )
        )

        audit_events = [
            event.to_dict()
            for event in self.orchestrator.event_logger.list_events()
            if event.details.get("run_id") == response.run_id
        ]

        record = OrchestratorRunRecord(
            run_id=response.run_id,
            trace_id=response.trace_id,
            created_at=response.created_at,
            actor_id=actor_id,
            prompt=prompt,
            requires_privacy=requires_privacy,
            metadata=resolved_metadata,
            recommendation=response.recommendation,
            llm_provider=response.llm_provider,
            workflow_state=response.workflow_state,
            execution_status=response.execution_status,
            memory_record_id=response.memory_record_id,
            requires_human_approval=response.requires_human_approval,
            routing_mode=response.routing_mode,
            selected_steps=response.selected_steps,
            audit_events=audit_events,
        )
        self.run_store.add(record)

        return record.to_response_dict()

    def get_run(self, run_id: str) -> Optional[dict[str, Any]]:
        record = self.run_store.get(run_id)
        if record is None:
            return None
        return record.to_detail_dict()
