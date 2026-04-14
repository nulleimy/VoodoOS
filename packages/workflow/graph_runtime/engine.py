from packages.workflow.graph_runtime.models import WorkflowCheckpoint, WorkflowNode
from packages.workflow.scheduler.engine import WorkflowScheduler


class WorkflowRuntime:
    def __init__(self) -> None:
        self.scheduler = WorkflowScheduler()

    def execute(
        self,
        workflow_id: str,
        nodes: list[WorkflowNode],
    ) -> WorkflowCheckpoint:
        return self.scheduler.run(workflow_id=workflow_id, nodes=nodes)
