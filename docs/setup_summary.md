# Bootcamp Setup Summary

## Bootcamp Requirements
- Groq as primary LLM
- Fallback chain (multi-provider)
- CPU embeddings (sentence-transformers)
- Cross-encoder reranking
- Vector DB: PostgreSQL + pgvector
- Chroma only for prototyping
- End-to-end RAG pipeline
- Evaluation (RAGAS / LLM-based)
- MLflow tracking
- .env usage (NO hardcoded keys)

## What is Completed
- Groq LLM (primary)
- OpenRouter fallback (basic)
- sentence-transformers embeddings (CPU)
- cross-encoder reranking (CPU)
- ChromaDB vector store (temporary)
- End-to-end RAG pipeline
- LLM-based evaluation
- MLflow tracking
- .env-based secret management
- Docker setup

## What Failed / Not Implemented
- PostgreSQL + pgvector (Windows install issues)
- pg_trgm (BM25 search)
- Apache AGE (graph)
- Full fallback chain (Cerebras, Google AI Studio)
- HuggingFace API for embeddings

## Why ChromaDB is Used
PostgreSQL + pgvector could not be installed on Windows. ChromaDB is used for local prototyping until WSL/Linux is available.

## Current Status
- Core setup complete
- Ready for further extension
- Limitations documented
