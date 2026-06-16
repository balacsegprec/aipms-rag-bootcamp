# AI-PMS RAG Bootcamp

An enterprise-grade, multi-tenant Retrieval-Augmented Generation (RAG) system tailored for construction domain operations (DMRC).

## Overview

The AI-PMS RAG system provides an intelligent document retrieval and question-answering service. It operates over a specialized corpus of construction documents, including legal contracts (GCC/FIDIC), quality defect reports (NCRs), daily progress reports (DPRs), and official correspondence. 

It exists to solve the critical need for fast, accurate, and secure information retrieval in complex infrastructure projects, where data is often fragmented across multiple systems and tenants. The main use cases include:
- Querying specific clauses from dense legal contracts.
- Investigating non-conformance reports (NCR) and corrective actions.
- Analyzing daily progress metrics.
- Securely retrieving stakeholder correspondence without cross-tenant data leaks.

## Features

- **Hybrid Retrieval**: Combines `pgvector` dense cosine similarity with PostgreSQL `pg_trgm` sparse keyword matching using Reciprocal Rank Fusion (RRF).
- **Intelligent Query Routing**: Sequential LLM intent classifier routes queries to specific domain strategies.
- **Agentic Orchestration**: LangGraph-based state machine that evaluates context sufficiency and retries retrieval up to 3 times before hallucinating.
- **Robust LLM Failover**: Sequential provider fallback (Groq → OpenRouter → Cerebras → Gemini) ensures high availability.
- **Enterprise Security**: Row-Level Security (RLS) guarantees multi-tenant data isolation directly at the database engine level.
- **Adversarial Defenses**: Pre-retrieval prompt injection regex filters and domain-specific semantic centroid similarity blockers.
- **Audit Logging**: Comprehensive Layer 4 CDM logging (timestamp, tenant_id, query_hash, retrieved_chunk_ids, response_hash, latency_ms).

## Architecture

```mermaid
flowchart TD

    User --> API[FastAPI Endpoint]
    API --> Security[Adversarial & Injection Filter]
    Security --> Router[LLM Query Router]
    
    Router -->|Intent| Agent[LangGraph Agent]
    
    Agent --> Retriever[Hybrid Retriever]
    
    Retriever --> VectorDB[PostgreSQL pgvector]
    Retriever --> SparseDB[PostgreSQL pg_trgm]
    
    VectorDB --> RLS[RLS Tenant Isolation]
    SparseDB --> RLS
    
    RLS --> Fusion[Reciprocal Rank Fusion]
    Fusion --> Eval[Context Sufficiency Evaluator]
    
    Eval -->|Insufficient & Loops < 3| Retriever
    Eval -->|Sufficient or Loops >= 3| Generator[Answer Generator]
    
    Generator --> LLM[Robust Failover LLM]
    LLM --> Audit[Audit Ledger]
    Audit --> Response
```

## Technology Stack

- **Backend**: FastAPI, Python 3.12+, Uvicorn
- **AI/LLM**: LangChain, OpenAI API, Groq, OpenRouter, Cerebras, Gemini, HuggingFace Transformers
- **Retrieval**: LangGraph
- **Database**: PostgreSQL 12+, pgvector, pg_trgm
- **Infrastructure**: Docker, Docker Compose
- **Testing**: pytest, RAGAS, MLflow

## Project Structure

```text
.
├── src/
│   ├── agents/          # LangGraph orchestration and query routing
│   ├── api/             # FastAPI application and routes
│   ├── chunkers/        # Domain-specific document splitting logic
│   ├── core/            # Core DB, LLM, pipeline, and security components
│   ├── evals/           # Evaluation metrics logic
│   └── utils/           # Configuration and environment management
├── scripts/
│   ├── dev/             # Development scripts
│   ├── evaluation/      # Evaluation scripts
│   ├── experiments/     # Experimental stubs
│   ├── ingest/          # Data chunking and ingestion scripts
│   └── migration/       # Database migrations
├── data/                # Sample synthetic corpora
├── docs/                # Architecture decisions and planning guides
├── experiments/         # Output logs from various experiments
├── tests/               # Pytest suite (unit and integration)
└── docker-compose.yml   # PostgreSQL + pgvector infrastructure
```

## Retrieval Pipeline

1. **Query Processing**: The incoming query is sanitized against prompt injection patterns and checked against a semantic centroid to ensure it belongs to the construction domain.
2. **Retrieval**: An LLM-based query router determines the specific domain intent. The retriever executes both dense vector search and sparse trigram search against PostgreSQL.
3. **Fusion**: Results from both searches are combined and scored using a custom Reciprocal Rank Fusion (RRF) algorithm.
4. **Context Generation**: The fused results are returned to the LangGraph agent state.
5. **LLM Generation**: An evaluator node checks if the context is sufficient to answer the query. If insufficient, it loops back to retrieve again (up to 3 times). Once sufficient, the answer generator node builds the prompt and streams it to the LLM.
6. **Robust Failover**: The generation step utilizes a custom wrapper that sequentially attempts multiple LLM providers to guarantee an answer.

## Ingestion Pipeline

1. **Document Upload**: Raw documents (PDFs, JSON, XLSX) are read from the filesystem.
2. **Chunking**: Specialized chunkers apply targeted splitting strategies:
   - **Contracts**: Semantic heading-aware splitting.
   - **NCRs / DPRs**: Structure-aware splitting coupling IDs to body content.
   - **Correspondence**: Metadata-injected paragraph splitting (Ref, Date, From, To).
3. **Embedding**: Chunks are processed by a local `all-MiniLM-L6-v2` SentenceTransformer to generate 384-dimensional dense vectors.
4. **Indexing**: Vectors and raw text are inserted into PostgreSQL. `pgvector` creates an `ivfflat` index, and `pg_trgm` creates a `GIN` index.

## Security

- **Authentication**: Secured via an `X-API-Key` header verified against a pre-configured dictionary in memory.
- **Multi-tenancy**: Strictly enforced via PostgreSQL Row-Level Security (RLS) policies. Database queries are scoped using `SET LOCAL app.current_tenant_id`.
- **Prompt Injection Defenses**: Pre-retrieval regex heuristic blocking common jailbreak patterns.
- **Data Isolation**: Verified zero cross-tenant leakage.
- **Audit Logging**: Every query and its retrieved chunks are hashed (SHA-256) and appended to a JSON ledger and an internal database table for compliance.

## API Reference

| Endpoint | Method | Headers | Body | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/query` | `POST` | `X-API-Key` | `{"query": str, "tenant_id": str, "entity_type_filter": Optional[str]}` | Main RAG query endpoint. |

## Installation

1. Clone the repository and navigate into it.
2. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Set the following variables in your `.env` file:

| Variable | Description | Example |
| :--- | :--- | :--- |
| `POSTGRES_URL` | PostgreSQL connection string | `postgresql://user:password@localhost:5432/db` |
| `GROQ_API_KEY` | Groq API Key | `gsk_...` |
| `OPENROUTER_API_KEY` | OpenRouter API Key | `sk-or-v1-...` |
| `CEREBRAS_API_KEY` | Cerebras API Key | `csk-...` |
| `GEMINI_API_KEY` | Google Gemini API Key | `AIza...` |
| `OPENAI_API_KEY` | OpenAI API Key (Optional) | `sk-...` |
| `HF_TOKEN` | HuggingFace Token (Optional) | `hf_...` |

## Running Locally

1. Start the database infrastructure:
   ```bash
   docker-compose up -d
   ```
2. Initialize the database schema:
   ```bash
   python scripts/reinit_db.py
   ```
3. Start the FastAPI server:
   ```bash
   uvicorn src.api.main:app --reload
   ```

## Testing

Run the full integration and unit test suite using `pytest`:

```bash
python -m pytest tests/ -v
```

## Deployment

The application is containerized and ready for Docker-based deployment.

1. Build the Docker image:
   ```bash
   docker build -t aipms-rag .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 --env-file .env aipms-rag
   ```

## Performance & Evaluation

Based on recorded experiments in `docs/docs_for_planning/Deliverables_Guide_Nishitha_FINAL.md`:

- **Embedding Latency (p95)**: ~2.8ms (using `all-MiniLM-L6-v2`)
- **BM25 Search (p95)**: ~15ms
- **Vector Search (p95)**: ~0.02ms
- **RRF Fusion (p95)**: ~2.0ms
- **LLM Generation (Llama 3.1)**: ~13.7s (Network dependent)

## Future Improvements

- Deploy local L40S GPU hosting or prompt caching to mitigate LLM API network bottlenecks and comply with sub-5s NFR limits.
- Scale out PostgreSQL RLS strategies for handling 50+ distinct subcontractor tenants efficiently.
- Automate the ingestion pipeline to convert weekly correspondence into entity-relation nodes in the database.
