from typing import List


class HardStopEvaluator:
    def should_stop(self, risk_flags: List[str]) -> bool:
        stop_flags = {"legal_block", "unsafe_execution", "policy_violation"}
        return any(flag in stop_flags for flag in risk_flags)
