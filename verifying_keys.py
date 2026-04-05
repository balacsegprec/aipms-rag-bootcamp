import os
from dotenv import load_dotenv

load_dotenv()

keys = [
    "GROQ_API_KEY",
    "GOOGLE_API_KEY",
    "HF_API_KEY",
    "OPENROUTER_API_KEY",
    "CEREBRAS_API_KEY"
]

for k in keys:
    print(k, ":", "OK" if os.getenv(k) else "MISSING")