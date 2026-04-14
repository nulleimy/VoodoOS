from packages.orchestrator.engine import VoodooOrchestrator
from packages.orchestrator.models import OrchestratorRequest


def test_orchestrator_uses_analysis_routing() -> None:
    orchestrator = VoodooOrchestrator()

    response = orchestrator.run(
        OrchestratorRequest(
            prompt="Analyze this contract",
            requires_privacy=True,
            actor_id="system",
        )
    )

    assert response.llm_provider == "local"
    assert response.workflow_state == "skipped"
    assert response.execution_status == "skipped"


def test_orchestrator_uses_execution_routing() -> None:
    orchestrator = VoodooOrchestrator()

    response = orchestrator.run(
        OrchestratorRequest(
            prompt="Send this message now",
            requires_privacy=False,
            actor_id="system",
        )
    )

    assert response.execution_status == "ok"
    assert response.requires_human_approval is True
