
import os
from dotenv import load_dotenv
import requests

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

query = "Explain artificial intelligence in simple terms"


# -------------------------------
# 1. GROQ (FIXED MODEL)
# -------------------------------
def call_groq():
    try:
        from openai import OpenAI

        client = OpenAI(
            api_key=GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1"
        )

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": query}]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("❌ Groq failed:", e)
        return None


# -------------------------------
# 2. GOOGLE (ROBUST)
# -------------------------------
def call_google():
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GOOGLE_API_KEY}"

        data = {
            "contents": [{"parts": [{"text": query}]}]
        }

        res = requests.post(url, json=data)
        res_json = res.json()

        if "candidates" in res_json:
            return res_json["candidates"][0]["content"]["parts"][0]["text"]
        else:
            print("Google response:", res_json)
            return None

    except Exception as e:
        print("❌ Google failed:", e)
        return None


# -------------------------------
# 3. HUGGING FACE (NEW API)
# -------------------------------
def call_hf():
    try:
        url = "https://router.huggingface.co/hf-inference/models/google/flan-t5-large"

        headers = {
            "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
        }

        data = {"inputs": query}

        res = requests.post(url, headers=headers, json=data)
        output = res.json()

        if isinstance(output, list):
            return output[0]["generated_text"]
        else:
            print("HF response:", output)
            return None

    except Exception as e:
        print("❌ HUGGINGFACE failed:", e)
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

    print("Trying HuggingFace...")
    result = call_hf()
    if result:
        return result

    return "All providers failed."


# -------------------------------
# RUN
# -------------------------------
if __name__ == "__main__":
    output = fallback_chain()
    print("\n✅ Final Output:\n")
    print(output)