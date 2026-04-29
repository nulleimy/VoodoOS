from dataclasses import asdict, dataclass, field
from typing import Any, Optional


@dataclass
class OrchestratorRunRecord:
    run_id: str
    trace_id: str
    created_at: str
    actor_id: str
    prompt: str
    requires_privacy: bool
    metadata: dict[str, Any]
    recommendation: str
    llm_provider: str
    workflow_state: str
    execution_status: str
    memory_record_id: str
    requires_human_approval: bool
    routing_mode: str
    selected_steps: list[str] = field(default_factory=list)
    audit_events: list[dict[str, Any]] = field(default_factory=list)

    def to_response_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "trace_id": self.trace_id,
            "created_at": self.created_at,
            "recommendation": self.recommendation,
            "llm_provider": self.llm_provider,
            "workflow_state": self.workflow_state,
            "execution_status": self.execution_status,
            "memory_record_id": self.memory_record_id,
            "requires_human_approval": self.requires_human_approval,
            "routing_mode": self.routing_mode,
            "selected_steps": self.selected_steps,
        }

    def to_detail_dict(self) -> dict[str, Any]:
        return asdict(self)


class OrchestratorRunStore:
    def __init__(self) -> None:
        self._records: dict[str, OrchestratorRunRecord] = {}

    def add(self, record: OrchestratorRunRecord) -> None:
        self._records[record.run_id] = record

    def get(self, run_id: str) -> Optional[OrchestratorRunRecord]:
        return self._records.get(run_id)

    def list_all(self) -> list[OrchestratorRunRecord]:
        return list(self._records.values())
