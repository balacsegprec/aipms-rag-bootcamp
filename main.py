import os
from dotenv import load_dotenv
import requests

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CEREBRAS_API_KEY = os.getenv("CEREBRAS_API_KEY")

query = "Explain artificial intelligence in simple terms"


# -------------------------------
# 1. GROQ
# -------------------------------
def call_groq():
    try:
        from openai import OpenAI

        client = OpenAI(
            api_key=GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1"
        )

        res = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": query}]
        )

        return res.choices[0].message.content

    except Exception as e:
        print("❌ Groq failed:", e)
        return None


# -------------------------------
# 2. GOOGLE
# -------------------------------
def call_google():
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GOOGLE_API_KEY}"

        data = {"contents": [{"parts": [{"text": query}]}]}

        res = requests.post(url, json=data).json()

        if "candidates" in res:
            return res["candidates"][0]["content"]["parts"][0]["text"]
        else:
            print("❌ Google response:", res)
            return None

    except Exception as e:
        print("❌ Google failed:", e)
        return None


# -------------------------------
# 3. OPENAI
# -------------------------------
def call_openai():
    try:
        from openai import OpenAI

        client = OpenAI(api_key=OPENAI_API_KEY)

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": query}]
        )

        return res.choices[0].message.content

    except Exception as e:
        print("❌ OpenAI failed:", e)
        return None


# -------------------------------
# 4. CEREBRAS
# -------------------------------
def call_cerebras():
    try:
        url = "https://api.cerebras.ai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {CEREBRAS_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama3.1-8b",
            "messages": [{"role": "user", "content": query}]
        }

        res = requests.post(url, headers=headers, json=data).json()

        return res["choices"][0]["message"]["content"]

    except Exception as e:
        print("❌ Cerebras failed:", e)
        return None


# -------------------------------
# 5. HUGGING FACE
# -------------------------------
def call_hf():
    try:
        url = "https://router.huggingface.co/hf-inference/models/google/flan-t5-large"

        headers = {
            "Authorization": f"Bearer {HF_API_KEY}"
        }

        data = {"inputs": query}

        res = requests.post(url, headers=headers, json=data).json()

        if isinstance(res, list):
            return res[0]["generated_text"]
        else:
            print("❌ HF response:", res)
            return None

    except Exception as e:
        print("❌ HF failed:", e)
        return None


# -------------------------------
# FALLBACK CHAIN
# -------------------------------
def fallback_chain():
    print("🚀 Running fallback chain...\n")

    print("Trying Groq...")
    result = call_groq()
    if result:
        return result

    print("Trying Google...")
    result = call_google()
    if result:
        return result

    print("Trying OpenAI...")
    result = call_openai()
    if result:
        return result

    print("Trying Cerebras...")
    result = call_cerebras()
    if result:
        return result

    print("Trying HuggingFace...")
    result = call_hf()
    if result:
        return result

    return "❌ All providers failed."


# -------------------------------
# RUN
# -------------------------------
if __name__ == "__main__":
    output = fallback_chain()
    print("\n✅ Final Output:\n")
    print(output)