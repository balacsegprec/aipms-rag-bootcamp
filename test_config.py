from config.api_config import get_config

config = get_config()

print("🔍 Checking Config Usage...\n")

# APIs
print("GROQ Model:", config.groq.model)
print("Google Model:", config.google.model)

# Embedding + Reranker
print("Embedding Model:", config.embedding_models.primary)
print("Reranker Model:", config.embedding_models.reranker)

# Fallback Order
print("Fallback Order:", config.get_llm_fallback_order())

# Configured APIs
print("Configured APIs:", config.get_configured_apis())

print("\n✅ Config working correctly")