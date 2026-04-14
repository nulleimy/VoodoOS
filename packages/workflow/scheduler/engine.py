from packages.workflow.graph_runtime.models import WorkflowCheckpoint, WorkflowNode
from packages.workflow.retries.policy import RetryPolicy


class WorkflowScheduler:
    def __init__(self, retry_policy: RetryPolicy | None = None) -> None:
        self.retry_policy = retry_policy or RetryPolicy()

    def run(
        self,
        workflow_id: str,
        nodes: list[WorkflowNode],
    ) -> WorkflowCheckpoint:
        checkpoint = WorkflowCheckpoint(workflow_id=workflow_id, state="analysis")

        for node in nodes:
            checkpoint.last_completed_node = node.node_id
            checkpoint.state = f"completed:{node.node_type}"

        checkpoint.state = "complete"
        return checkpoint
