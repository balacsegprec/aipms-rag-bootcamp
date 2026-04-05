from sentence_transformers import SentenceTransformer

minilm = SentenceTransformer('all-MiniLM-L6-v2')
bge = SentenceTransformer('BAAI/bge-large-en-v1.5')
nomic = SentenceTransformer('nomic-ai/nomic-embed-text-v1')


def get_embeddings(texts, model_name="bge"):
    if not texts:
        raise ValueError("No text provided for embeddings")

    if model_name == "minilm":
        return minilm.encode(texts).tolist()
    elif model_name == "bge":
        return bge.encode(texts).tolist()
    elif model_name == "nomic":
        return nomic.encode(texts).tolist()