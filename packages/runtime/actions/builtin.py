from packages.runtime.actions.models import ActionRequest, ActionResult


def echo_action(request: ActionRequest) -> ActionResult:
    return ActionResult(
        action_name=request.action_name,
        status="ok",
        output={"echo": request.payload},
    )


def simulate_external_call_action(request: ActionRequest) -> ActionResult:
    return ActionResult(
        action_name=request.action_name,
        status="ok",
        output={"message": "Simulated external call complete."},
    )
