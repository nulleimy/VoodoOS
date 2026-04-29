import json
import sqlite3
from pathlib import Path

from packages.observability.logging.models import AuditEvent


class SQLiteAuditStore:
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
                CREATE TABLE IF NOT EXISTS audit_events (
                    event_type TEXT NOT NULL,
                    actor_id TEXT NOT NULL,
                    target TEXT NOT NULL,
                    status TEXT NOT NULL,
                    details TEXT NOT NULL
                )
                """
            )
            conn.commit()

    def add(self, event: AuditEvent) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO audit_events
                (event_type, actor_id, target, status, details)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    event.event_type,
                    event.actor_id,
                    event.target,
                    event.status,
                    json.dumps(event.details),
                ),
            )
            conn.commit()

    def list_all(self) -> list[AuditEvent]:
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT event_type, actor_id, target, status, details
                FROM audit_events
                """
            ).fetchall()

        return [
            AuditEvent(
                event_type=row[0],
                actor_id=row[1],
                target=row[2],
                status=row[3],
                details=json.loads(row[4]),
            )
            for row in rows
        ]
