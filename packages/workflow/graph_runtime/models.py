from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class WorkflowNode:
    node_id: str
    node_type: str
    payload: dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkflowCheckpoint:
    workflow_id: str
    last_completed_node: Optional[str] = None
    state: str = "idle"
    metadata: dict[str, Any] = field(default_factory=dict)
