from sentence_transformers import SentenceTransformer, CrossEncoder

print("🔄 Loading embedding model...")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

embedding = embedding_model.encode(["test"])
print("✅ Embedding model working")

print("🔄 Loading reranker model...")
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-12-v2")

score = reranker.predict([("q", "doc")])
print("✅ Reranker working")

print("🎉 All models verified successfully")