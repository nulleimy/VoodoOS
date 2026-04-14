from packages.orchestrator.engine import VoodooOrchestrator
from packages.orchestrator.models import OrchestratorRequest


def test_orchestrator_runs_end_to_end() -> None:
    orchestrator = VoodooOrchestrator()

    response = orchestrator.run(
        OrchestratorRequest(
            prompt="Evaluate this situation and respond",
            requires_privacy=True,
            actor_id="system",
        )
    )

    assert "Primary decision axis" in response.recommendation
    assert response.llm_provider == "local"
    assert response.workflow_state == "skipped"
    assert response.execution_status == "skipped"
    assert response.memory_record_id == "mem-orchestrator-001"
