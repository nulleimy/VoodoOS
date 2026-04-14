from packages.integrations.llm.models import LLMRequest, LLMResponse


class BaseLLMProvider:
    provider_name = "base"

    def generate(self, request: LLMRequest) -> LLMResponse:
        raise NotImplementedError


class LocalLLMProvider(BaseLLMProvider):
    provider_name = "local"

    def generate(self, request: LLMRequest) -> LLMResponse:
        return LLMResponse(
            content=f"LOCAL::{request.prompt}",
            provider=self.provider_name,
            fallback_used=False,
        )


class CloudLLMProvider(BaseLLMProvider):
    provider_name = "cloud"

    def generate(self, request: LLMRequest) -> LLMResponse:
        return LLMResponse(
            content=f"CLOUD::{request.prompt}",
            provider=self.provider_name,
            fallback_used=False,
        )


class FailingCloudLLMProvider(BaseLLMProvider):
    provider_name = "cloud"

    def generate(self, request: LLMRequest) -> LLMResponse:
        raise RuntimeError("Cloud provider unavailable")
