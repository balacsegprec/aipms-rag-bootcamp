import chromadb

client = chromadb.Client()

# Reset collection (important when switching models)
try:
    client.delete_collection("rag_demo")
except:
    pass

collection = client.get_or_create_collection("rag_demo")


def add_documents(documents, embeddings):
    ids = [str(i) for i in range(len(documents))]

    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids
    )


def query_db(query_embedding, k=6):
    return collection.query(
        query_embeddings=query_embedding,
        n_results=k
    )