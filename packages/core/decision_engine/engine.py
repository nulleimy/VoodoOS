from packages.core.conflict_resolution.engine import ConflictResolver
from packages.core.decision_engine.models import DecisionContext, DecisionResult
from packages.core.scoring.engine import ScoringEnvelope


class DecisionEngine:
    def __init__(self) -> None:
        self.resolver = ConflictResolver(
            default_priority={
                "legal": 100,
                "risk": 90,
                "truth": 80,
                "speed": 50,
                "growth": 40,
            }
        )

    def evaluate(self, context: DecisionContext) -> DecisionResult:
        risk_score = min(1.0, 0.15 * len(context.risk_flags))
        confidence_score = 0.85 if context.intent else 0.25

        scoring = ScoringEnvelope(
            risk_score=risk_score,
            confidence_score=confidence_score,
            impact_score=0.7,
            reversibility_score=0.6,
        )

        winner = self.resolver.resolve(
            {
                "legal": 0.9 if "legal" in context.constraints else 0.1,
                "risk": 0.8 if context.risk_flags else 0.2,
                "speed": 0.5,
                "growth": 0.4,
            }
        )

        requires_human_approval = risk_score >= 0.5 or winner == "legal"

        return DecisionResult(
            recommendation=f"Primary decision axis: {winner}",
            reasoning_summary=f"Final weighted score: {scoring.final_score()}",
            risk_score=risk_score,
            confidence_score=confidence_score,
            requires_human_approval=requires_human_approval,
        )
