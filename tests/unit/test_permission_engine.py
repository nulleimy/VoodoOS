from packages.governance.permissions.engine import PermissionEngine
from packages.governance.permissions.models import PermissionRequest
from packages.governance.policy_engine.models import CapabilityPolicy


def test_permission_engine_allows_standard_capability() -> None:
    engine = PermissionEngine()
    request = PermissionRequest(
        agent_id="agent-1",
        capability="read_memory",
        reason="Need context",
    )
    policy = CapabilityPolicy(
        agent_id="agent-1",
        allowed_capabilities=["read_memory", "write_memory"],
        requires_human_approval_for=[],
    )

    decision = engine.evaluate(request, policy)

    assert decision.allowed is True
    assert decision.requires_human_approval is False


def test_permission_engine_requires_approval() -> None:
    engine = PermissionEngine()
    request = PermissionRequest(
        agent_id="agent-1",
        capability="send_email",
        reason="External communication",
    )
    policy = CapabilityPolicy(
        agent_id="agent-1",
        allowed_capabilities=["send_email"],
        requires_human_approval_for=["send_email"],
    )

    decision = engine.evaluate(request, policy)

    assert decision.allowed is True
    assert decision.requires_human_approval is True


def test_permission_engine_denies_unlisted_capability() -> None:
    engine = PermissionEngine()
    request = PermissionRequest(
        agent_id="agent-1",
        capability="delete_records",
        reason="Dangerous operation",
    )
    policy = CapabilityPolicy(
        agent_id="agent-1",
        allowed_capabilities=["read_memory"],
        requires_human_approval_for=[],
    )

    decision = engine.evaluate(request, policy)

    assert decision.allowed is False
