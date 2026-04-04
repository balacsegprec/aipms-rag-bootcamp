# ============================================================================
# AI-PMS RAG Bootcamp — API Configuration Management
# 
# Purpose: Centralized, secure configuration for all free APIs
# This file loads settings from .env and provides easy access
# ============================================================================

import os
from typing import Dict, Optional
from dataclasses import dataclass
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)


# ============================================================================
# DATA CLASSES FOR TYPE SAFETY
# ============================================================================

@dataclass
class GroqConfig:
    """Groq API configuration"""
    api_key: str
    base_url: str = "https://api.groq.com/openai/v1"
    model: str = "llama-3.3-70b-versatile"
    model_fast: str = "llama-3.1-8b-instant"
    rate_limit_delay: float = 2.0  # seconds
    
    def is_configured(self) -> bool:
        return bool(self.api_key and self.api_key != "gsk_xxx_placeholder_xxx")


@dataclass
class GoogleConfig:
    """Google AI Studio configuration"""
    api_key: str
    model: str = "gemini-2.5-flash"
    rate_limit_delay: float = 1.0  # seconds
    
    def is_configured(self) -> bool:
        return bool(self.api_key and self.api_key != "AIza_xxx_placeholder_xxx")


@dataclass
class HuggingFaceConfig:
    """HuggingFace configuration"""
    token: str
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    base_url: str = "https://api-inference.huggingface.co"
    rate_limit_delay: float = 36.0  # seconds
    
    def is_configured(self) -> bool:
        return bool(self.token and self.token != "hf_xxx_placeholder_xxx")


@dataclass
class OpenRouterConfig:
    """OpenRouter configuration"""
    api_key: str
    base_url: str = "https://openrouter.ai/api/v1"
    model: str = "deepseek/deepseek-chat-v3-0324:free"
    
    def is_configured(self) -> bool:
        return bool(self.api_key and self.api_key != "sk-or-xxx_placeholder_xxx")


@dataclass
class CerebrasConfig:
    """Cerebras configuration"""
    api_key: str
    base_url: str = "https://api.cerebras.ai/v1"
    model: str = "llama-3.3-70b"
    
    def is_configured(self) -> bool:
        return bool(self.api_key and self.api_key != "csk_xxx_placeholder_xxx")


@dataclass
class DatabaseConfig:
    """PostgreSQL + pgvector configuration"""
    host: str
    port: int
    user: str
    password: str
    database: str
    
    def get_connection_string(self) -> str:
        """Generate PostgreSQL connection string"""
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
    
    def is_configured(self) -> bool:
        return all([self.host, self.port, self.user, self.database])


@dataclass
class EmbeddingModelConfig:
    """Embedding model configuration"""
    primary: str = "all-MiniLM-L6-v2"
    bge: str = "BAAI/bge-large-en-v1.5"
    nomic: str = "nomic-ai/nomic-embed-text-v1.5"
    reranker: str = "cross-encoder/ms-marco-MiniLM-L-12-v2"


# ============================================================================
# MAIN CONFIGURATION CLASS
# ============================================================================

class Config:
    """Master configuration for RAG bootcamp no-GPU setup"""
    
    def __init__(self):
        """Initialize all configurations from environment variables"""
        
        # LLM APIs
        self.groq = GroqConfig(
            api_key=os.getenv("GROQ_API_KEY", "gsk_xxx_placeholder_xxx"),
            model=os.getenv("LLM_MODEL_GROQ", "llama-3.3-70b-versatile"),
            model_fast=os.getenv("LLM_MODEL_GROQ_FAST", "llama-3.1-8b-instant"),
            rate_limit_delay=float(os.getenv("GROQ_RATE_LIMIT_DELAY_SECONDS", "2"))
        )
        
        self.google = GoogleConfig(
            api_key=os.getenv("GOOGLE_API_KEY", "AIza_xxx_placeholder_xxx"),
            model=os.getenv("LLM_MODEL_GOOGLE", "gemini-2.5-flash"),
            rate_limit_delay=float(os.getenv("GOOGLE_RATE_LIMIT_DELAY_SECONDS", "1"))
        )
        
        self.huggingface = HuggingFaceConfig(
            token=os.getenv("HF_TOKEN", "hf_xxx_placeholder_xxx"),
            embedding_model=os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"),
            rate_limit_delay=float(os.getenv("HF_RATE_LIMIT_DELAY_SECONDS", "36"))
        )
        
        self.openrouter = OpenRouterConfig(
            api_key=os.getenv("OPENROUTER_API_KEY", "sk-or-xxx_placeholder_xxx"),
            model=os.getenv("LLM_MODEL_OPENROUTER", "deepseek/deepseek-chat-v3-0324:free")
        )
        
        self.cerebras = CerebrasConfig(
            api_key=os.getenv("CEREBRAS_API_KEY", "csk_xxx_placeholder_xxx"),
            model=os.getenv("LLM_MODEL_CEREBRAS", "llama-3.3-70b")
        )
        
        # Database
        self.database = DatabaseConfig(
            host=os.getenv("DATABASE_HOST", "localhost"),
            port=int(os.getenv("DATABASE_PORT", "5432")),
            user=os.getenv("DATABASE_USER", "bootcamp_user"),
            password=os.getenv("DATABASE_PASSWORD", "your_secure_password_here"),
            database=os.getenv("DATABASE_NAME", "bootcamp_rag")
        )
        
        # Embedding models
        self.embedding_models = EmbeddingModelConfig(
            primary=os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2"),
            bge=os.getenv("EMBEDDING_MODEL_BGE", "BAAI/bge-large-en-v1.5"),
            nomic=os.getenv("EMBEDDING_MODEL_NOMIC", "nomic-ai/nomic-embed-text-v1.5"),
            reranker=os.getenv("RERANKER_MODEL", "cross-encoder/ms-marco-MiniLM-L-12-v2")
        )
        
        # Paths
        self.data_path = os.getenv("DATA_PATH", "/data/datasets")
        self.log_path = os.getenv("LOG_PATH", "./logs")
        self.notebooks_path = os.getenv("NOTEBOOKS_PATH", "./notebooks")
        self.scripts_path = os.getenv("SCRIPTS_PATH", "./scripts")
        
        # Experiment settings
        self.experiment_tracking_enabled = os.getenv("EXPERIMENT_TRACKING_ENABLED", "true").lower() == "true"
        self.mlflow_tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
        self.ragas_query_count = int(os.getenv("RAGAS_QUERY_COUNT", "50"))
        self.top_k_retrieval = int(os.getenv("TOP_K_RETRIEVAL", "5"))
        self.top_k_rerank = int(os.getenv("TOP_K_RERANK", "30"))
        
        # Logging
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.log_format = os.getenv("LOG_FORMAT", "json")
        self.debug_mode = os.getenv("DEBUG_MODE", "false").lower() == "true"
        self.verbose_logging = os.getenv("VERBOSE_LOGGING", "false").lower() == "true"
        
        # Fallback order
        fallback_str = os.getenv("LLM_FALLBACK_ORDER", "groq,openrouter,cerebras,google")
        self.llm_fallback_order = [p.strip() for p in fallback_str.split(",")]
        
        # Feature flags
        self.enable_multi_hop = os.getenv("ENABLE_MULTI_HOP_RETRIEVAL", "true").lower() == "true"
        self.enable_langgraph = os.getenv("ENABLE_LANGGRAPH_AGENT", "true").lower() == "true"
        self.enable_ragas = os.getenv("ENABLE_RAGAS_EVALUATION", "true").lower() == "true"
        self.enable_experiment_tracking = os.getenv("ENABLE_EXPERIMENT_TRACKING", "true").lower() == "true"
    
    def validate(self) -> Dict[str, bool]:
        """Validate configuration and return status of each API
        
        Returns:
            Dict with API names as keys and True/False for configured status
        """
        status = {
            "groq": self.groq.is_configured(),
            "google": self.google.is_configured(),
            "huggingface": self.huggingface.is_configured(),
            "openrouter": self.openrouter.is_configured(),
            "cerebras": self.cerebras.is_configured(),
            "database": self.database.is_configured()
        }
        return status
    
    def get_configured_apis(self) -> list:
        """Get list of configured API providers"""
        status = self.validate()
        return [api for api, is_conf in status.items() if is_conf and api != "database"]
    
    def get_database_connection_string(self) -> str:
        """Get PostgreSQL connection string"""
        return self.database.get_connection_string()
    
    def get_llm_fallback_order(self) -> list:
        """Get LLM providers in fallback order"""
        # Filter to only include configured providers
        configured = self.get_configured_apis()
        return [p for p in self.llm_fallback_order if p in configured]
    
    def log_configuration_summary(self):
        """Log configuration status without exposing secrets"""
        logger.info("=" * 70)
        logger.info("RAG Bootcamp Configuration Summary")
        logger.info("=" * 70)
        
        status = self.validate()
        
        logger.info("API Providers:")
        for api, is_conf in status.items():
            if api != "database":
                status_str = "✓ CONFIGURED" if is_conf else "✗ NOT CONFIGURED"
                logger.info(f"  {api:20} {status_str}")
        
        logger.info(f"\nDatabase: {'✓ CONFIGURED' if status['database'] else '✗ NOT CONFIGURED'}")
        
        logger.info(f"\nFallback Order: {' → '.join(self.get_llm_fallback_order())}")
        logger.info(f"Experiment Tracking: {'ENABLED' if self.experiment_tracking_enabled else 'DISABLED'}")
        logger.info(f"Multi-hop Retrieval: {'ENABLED' if self.enable_multi_hop else 'DISABLED'}")
        logger.info(f"LangGraph Agent: {'ENABLED' if self.enable_langgraph else 'DISABLED'}")
        logger.info(f"RAGAS Evaluation: {'ENABLED' if self.enable_ragas else 'DISABLED'}")
        
        logger.info("=" * 70)


# ============================================================================
# SINGLETON INSTANCE
# ============================================================================

# Create global config instance
config = Config()


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_config() -> Config:
    """Get the global configuration instance"""
    return config


def validate_config() -> bool:
    """Validate that at least one LLM API is configured
    
    Returns:
        True if configuration is valid, False otherwise
    """
    configured_apis = config.get_configured_apis()
    
    if not configured_apis:
        logger.error(
            "❌ No API providers configured!\n"
            "Please set at least one of these environment variables:\n"
            "  - GROQ_API_KEY\n"
            "  - GOOGLE_API_KEY\n"
            "  - OPENROUTER_API_KEY\n"
            "  - CEREBRAS_API_KEY\n"
            "See .env.example for template."
        )
        return False
    
    logger.info(f"✓ Configuration valid. Available APIs: {', '.join(configured_apis)}")
    return True


# ============================================================================
# AUTOMATIC VALIDATION ON IMPORT
# ============================================================================

if __name__ == "__main__":
    # Configure logging for testing
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Test validation
    print("\nConfiguration Validation Test:")
    print("-" * 70)
    config.log_configuration_summary()
    
    is_valid = validate_config()
    print(f"\nValidation Result: {'✓ PASS' if is_valid else '✗ FAIL'}")
