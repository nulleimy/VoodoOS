from packages.core.state_machine.states import ExecutionState


def test_execution_state_values() -> None:
    assert ExecutionState.IDLE.value == "idle"
    assert ExecutionState.RECOVERY.value == "recovery"
