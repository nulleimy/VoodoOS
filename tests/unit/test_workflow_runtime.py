from packages.workflow.graph_runtime.engine import WorkflowRuntime
from packages.workflow.graph_runtime.models import WorkflowNode


def test_workflow_runtime_executes_nodes() -> None:
    runtime = WorkflowRuntime()
    nodes = [
        WorkflowNode(node_id="n1", node_type="decision"),
        WorkflowNode(node_id="n2", node_type="tool_call"),
    ]

    checkpoint = runtime.execute(workflow_id="wf-001", nodes=nodes)

    assert checkpoint.workflow_id == "wf-001"
    assert checkpoint.last_completed_node == "n2"
    assert checkpoint.state == "complete"
