from packages.core.decision_engine.engine import DecisionEngine
from packages.core.decision_engine.models import DecisionContext
from packages.governance.permissions.engine import PermissionEngine
from packages.governance.policy_engine.models import CapabilityPolicy
from packages.integrations.llm.models import LLMRequest
from packages.integrations.llm.router import LLMRouter
from packages.memory.episodic.models import EpisodicMemoryRecord, MemoryScope
from packages.memory.episodic.repository import EpisodicMemoryRepository
from packages.observability.logging.event_logger import EventLogger
from packages.observability.logging.models import AuditEvent
from packages.orchestrator.models import OrchestratorRequest, OrchestratorResponse
from packages.orchestrator.router import IntelligentRouter
from packages.runtime.actions.builtin import echo_action
from packages.runtime.actions.models import ActionRequest
from packages.runtime.actions.registry import ActionRegistry
from packages.runtime.executor.task_executor import TaskExecutor
from packages.workflow.graph_runtime.engine import WorkflowRuntime
from packages.workflow.graph_runtime.models import WorkflowNode


class VoodooOrchestrator:
    def __init__(self) -> None:
        self.decision_engine = DecisionEngine()
        self.llm_router = LLMRouter()
        self.memory_repo = EpisodicMemoryRepository()
        self.workflow_runtime = WorkflowRuntime()
        self.event_logger = EventLogger()
        self.permission_engine = PermissionEngine()
        self.router = IntelligentRouter()

        self.action_registry = ActionRegistry()
        self.action_registry.register("echo_action", echo_action)

        self.task_executor = TaskExecutor(
            registry=self.action_registry,
            permission_engine=self.permission_engine,
            event_logger=self.event_logger,
        )

        self.policy = CapabilityPolicy(
            agent_id="system",
            allowed_capabilities=["echo_action"],
            requires_human_approval_for=[],
        )

    def run(self, request: OrchestratorRequest) -> OrchestratorResponse:
        routing = self.router.route(request.prompt)

        decision = self.decision_engine.evaluate(
            DecisionContext(
                intent=request.prompt,
                constraints=[],
                risk_flags=[],
                metadata=request.metadata,
            )
        )

        llm_provider = "none"
        if "llm" in routing.selected_steps:
            llm_response = self.llm_router.route(
                LLMRequest(
                    prompt=request.prompt,
                    requires_privacy=request.requires_privacy,
                )
            )
            llm_provider = llm_response.provider

        workflow_state = "skipped"
        if "workflow" in routing.selected_steps:
            checkpoint = self.workflow_runtime.execute(
                workflow_id="wf-orchestrator-001",
                nodes=[
                    WorkflowNode(node_id="n1", node_type="decision"),
                    WorkflowNode(node_id="n2", node_type="workflow"),
                ],
            )
            workflow_state = checkpoint.state

        execution_status = "skipped"
        if "execution" in routing.selected_steps:
            execution_result = self.task_executor.execute(
                ActionRequest(
                    action_name="echo_action",
                    payload={"prompt": request.prompt},
                    actor_id=request.actor_id,
                ),
                self.policy,
            )
            execution_status = execution_result.status

        record = EpisodicMemoryRecord(
            record_id="mem-orchestrator-001",
            scope=MemoryScope(user_id="u1", project_id="p1", agent_id=request.actor_id),
            summary=f"Orchestrator processed: {request.prompt}",
            tags=["orchestrator", routing.mode],
        )
        self.memory_repo.add(record)

        self.event_logger.log(
            AuditEvent(
                event_type="orchestrator_run",
                actor_id=request.actor_id,
                target="voodoo_orchestrator",
                status="complete",
                details={
                    "routing_mode": routing.mode,
                    "selected_steps": routing.selected_steps,
                    "llm_provider": llm_provider,
                    "workflow_state": workflow_state,
                    "execution_status": execution_status,
                },
            )
        )

        return OrchestratorResponse(
            recommendation=decision.recommendation,
            llm_provider=llm_provider,
            workflow_state=workflow_state,
            execution_status=execution_status,
            memory_record_id=record.record_id,
            requires_human_approval=routing.requires_human_approval
            or decision.requires_human_approval,
        )
