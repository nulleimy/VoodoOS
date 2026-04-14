from packages.governance.policy_engine.models import CapabilityPolicy
from packages.shared.settings.config_loader import ConfigLoader


class CapabilityPolicyLoader:
    def __init__(self) -> None:
        self.config_loader = ConfigLoader()

    def load(self, path: str) -> CapabilityPolicy:
        data = self.config_loader.load_yaml(path)

        return CapabilityPolicy(
            agent_id=data["agent_id"],
            allowed_capabilities=data.get("allowed_capabilities", []),
            requires_human_approval_for=data.get("requires_human_approval_for", []),
        )
