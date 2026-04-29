import json
from pathlib import Path

from packages.observability.logging.models import AuditEvent


class EventLogger:
    def __init__(self) -> None:
        self._events: list[AuditEvent] = []

    def log(self, event: AuditEvent) -> None:
        self._events.append(event)

    def list_events(self) -> list[AuditEvent]:
        return list(self._events)

    def export_json(self, path: str) -> None:
        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        payload = [event.to_dict() for event in self._events]
        file_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
