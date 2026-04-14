from packages.core.decision_engine.engine import DecisionEngine
from packages.core.decision_engine.models import DecisionContext


def test_decision_engine_returns_result() -> None:
    engine = DecisionEngine()
    context = DecisionContext(
        intent="Prepare a contract decision",
        constraints=["legal"],
        risk_flags=["compliance", "liability"],
    )

    result = engine.evaluate(context)

    assert "Primary decision axis" in result.recommendation
    assert result.risk_score > 0
    assert result.confidence_score > 0
    assert result.requires_human_approval is True
