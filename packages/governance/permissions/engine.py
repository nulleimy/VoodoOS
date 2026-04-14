from packages.governance.permissions.models import PermissionDecision, PermissionRequest
from packages.governance.policy_engine.models import CapabilityPolicy


class PermissionEngine:
    def evaluate(
        self,
        request: PermissionRequest,
        policy: CapabilityPolicy,
    ) -> PermissionDecision:
        if request.capability not in policy.allowed_capabilities:
            return PermissionDecision(
                allowed=False,
                requires_human_approval=False,
                reason="Capability not allowed by policy.",
            )

        if request.capability in policy.requires_human_approval_for:
            return PermissionDecision(
                allowed=True,
                requires_human_approval=True,
                reason="Capability allowed but requires human approval.",
            )

        return PermissionDecision(
            allowed=True,
            requires_human_approval=False,
            reason="Capability allowed by policy.",
        )
