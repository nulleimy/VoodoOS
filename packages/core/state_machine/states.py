from enum import Enum


class ExecutionState(str, Enum):
    IDLE = "idle"
    ANALYSIS = "analysis"
    DECISION = "decision"
    EXECUTION = "execution"
    VERIFY = "verify"
    COMPLETE = "complete"
    FAILURE = "failure"
    RECOVERY = "recovery"
