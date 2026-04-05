from sentence_transformers import SentenceTransformer

# Load models
model1 = SentenceTransformer("BAAI/bge-large-en-v1.5")
model2 = SentenceTransformer("nomic-ai/nomic-embed-text-v1")

text = "Hello world"

# Generate embeddings
emb1 = model1.encode(text)
emb2 = model2.encode(text)

print("BGE embedding length:", len(emb1))
print("Nomic embedding length:", len(emb2))