from dataclasses import dataclass
from typing import Optional


@dataclass
class RoutingDecision:
    mode: str
    selected_steps: list[str]
    requires_human_approval: bool = False


class IntelligentRouter:
    def route(self, prompt: str, risk_flags: Optional[list[str]] = None) -> RoutingDecision:
        risk_flags = risk_flags or []

        lowered = prompt.lower()

        if "send" in lowered or "delete" in lowered:
            return RoutingDecision(
                mode="execution",
                selected_steps=["decision", "governance", "execution", "audit"],
                requires_human_approval=True,
            )

        if "analyze" in lowered or "evaluate" in lowered:
            return RoutingDecision(
                mode="analysis",
                selected_steps=["decision", "llm", "memory", "audit"],
                requires_human_approval=False,
            )

        if risk_flags:
            return RoutingDecision(
                mode="guarded",
                selected_steps=["decision", "governance", "workflow", "audit"],
                requires_human_approval=True,
            )

        return RoutingDecision(
            mode="standard",
            selected_steps=["decision", "workflow", "memory", "audit"],
            requires_human_approval=False,
        )
