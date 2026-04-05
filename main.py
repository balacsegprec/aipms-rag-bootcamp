from dotenv import load_dotenv
load_dotenv()

from rag_pipeline import run_rag

query = "Explain retrieval augmented generation and its advantages"

answer = run_rag("sample.pdf", query, model_name="bge")

print("\nFinal Answer:\n")
print(answer)