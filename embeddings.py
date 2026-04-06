from sentence_transformers import SentenceTransformer
from config.api_config import get_config

# Load config
config = get_config()

# Load embedding model from config
model = SentenceTransformer(config.embedding_models.primary)


def get_embeddings(texts):
    return model.encode(texts)
