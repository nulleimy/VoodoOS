from fastapi.testclient import TestClient

from apps.api.app.main import app

client = TestClient(app)


def test_orchestrator_api_runs_analysis_mode() -> None:
    response = client.post(
        "/orchestrator/run",
        json={
            "prompt": "Evaluate this situation and respond",
            "requires_privacy": True,
            "actor_id": "system",
            "metadata": {"source": "unit-test"},
        },
    )

    assert response.status_code == 200

    payload = response.json()
    assert "Primary decision axis" in payload["recommendation"]
    assert payload["llm_provider"] == "local"
    assert payload["workflow_state"] == "skipped"
    assert payload["execution_status"] == "skipped"
    assert payload["memory_record_id"] == "mem-orchestrator-001"
    assert payload["routing_mode"] == "analysis"
    assert payload["selected_steps"] == ["decision", "llm", "memory", "audit"]
    assert payload["requires_human_approval"] is False


def test_orchestrator_api_requires_prompt() -> None:
    response = client.post(
        "/orchestrator/run",
        json={
            "prompt": "",
        },
    )

    assert response.status_code == 422
