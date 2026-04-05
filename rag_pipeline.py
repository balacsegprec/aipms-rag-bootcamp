from embeddings import get_embeddings
from vectordb import add_documents, query_db
from llm import generate_answer
from utils import load_pdf, split_text
from reranker import rerank


def run_rag(pdf_path, query, model_name="bge"):
    # Load PDF
    text = load_pdf(pdf_path)

    # Split text
    documents = split_text(text)

    # Embed documents
    embeddings = get_embeddings(documents, model_name=model_name)

    # Store in DB
    add_documents(documents, embeddings)

    # Embed query
    query_embedding = get_embeddings([query], model_name=model_name)

    # Retrieve
    results = query_db(query_embedding, k=6)
    retrieved_docs = list(set(results["documents"][0]))

    print("\nBefore Rerank:\n", retrieved_docs)

    # Rerank
    retrieved_docs = rerank(query, retrieved_docs, top_k=3)

    print("\nAfter Rerank:\n", retrieved_docs)

    # Build context
    context = "\n".join(retrieved_docs)

    # Generate answer
    answer = generate_answer(context, query)

    return answer