from packages.integrations.storage.sqlite_memory_store import SQLiteMemoryStore
from packages.memory.episodic.models import EpisodicMemoryRecord, MemoryScope


def test_sqlite_memory_store_add_and_list(tmp_path) -> None:
    db_path = tmp_path / "memory.db"
    store = SQLiteMemoryStore(str(db_path))

    record = EpisodicMemoryRecord(
        record_id="mem-001",
        scope=MemoryScope(user_id="u1", project_id="p1", agent_id="a1"),
        summary="Persistent memory record",
        tags=["persistent", "memory"],
    )

    store.add(record)
    items = store.list_all()

    assert len(items) == 1
    assert items[0].record_id == "mem-001"
    assert "persistent" in items[0].tags
