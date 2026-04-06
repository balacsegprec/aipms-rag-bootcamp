from sklearn.metrics.pairwise import cosine_similarity


# Store documents + embeddings in memory
stored_docs = []
stored_embeddings = []


def add_documents(documents, embeddings):
    global stored_docs, stored_embeddings

    stored_docs = documents
    stored_embeddings = embeddings


def query_db(query_embedding, k=6):
    global stored_docs, stored_embeddings

    if not stored_docs:
        return {"documents": [[]]}

    scores = cosine_similarity(query_embedding, stored_embeddings)[0]

    # get top k indices
    top_k_idx = scores.argsort()[-k:][::-1]

    results = [stored_docs[i] for i in top_k_idx]

    return {"documents": [results]}
