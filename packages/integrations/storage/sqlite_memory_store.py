import sqlite3
from pathlib import Path

from packages.memory.episodic.models import EpisodicMemoryRecord, MemoryScope


class SQLiteMemoryStore:
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        return sqlite3.connect(self.db_path)

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS episodic_memory (
                    record_id TEXT PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    project_id TEXT NOT NULL,
                    agent_id TEXT NOT NULL,
                    summary TEXT NOT NULL,
                    tags TEXT NOT NULL
                )
                """
            )
            conn.commit()

    def add(self, record: EpisodicMemoryRecord) -> None:
        tags = ",".join(record.tags)
        with self._connect() as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO episodic_memory
                (record_id, user_id, project_id, agent_id, summary, tags)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    record.record_id,
                    record.scope.user_id,
                    record.scope.project_id,
                    record.scope.agent_id,
                    record.summary,
                    tags,
                ),
            )
            conn.commit()

    def list_all(self) -> list[EpisodicMemoryRecord]:
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT record_id, user_id, project_id, agent_id, summary, tags
                FROM episodic_memory
                ORDER BY record_id
                """
            ).fetchall()

        results: list[EpisodicMemoryRecord] = []
        for row in rows:
            results.append(
                EpisodicMemoryRecord(
                    record_id=row[0],
                    scope=MemoryScope(
                        user_id=row[1],
                        project_id=row[2],
                        agent_id=row[3],
                    ),
                    summary=row[4],
                    tags=row[5].split(",") if row[5] else [],
                )
            )
        return results
