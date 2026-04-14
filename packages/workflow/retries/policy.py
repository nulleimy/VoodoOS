from dataclasses import dataclass


@dataclass
class RetryPolicy:
    max_attempts: int = 3
    backoff_seconds: float = 0.0

    def should_retry(self, attempt: int) -> bool:
        return attempt < self.max_attempts
