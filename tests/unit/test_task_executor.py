from packages.governance.permissions.engine import PermissionEngine
from packages.governance.policy_engine.models import CapabilityPolicy
from packages.observability.logging.event_logger import EventLogger
from packages.runtime.actions.builtin import echo_action
from packages.runtime.actions.models import ActionRequest
from packages.runtime.actions.registry import ActionRegistry
from packages.runtime.executor.task_executor import TaskExecutor


def test_task_executor_executes_allowed_action() -> None:
    registry = ActionRegistry()
    registry.register("echo_action", echo_action)

    executor = TaskExecutor(
        registry=registry,
        permission_engine=PermissionEngine(),
        event_logger=EventLogger(),
    )

    policy = CapabilityPolicy(
        agent_id="system",
        allowed_capabilities=["echo_action"],
        requires_human_approval_for=[],
    )

    result = executor.execute(
        ActionRequest(action_name="echo_action", payload={"hello": "world"}),
        policy,
    )

    assert result.status == "ok"
    assert result.output["echo"]["hello"] == "world"


def test_task_executor_denies_unapproved_action() -> None:
    registry = ActionRegistry()
    registry.register("echo_action", echo_action)

    executor = TaskExecutor(
        registry=registry,
        permission_engine=PermissionEngine(),
        event_logger=EventLogger(),
    )

    policy = CapabilityPolicy(
        agent_id="system",
        allowed_capabilities=[],
        requires_human_approval_for=[],
    )

    result = executor.execute(
        ActionRequest(action_name="echo_action", payload={"hello": "world"}),
        policy,
    )

    assert result.status == "denied"
