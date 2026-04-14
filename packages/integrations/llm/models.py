from dataclasses import dataclass


@dataclass
class LLMRequest:
    prompt: str
    requires_privacy: bool = False
    prefer_low_cost: bool = False


@dataclass
class LLMResponse:
    content: str
    provider: str
    fallback_used: bool = False
