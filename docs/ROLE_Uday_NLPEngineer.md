# 🧠 ROLE: UDAY — NLP / RAG ENGINEER

**Reporting To**: Vaibhav (Strategic Advisor), Chowdappa (Sprint Master)  
**Coordinates With**: Backend1 (Infrastructure), Backend2 (APIs/Data)  
**Technical Authority**: embedding model, retrieval strategy, RAG pipeline  
**Contact Emergency**: Chowdappa (within 1 hour), Vaibhav (if >2 hrs blocked)

---

## 📍 YOUR ROLE IN 30 SECONDS

You are the **technical brain** behind the RAG pipeline.

Your job:
- ✅ Design + implement embedding strategy
- ✅ Implement 5 retrieval strategies (BM25, vector, fusion, multi-hop, agentic)
- ✅ Run breaking experiments (find edge cases)
- ✅ Optimize for latency + accuracy
- ✅ Write evaluation code (RAGAS)

**Note**: You don't manage team, don't give presentations. You code.

---

# 📅 YOUR DAILY CHECKLIST (April 4-26)

## PHASE 0: PRE-BOOTCAMP (April 4-14)

### **April 4 (Friday) — TODAY**

**YOUR TASK**: Shallow read + prep environment

- [ ] Read MASTER_BOOTCAMP_PLAYBOOK.md (sections 1-3, 5-8)
- [ ] Read ROLE_Backend1_Infrastructure.md (understand what infra will exist)
- [ ] Read ai_execution_plan.md (understand what AI co-pilot will generate)

**PREP WORK** (optional, if working):
- [ ] Clone LangChain + LangGraph repo locally (just clone, don't run)
- [ ] Install locally: `sentence-transformers` (for embedding testing)
- [ ] Install locally: `chromadb` (for quick local testing before PostgreSQL)
- [ ] Create folder: `/aipms-rag-bootcamp/notebooks/`

**YOUR DEPENDENCIES**:
- ⏳ Backend1: HPC infrastructure (awaiting Apr 12)
- ⏳ Backend2: API credentials (awaiting Apr 9-10)
- ⏳ Chowdappa: MD approval (awaiting Apr 10)

---

### **April 5 (Saturday)**

**STATUS**: Weekend

- [ ] Review LangChain documentation (1 hr)
  - Chains
  - Retrievers
  - QA chains
- [ ] Review LangGraph documentation (1 hr)
  - State graphs
  - Node definitions
  - Router patterns
- [ ] Optional: Download embedding model locally (sentence-transformers all-MiniLM) - it's small (22MB)

---

### **April 6 (Sunday)**

**STATUS**: Weekend

- [ ] Review RAGAS evaluation framework
  - Metrics: Faithfulness, AnswerRelevancy, ContextPrecision, ContextRecall, AspectCritique
  - How to setup evaluator model + LLM for evaluation
  - Golden dataset format

- [ ] Think through: Chunking strategies to test
  - Strategy 1: fixed 512 tokens
  - Strategy 2: recursive (500 tokens, 50 overlap)
  - Strategy 3: semantic (by paragraph)
  - Strategy 4: document-structure-aware (by section)
  - Strategy 5: parent-child (fine-grain chunks + parent doc reference)

---

### **April 7 (Monday)**

**YOUR TASK**: Finalize test queries + evaluation framework (offline work, no infrastructure needed)

- [ ] Create golden query dataset (50+ queries)
  - Format: JSON with fields: query | correct_answer | expected_context | difficulty (easy/hard)
  - Source: Based on Kaggle contracts, GCC clauses, DMRC policies
- [ ] Example query format:
  ```json
  {
    "query": "What are the penalties for late submission in government contracts?",
    "correct_answer": "Penalties as per clause 15.2 of contract terms",
    "expected_context": "GCC clause 15, Contract penalties section",
    "difficulty": "medium"
  }
  ```

- [ ] Document: `/notebooks/golden_queries_v1.json` (save locally, will transfer to HPC)

---

### **April 8 (Tuesday)**

**YOUR TASK**: Create evaluation harness (no infrastructure needed yet)

- [ ] Write Python script (local, on your laptop):
  ```python
  # File: evaluate_rag.py
  # Functions:
  # - load_golden_queries(path)
  # - evaluate_precision_at_k(results, ground_truth, k=5)
  # - evaluate_latency(query, pipeline, num_runs=10)
  # - evaluate_ragas_metrics(query, context, generation, evaluator_llm)
  # - generate_report()
  
  # Save as: /notebooks/evaluate_rag.py
  ```

- [ ] Document: `/notebooks/evaluation_harness_design.txt` (pseudo-code)

---

### **April 9 (Wednesday)**

**YOUR TASK**: Offline preparation (no infrastructure yet)

- [ ] Write chunking strategy implementations (local):
  - `chunking_fixed.py` (512 tokens)
  - `chunking_recursive.py` (500 + 50 overlap)
  - `chunking_semantic.py` (by paragraph)
  - `chunking_structure.py` (by document header)
  - `chunking_parent_child.py` (hierarchical)
- [ ] Save at: `/notebooks/chunking_strategies/`

- [ ] Identify 3 sample contracts (small ones, ~10 pages each) for Day 1 testing
  - What: Download locally to test chunking offline
  - Goal: See how each strategy chunks these before testing on full dataset

---

### **April 10 (Thursday)**

**YOUR TASK**: Wait for MD approval + finalize templates

**MORNING**:
- [ ] Check with Chowdappa: "Has MD approved yet?"
- [ ] If NO: Continue prep work below
- [ ] If YES: Prepare Day 0 infrastructure kick-off

**PREP WORK**:
- [ ] Create template: `/notebooks/day1_embedding_comparison.ipynb`
  - Pseudo-code for embeddings testing
  - Placeholders for: model1, model2, model3 comparisons
  - Latency measurement setup
  - Precision@5 measurement
  - UMAP visualization code

- [ ] Create template: `/notebooks/breaking_experiments.ipynb`
  - 5 experiment skeletons (FE-01 to FE-05)
  - Error checking logic
  - Result logging format

---

### **April 11 (Friday)**

**YOUR TASK**: Final prep before Day 0

**MORNING**:
- [ ] Confirm with Backend1: "PostgreSQL + pgvector running? Can I SSH + access?"
- [ ] Confirm with Backend2: "API keys ready? Can I test them?"

**IF ALL YES**:
- [ ] Download infrastructure scripts from AI co-pilot (Bash + SQL)
- [ ] Review scripts (understand what infra will look like)

**AFTERNOON**:
- [ ] Create checklist: `/daily-logs/day0_infrastructure_requirements.txt`
  ```
  PostgreSQL: __ running
  pgvector: __ extension loaded
  Jupyter: __ accessible on port XXXX
  Groq API: __ tested
  Google API: __ tested
  Sample data: __ loaded in PostgreSQL
  ```

- [ ] Prepare mind: "By 6 PM tomorrow (Apr 12), I need PostgreSQL + Jupyter ready to code"

---

## PHASE 1: DAY 0 INFRASTRUCTURE SPIKE (April 12-13)

### **April 12 (Saturday) — INFRASTRUCTURE DAY 1**

**9:00 AM KICKOFF** — You're on standby (Backend1 is main actor)

- [ ] **9:00 AM**: Chowdappa check-in
  - Q: "Is PostgreSQL installation started?"
  - Q: "Any blockers already?"
  - Your role: OBSERVER + ADVISOR (if they ask technical questions)

- [ ] **10:00 AM**: Backend1 SSH working? Can you access HPC?
  - Test logins to Jupyter
  - Try importing Python libraries (pandas, sklearn, langchain)
  - If Python import fails → Report to Backend1 + Chowdappa

**12:00 PM**: Should PostgreSQL be running? Backend1 reports to you

- [ ] [ ] PostgreSQL running? (ask Backend1 to run: `psql -U postgres -c "SELECT version();"`
- [ ] [ ] pgvector extension? (ask: `psql -U postgres -c "CREATE EXTENSION IF NOT EXISTS vector;"`
- [ ] [ ] If error → debug with Backend1 (usually dependency issue)

**3:00 PM**: Still waiting for infra? Prepare Day 1 code

- [ ] Download your local scripts to HPC:
  - Chunking strategies → `/HPC/chunking_strategies/`
  - Evaluation harness → `/HPC/evaluate_rag.py`
  - Golden queries → `/HPC/golden_queries_v1.json`
- [ ] If SFTP not working yet → save to `/tmp/` for transfer

**6:00 PM**: Infrastructure checkpoint

- [ ] PostgreSQL: ✅ or ❌?
- [ ] Jupyter: ✅ or ❌?
- [ ] If both ✅: You're ready for Day 1. Get rest.
- [ ] If any ❌: Document blocker, Chowdappa handles escalation

---

### **April 13 (Sunday) — INFRASTRUCTURE DAY 2 (FINAL)**

**9:00 AM**: PostgreSQL + Jupyter MUST be ready today

- [ ] Quick test: Can you login to Jupyter from laptop?
  - [ ] `jupyter notebook --ip=0.0.0.0 --port=8888` (Backend2 should have this running)
  - [ ] Test: Open http://[HPC-IP]:8888 in browser
  - [ ] Import: `import psycopg2` + `from langchain.embeddings import HuggingFaceEmbeddings`

**10:00 AM**: You're here to **validate infrastructure is correct**

- [ ] PostgreSQL test:
  ```sql
  CREATE TABLE test_vectors (id SERIAL, embedding vector(384));
  INSERT INTO test_vectors VALUES (1, '[0.1, 0.2, ..., 0.384]');
  SELECT * FROM test_vectors;
  \q
  ```
  - [ ] Works? ✅ PostgreSQL + pgvector ready
  - [ ] Fails? ❌ Report to Backend1

**11:00 AM**: API test

- [ ] Ask Backend2: "Are API keys loaded into environment?"
  - [ ] Export GROQ_API_KEY? (check: `echo $GROQ_API_KEY` on HPC)
  - [ ] Export GOOGLE_API_KEY?
  - [ ] Export HF_TOKEN?
  - [ ] Export OPENROUTER_KEY?

- [ ] Test in Python:
  ```python
  from groq import Groq
  client = Groq()  # Should use env var
  # If import works, API ready ✅
  ```

**12:00 PM**: Load sample data

- [ ] Backend2 should have already downloaded datasets. You verify:
  - [ ] Kaggle contracts: `/data/datasets/kaggle-enterprise-rag/` - count .md files
  - [ ] GCC: `/data/datasets/indian-railways-gcc-2022/` - PDF exists + readable?
  - [ ] DMRC: `/data/datasets/synthetic-dmrc/` - count YAML files
  - [ ] Document: `/daily-logs/apr13_data_verification.txt`

**1:00 PM - 4:00 PM**: First PostgreSQL data load (CRITICAL)

- [ ] Create notebook: `/notebooks/day0_load_sample_data.ipynb`
  ```python
  # Steps:
  # 1. Load 10 sample documents (Kaggle)
  # 2. Chunk using chunking_fixed strategy
  # 3. Generate embeddings (all-MiniLM-L6-v2)
  # 4. Insert into PostgreSQL
  # 5. Test similarity search: retrieve top-3 for test query
  ```

- [ ] If this works → Entire pipeline works → Ready for Monday ✅
- [ ] If password auth fails → Backend1 fixes PostgreSQL permissions
- [ ] If embedding fails → Check HuggingFace token + internet

**4:00 PM - 5:30 PM**: Finalize checklist

- [ ] PostgreSQL: ✅ Can insert + retrieve + similarity search works
- [ ] Jupyter: ✅ All imports work (langchain, chromadb, sentence-transformers, ragas)
- [ ] APIs: ✅ All keys loaded correctly
- [ ] Data: ✅ Samples loaded, chunking works
- [ ] Document: `/daily-logs/apr13_infrastructure_final_check.txt` — SUCCESS ✅ or FAILURE ❌

**6:00 PM FINAL**:
- [ ] If ALL ✅:
  - Message to Chowdappa: "Infrastructure ready. Day 1 bootcamp can start Monday 9 AM"
  - Rest well, you earned it
- [ ] If ANY ❌:
  - Message to Chowdappa: "Infrastructure incomplete. [Issue]. Blocking Day 1."
  - Chowdappa escalates to Vaibhav + activates Colab contingency

---

## PHASE 2: WEEK 1 BOOTCAMP (April 15-19)

**OVERALL GOAL WEEK 1**: Build proof-of-concept RAG that handles 1 contract type (Kaggle enterprise contracts)

### **April 15 (Monday) — DAY 1: EMBEDDING COMPARISON**

**9:00 AM STANDUP** (15 mins)
- Your today: "Comparing 3 embedding models for latency + quality"
- Backend1: "Monitoring PostgreSQL"
- Backend2: "Monitoring APIs + data pipeline"

**9:15 AM - 12:00 PM**: Embedding Model Comparison

- [ ] **Task**: Test 3 embedding models on 100 sample queries

  **Model 1**: `all-MiniLM-L6-v2` (22MB, fast, baseline)
  - Dimensions: 384
  - Inference time per document: ~10ms (CPU)

  **Model 2**: `BAAI/bge-large-en-v1.5` (335MB, slower, better quality)
  - Dimensions: 1024
  - Inference time per document: ~50ms (CPU)

  **Model 3**: `nomic-embed-text-v1.5` (250MB, medium, good enterprise)
  - Dimensions: 768
  - Inference time per document: ~30ms (CPU)

- [ ] Notebook: `/notebooks/day1_embedding_comparison.ipynb`
  - [ ] Load 100 Kaggle contracts (randomly sampled)
  - [ ] Chunk each using chunking_fixed (512 tokens)
  - [ ] Generate embeddings using model 1, 2, 3
  - [ ] Metric: Encoding time for 100 docs (should be < 10 secs for Day 1 PoC)
  - [ ] Metric: Similarity search latency (retrieve top-5) — should be < 100ms per query

**12:00 PM - 1:00 PM**: Lunch break

**1:00 PM - 5:00 PM**: Quality evaluation

- [ ] For each model:
  - [ ] Test on 20 golden queries
  - [ ] Metric: Precision@5 (does correct document appear in top-5?)
  - [ ] Document precision numbers

- [ ] Visualization:
  - [ ] UMAP plot: Visualize 1000 embeddings in 2D space for each model
  - [ ] Expected: Contracts should cluster by type (if UMAP clean, embeddings are good)

**5:00 PM - 6:00 PM**: Decision + Documentation

- [ ] **DECISION**: Which model for Day 2-5?
  - [ ] Criteria: Best precision@5 + acceptable latency
  - [ ] If tie: Choose smaller model (faster inference)

- [ ] Document: `/daily-logs/apr15_day1_embedding_decision.txt`
  ```
  Model Selected: [Model name]
  Precision@5: X%
  Avg Latency: Y ms
  Reason: [Why this model]
  
  Alternative if degradation: Switch to [Model2] if precision drops
  ```

- [ ] Update dashboard: `/metrics-dashboard/latency_tracking.csv`
  ```
  Date,Task,Latency_ms,Precision_at5
  2026-04-15,Embedding_Model1,X,Y
  2026-04-15,Embedding_Model2,X,Y
  2026-04-15,Embedding_Model3,X,Y
  ```

**EXIT CRITERIA**:
- ✅ 3 embeddings compared
- ✅ Precision@5 baseline established (target: >70%)
- ✅ Model selected for Day 2+
- ✅ UMAP visualization confirms good clustering

---

### **April 16 (Tuesday) — DAY 2: CHUNKING STRATEGIES**

**9:00 AM STANDUP**
- Your today: "Comparing 5 chunking strategies"

**9:15 AM - 12:00 PM**: Implement + Test Chunking

- [ ] **Task**: Test 5 chunking strategies (you wrote code locally, now run)

  **Strategy 1**: Fixed window (512 tokens)
  - Pros: Fast, predictable
  - Cons: May cut sentences mid-word

  **Strategy 2**: Recursive (500 tokens, 50 overlap)
  - Pros: Keeps context
  - Cons: Slightly larger storage

  **Strategy 3**: Semantic (by paragraph/section)
  - Pros: Semantically coherent
  - Cons: Variable size chunks

  **Strategy 4**: Document structure-aware (by section\heading)
  - Pros: Preserves hierarchy
  - Cons: Complex to implement

  **Strategy 5**: Parent-child (hierarchical)
  - Pros: Can retrieve parent + siblings
  - Cons: More storage, more retrieval logic

- [ ] Notebook: `/notebooks/day2_chunking_comparison.ipynb`
  - [ ] Load 100 Kaggle contracts
  - [ ] Apply all 5 chunking strategies
  - [ ] Metric: Avg chunk size (how many tokens?)
  - [ ] Metric: Number of chunks per document
  - [ ] Metric: Search time × Number of chunks (trade-off)

**12:00 PM - 1:00 PM**: Lunch

**1:00 PM - 5:00 PM**: Quality evaluation

- [ ] For each strategy:
  - [ ] Test on 20 golden queries
  - [ ] Metric: Precision@5 (does correct chunk appear in top-5?)
  - [ ] Metric: Redundancy (how many duplicate chunks?)

**5:00 PM - 6:00 PM**: Decision + Documentation

- [ ] **DECISION**: Which chunking strategy for Day 3-5?

- [ ] Document: `/daily-logs/apr16_day2_chunking_decision.txt`
  ```
  Strategy Selected: [Name]
  Avg Chunk Size: X tokens
  Chunks per Doc: Y
  Precision@5: Z%
  Reason: [Why selected]
  ```

**EXIT CRITERIA**:
- ✅ 5 strategies tested + compared
- ✅ Chunking strategy selected (best precision@5)
- ✅ Chunk inventory: Know how many vectors to store

---

### **April 17 (Wednesday) — DAY 3: BREAKING EXPERIMENTS (CRITICAL)**

**🔴 THIS IS THE MOST IMPORTANT DAY.** You expose your system to failure modes.

**9:00 AM STANDUP**
- Your today: "Running 5 breaking experiments to find edge cases"

**9:15 AM - 12:00 PM**: FE-01 + FE-02 Failures

**FE-01: Cross-Entity Confusion**
- [ ] Create adversarial query: "Penalties for late payment in railway vs highway contracts"
- [ ] This query mentions 2 entity types that might confuse retriever
- [ ] Expected failure: Retriever mixes entities (railway + highway + penalty)
- [ ] Test: Does system return ONLY railway penalties or mix?
- [ ] Notebook: `/notebooks/day3_fe01_cross_entity_confusion.ipynb`
- [ ] Fix (if failed):
  - Option A: Add entity filter (contract_type=railway)
  - Option B: Use doc-level metadata filtering
  - Option C: Reranker catches error
- [ ] Document: `/daily-logs/apr17_fe01_result.txt` — PASS ✅ or FAIL ❌ + Fix

**FE-02: Contract Version Confusion**
- [ ] Create query: "What is the new penalty clause?" (ambiguous — new to whom?)
- [ ] Expected failure: Retriever returns OLD version (outdated)
- [ ] Test: System retrieves latest version only?
- [ ] Fix:
  - Option A: Add version filter (version >= 2022)
  - Option B: Chunk metadata includes contract_date
  - Option C: Reranker scores recent versions higher
- [ ] Document: `/daily-logs/apr17_fe02_result.txt`

**12:00 PM - 1:00 PM**: Lunch

**1:00 PM - 3:00 PM**: FE-03 + FE-04 Failures

**FE-03: Long Document Bias**
- [ ] Create 2 documents: 1 short (5 pages), 1 long (100 pages)
- [ ] Both contain answer to a query, but answer is at very different locations
- [ ] Expected failure: Retriever biases towards long document (more chunks = more similarity hits)
- [ ] Test: Does system fairly rank both?
- [ ] Fix:
  - Option A: Normalize by document length
  - Option B: Use cross-encoder reranker (better semantic match)
  - Option C: BM25 + vector fusion (RRF) reduces bias
- [ ] Document: `/daily-logs/apr17_fe03_result.txt`

**FE-04: Adversarial Query**
- [ ] Create query: "What does NOT apply in this contract?"
- [ ] Expected failure: LLM generates contradiction
- [ ] Test: Does system refuse or generate wrong answer?
- [ ] Fix:
  - Option A: LLM system prompt includes "do not invent"
  - Option B: Check generated answer against retrieved context (self-verification)
  - Option C: Use lower-temp LLM (less creative = more grounded)
- [ ] Document: `/daily-logs/apr17_fe04_result.txt`

**3:00 PM - 5:00 PM**: FE-05 Failure

**FE-05: Tenant/Package Leakage**
- [ ] Simulate: User A queries "My contract penalties" but retriever returns User B's contract
- [ ] Expected failure: No isolation, all users see all data
- [ ] Test: Add contract_owner metadata filter. Does system properly isolate?
- [ ] Fix:
  - Option A: Add WHERE clause: `WHERE contract_owner = current_user`
  - Option B: Embed user_id into chunk metadata
  - Option C: Query routing (route per-tenant search)
- [ ] Document: `/daily-logs/apr17_fe05_result.txt`

**5:00 PM - 6:00 PM**: Summary + Fixes

- [ ] **All 5 failures documented** (passed or failed with fix)
- [ ] Create fix implementations for any failures
- [ ] Document: `/daily-logs/apr17_breaking_experiments_summary.txt`
  ```
  FE-01 Cross-Entity: PASS ✅ / FAIL ❌ [Fixed by ___]
  FE-02 Version: PASS ✅ / FAIL ❌ [Fixed by ___]
  FE-03 Long Doc Bias: PASS ✅ / FAIL ❌ [Fixed by ___]
  FE-04 Adversarial: PASS ✅ / FAIL ❌ [Fixed by ___]
  FE-05 Tenant Leakage: PASS ✅ / FAIL ❌ [Fixed by ___]
  
  Overall Status: Ready for prod ✅ / Needs hardening ❌
  ```

**EXIT CRITERIA**:
- ✅ All 5 experiments run
- ✅ Failures identified + solutions documented
- ✅ Critical fixes implemented

---

### **April 18 (Thursday) — DAY 4: HYBRID SEARCH + RERANKING**

**9:00 AM STANDUP**
- Your today: "Implementing hybrid search (BM25 + Vector + RRF + Reranking)"

**9:15 AM - 12:00 PM**: Hybrid Search Implementation

- [ ] **Task**: Combine BM25 + Vector search with Reciprocal Rank Fusion

- [ ] Notebook: `/notebooks/day4_hybrid_search.ipynb`
  - [ ] Step 1: BM25 search (PostgreSQL tsvector)
    ```sql
    SELECT id, chunk_text, ts_rank_cd(to_tsvector(chunk_text), query) AS score
    FROM chunks
    WHERE to_tsvector(chunk_text) @@ query
    LIMIT 10;
    ```
  - [ ] Step 2: Vector search
    ```sql
    SELECT id, chunk_text, 1 - (embedding <=> query_embedding) AS score
    FROM chunks
    ORDER BY embedding <=> query_embedding
    LIMIT 10;
    ```
  - [ ] Step 3: RRF Fusion
    ```
    RRF_score = 1/(60 + rank_bm25) + 1/(60 + rank_vector)
    ```

- [ ] Test on 20 golden queries:
  - [ ] Metric: Precision@5 (is correct context in top-5?)
  - [ ] Target: >85% (better than embedding alone)
  - [ ] Metric: Latency (BM25 + Vector together)

**12:00 PM - 1:00 PM**: Lunch

**1:00 PM - 4:00 PM**: Reranking Implementation

- [ ] **Task**: Apply cross-encoder reranker to hybrid search results

- [ ] Model: `cross-encoder/ms-marco-MiniLM-L-12-v2`
  - Scores document-query pairs on relevance scale 0-1
  - Slower than embedding (but only on top-10, not all)

- [ ] Pipeline:
  ```python
  # 1. Hybrid search → top 30 results
  # 2. Reranker scores each: relevance_score = reranker(query, chunk)
  # 3. Sort by relevance_score, return top 5
  ```

- [ ] Test:
  - [ ] 20 golden queries
  - [ ] Metric: Precision@5 (should be 90%+)
  - [ ] Metric: Latency (embedding + BM25 + reranker)
  - [ ] Target: < 1 second total

**4:00 PM - 5:00 PM**: Final Optimization

- [ ] Latency breakdown:
  - Embedding query: ~20ms
  - BM25 search: ~30ms
  - Vector search: ~50ms
  - Reranking (top-30): ~100ms
  - TOTAL: ~200ms (well under 2s target) ✅

- [ ] Document: `/daily-logs/apr18_day4_hybrid_search.txt`
  ```
  Hybrid Search Precision@5: X%
  Reranking Precision@5: Y%
  Latency (total): Z ms
  BM25 time: A ms
  Vector time: B ms
  Reranker time: C ms
  Status: Ready for LLM integration
  ```

**EXIT CRITERIA**:
- ✅ Hybrid search working (BM25 + Vector + RRF)
- ✅ Reranking working
- ✅ Precision@5 > 85%
- ✅ Latency < 1 second

---

### **April 19 (Friday) — DAY 5: END-TO-END RAG v1**

**9:00 AM STANDUP**
- Your today: "Building complete RAG v1 (retrieval → LLM generation)"

**9:15 AM - 12:00 PM**: Integration

- [ ] **Task**: Connect hybrid search + reranker to LLM (Groq Llama 3.3 70B)

- [ ] Notebook: `/notebooks/day5_rag_e2e_v1.ipynb`
  ```python
  # 1. Query input
  # 2. Hybrid search → top-5 chunks
  # 3. Reranker → filtered top-5
  # 4. LLM prompt:
  #    "Context: [Top 5 chunks]
  #     Question: [User query]
  #     Answer (cite source):"
  # 5. LLM generation (Groq)
  # 6. Parse + return answer
  ```

- [ ] Test:
  - [ ] 20 golden queries
  - [ ] Generate answers using Groq
  - [ ] Metric: Latency (total pipeline)
  - [ ] Metric: Answer quality (does it cite sources?)

**12:00 PM - 1:00 PM**: Lunch

**1:00 PM - 4:00 PM**: Demo Preparation

- [ ] **Task**: Create presentation notebook (what Chowdappa will demo Monday)

- [ ] Notebook: `/notebooks/demo_rag_v1.ipynb`
  ```python
  # Demo 1: Single query walkthrough
  query = "What are penalties for late payment in supply contracts?"
  # Show: Retrieval → Reranking → LLM generation
  
  # Demo 2: Latency breakdown
  # Show: 50ms retrieval, 100ms reranking, 800ms LLM = 950ms total
  
  # Demo 3: Precision@5 comparison
  # Chart: Embedding-only vs BM25-only vs Hybrid vs Hybrid+Reranker
  
  # Demo 4: Breaking experiments
  # Show: Cross-entity handling, version isolation, tenant safety
  ```

**4:00 PM - 5:00 PM**: Final Metrics + Documentation

- [ ] Document: `/daily-logs/apr19_day5_rag_e2e.txt`
  ```
  End-to-End RAG Status: READY ✅ / ISSUES ❌
  
  Precision@5: X%
  Latency Components:
    - Query encoding: A ms
    - Hybrid search: B ms
    - Reranking: C ms
    - LLM generation: D ms
    - TOTAL: E ms (target: <2s)
  
  Demo Readiness: Ready to show Chowdappa
  
  Week 1 Deliverables:
    ✅ Embedding model selected
    ✅ Chunking strategy selected
    ✅ Breaking experiments passed
    ✅ Hybrid search + reranking working
    ✅ End-to-end RAG v1 working
    ✅ 20 demo queries tested
  ```

- [ ] Update metrics dashboard: `/metrics-dashboard/latency_tracking.csv`
  ```
  Date,Task,Latency_ms,Precision_at5
  2026-04-19,RAG_E2E_v1,950,92%
  ```

**5:00 PM - 6:00 PM**: Week 1 Retrospective

- [ ] Document: `/weekly-summaries/week1_summary.md`
  ```markdown
  # Week 1 Summary (Apr 15-19)
  
  ## ✅ What Went Well
  - Embedding comparison completed on schedule
  - Chunking strategy optimized early
  - Breaking experiments caught 2 critical issues
  - Hybrid search exceeded precision target
  
  ## ❌ What Broke + How Fixed
  - FE-03 (long doc bias): Fixed with RRF weighting
  - Tenant isolation missing: Added WHERE clause
  - Latency spike on Day 4: Reduced rerank size from 30 to 10
  
  ## 📊 Final Metrics
  - Precision@5: 92% (target: >85%) ✅
  - Latency: 950ms (target: <2s) ✅
  - System confidence: Ready for Week 2 complexity
  
  ## 🎯 Week 2 Priorities
  1. Multi-hop retrieval (2-3 step queries)
  2. LangGraph agentic RAG (dynamic routing)
  3. RAGAS evaluation (50+ queries, golden dataset)
  4. Performance hardening (scale from 100 docs → 10K docs)
  ```

**EXIT CRITERIA**:
- ✅ Complete RAG v1 pipeline working
- ✅ Demo prepared + rehearsed
- ✅ Precision > 85%, Latency < 2s
- ✅ All Week 1 goals achieved

---

## PHASE 3: WEEK 2 BOOTCAMP (April 22-26)

**OVERALL GOAL WEEK 2**: Build agentic RAG + evaluation framework

### **April 22 (Monday) — DAY 6: QUERY ROUTING**

**9:00 AM STANDUP**
- Your today: "Implementing query router (classify → route to strategy)"

**9:15 AM - 6:00 PM**: Same daily rhythm as Week 1

- [ ] **Task**: Build LangGraph router
  - Step 1: Classify query type (single-hop vs multi-hop, retrieval-needed?)
  - Step 2: Route to strategy (vector search vs BM25 vs multi-hop)
  - Step 3: Execute strategy
  - Step 4: Synthesize answer

- [ ] Document: `/daily-logs/apr22_day6_query_routing.txt`

---

### **April 23 (Tuesday) — DAY 7: LANGGRAPH AGENT**

- [ ] **Task**: Multi-hop reasoning
  - Query: "What penalties apply to suppliers who miss deadlines for payments under government contracts?"
  - Step 1: Retrieve (penalties article)
  - Step 2: Retrieve (supplier clauses)
  - Step 3: Synthesize (combine)

- [ ] Document: `/daily-logs/apr23_day7_langgraph.txt`

---

### **April 24 (Wednesday) — DAY 8: RAGAS EVALUATION**

- [ ] **Task**: Run full RAGAS evaluation on golden dataset (50+ queries)
  - Metrics: Faithfulness, AnswerRelevancy, ContextPrecision, ContextRecall
  - Target: All > 0.75

- [ ] Document: `/daily-logs/apr24_day8_ragas_eval.txt`

---

### **April 25 (Thursday) — DAY 9: PERFORMANCE HARDENING**

- [ ] **Task**: Scale from 100 docs → 10K docs
  - Latency should stay < 2s
  - Vector indexing (pgvector can handle 10K easily)

- [ ] Document: `/daily-logs/apr25_day9_scaling.txt`

---

### **April 26 (Friday) — DELIVERY DAY**

- [ ] Demo + presentation
- [ ] All code pushed to GitHub
- [ ] Final documentation filled

---

# ⚠️ BLOCKERS YOU'LL FACE

## **Blocker 1: PostgreSQL Connection Fails**

**When**: Day 0 (Apr 13) or Day 1 (Apr 15)

**Impact**: Can't run any code

**Resolution**:
1. Check: Is PostgreSQL running? (`psql -U postgres -c "SELECT 1"` on HPC)
2. Check: Is pgvector installed? (`psql -U postgres -c "CREATE EXTENSION vector"`)
3. If both fail → Contact Backend1 + Chowdappa
4. Fallback: Use ChromaDB (no SQL, just Python dict-based)

**Whom to Contact**: Backend1 → Chowdappa

---

## **Blocker 2: API Rate Limit Hit**

**When**: Day 1-5 (when calling Groq repeatedly)

**Impact**: LLM calls fail mid-task

**Resolution**:
1. Check: Which API hit limit? (Groq: 30 req/min)
2. Batch requests (wait, then retry in batch)
3. Switch to Google AI Studio (lower rate limit, but doesn't fail as often)
4. Use cached responses (don't re-query same thing)

**Whom to Contact**: Backend2 (manages API keys) → Chowdappa

---

## **Blocker 3: Embedding Model Too Slow**

**When**: Day 1 (early signal)

**Impact**: Encoding 100 docs takes > 30 mins (unacceptable)

**Resolution**:
1. Switch to smaller model (all-MiniLM L6 instead of BGE)
2. Batch encode (faster than one-by-one)
3. Use GPU acceleration if available (unlikely on GPREC HPC CPU-only)

**Whom to Contact**: You decide + document choice → Chowdappa

---

## **Blocker 4: Precision@5 Below 70% on Day 1**

**When**: Day 1 (early signal of architecture problem)

**Impact**: Downstream tasks assume >70% baseline precision

**Resolution**:
1. Analyze: Why is precision low?
   - Bad embeddings? → Try different model
   - Bad chunking? → Refine chunk size
   - Bad query? → Refine golden dataset
2. Iterate quickly (each model takes 5 mins to test)
3. If still failing → Escalate to Vaibhav (may need design change)

**Whom to Contact**: Chowdappa (for model switch), Vaibhav (for design change)

---

## **Blocker 5: Breaking Experiment Reveals Unfixable Issue**

**When**: Day 3 (FE-01 to FE-05)

**Impact**: System fails on production edge case

**Resolution**:
1. Document issue + why unfixable in time
2. Propose workaround (if system can detect + handle gracefully)
3. Escalate to Vaibhav (accept limitation or redesign?)

**Whom to Contact**: Vaibhav (architectural decision) → Chowdappa (timeline impact)

---

# 📞 ESCALATION CHART

```
YOU HIT TECHNICAL BLOCKER
    ↓
Can you fix in 2 hours?
    ↓
[YES] → Fix + document
[NO]  → Contact:
         - Backend1 (infrastructure issues)
         - Backend2 (data/API issues)
         - Chowdappa (coordination)
         ↓
Chowdappa helps → Can fix in 4 hours?
    ↓
[YES] → Continue
[NO]  → Chowdappa escalates to Vaibhav
         ↓
Vaibhav decision: Continue / Pivot / Accept limitation
```

---

# 💾 YOUR DOCUMENTATION STRUCTURE

```
/aipms-rag-bootcamp/
  ├── notebooks/
  │   ├── golden_queries_v1.json
  │   ├── chunking_strategies/
  │   │   ├── chunking_fixed.py
  │   │   ├── chunking_recursive.py
  │   │   ├── chunking_semantic.py
  │   │   ├── chunking_structure.py
  │   │   └── chunking_parent_child.py
  │   ├── day0_load_sample_data.ipynb
  │   ├── day1_embedding_comparison.ipynb
  │   ├── day2_chunking_comparison.ipynb
  │   ├── day3_fe01_cross_entity_confusion.ipynb
  │   ├── day3_fe02_contract_version_confusion.ipynb
  │   ├── day3_fe03_long_doc_bias.ipynb
  │   ├── day3_fe04_adversarial_query.ipynb
  │   ├── day3_fe05_tenant_leakage.ipynb
  │   ├── day4_hybrid_search.ipynb
  │   ├── day5_rag_e2e_v1.ipynb
  │   ├── demo_rag_v1.ipynb
  │   ├── day6_query_routing.ipynb
  │   ├── day7_langgraph_agent.ipynb
  │   ├── day8_ragas_evaluation.ipynb
  │   └── day9_scaling.ipynb
  ├── daily-logs/
  │   ├── apr15_day1_embedding_decision.txt
  │   ├── apr16_day2_chunking_decision.txt
  │   ├── apr17_breaking_experiments_summary.txt
  │   ├── apr18_day4_hybrid_search.txt
  │   ├── apr19_day5_rag_e2e.txt
  │   ├── apr22_day6_query_routing.txt
  │   ├── apr23_day7_langgraph.txt
  │   ├── apr24_day8_ragas_eval.txt
  │   └── apr25_day9_scaling.txt
  ├── weekly-summaries/
  │   ├── week1_summary.md
  │   └── week2_summary.md
  └── metrics-dashboard/
      └── latency_tracking.csv
```

---

# ✅ SUCCESS CRITERIA FOR YOUR ROLE

**By April 26, 6 PM**:

- ✅ All code written + tested
- ✅ Week 1 PoC (embedding + chunking + breaking)
- ✅ Week 2 advanced (routing + agent + RAGAS)
- ✅ Precision@5 > 85%
- ✅ Latency < 2 seconds
- ✅ Demo works 3+ times (rehearsed)
- ✅ All daily logs documented
- ✅ No silent failures (all blockers escalated on time)

**You are the code owner. You ship working RAG by Friday 5 PM.**

---

**END OF UDAY ROLE GUIDE**
