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
    assert payload["run_id"].startswith("run-")
    assert payload["trace_id"].startswith("trace-")
    assert payload["created_at"]
    assert "Primary decision axis" in payload["recommendation"]
    assert payload["llm_provider"] == "local"
    assert payload["workflow_state"] == "skipped"
    assert payload["execution_status"] == "skipped"
    assert payload["memory_record_id"] == "mem-orchestrator-001"
    assert payload["routing_mode"] == "analysis"
    assert payload["selected_steps"] == ["decision", "llm", "memory", "audit"]
    assert payload["requires_human_approval"] is False


def test_orchestrator_api_can_retrieve_run_detail() -> None:
    create_response = client.post(
        "/orchestrator/run",
        json={
            "prompt": "Evaluate this situation and store the run",
            "requires_privacy": False,
            "actor_id": "system",
            "metadata": {"source": "detail-test"},
        },
    )

    assert create_response.status_code == 200
    run_id = create_response.json()["run_id"]

    detail_response = client.get(f"/orchestrator/runs/{run_id}")

    assert detail_response.status_code == 200

    payload = detail_response.json()
    assert payload["run_id"] == run_id
    assert payload["trace_id"].startswith("trace-")
    assert payload["actor_id"] == "system"
    assert payload["prompt"] == "Evaluate this situation and store the run"
    assert payload["metadata"] == {"source": "detail-test"}
    assert payload["routing_mode"] == "analysis"
    assert payload["audit_events"]
    assert payload["audit_events"][0]["details"]["run_id"] == run_id


def test_orchestrator_api_returns_404_for_unknown_run() -> None:
    response = client.get("/orchestrator/runs/run-does-not-exist")

    assert response.status_code == 404
    assert response.json()["detail"] == "Orchestrator run not found"


def test_orchestrator_api_requires_prompt() -> None:
    response = client.post(
        "/orchestrator/run",
        json={
            "prompt": "",
        },
    )

    assert response.status_code == 422
