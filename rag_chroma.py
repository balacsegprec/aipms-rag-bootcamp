
# --- Refactored for production, dotenv, fallback, merged logic ---
from sentence_transformers import SentenceTransformer, CrossEncoder
from openai import OpenAI
import chromadb
import sys
import time
import os
from dotenv import load_dotenv

load_dotenv()

TOP_K = 3
FINAL_K = 2

# ---- SETUP MODELS ----
try:
    embed_model = SentenceTransformer("all-MiniLM-L6-v2")
    reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-12-v2")
    print("[INFO] Models loaded")
except Exception as e:
    print(f"[ERROR] Model load failed: {e}")
    sys.exit(1)

# ---- CHROMA SETUP ----
try:
    client = chromadb.Client()
    collection = client.get_or_create_collection(name="rag_docs")
    print("[INFO] Chroma initialized")
except Exception as e:
    print(f"[ERROR] Chroma init failed: {e}")
    sys.exit(1)

# ---- DATA (for demo, replace with your loader) ----
documents = [
    "AI is used in healthcare for diagnosis",
    "Machine learning improves with data",
    "Deep learning uses neural networks",
    "Python is widely used for AI development"
]

try:
    embeddings = embed_model.encode(documents).tolist()
    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=[str(i) for i in range(len(documents))]
    )
    print("[INFO] Documents stored in Chroma")
except Exception as e:
    print(f"[ERROR] Chroma insert failed: {e}")
    sys.exit(1)

# ---- FALLBACK LLM FUNCTION ----
def query_llm(messages):
    providers = [
        {
            "name": "groq",
            "base_url": "https://api.groq.com/openai/v1",
            "api_key": os.getenv("GROQ_API_KEY"),
            "model": "llama-3.3-70b-versatile"
        },
        {
            "name": "openrouter",
            "base_url": "https://openrouter.ai/api/v1",
            "api_key": os.getenv("OPENROUTER_API_KEY"),
            "model": "deepseek/deepseek-chat-v3-0324:free"
        }
    ]
    for p in providers:
        if not p["api_key"]:
            continue
        try:
            client = OpenAI(
                base_url=p["base_url"],
                api_key=p["api_key"]
            )
            response = client.chat.completions.create(
                model=p["model"],
                messages=messages,
                temperature=0.1
            )
            print(f"[INFO] Used provider: {p['name']}")
            return response.choices[0].message.content
        except Exception as e:
            print(f"[WARN] {p['name']} failed: {e}")
            time.sleep(1)
    return "[ERROR] All LLM providers failed"

# ---- RAG FUNCTION ----
def ask_rag(query):
    if not query or not query.strip():
        return "[ERROR] Empty query"
    try:
        query_embedding = embed_model.encode([query])[0].tolist()
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=TOP_K
        )
        top_docs = results.get("documents", [[]])[0]
        if not top_docs:
            return "[ERROR] No documents retrieved"
    except Exception as e:
        return f"[ERROR] Retrieval failed: {e}"
    print("\n[INFO] Top-K retrieved:")
    for i, d in enumerate(top_docs):
        print(f"{i+1}. {d}")
    # ---- RERANK ----
    try:
        pairs = [(query, doc) for doc in top_docs]
        scores = reranker.predict(pairs)
        ranked = sorted(zip(scores, top_docs), reverse=True)
        final_docs = [doc for _, doc in ranked[:FINAL_K]]
        if not final_docs:
            return "[ERROR] Reranking returned empty results"
    except Exception as e:
        return f"[ERROR] Reranking failed: {e}"
    print("\n[INFO] After reranking:")
    for i, d in enumerate(final_docs):
        print(f"{i+1}. {d}")
    combined_context = "\n".join(final_docs)
    # ---- LLM CALL (WITH FALLBACK) ----
    answer = query_llm([
        {"role": "system", "content": "Answer using the given context."},
        {"role": "user", "content": f"Context:\n{combined_context}\n\nQuestion: {query}"}
    ])
    return answer

if __name__ == "__main__":
    print("[INFO] Running RAG with Chroma + Fallback...\n")
    query = "How is AI used in medicine?"
    answer = ask_rag(query)
    print("\n[FINAL ANSWER]\n", answer)