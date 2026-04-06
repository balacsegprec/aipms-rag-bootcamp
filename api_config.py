import os
from dataclasses import dataclass
from typing import Dict, List
from dotenv import load_dotenv

# Load .env
load_dotenv()


# ============================================================================
# DATA CLASSES
# ============================================================================

@dataclass
class GroqConfig:
    api_key: str
    base_url: str = "https://api.groq.com/openai/v1"
    model: str = "llama-3.3-70b-versatile"
    model_fast: str = "llama-3.1-8b-instant"
    rate_limit_delay: float = 2.0

    def is_configured(self):
        return bool(self.api_key and "placeholder" not in self.api_key)


@dataclass
class GoogleConfig:
    api_key: str
    model: str = "gemini-2.5-flash"
    rate_limit_delay: float = 1.0

    def is_configured(self):
        return bool(self.api_key and "placeholder" not in self.api_key)


@dataclass
class HuggingFaceConfig:
    token: str
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"

    def is_configured(self):
        return bool(self.token and "placeholder" not in self.token)


@dataclass
class OpenRouterConfig:
    api_key: str
    base_url: str = "https://openrouter.ai/api/v1"
    model: str = "deepseek/deepseek-chat-v3-0324:free"

    def is_configured(self):
        return bool(self.api_key and "placeholder" not in self.api_key)


@dataclass
class CerebrasConfig:
    api_key: str
    base_url: str = "https://api.cerebras.ai/v1"
    model: str = "llama-3.3-70b"

    def is_configured(self):
        return bool(self.api_key and "placeholder" not in self.api_key)


@dataclass
class EmbeddingModelConfig:
    primary: str = "all-MiniLM-L6-v2"
    reranker: str = "cross-encoder/ms-marco-MiniLM-L-12-v2"


# ============================================================================
# MAIN CONFIG
# ============================================================================

class Config:
    def __init__(self):

        # APIs
        self.groq = GroqConfig(
            api_key=os.getenv("GROQ_API_KEY", ""),
            model=os.getenv("LLM_MODEL_GROQ", "llama-3.3-70b-versatile")
        )

        self.google = GoogleConfig(
            api_key=os.getenv("GOOGLE_API_KEY", ""),
            model=os.getenv("LLM_MODEL_GOOGLE", "gemini-2.5-flash")
        )

        self.huggingface = HuggingFaceConfig(
            token=os.getenv("HF_TOKEN", ""),
            embedding_model=os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
        )

        self.openrouter = OpenRouterConfig(
            api_key=os.getenv("OPENROUTER_API_KEY", "")
        )

        self.cerebras = CerebrasConfig(
            api_key=os.getenv("CEREBRAS_API_KEY", "")
        )

        # Models
        self.embedding_models = EmbeddingModelConfig(
            primary=os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2"),
            reranker=os.getenv("RERANKER_MODEL", "cross-encoder/ms-marco-MiniLM-L-12-v2")
        )

        # Fallback order
        fallback_str = os.getenv("LLM_FALLBACK_ORDER", "groq,openrouter,cerebras,google")
        self.llm_fallback_order = [x.strip() for x in fallback_str.split(",")]

    # ============================================================================
    # METHODS
    # ============================================================================

    def validate(self) -> Dict[str, bool]:
        return {
            "groq": self.groq.is_configured(),
            "google": self.google.is_configured(),
            "huggingface": self.huggingface.is_configured(),
            "openrouter": self.openrouter.is_configured(),
            "cerebras": self.cerebras.is_configured(),
        }

    def get_configured_apis(self) -> List[str]:
        return [k for k, v in self.validate().items() if v]

    def get_llm_fallback_order(self) -> List[str]:
        configured = self.get_configured_apis()
        return [p for p in self.llm_fallback_order if p in configured]


# ============================================================================
# SINGLETON
# ============================================================================

_config = Config()


def get_config() -> Config:
    return _config