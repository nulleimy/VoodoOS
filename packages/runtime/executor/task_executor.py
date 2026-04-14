from packages.governance.permissions.engine import PermissionEngine
from packages.governance.permissions.models import PermissionRequest
from packages.governance.policy_engine.models import CapabilityPolicy
from packages.observability.logging.event_logger import EventLogger
from packages.observability.logging.models import AuditEvent
from packages.runtime.actions.models import ActionRequest, ActionResult
from packages.runtime.actions.registry import ActionRegistry


class TaskExecutor:
    def __init__(
        self,
        registry: ActionRegistry,
        permission_engine: PermissionEngine,
        event_logger: EventLogger,
    ) -> None:
        self.registry = registry
        self.permission_engine = permission_engine
        self.event_logger = event_logger

    def execute(
        self,
        request: ActionRequest,
        policy: CapabilityPolicy,
    ) -> ActionResult:
        permission = self.permission_engine.evaluate(
            PermissionRequest(
                agent_id=request.actor_id,
                capability=request.action_name,
                reason="Runtime execution request",
            ),
            policy,
        )

        if not permission.allowed:
            self.event_logger.log(
                AuditEvent(
                    event_type="action_execution",
                    actor_id=request.actor_id,
                    target=request.action_name,
                    status="denied",
                    details={"reason": permission.reason},
                )
            )
            return ActionResult(
                action_name=request.action_name,
                status="denied",
                output={"reason": permission.reason},
            )

        handler = self.registry.get(request.action_name)
        result = handler(request)

        self.event_logger.log(
            AuditEvent(
                event_type="action_execution",
                actor_id=request.actor_id,
                target=request.action_name,
                status=result.status,
                details=result.output,
            )
        )

        return result
