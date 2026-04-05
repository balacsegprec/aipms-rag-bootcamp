import os
from groq import Groq


def generate_answer(context, query):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""
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

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content