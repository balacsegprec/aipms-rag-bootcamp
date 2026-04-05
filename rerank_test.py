from sentence_transformers import CrossEncoder

# Load model (downloads automatically)
model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-12-v2")

query = "What is AI?"

docs = [
    "Artificial Intelligence is the simulation of human intelligence.",
    "Bananas are yellow and sweet.",
    "AI is used in machine learning and deep learning."
]

# Create pairs (query, doc)
pairs = [(query, doc) for doc in docs]

# Get relevance scores
scores = model.predict(pairs)

# Combine & sort
results = list(zip(docs, scores))
results.sort(key=lambda x: x[1], reverse=True)

# Print ranked results
for doc, score in results:
    print(f"{score:.4f} -> {doc}")