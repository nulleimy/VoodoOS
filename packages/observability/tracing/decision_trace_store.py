from typing import Optional

from packages.observability.logging.models import DecisionTrace


class DecisionTraceStore:
    def __init__(self) -> None:
        self._traces: list[DecisionTrace] = []

    def add(self, trace: DecisionTrace) -> None:
        self._traces.append(trace)

    def get(self, trace_id: str) -> Optional[DecisionTrace]:
        for trace in self._traces:
            if trace.trace_id == trace_id:
                return trace
        return None

    def list_all(self) -> list[DecisionTrace]:
        return list(self._traces)
