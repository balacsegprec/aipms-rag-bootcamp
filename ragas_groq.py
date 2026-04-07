from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

def evaluate_with_groq(query, context, answer):
    prompt = f"""
You are evaluating a RAG system.

Question: {query}
Context: {context}
Answer: {answer}

Evaluate:
1. Faithfulness (0-1)
2. Relevance (0-1)

Return ONLY JSON:
{{"faithfulness": value, "relevance": value}}
"""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[ERROR] {e}"

if __name__ == "__main__":
    print("[INFO] Running Groq-based evaluation...\n")
    query = "How is AI used in medicine?"
    context = "AI is used in healthcare for diagnosis"
    answer = "AI is used in healthcare for diagnosis"
    result = evaluate_with_groq(query, context, answer)
    print("[RESULT]")
    print(result)