from packages.core.decision_engine.engine import DecisionEngine
from packages.core.decision_engine.models import DecisionContext
from packages.integrations.llm.models import LLMRequest
from packages.integrations.llm.router import LLMRouter
from packages.memory.episodic.models import EpisodicMemoryRecord, MemoryScope
from packages.memory.episodic.repository import EpisodicMemoryRepository
from packages.workflow.graph_runtime.engine import WorkflowRuntime
from packages.workflow.graph_runtime.models import WorkflowNode


class PipelineService:
    def __init__(self) -> None:
        self.decision_engine = DecisionEngine()
        self.llm_router = LLMRouter()
        self.memory_repo = EpisodicMemoryRepository()
        self.workflow_runtime = WorkflowRuntime()

    def run(self, prompt: str, requires_privacy: bool = False) -> dict:
        decision = self.decision_engine.evaluate(
            DecisionContext(
                intent=prompt,
                constraints=[],
                risk_flags=[],
            )
        )

        llm_response = self.llm_router.route(
            LLMRequest(
                prompt=prompt,
                requires_privacy=requires_privacy,
            )
        )

        checkpoint = self.workflow_runtime.execute(
            workflow_id="wf-pipeline-001",
            nodes=[
                WorkflowNode(node_id="n1", node_type="decision"),
                WorkflowNode(node_id="n2", node_type="llm_call"),
            ],
        )

        record = EpisodicMemoryRecord(
            record_id="mem-pipeline-001",
            scope=MemoryScope(user_id="u1", project_id="p1", agent_id="system"),
            summary=f"Prompt processed: {prompt}",
            tags=["pipeline"],
        )
        self.memory_repo.add(record)

        return {
            "recommendation": decision.recommendation,
            "llm_provider": llm_response.provider,
            "workflow_state": checkpoint.state,
            "memory_record_id": record.record_id,
            "requires_human_approval": decision.requires_human_approval,
        }
