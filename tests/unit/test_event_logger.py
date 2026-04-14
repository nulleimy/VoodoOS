import json
from pathlib import Path

from packages.observability.logging.event_logger import EventLogger
from packages.observability.logging.models import AuditEvent


def test_event_logger_log_and_list() -> None:
    logger = EventLogger()
    logger.log(
        AuditEvent(
            event_type="permission_check",
            actor_id="agent-1",
            target="send_email",
            status="allowed",
        )
    )

    events = logger.list_events()
    assert len(events) == 1
    assert events[0].event_type == "permission_check"


def test_event_logger_export_json(tmp_path: Path) -> None:
    logger = EventLogger()
    logger.log(
        AuditEvent(
            event_type="workflow_run",
            actor_id="system",
            target="wf-001",
            status="complete",
        )
    )

    output = tmp_path / "audit.json"
    logger.export_json(str(output))

    data = json.loads(output.read_text(encoding="utf-8"))
    assert len(data) == 1
    assert data[0]["target"] == "wf-001"
