from typing import List, Optional

from packages.memory.episodic.models import EpisodicMemoryRecord


class EpisodicMemoryRepository:
    def __init__(self) -> None:
        self._records: List[EpisodicMemoryRecord] = []

    def add(self, record: EpisodicMemoryRecord) -> None:
        self._records.append(record)

    def get(self, record_id: str) -> Optional[EpisodicMemoryRecord]:
        for record in self._records:
            if record.record_id == record_id:
                return record
        return None

    def list_all(self) -> List[EpisodicMemoryRecord]:
        return list(self._records)
