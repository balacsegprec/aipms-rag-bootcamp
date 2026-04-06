from sentence_transformers import CrossEncoder
from config.api_config import get_config

# Load config
config = get_config()

# Load model from config
model = CrossEncoder(config.embedding_models.reranker)


def rerank(query, documents, top_k=3):
    pairs = [(query, doc) for doc in documents]
    scores = model.predict(pairs)

    scored_docs = list(zip(documents, scores))
    scored_docs.sort(key=lambda x: x[1], reverse=True)

    return [doc for doc, _ in scored_docs[:top_k]]
