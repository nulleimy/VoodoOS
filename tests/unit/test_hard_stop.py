from packages.governance.hard_stop.engine import HardStopEvaluator


def test_hard_stop_triggers_on_stop_flags() -> None:
    evaluator = HardStopEvaluator()

    assert evaluator.should_stop(["policy_violation"]) is True
    assert evaluator.should_stop(["legal_block"]) is True


def test_hard_stop_ignores_safe_flags() -> None:
    evaluator = HardStopEvaluator()

    assert evaluator.should_stop(["low_confidence"]) is False
