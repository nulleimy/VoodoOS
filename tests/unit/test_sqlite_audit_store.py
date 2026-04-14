from packages.integrations.storage.sqlite_audit_store import SQLiteAuditStore
from packages.observability.logging.models import AuditEvent


def test_sqlite_audit_store_add_and_list(tmp_path) -> None:
    db_path = tmp_path / "audit.db"
    store = SQLiteAuditStore(str(db_path))

    event = AuditEvent(
        event_type="decision_made",
        actor_id="system",
        target="pipeline",
        status="ok",
        details={"score": 0.92},
    )

    store.add(event)
    items = store.list_all()

    assert len(items) == 1
    assert items[0].event_type == "decision_made"
    assert items[0].details["score"] == 0.92
