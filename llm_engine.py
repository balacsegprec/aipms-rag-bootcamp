import os
from dotenv import load_dotenv

from providers.google import call_google
from providers.hf import call_hf

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

query = "Explain artificial intelligence in simple terms"


# -----------------------
# GROQ (inline or separate)
# -----------------------
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


# -----------------------
# FALLBACK ENGINE
# -----------------------
def fallback_chain():
    print("🔥 ENTERED FALLBACK ENGINE\n")

    providers = [
        ("Groq", lambda q: call_groq()),
        ("Google", lambda q: call_google(q, GOOGLE_API_KEY)),
        ("HuggingFace", lambda q: call_hf(q, HUGGINGFACE_API_KEY))
    ]

    for name, func in providers:
        print(f"👉 Trying {name}...")

        try:
            result = func(query)

            if result:
                print(f"✅ {name} SUCCESS\n")
                return result

            else:
                print(f"❌ {name} returned empty response\n")

        except Exception as e:
            print(f"❌ {name} error: {e}")

    return "🚨 All providers failed"


# -----------------------
# RUN
# -----------------------
if __name__ == "__main__":
    output = fallback_chain()
    print("\n✅ FINAL OUTPUT:\n")
    print(output)