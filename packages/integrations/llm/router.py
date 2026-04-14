from typing import Optional

from packages.integrations.llm.models import LLMRequest, LLMResponse
from packages.integrations.llm.providers import BaseLLMProvider, CloudLLMProvider, LocalLLMProvider


class LLMRouter:
    def __init__(
        self,
        local_provider: Optional[BaseLLMProvider] = None,
        cloud_provider: Optional[BaseLLMProvider] = None,
    ) -> None:
        self.local_provider = local_provider or LocalLLMProvider()
        self.cloud_provider = cloud_provider or CloudLLMProvider()

    def route(self, request: LLMRequest) -> LLMResponse:
        if request.requires_privacy:
            return self.local_provider.generate(request)

        try:
            return self.cloud_provider.generate(request)
        except Exception:
            fallback = self.local_provider.generate(request)
            fallback.fallback_used = True
            return fallback
