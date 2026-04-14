from packages.observability.logging.models import DecisionTrace
from packages.observability.tracing.decision_trace_store import DecisionTraceStore


def test_decision_trace_store_add_and_get() -> None:
    store = DecisionTraceStore()
    trace = DecisionTrace(
        trace_id="trace-001",
        steps=["intent_parsed", "risk_scored", "recommendation_generated"],
    )

    store.add(trace)
    fetched = store.get("trace-001")

    assert fetched is not None
    assert fetched.trace_id == "trace-001"
    assert len(fetched.steps) == 3
