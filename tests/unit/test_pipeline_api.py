from fastapi.testclient import TestClient

from apps.api.app.main import app


def test_pipeline_run_endpoint() -> None:
    client = TestClient(app)

    response = client.post(
        "/pipeline/run",
        json={"prompt": "Analyze this decision", "requires_privacy": True},
    )

    assert response.status_code == 200
    data = response.json()
    assert "recommendation" in data
    assert data["llm_provider"] == "local"
    assert data["workflow_state"] == "complete"
    assert data["memory_record_id"] == "mem-pipeline-001"
