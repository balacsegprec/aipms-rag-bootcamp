# WORKFLOW EXECUTION PLAN (Apr 12-26)
## What I (AI) Can Do | What You Must Do

---

## 🎯 OVERALL STRATEGY

**I can be your 80% solution. You must own the 20% (human parts).**

### **MY CAPABILITIES (What I Can Easily Complete)**
✅ Write code for RAG pipeline  
✅ Create data processing scripts  
✅ Generate documentation & templates  
✅ Design evaluation frameworks  
✅ Troubleshoot code issues  
✅ Create demo scripts & slides  
✅ Generate all [TO FILL] sections templates  
✅ Build test cases  
✅ Plan workflows  

### **YOUR CAPABILITIES (What Only You Can Do)**
❌ Install software on actual HPC machine  
❌ Configure PostgreSQL + pgvector extensions on live server  
❌ Test APIs with real credentials  
❌ Run experiments on actual data  
❌ Make real-time decisions when things fail  
❌ Manage team (students, Uday, Vaibhav)  
❌ Handle hardware failures  
❌ Visit HPC lab physically  
❌ Approve final deliverables  

---

## 📅 PHASE 1: INFRASTRUCTURE SPIKE (April 12-13, Fri-Sat)

### **WHAT NEEDS TO HAPPEN**

**Day 0 (Apr 12-13)**: Backend students + you set up infrastructure

```
CHECKLIST (Backend Students Own This):

Task 1: PostgreSQL + pgvector Setup
  ☐ SSH into GPREC HPC
  ☐ Install PostgreSQL 14+
  ☐ Create pgvector extension
  ☐ Test: Create sample table, insert vectors, run similarity query
  
Task 2: Apache AGE + pg_trgm
  ☐ Build Apache AGE from source or apt install
  ☐ Create AGE extension
  ☐ Enable pg_trgm
  ☐ Test: BM25 search on test data

Task 3: Jupyter Lab Server
  ☐ Install Python 3.10+
  ☐ pip install jupyterlab
  ☐ Launch shared server: jupyter lab --ip=0.0.0.0 --port=8888
  ☐ Test: All 4 team members can login from different computers

Task 4: API Keys Test
  ☐ Set environment variables (Groq, Google, HuggingFace, OpenRouter)
  ☐ Test 1 API call to each (confirm it works)
  
Task 5: Datasets Staged
  ☐ Download Kaggle Enterprise RAG (2 GB)
  ☐ Download GCC 2022 PDF (3 MB)
  ☐ Get synthetic DMRC data from Vaibhav
  ☐ Verify all 3 on GPREC shared storage
```

---

### **WHAT I CAN HELP WITH (PHASE 1)**

**✅ I CAN CREATE FOR YOU:**

1. **Infrastructure Setup Script** (bash script to automate most of this)
```bash
# I'll write a script like:
# sudo apt-get install postgresql postgresql-contrib
# sudo apt-get install python3-pip
# pip install sentence-transformers pgvector langchain ragas
# ... and so on
```

2. **PostgreSQL initialization script** (SQL)
```sql
-- Create vector extension
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- Create test table
CREATE TABLE embeddings (
    id SERIAL PRIMARY KEY,
    text TEXT,
    embedding vector(384),
    entity_type TEXT
);

-- Create HNSW index for fast search
CREATE INDEX ON embeddings USING hnsw (embedding vector_cosine_ops);
```

3. **API testing script** (Python)
```python
# I'll write a script that tests all 4 APIs
# Confirms each one works
# Saves credentials securely
```

4. **Jupyter Lab setup verification** (bash)
```bash
# Check if Jupyter running on port 8888
# Check if all datasets present
# Check API keys loaded
```

---

### **❌ WHAT ONLY YOU CAN DO (PHASE 1)**

- 🚨 **SSH into actual GPREC HPC machine** — You have login, I don't
- 🚨 **Install PostgreSQL/pgvector on real hardware** — You execute, I guide
- 🚨 **Handle hardware failures** — "Disk full", "PostgreSQL crashes", etc. — You fix
- 🚨 **Approve "infra is ready"** — Only you can sign off
- 🚨 **Call lab admin if things break** — Human-to-human coordination

---

### **🔴 POTENTIAL PROBLEMS (PHASE 1)**

**Problem 1: PostgreSQL extension build fails**
- **Why**: pgvector needs C compiler, dependencies
- **I can help**: Generate correct build script
- **You must**: Execute on HPC, troubleshoot errors, ask IT if compiler missing
- **Workaround if needed**: Use ChromaDB as fallback (no pgvector needed)

**Problem 2: Jupyter Lab not accessible from outside HPC**
- **Why**: Firewall, network config
- **I can help**: Debug script to check connectivity
- **You must**: Contact HPC admin to allow port 8888
- **Workaround if needed**: Use reverse SSH tunnel or Colab

**Problem 3: API keys don't work**
- **Why**: Typo, account not activated, rate limit
- **I can help**: Check API syntax, test template
- **You must**: Verify credentials, create accounts if needed

**Problem 4: Datasets too large, storage full**
- **Why**: 75 GB not enough
- **I can help**: Compress dataset script, sample smaller dataset
- **You must**: Ask HPC admin for more storage or delete old data

**Success Criteria by EOD Apr 13**:
- ✅ Uday can SSH into GPREC
- ✅ Run Python: `from sentence_transformers import SentenceTransformer`
- ✅ Run SQL: Create vector table + insert test vector
- ✅ Jupyter Lab accessible from browser
- ✅ Can call Groq API successfully

---

## 📈 PHASE 2: WEEK 1 BOOTCAMP (April 15-19)

### **WHAT HAPPENS EACH DAY**

**Day 1 (Mon 15 Apr): Embedding Fundamentals**
- Uday: Create 3 embedding models, UMAP visualization
- Backend: Ensure data pipeline works
- You: Document progress, check if on schedule

**Day 2 (Tue 16 Apr): Chunking Strategies**
- Uday: Test 5 chunking methods on FIDIC data
- Backend: Optimize data loading
- You: Log findings, any issues?

**Day 3 (Wed 17 Apr): Breaking Experiments**
- All: Run 5 failure tests (cross-entity confusion, etc.)
- You: Log each failure + root cause
- Backend: Implement fixes

**Day 4 (Thu 18 Apr): Hybrid Search + Reranking**
- Uday: Implement BM25 + vector fusion + reranking
- Backend: Integrate with pgvector
- You: Benchmark latency (must be < 2 seconds)

**Day 5 (Fri 19 Apr): End-to-End Pipeline**
- All: First complete RAG working
- You: Run 20 test queries, save results
- Document: What works, what's still broken

---

### **WHAT I CAN HELP WITH (PHASE 2)**

**✅ BEFORE PHASE 2 STARTS, I'll create:**

1. **Day 1 Embedding Script** (ready-to-run)
```python
# embedding_comparison.py
# Load 3 models (all-MiniLM, bge-large, nomic)
# Embed 100 FIDIC clauses
# UMAP visualization
# Output: Comparison metrics table
```

2. **Day 2 Chunking Template** (5 strategies)
```python
# chunking_comparison.py
# Test: Fixed, Recursive, Semantic, Document-aware, Parent-child
# Output: P@5 scores for each strategy
# Recommendation: Which is best
```

3. **Day 3 Breaking Experiments Script**
```python
# breaking_experiments.py
# FE-01 through FE-05 automated
# Each test documents: Query, Expected, Actual, Root cause, Fix
# Output: Failure log (fills MYdeliverables.txt FE-01 to FE-05)
```

4. **Day 4 Hybrid Search Implementation**
```python
# hybrid_search.py
# BM25 search (PostgreSQL tsvector)
# Vector search (pgvector similarity)
# RRF fusion (Reciprocal Rank Fusion)
# Reranking (cross-encoder/ms-marco)
# Output: Speed + accuracy comparison
```

5. **Day 5 End-to-End RAG Pipeline**
```python
# rag_pipeline.py
# Load documents → chunk → embed → store in pgvector
# User query → hybrid search → rerank → LLM (Groq API)
# Output: Final answer with metrics
```

6. **Daily Log Template** (you fill this each day)
```yaml
# daily_log.yaml
Date: Apr 15
Team: Uday, Backend1, Backend2, Chowdappa
Status: ✅ / 🟡 / 🔴
Completed:
  - Embedding comparison done (chose bge-large)
Blockers:
  - None
Tomorrow:
  - Start chunking strategies
```

---

### **❌ WHAT I CANNOT DO (PHASE 2)**

- 🚨 **Run code on GPREC in real-time** — I can't execute, only generate code
- 🚨 **Test APIs with YOUR credentials** — You must run the test
- 🚨 **Handle "PostgreSQL crashed" at 3 AM** — You must wake up and fix it
- 🚨 **Make a decision: Is this result good or bad?** — You + Uday decide
- 🚨 **Manage student conflicts** — Only you can manage team dynamics
- 🚨 **Approve "we're ready for next phase"** — Your call

---

### **🔴 PROBLEMS LIKELY TO HIT IN WEEK 1**

**Problem 1: Embedding latency too high**
- Cause: all-MiniLM model on CPU takes 10 sec per 100 clauses
- **I fix**: Offer Groq/HuggingFace API embedding as fallback
- **You do**: Decide: CPU vs API? (API is slower but removes load)

**Problem 2: PostgreSQL becomes slow after 1000 vectors**
- Cause: No index yet, or HNSW index not optimized
- **I fix**: Create optimized index script
- **You do**: Run it, test speed improvement

**Problem 3: Chunking creates 10,000 chunks (too many)**
- Cause: Fixed-size chunking too granular
- **I fix**: Switch to recursive or semantic chunking, show code
- **You do**: Run new chunking, time how long it takes

**Problem 4: Uday says "My embeddings are garbage"**
- Cause: Wrong embedding model or bad chunking
- **I fix**: Generate isolation test (test each model separately)
- **You do**: Run tests, interpret results, decide which model to keep

**Problem 5: Reranking takes 5 seconds (too slow)**
- Cause: Cross-encoder running on CPU
- **I fix**: Offer batched reranking or reduce top-K
- **You do**: Choose trade-off (speed vs accuracy)

---

### **✅ FILLABLE DOCUMENTS BY END OF WEEK 1**

By Friday Apr 19, I'll help you fill:
- ✅ `MYdeliverables.txt` → D1, D2, D3 (architecture, embedding, chunking)
- ✅ `MYdeliverables.txt` → D4 (breaking experiments FE-01 to FE-05)
- ✅ `failure_log.md` (all blocker + fix history)
- ✅ `metrics_table.csv` (latency, precision, accuracy for each strategy)

---

## 🚀 PHASE 3: WEEK 2 BOOTCAMP (April 22-26)

### **WHAT HAPPENS EACH DAY**

**Day 6-7 (Mon 22 - Tue 23): Multi-hop Retrieval + LangGraph**
- Uday: Build query router, multi-hop logic
- Backend: Integrate with agentic framework
- You: Test 3 complex queries (need 2+ hops to answer)

**Day 8 (Wed 24): RAGAS Evaluation**
- Uday: Run RAGAS on 50+ queries
- Backend: Collect metrics (Precision, Recall, F1, BLEU, etc.)
- You: Validate: Does metric match reality?

**Day 9-10 (Thu 25 - Fri 26): Demo Prep + Submission**
- All: Polish demo, write slides, prepare presentation
- You: Fill final [TO FILL] sections, compile deliverables
- Submit: Presentation to Vaibhav + Madhu Sir

---

### **WHAT I CAN HELP WITH (PHASE 3)**

**✅ I'LL CREATE:**

1. **LangGraph Query Router** (ready-to-use)
```python
# query_router.py
# Classify query: Factoid vs Quantitative vs Reasoning
# Route to: Vector search vs SQL vs Multi-hop
# Output: Decision trace for each query
```

2. **Multi-hop Orchestrator** (ready-to-use)
```python
# multi_hop_retrieval.py
# Step 1: Find all FCCs related to "time-bar"
# Step 2: Find all NCRs linked to those FCCs
# Step 3: Synthesize: Are any NCRs blocking time-bar compliance?
# Output: Hierarchical result with decision path
```

3. **RAGAS Evaluation Pipeline** (ready-to-use)
```python
# ragas_evaluation.py
# Load 50+ golden queries
# Run each through RAG pipeline
# Calculate: Faithfulness, AnswerRelevancy, ContextPrecision, etc.
# Output: Metrics table + visualization
```

4. **Live Demo Script** (ready-to-present)
```python
# live_demo.py
# Query 1: "Time-bar clauses for XX contract"
# Query 2: "NCRs blocking critical path activities"
# Query 3: "Comparison of payment terms across 3 contracts"
# Shows: Speed, accuracy, confidence, limitations
```

5. **Presentation Deck** (Google Slides / PowerPoint template)
- Slide 1: Problem statement + business value
- Slide 2: Architecture diagram
- Slide 3: Embedding model comparison results
- Slide 4: Retrieval strategy comparison
- Slide 5: Failure analysis + lessons learned
- Slide 6: Live demo
- Slide 7: Metrics + recommendation
- Slide 8: Next steps for production

6. **Filled Deliverables Document**
```
I'll auto-fill:
- D6: LangGraph agentic RAG architecture
- D7: RAGAS evaluation results
- D8: Risk summary + recommendations  
- D9: Architecture decision log
```

---

### **❌ WHAT I CANNOT DO (PHASE 3)**

- 🚨 **Actually present the demo to Vaibhav** — You present, I just helped create script
- 🚨 **Handle live Q&A** — You must answer Vaibhav's questions
- 🚨 **Judge if metrics are "good enough"** — You + Vaibhav decide
- 🚨 **Make final architecture recommendation** — You own this decision
- 🚨 **File final presentation** — You submit

---

### **🔴 PROBLEMS LIKELY TO HIT IN WEEK 2**

**Problem 1: RAGAS evaluation takes too long**
- Cause: 50 queries × 30 seconds each = 25 minutes
- **I fix**: Parallel evaluation script, sample-based evaluation
- **You do**: Decide: Full or sampled? (Trade-off?)

**Problem 2: Multi-hop query fails halfway**
- Cause: Step 1 returns nothing, Step 2 can't proceed
- **I fix**: Add fallback: If Step 1 empty, switch to Step 2 only
- **You do**: Test fallback, decide if acceptable

**Problem 3: Demo latency is 8 seconds (too slow)**
- Cause: Multiple hops + reranking + LLM generation bottleneck
- **I fix**: Optimize query caching, batch calls
- **You do**: Test optimized version, accept or retry

**Problem 4: LLM hallucinating answers**
- Cause: RAG retrieving irrelevant chunks
- **I fix**: Adjust confidence threshold, add guardrails
- **You do**: Test, validate outputs look correct

**Problem 5: Time running out on Friday**
- Cause: Demo not ready, slides incomplete
- **I fix**: Automated all slides + demo script by Wed
- **You do**: 1-hour rehearsal on Thu, final polish on Fri morning

---

## 💡 HONEST ASSESSMENT: WHAT I CAN vs CANNOT DO

### **WHAT I CAN EASILY COMPLETE (80%)**

| Task | Difficulty | I Can Do |
|------|------------|----------|
| Write RAG pipeline code | Easy | ✅ 100% |
| Create embeddings script | Easy | ✅ 100% |
| Generate chunking strategies | Easy | ✅ 100% |
| Write hybrid search SQL | Easy | ✅ 100% |
| Build RAGAS evaluation | Easy | ✅ 100% |
| Create demo script | Easy | ✅ 100% |
| Generate documentation | Easy | ✅ 100% |
| Fill [TO FILL] templates | Easy | ✅ 100% |
| Create test cases | Easy | ✅ 100% |
| Write infrastructure scripts | Easy | ✅ 90% (you execute) |
| Troubleshoot code errors | Medium | ✅ 90% (need error logs) |
| Design evaluation metrics | Medium | ✅ 100% |
| Create presentation slides | Medium | ✅ 100% |
| Generate daily log templates | Easy | ✅ 100% |

---

### **WHAT I CANNOT DO (20% — YOU MUST OWN)**

| Task | Difficulty | Why I Can't | You Must |
|------|------------|------------|---------|
| Install PostgreSQL on HPC | Hard | No SSH access | Execute + troubleshoot |
| Configure pgvector extension | Hard | Need real hardware | Execute + handle errors |
| Test APIs with credentials | Medium | No credentials | Run test + handle failures |
| Run code on GPREC | Hard | No access | Execute daily |
| Handle hardware crashes | Hard | Can't reboot server | Escalate to IT |
| Approve deliverables | Hard | Need human judgment | Final sign-off |
| Manage team (students, Uday) | Hard | Not qualified | Lead meetings, resolve conflicts |
| Make real-time decisions | Hard | Context-dependent | Decide: continue or pivot? |
| Present to stakeholders | Hard | Not authorized | Deliver the demo |
| Answer "Is this good enough?" | Hard | Subjective | You + Vaibhav decide |

---

## 📊 OVERALL SUMMARY

### **WEEK-BY-WEEK EFFORT SPLIT**

```
PHASE 1 (Apr 12-13): Infrastructure Setup
  Effort: 80% Backend students + Lab admin, 20% I help with scripts
  Risk: CRITICAL — If this fails, bootcamp can't start
  Duration: 2 days (48 hours)
  
PHASE 2 (Apr 15-19): Week 1 Bootcamp (Build & Break)
  Effort: 50% Uday (code), 30% Backend (data/APIs), 20% You (coordination)
  I provide: Ready-to-run code templates
  Risk: HIGH — Embedding/chunking decisions critical today
  Duration: 5 days, ~40 hours of real work per person
  
PHASE 3 (Apr 22-26): Week 2 Bootcamp (Polish & Demo)
  Effort: 40% Uday (evaluation), 20% Backend (integration), 40% You (demo prep)
  I provide: RAGAS scripts, demo slides, presentation
  Risk: MEDIUM — Time pressure on presentation
  Duration: 5 days, ~30 hours of real work
```

---

### **WHAT IF YOU ASSIGN ME TO "COMPLETE THIS TASK"?**

**❌ I CANNOT COMPLETE 100% ALONE BECAUSE:**

1. **No hardware access** — I can't SSH into GPREC HPC, install software, or test on real data
2. **No credentials** — I can't use your API keys, GitHub account, or run actual LLMs
3. **No real-time feedback** — I can't see if PostgreSQL crashed or if experiments failed
4. **No authority** — I can't make final business decisions (is this architecture good?) or present to stakeholders
5. **No team management** — I can't lead the students or resolve conflicts

---

### **WHAT I CAN DO IF YOU GIVE ME THIS TASK:**

**✅ BEFORE BOOTCAMP STARTS (April 4-14):**
- Generate all infrastructure scripts (bash, Python, SQL)
- Create all code templates (embeddings, chunking, retrieval, evaluation)
- Fill all deliverables document templates with [EXAMPLE] sections
- Write daily standup templates
- Create presentation deck (90% complete)
- Generate troubleshooting guide for common problems
- Create risk mitigation scripts

**✅ DURING BOOTCAMP (April 15-26):**
- Receive error logs from you, troubleshoot code issues
- Generate optimized code fixes in real-time
- Update templates with your actual results
- Fill presentation with your real metrics/screenshots
- Generate evaluation reports
- Create final deliverables document with your data

**❌ CANNOT DURING BOOTCAMP:**
- Run experiments myself
- Manage team meetings
- Make decisions (you must decide)
- Present to stakeholders

---

## 🎯 RECOMMENDED WORKFLOW

**I recommend you do THIS:**

### **TASK ASSIGNMENT MODEL (SUGGESTED)**

**April 4-14 (Before Bootcamp):**
- **Me (AI)**: Generate ALL code, scripts, templates, presentations (I work 24/7, deliver by Apr 13)
- **You (Chowdappa)**: Visit HPC lab, confirm resources, coordinate team prep
- **Backend Students**: Create API accounts, download datasets
- **Uday**: Review all scripts, ask me questions

**April 12-13 (Day 0):**
- **Backend Students**: Execute infrastructure scripts I created
- **You**: Supervise, troubleshoot, escalate issues
- **Me (AI)**: Provide debugging support via error logs you send

**April 15-26 (Bootcamp):**
- **Uday**: Run code templates I provided, decide on model choices
- **Backend**: Monitor APIs, manage data pipeline
- **You**: Daily coordination, log findings, flag blockers
- **Me (AI)**: Fix code issues you report, update deliverables with your results

**April 26 (Submission):**
- **You**: Final review, present demo
- **Me (AI)**: Auto-fill remaining [TO FILL] sections with your data
- **Vaibhav**: Approve architecture recommendations

---

## 🚨 CRITICAL BLOCKERS (Where You MUST Intervene)

**These problems need YOUR decision in real-time:**

1. **PostgreSQL can't start** → You contact HPC admin
2. **Embedding model is too slow** → You decide: CPU vs Cloud API?
3. **Chunking strategy A vs B conflict** → You + Uday decide together
4. **Demo latency is 10 sec (requirement is 5 sec)** → You decide: Optimize more or accept limitation?
5. **Uday says "this architecture won't scale"** → You escalate to Vaibhav
6. **Student issues (sick, can't attend)** → You replace or reschedule
7. **RAGAS metrics show low performance** → You decide: Tweak parameters or report as-is?

---

## 📋 HOW TO WORK WITH ME (OPTIMAL WORKFLOW)

**SEND ME:**
```
1. Error logs (full stack trace)
2. Current metrics (what's working, what's not)
3. Questions (specific, not "how do I do RAG?")
4. Constraints (time, hardware limits)
5. Your decision on previous blocker
```

**I'LL SEND YOU:**
```
1. Fixed code (copy-paste ready)
2. Updated metrics/templates
3. Clear explanations (avoid jargon)
4. Multiple options (pros/cons of each)
5. Risk warnings (if decision might fail)
```

**DO NOT SEND ME:**
```
❌ "Don't worry, just fix everything"
❌ Vague errors ("it doesn't work")
❌ Decisions for humans to make ("which is better?")
❌ Requests I can't do ("run the script yourself")
```

---

## ✅ FINAL ANSWER: CAN I COMPLETE THIS?

**For Apr 12-26 Workflow:**

| Component | Can I Complete? | Timeline | Notes |
|-----------|-----------------|----------|-------|
| All code | ✅ YES | By Apr 13 | Ready-to-use, copy-paste |
| All templates | ✅ YES | By Apr 13 | Fill-in-the-blank format |
| All scripts | ✅ YES | By Apr 13 | Infrastructure, evaluation, demo |
| All docs | ✅ YES | By Apr 13 | [TO FILL] sections created |
| All slides | ✅ YES | By Apr 13 | 8 slides with placeholder data |
| Infrastructure setup | 🟡 PARTIAL | Apr 13 | I write scripts, you run them |
| Bootcamp execution | 🟡 PARTIAL | Apr 15-26 | I generate code, you + team runs it |
| Final presentation | 🟡 PARTIAL | Apr 26 | I write slides, you present |
| **FULL WORKFLOW** | ❌ NO | Apr 12-26 | You must own execution + decisions |

**Simple answer: I can be your 80% solution. You own the 20%.** ✨

---

## 🎓 WHAT I'LL DELIVER TO YOU RIGHT NOW

**If you say "YES, start!"**, I can create:

1. ✅ **Day 0 Infrastructure Setup Script** (bash + Python)
2. ✅ **Day 1-5 Code Templates** (embeddings, chunking, RAG, etc.)
3. ✅ **Day 6-8 Evaluation & Agentic RAG Code**
4. ✅ **Daily Standup Templates** (copy-paste each morning)
5. ✅ **MYdeliverables.txt Auto-Fill Templates** (80% pre-filled)
6. ✅ **Presentation Deck** (7 slides, ready for your data)
7. ✅ **Troubleshooting Guide** (common problems + solutions)
8. ✅ **Risk Mitigation Scripts** (contingency plans)
9. ✅ **Evaluation Metrics Dashboard** (auto-update with data)
10. ✅ **Final Submission Checklist** (make sure nothing missed)

**Total: ~2000 lines of production-ready code + 50 pages of documentation.**

---

**WANT ME TO START? SAY "YES" and I'll deliver everything by Apr 13.**

OR

**Want specific parts first? Tell me which and I'll start today.**
