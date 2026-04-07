import mlflow
import json
import time
from rag_chroma import ask_rag
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

queries = [
    "How is AI used in medicine?",
    "What is machine learning?",
    "Explain deep learning",
    "Why is Python used in AI?"
]

def evaluate(query, context, answer):
    prompt = f"""
Evaluate RAG output.

Question: {query}
Context: {context}
Answer: {answer}

Return ONLY JSON:
{{"faithfulness": value, "relevance": value}}
"""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        raw = response.choices[0].message.content.strip()
        try:
            return json.loads(raw)
        except Exception:
            print("[WARN] JSON parse failed:", raw)
            return None
    except Exception as e:
        print(f"[ERROR] LLM evaluation failed: {e}")
        return None

print("[INFO] Starting MLflow logging...\n")
for q in queries:
    with mlflow.start_run():
        print(f"\n--- Query: {q}")
        try:
            answer = ask_rag(q)
            if not answer or len(answer.strip()) == 0:
                print("[WARN] Empty answer")
                mlflow.log_param("query", q)
                mlflow.log_param("status", "empty_answer")
                continue
            context = answer
            scores = evaluate(q, context, answer)
            if scores is None:
                print("[WARN] Skipping due to eval failure")
                mlflow.log_param("query", q)
                mlflow.log_param("status", "eval_failed")
                continue
            faith = scores.get("faithfulness")
            rel = scores.get("relevance")
            if faith is None or rel is None:
                print("[WARN] Missing keys in result:", scores)
                mlflow.log_param("query", q)
                mlflow.log_param("status", "bad_format")
                continue
            mlflow.log_param("query", q)
            mlflow.log_param("model", "llama-3.3-70b")
            mlflow.log_metric("faithfulness", float(faith))
            mlflow.log_metric("relevance", float(rel))
            print("[ANSWER]", answer)
            print("[SCORES]", scores)
        except Exception as e:
            print(f"[ERROR] Pipeline failed: {e}")
            mlflow.log_param("query", q)
            mlflow.log_param("status", "pipeline_failed")
        time.sleep(2)
print("\n[INFO] Done.")