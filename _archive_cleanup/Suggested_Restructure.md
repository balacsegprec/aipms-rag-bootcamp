# AI-PMS RAG LAB — Production Repository Architecture

Enterprise-grade RAG research + engineering repository structure
Designed for:

* AI-PMS
* DMRC-oriented RAG experimentation
* Multi-strategy retrieval research
* Production-ready backend evolution
* Future frontend integration
* Docker + CI/CD deployment
* WSL → Ubuntu migration
* Multi-contributor experimentation

Current Contributors:

* Balu
* Nishitha

---

# Core Design Philosophy

This repository is NOT:

* a tutorial repo
* a notebook dump
* a temporary bootcamp folder
* a collection of random RAG experiments

This repository IS:

* a modular RAG engineering lab
* a scalable backend platform
* a retrieval experimentation system
* a future production AI platform
* an evaluation-first architecture

The structure separates:

* production systems
* experimentation
* evaluation
* infrastructure
* deployment
* contributor-specific research

This prevents:

* notebook chaos
* duplicated experiments
* mixed production/research code
* merge conflicts
* undocumented experiments
* deployment confusion

---

# FINAL PRODUCTION REPOSITORY STRUCTURE

```text
aipms-rag-lab/
│
├── README.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── LICENSE
├── .env.example
├── .gitignore
├── Makefile
│
├── apps/
│   │
│   ├── api/
│   │   ├── src/
│   │   │   ├── routes/
│   │   │   ├── middleware/
│   │   │   ├── schemas/
│   │   │   ├── orchestration/
│   │   │   ├── dependencies/
│   │   │   └── main.py
│   │   │
│   │   ├── tests/
│   │   └── Dockerfile
│   │
│   ├── web/
│   │   ├── src/
│   │   ├── public/
│   │   ├── tests/
│   │   └── Dockerfile
│   │
│   └── playground/
│       ├── internal-chat-ui/
│       ├── retrieval-debugger/
│       └── evaluation-viewer/
│
├── core/
│   │
│   ├── ingestion/
│   │   ├── parsers/
│   │   ├── cleaners/
│   │   ├── validators/
│   │   └── metadata/
│   │
│   ├── chunking/
│   │   ├── contract/
│   │   ├── ncr/
│   │   ├── dpr/
│   │   ├── correspondence/
│   │   └── meeting_minutes/
│   │
│   ├── embeddings/
│   │   ├── providers/
│   │   ├── benchmark/
│   │   └── cache/
│   │
│   ├── retrieval/
│   │   ├── vector/
│   │   ├── bm25/
│   │   ├── hybrid/
│   │   ├── hyde/
│   │   ├── multi_query/
│   │   ├── reranking/
│   │   └── graph_rag/
│   │
│   ├── llm/
│   │   ├── providers/
│   │   ├── prompts/
│   │   ├── routing/
│   │   └── fallback/
│   │
│   ├── evaluation/
│   │   ├── ragas/
│   │   ├── metrics/
│   │   ├── golden_dataset/
│   │   └── experiment_runner/
│   │
│   ├── observability/
│   │   ├── tracing/
│   │   ├── logging/
│   │   ├── telemetry/
│   │   └── dashboards/
│   │
│   └── security/
│       ├── tenant_isolation/
│       ├── access_control/
│       └── pii_checks/
│
├── research/
│   │
│   ├── shared/
│   │   ├── datasets/
│   │   ├── notebooks/
│   │   ├── visualizations/
│   │   └── baselines/
│   │
│   ├── balu/
│   │   ├── experiments/
│   │   ├── findings/
│   │   ├── notebooks/
│   │   └── logs/
│   │
│   └── nishitha/
│       ├── experiments/
│       ├── findings/
│       ├── notebooks/
│       └── logs/
│
├── datasets/
│   │
│   ├── manifests/
│   ├── synthetic/
│   ├── enterprise_rag/
│   ├── gcc_contracts/
│   └── processed/
│
├── infra/
│   │
│   ├── docker/
│   │   ├── api.Dockerfile
│   │   ├── web.Dockerfile
│   │   ├── worker.Dockerfile
│   │   └── docker-compose.yml
│   │
│   ├── postgres/
│   ├── pgvector/
│   ├── apache-age/
│   ├── nginx/
│   │
│   ├── monitoring/
│   │   ├── prometheus/
│   │   ├── grafana/
│   │   └── loki/
│   │
│   └── scripts/
│
├── deployment/
│   │
│   ├── local/
│   │   ├── windows-wsl/
│   │   └── ubuntu-dev/
│   │
│   ├── staging/
│   └── production/
│
├── docs/
│   │
│   ├── 00-start-here/
│   │
│   ├── 01-product/
│   │   ├── vision.md
│   │   ├── architecture.md
│   │   └── roadmap.md
│   │
│   ├── 02-onboarding/
│   │   ├── balu.md
│   │   ├── nishitha.md
│   │   ├── setup-wsl.md
│   │   ├── setup-ubuntu.md
│   │   └── contributor-flow.md
│   │
│   ├── 03-rag/
│   │   ├── embeddings.md
│   │   ├── chunking.md
│   │   ├── retrieval.md
│   │   ├── reranking.md
│   │   ├── graph-rag.md
│   │   └── evaluation.md
│   │
│   ├── 04-api/
│   ├── 05-frontend/
│   ├── 06-deployment/
│   ├── 07-security/
│   ├── 08-experiments/
│   └── archive/
│
├── scripts/
│   ├── bootstrap/
│   ├── ingestion/
│   ├── evaluation/
│   ├── benchmarks/
│   └── maintenance/
│
├── storage/
│   ├── vector_indexes/
│   ├── cache/
│   └── exports/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── rag/
│   ├── api/
│   └── load/
│
└── .github/
    │
    ├── workflows/
    │   ├── ci.yml
    │   ├── lint.yml
    │   ├── tests.yml
    │   └── docker.yml
    │
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```

---

# WHY THIS STRUCTURE WORKS

## apps/

Contains actual runnable applications.

Separates:

* backend API
* frontend
* playground/debugging tools

Prevents experimental code from leaking into production APIs.

---

## core/

The reusable RAG engine.

This is the heart of the platform.

Contains:

* ingestion
* chunking
* retrieval
* reranking
* GraphRAG
* evaluation
* observability
* security

This structure directly supports:

* hybrid retrieval
* HyDE
* multi-query retrieval
* metadata filtering
* reranking
* future GraphRAG
* future agentic workflows

---

## research/

The most important architectural decision.

Every contributor gets isolated experiment space.

Example:

```text
research/balu/experiments/exp-001-hyde/
research/nishitha/experiments/exp-003-ragas/
```

This solves:

* duplicated work
* unclear ownership
* copied experiments
* notebook chaos
* mixed observations
* Git conflicts

Shared baselines remain in:

```text
research/shared/
```

---

## datasets/

Datasets separated from production code.

Supports:

* Kaggle enterprise RAG dataset
* GCC contract datasets
* synthetic DMRC datasets

Large corpora should NEVER be committed directly into Git.

Use:

* manifests
* download scripts
* preprocessing pipelines

---

## infra/

Everything infrastructure-related.

Contains:

* Docker
* pgvector
* Apache AGE
* nginx
* monitoring
* Grafana
* Prometheus
* Loki

Keeps infrastructure separate from application logic.

---

## deployment/

Deployment stages clearly separated.

Supports:

* temporary WSL development
* Ubuntu development
* future production deployment

Prevents:

* WSL hacks leaking into production docs
* Ubuntu confusion
* deployment inconsistency

---

## docs/

Clean documentation hierarchy.

Only 3 documentation categories exist:

1. Living Docs
   Current architecture and setup.

2. Research Docs
   Experiment findings and observations.

3. Archived Material
   Old bootcamp docs and reference material.

This prevents duplicated markdown chaos.

---

# CONTRIBUTOR FLOW

Current Contributors:

* Balu
* Nishitha

Each contributor:

* owns experiments
* owns findings
* owns logs
* owns notebooks

Shared infrastructure is collaborative.

Experiment results are independent.

This directly aligns with the review feedback:

* independent observations
* independent Git history
* independent experiment analysis

---

# EDGE CASES THIS STRUCTURE HANDLES

## Future Frontend

Already isolated in:

```text
apps/web/
```

---

## API Scaling

Backend already modularized.

Supports:

* REST
* WebSockets
* streaming responses
* async retrieval

---

## GPU Migration

LLM providers abstracted.

Can switch:

* Groq
* vLLM
* OpenRouter
* Cerebras
  without rewriting retrieval logic.

---

## Multi-Tenant Isolation

Security layer already separated.

Supports:

* tenant filtering
* RLS
* metadata isolation
* future auth systems

---

## Large PDFs

Dedicated ingestion pipeline.

Supports:

* OCR
* parsing
* validation
* chunking strategies

---

## Experiment Explosion

Research directories isolate chaos from production.

---

## Future Students

Simply add:

```text
research/student-name/
```

---

# WHAT SHOULD BE REMOVED FROM CURRENT REPO

Delete:

* latest/
* final/
* final_final/
* temp/
* backup/
* test/
* copy/
* old_notebooks/

Delete:

* duplicate markdown docs
* random screenshots
* old setup hacks
* root-level notebooks
* experimental scripts mixed into production folders

Archive:

* original bootcamp docs
* old setup notes
* temporary experiments
* deprecated architecture drafts

---

# CLEAN BRANCH STRATEGY

```text
main
develop

feature/balu-hyde
feature/balu-rerank

feature/nishitha-ragas
feature/nishitha-multiquery
```

No direct commits to main.

---

# FUTURE ROADMAP

Phase 1:

* clean modular repo
* ingestion
* chunking
* retrieval
* evaluation

Phase 2:

* API layer
* internal playground UI
* Docker standardization

Phase 3:

* frontend integration
* auth
* multi-user workflows

Phase 4:

* GraphRAG
* agentic orchestration
* workflow routing

Phase 5:

* production deployment
* observability
* telemetry
* scaling
* load testing

---

# FINAL PRINCIPLE

The repository should feel like:

* an AI systems lab
* a production engineering platform
* a retrieval research environment
* an enterprise RAG foundation

NOT:

* a student tutorial repo
* a notebook collection
* a bootcamp dump
* a random AI experiments folder