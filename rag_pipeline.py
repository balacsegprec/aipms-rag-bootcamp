
import logging
logging.getLogger("transformers").setLevel(logging.ERROR)
from embeddings import get_embeddings
from vectordb import add_documents, query_db
from utils import load_pdf, split_text
from reranker import rerank

# ✅ Dev-provided modules
from scripts.fallback_chain import query_llm
from config.api_config import get_config


def run_rag(pdf_path, query, model_name="bge"):
    # 1. Load PDF
    text = load_pdf(pdf_path)

    # 2. Split into chunks
    documents = split_text(text)

    # 3. Generate embeddings
    embeddings = get_embeddings(documents)

    # 4. Store in vector DB (in-memory for now)
    add_documents(documents, embeddings)

    # 5. Embed query
    query_embedding = get_embeddings([query])

    # 6. Retrieve top documents
    results = query_db(query_embedding, k=6)
    retrieved_docs = results["documents"][0]

    print("\nBefore Rerank:\n", retrieved_docs)

    # 7. Rerank
    retrieved_docs = rerank(query, retrieved_docs, top_k=3)

    print("\nAfter Rerank:\n", retrieved_docs)

    # 8. Build context
    context = "\n".join(retrieved_docs)

    # 9. Load and validate config
    config = get_config()
    config.validate()

    # 10. Build message (IMPORTANT 🔥)
    messages = [
        {
            "role": "user",
            "content": f"""
You are a helpful AI assistant.

Answer the question using the context below.
If the answer is partially available, explain using the context.
Only say "I don't know" if absolutely no relevant information exists.

Context:
{context}

Question:
{query}

Answer:
"""
        }
    ]

    # 11. Call fallback chain
    answer, provider = query_llm(messages)

    print(f"\nAnswer generated using: {provider}")

    return answer
