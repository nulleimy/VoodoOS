from packages.memory.episodic.models import EpisodicMemoryRecord, MemoryScope
from packages.memory.episodic.repository import EpisodicMemoryRepository


def test_memory_repository_add_and_get() -> None:
    repo = EpisodicMemoryRepository()
    record = EpisodicMemoryRecord(
        record_id="mem-001",
        scope=MemoryScope(user_id="u1", project_id="p1", agent_id="a1"),
        summary="Negotiation outcome stored.",
        tags=["negotiation", "outcome"],
    )

    repo.add(record)
    fetched = repo.get("mem-001")

    assert fetched is not None
    assert fetched.record_id == "mem-001"
    assert fetched.summary == "Negotiation outcome stored."


def test_memory_repository_list_all() -> None:
    repo = EpisodicMemoryRepository()
    repo.add(
        EpisodicMemoryRecord(
            record_id="mem-002",
            scope=MemoryScope(user_id="u1", project_id="p1", agent_id="a1"),
            summary="Second record",
        )
    )

    assert len(repo.list_all()) == 1
