from typing import List, Optional

from packages.observability.logging.models import DecisionTrace


class DecisionTraceStore:
    def __init__(self) -> None:
        self._traces: List[DecisionTrace] = []

    def add(self, trace: DecisionTrace) -> None:
        self._traces.append(trace)

    def get(self, trace_id: str) -> Optional[DecisionTrace]:
        for trace in self._traces:
            if trace.trace_id == trace_id:
                return trace
        return None

    def list_all(self) -> List[DecisionTrace]:
        return list(self._traces)
