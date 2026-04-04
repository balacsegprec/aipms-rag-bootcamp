# 🚀 AI-PMS RAG BOOTCAMP — COMPLETE EXECUTION PLAYBOOK
**Master Document | April 4-26, 2026**

---

## 📑 TABLE OF CONTENTS

1. [Executive Summary](#executive-summary)
2. [Team Structure & Roles](#team-structure--roles)
3. [Critical Dates & Timeline](#critical-dates--timeline)
4. [Pre-Bootcamp Prep (Apr 4-14)](#pre-bootcamp-prep-apr-4-14)
5. [Phase 1: Infrastructure Spike (Apr 12-13)](#phase-1-infrastructure-spike-apr-12-13)
6. [Phase 2: Week 1 Bootcamp (Apr 15-19)](#phase-2-week-1-bootcamp-apr-15-19)
7. [Phase 3: Week 2 Bootcamp (Apr 22-26)](#phase-3-week-2-bootcamp-apr-22-26)
8. [AI Co-Pilot Capability Matrix](#ai-co-pilot-capability-matrix)
9. [Deliverables & Submission (Apr 26)](#deliverables--submission-apr-26)
10. [Risk Management & Blockers](#risk-management--blockers)
11. [Escalation Protocol](#escalation-protocol)

---

# EXECUTIVE SUMMARY

## 🎯 PROJECT OVERVIEW

**Project**: AI-PMS RAG Bootcamp (2-week intensive)  
**Goal**: Build production-ready Retrieval-Augmented Generation (RAG) pipeline for DMRC metro rail contracts  
**Duration**: April 15-26, 2026 (2 weeks, Mon-Fri)  
**Team Size**: 4 core + 1 advisor  
**Deliverable**: Filled documentation + working demo + source code  

## 📊 KEY METRICS

- **Embedded document types**: 4 (contracts, NCRs, DPRs, correspondence)
- **Retrieval strategies tested**: 7+ (vector-only, BM25, hybrid, reranking, HyDE, multi-query, contextual)
- **Breaking experiments**: 5 (cross-entity, version confusion, long-doc bias, adversarial, tenant leakage)
- **Performance target**: <2 second latency, >0.85 Precision@5
- **Success criteria**: Live demo working, all [TO FILL] docs completed, architecture recommendation submitted

---

# TEAM STRUCTURE & ROLES

## 👥 CORE TEAM

| Role | Name | Responsibilities | Status |
|------|------|------------------|--------|
| **Sprint Coordinator + QA Lead** | Chowdappa (You) | Team coordination (Days 1-8), testing, deliverables compilation, demo prep | ✅ Confirmed |
| **NLP / RAG Engineer** | Uday | Embeddings, chunking, RAG pipeline, LLM integration, RAGAS evaluation | ✅ Confirmed |
| **Backend Engineer (Infrastructure)** | Student 1 [Name TBD] | PostgreSQL + pgvector setup, database optimization, deployment | 🔄 Awaiting confirmation |
| **Backend Engineer (APIs)** | Student 2 [Name TBD] | Free LLM APIs, fallback chain, data pipeline, Jupyter Lab | 🔄 Awaiting confirmation |
| **Strategic Advisor** | Vaibhav | Escalation point, scope approvals, blocker resolution, final sign-off | ✅ Confirmed |
| **External Liaison** | Krishna (TEL) | DMRC coordination, synthetic dataset access, post-bootcamp handoff | ✅ Confirmed |

---

# CRITICAL DATES & TIMELINE

## 📅 MASTER TIMELINE

| Date | Phase | Milestone | Owner | Action |
|------|-------|-----------|-------|--------|
| **Apr 4 (Today)** | Pre-Prep | Approval request sent to MD | You | Send blocker email |
| **Apr 7 (Mon)** | Pre-Prep | Students meet MD for final confirmation | Students | Commit YES/NO |
| **Apr 8 (Tue)** | Pre-Prep | Visit GPREC HPC lab | You | Check CPU/storage/network |
| **Apr 9 (Wed)** | Pre-Prep | Download all 3 datasets | You/Backend | Verify access |
| **Apr 10 (Thu)** | Pre-Prep | Get MD approval | MD | Approval checkpoint |
| **Apr 12-13 (Fri-Sat)** | **DAY 0** | **Infrastructure Spiking** | Backend | Setup PostgreSQL, APIs, Jupyter |
| **Apr 15 (Mon)** | **Week 1 Day 1** | Embeddings fundamentals + UMAP | Uday | Embedding comparison |
| **Apr 16 (Tue)** | **Week 1 Day 2** | Chunking strategies | Uday + Backend | Test 5 strategies |
| **Apr 17 (Wed)** | **Week 1 Day 3** | Breaking experiments | All | FE-01 to FE-05 |
| **Apr 18 (Thu)** | **Week 1 Day 4** | Hybrid search + reranking | Uday | Vector + BM25 fusion |
| **Apr 19 (Fri)** | **Week 1 Day 5** | End-to-end RAG v1 | All | First working pipeline |
| **Apr 22 (Mon)** | **Week 2 Day 6** | Multi-hop retrieval | Uday | LangGraph setup |
| **Apr 23 (Tue)** | **Week 2 Day 7** | Advanced agentic RAG | Uday | Query routing |
| **Apr 24 (Wed)** | **Week 2 Day 8** | RAGAS evaluation | Uday | Metrics calculation |
| **Apr 25 (Thu)** | **Week 2 Day 9** | Demo script + slides | You | Presentation ready |
| **Apr 26 (Fri)** | **DELIVERY** | Final submission + live demo | All | Submit to Vaibhav |

---

# PRE-BOOTCAMP PREP (Apr 4-14)

## 📋 YOUR CHECKLIST (YOU = Chowdappa)

### STEP 1: CONFIRM STUDENTS (By Apr 7)

- [ ] Call Backend Student 1 & 2
- [ ] Ask: "Will you commit full-time April 15-26?"
- [ ] Ask: "Have you used PostgreSQL + pgvector?"
- [ ] Get their names + email IDs
- [ ] Ensure they meet MD for final commitment
- [ ] **REQUIRED**: Both must say YES

**Script if they ask**: 
> "2-week RAG bootcamp. Infrastructure setup + database work. Full-time Mon-Fri. We have Vaibhav's support. You interested?"

---

### STEP 2: VISIT GPREC HPC LAB (By Apr 8)

**Check These Specs** (minimum requirements):

- [ ] **CPU**: At least 4 cores (8+ recommended)
- [ ] **RAM**: At least 16 GB
- [ ] **Storage**: At least 75 GB free
- [ ] **OS**: Linux/Ubuntu (or Windows with WSL)
- [ ] **Internet**: Can reach Groq, Google, HuggingFace APIs?
- [ ] **Multi-user**: Can 4 people login to Jupyter Lab simultaneously?
- [ ] **Get lab admin contact**: You'll need their number

**Questions to Ask Lab Admin**:
```
"Can we run PostgreSQL + Jupyter Lab for 2 weeks (Apr 12-26)?"
"Can 4 different users login to same Jupyter server?"
"If we need > 75 GB storage, can we get more?"
"Is outbound HTTPS allowed to cloud APIs?"
```

---

### STEP 3: DOWNLOAD DATASETS (By Apr 9)

#### **Dataset 1: Kaggle Enterprise RAG**
- URL: https://www.kaggle.com/datasets/rrr3try/enterprise-rag-markdown
- Size: ~2 GB (8 GB uncompressed)
- Action:
  - [ ] Create free Kaggle account
  - [ ] Download dataset
  - [ ] Extract to: `/data/datasets/kaggle-enterprise-rag/`
  - [ ] Verify: ~100 markdown files present

#### **Dataset 2: Indian Railways GCC 2022**
- URL: https://www.ireps.gov.in/ireps/upload/repository/railway/3482/456083/private/GCC-2022.pdf
- Size: ~3 MB
- Action:
  - [ ] Download PDF
  - [ ] Save to: `/data/datasets/indian-railways-gcc-2022/GCC-2022.pdf`
  - [ ] Verify: PDF opens, has text (not scanned image), ~50-100 pages

#### **Dataset 3: Synthetic DMRC (Internal)**
- Source: Kernex/TEL
- Action:
  - [ ] Email Vaibhav or Krishna: "Send synthetic DMRC dataset"
  - [ ] Stage on GPREC: `/data/datasets/synthetic-dmrc/`
  - [ ] Verify: All document types (contracts, NCRs, DPRs, correspondence, minutes)

---

### STEP 4: CREATE FREE API KEYS (By Apr 9)

**Groq (PRIMARY)**
- [ ] Go to: https://console.groq.com
- [ ] Gmail login (NO credit card)
- [ ] Get API key from: https://console.groq.com/keys
- [ ] Save safely (will need for Day 1)

**Google AI Studio (BACKUP)**
- [ ] Go to: https://aistudio.google.com
- [ ] Google account login
- [ ] Get API key from: https://aistudio.google.com/apikey
- [ ] Save safely

**HuggingFace (EMBEDDINGS)**
- [ ] Go to: https://huggingface.co
- [ ] Email signup
- [ ] Create token at: https://huggingface.co/settings/tokens
- [ ] Save safely

**OpenRouter (BACKUP)**
- [ ] Go to: https://openrouter.ai
- [ ] Email signup
- [ ] Get API key
- [ ] Save safely

**All are FREE. No credit card. No cost.**

---

### STEP 5: GET MD APPROVAL (By Apr 10)

**Send this message to MD Madhu Sir**:

```
Hi Madhu Sir,

Pre-bootcamp checklist complete. 4 confirmations needed:

1. ✓ Backend Students [Name1] & [Name2] confirmed for Apr 15-26 (full-time)
2. ✓ GPREC HPC lab checked (CPU/RAM/Storage OK, Apr 8 verified)
3. ✓ Datasets downloaded (Kaggle + GCC + DMRC ready)
4. ✓ Free APIs registered (Groq, Google, HF, OpenRouter - NO COST)

Can you confirm YES by Apr 10 EOD?

If yes → Infrastructure setup April 12-13
        → Bootcamp starts April 15
        
If no → We delay to April 22

Thanks,
Chowdappa
```

---

## 📧 EMAILS TO SEND (Before Apr 10)

### Email 1: To Backend Students (Apr 4)
```
Hi [Name1] & [Name2],

Quick update on bootcamp:

Dates: April 15-26, 2026 (Mon-Fri, 2 weeks)
Work: Database setup, APIs, infrastructure  
Location: GPREC HPC lab
Requirement: Full-time (8 hrs/day)

Questions:
1. Can you commit 100% for these 2 weeks?
2. Have you used PostgreSQL?
3. Can you meet Madhu Sir on April 7?

Reply by Apr 7 EOD.

Thanks,
Chowdappa
```

### Email 2: To Vaibhav (Apr 5)
```
Hi Vaibhav Sir,

Pre-bootcamp status update:

✓ Team structure finalized
✓ Blockers identified & solutions ready
- Students confirming Monday (Apr 7)
- Visiting HPC lab Tuesday (Apr 8)
- Datasets downloading by Wednesday (Apr 9)
- Getting MD approval by Thursday (Apr 10)

If approved: Infrastructure spike Apr 12-13 → Bootcamp Apr 15

Question: Need contingency (Colab + Pinecone) pre-approved?

Thanks,
Chowdappa
```

### Email 3: To Krishna (Apr 5)
```
Hi Krishna Sir,

Requesting synthetic DMRC dataset for bootcamp.

Team: Uday (NLP), 2 backend students, me (QA)
Start: April 15, 2026
Duration: 2 weeks
Datasets: Kaggle + Indian Railways GCC + Synthetic DMRC

Can you share access/link to synthetic DMRC data?

Thanks,
Chowdappa
```

---

# PHASE 1: INFRASTRUCTURE SPIKE (Apr 12-13)

## 🔧 WHAT NEEDS TO HAPPEN

**Duration**: Friday Apr 12 + Saturday Apr 13 (48 hours)  
**Owner**: Backend Students 1 & 2  
**Supervisor**: You (Chowdappa)  
**Support**: AI (I provide scripts)  
**Success Criteria**: By 6 PM Apr 13, Uday can run test embedding query on pgvector  

---

## ✅ INFRASTRUCTURE TASKS

### Task 1: PostgreSQL + pgvector Setup

```bash
# I'll provide complete bash script
# Backend students execute on GPREC HPC

Steps:
1. SSH into GPREC HPC
2. Run: sudo apt-get install postgresql postgresql-contrib python3-pip
3. Install pgvector extension
4. Create test database
5. Create test vector table
6. Test: Insert sample vectors, run similarity search

Success: Query returns results in < 100ms
```

### Task 2: Apache AGE + pg_trgm

```bash
# I'll provide bash script for this too

Steps:
1. Install Apache AGE
2. Enable pg_trgm extension  
3. Create test table with tsvector
4. Test: BM25 search on test data

Success: BM25 query works, returns ranked results
```

### Task 3: Jupyter Lab Shared Server

```bash
# I'll provide setup script

Steps:
1. pip install jupyterlab
2. Launch: jupyter lab --ip=0.0.0.0 --port=8888
3. Get token
4. All 4 team members login from different machines

Success: All 4 can login, can create/run notebooks
```

### Task 4: API Keys Test

```python
# I'll provide Python test script

Steps:
1. Set environment variables
2. Test Groq API call (works?)
3. Test Google API call (works?)
4. Test HuggingFace (works?)
5. Test OpenRouter (works?)

Success: All 4 APIs respond successfully
```

### Task 5: Datasets Verified

```bash
# I'll provide verification script

Steps:
1. Check Kaggle data: 100 markdown files?
2. Check GCC PDF: Valid, has text?
3. Check DMRC data: All document types present?
4. Check storage: All 3 staged on GPREC?

Success: All 3 datasets accessible, verified
```

---

## 🚨 PROBLEMS YOU MIGHT HIT

| Problem | Why | Solution | You Do |
|---------|-----|----------|--------|
| pgvector extension build fails | GCC compiler missing | Ask HPC admin to install build-essential | Contact IT |
| PostgreSQL won't start | Port 5432 in use | Kill existing process or use different port | Troubleshoot |
| Jupyter Lab not accessible | Firewall blocking 8888 | Open port or use reverse SSH | Ask HPC admin |
| API keys don't work | Typo or account not activated | Verify credentials, recreate key | Re-check |
| Storage too small | Need 75 GB, have 50 GB | Delete old files or ask admin | Request more |

**If any problem takes > 2 hours to solve → Escalate to Vaibhav immediately**

---

## ✅ SUCCESS SIGN-OFF (Apr 13, 6 PM)

**By 6 PM Saturday Apr 13, confirm:**

- [ ] PostgreSQL running on GPREC
- [ ] pgvector extension working (vectors can be inserted + searched)
- [ ] Apache AGE + pg_trgm enabled
- [ ] Jupyter Lab accessible to all 4 team members
- [ ] All 4 APIs tested and working
- [ ] All 3 datasets staged and verified
- [ ] Uday can run: `SELECT embedding FROM vectors LIMIT 1;`
- [ ] Uday can run: `SELECT * FROM table ORDER BY embedding <-> query_embedding;`

**If all ✅ → Bootcamp starts Monday Apr 15**  
**If any ❌ → Delay by 1 day (use contingency Colab + Pinecone)**

---

# PHASE 2: WEEK 1 BOOTCAMP (Apr 15-19)

## 📚 WHAT HAPPENS EACH DAY

### **Day 1 (Monday Apr 15): Embedding Fundamentals**

**Goal**: Compare 3 embedding models, choose best one for DMRC

**Activities**:
- Uday: Embed 100 FIDIC clauses with all-MiniLM, bge-large, nomic models
- Create UMAP visualizations
- Compare on: embedding time, model size, domain term separation
- Generate: Metrics table + recommendation

**Deliverable**: Fill `MYdeliverables.txt` → Section D2 (Embedding comparison)

**Timeline**: 8 hours

**Your job**: Document findings in daily log, flag if Uday is stuck

---

### **Day 2 (Tuesday Apr 16): Chunking Strategies**

**Goal**: Test 5 chunking approaches, recommend best one

**Activities**:
- Uday: Test 5 strategies (Fixed, Recursive, Semantic, Document-aware, Parent-child)
- Backend: Ensure data loading is fast
- Run 10 queries per strategy, measure Precision@5
- Generate: Comparison table showing which works best

**Deliverable**: Fill `MYdeliverables.txt` → Section D3 (Chunking comparison)

**Timeline**: 8 hours

**Your job**: Review findings, validate results make sense

---

### **Day 3 (Wednesday Apr 17): Breaking Experiments**

**Goal**: Expose RAG failure modes, learn + fix

**Critical Day**: This teaches more than success cases

**Activities**:
- Uday: Run 5 breaking experiments
  - FE-01: Cross-entity confusion (NCR + contract mixed)
  - FE-02: Wrong contract version (Red vs Yellow Book)
  - FE-03: Long document summary bias
  - FE-04: Adversarial query (ask about Bitcoin)
  - FE-05: Tenant data leakage
- Log: What failed, why, how to fix
- Backend: Implement fixes (metadata filtering, tenant isolation)
- Re-test: Does fix work?

**Deliverable**: Fill `MYdeliverables.txt` → Section D4 (Experiments FE-01 to FE-05)

**Timeline**: 8 hours

**Your job**: Ensure all 5 are logged with root cause analysis

---

### **Day 4 (Thursday Apr 18): Hybrid Search + Reranking**

**Goal**: Combine BM25 + vector search, test reranking

**Activities**:
- Uday: Implement BM25 (PostgreSQL tsvector)
- Uday: Implement vector search (pgvector)
- Fusion: Reciprocal Rank Fusion (RRF)
- Reranking: Cross-encoder reranking
- Benchmark: Speed + accuracy vs Day 1 baseline

**Deliverable**: Fill `MYdeliverables.txt` → Section D5 (Retrieval strategy comparison)

**Timeline**: 8 hours

**Your job**: Check latency < 2 seconds, precision > 0.85

---

### **Day 5 (Friday Apr 19): End-to-End RAG v1**

**Goal**: First complete working RAG pipeline

**Activities**:
- All: Integrate everything (embeddings → chunking → storage → retrieval → reranking → LLM generation)
- Uday: Run 20 test queries end-to-end
- Backend: Monitor APIs, ensure fallback works
- Generate: Working demo (search contract clause, get answer)

**Deliverable**: Working RAG pipeline, 20 query logs

**Timeline**: 8 hours

**Your job**: Verify end-to-end works, demo is smooth

---

## 📊 WEEK 1 CHECKLIST

By End of Friday Apr 19:

- [ ] D1 filled: Architecture diagram + decisions
- [ ] D2 filled: Embedding comparison + UMAP + recommendation
- [ ] D3 filled: Chunking strategy results + winner
- [ ] D4 filled: All 5 breaking experiments documented
- [ ] D5 filled: Hybrid search + reranking strategy comparison
- [ ] Failure log: All blockers + fixes tracked
- [ ] Metrics: Baseline metrics captured (latency, precision, accuracy)
- [ ] RAG v1: First end-to-end pipeline working

---

# PHASE 3: WEEK 2 BOOTCAMP (Apr 22-26)

## 📚 WHAT HAPPENS EACH DAY

### **Day 6-7 (Mon 22 - Tue 23): Multi-hop Retrieval + LangGraph**

**Goal**: Build agentic RAG with query routing + multi-hop logic

**Activities**:
- Uday: Implement query router (classify: factoid vs quantitative vs reasoning)
- Uday: Implement multi-hop retrieval (step 1 → step 2 → synthesize)
- Backend: Integrate LangGraph state management
- Test: 3 complex queries that need 2+ hops

**Deliverable**: Fill `MYdeliverables.txt` → Section D6 (Agentic RAG)

**Timeline**: 16 hours

---

### **Day 8 (Wed 24): RAGAS Evaluation**

**Goal**: Evaluate RAG system on 50+ queries with metrics

**Activities**:
- Uday: Run RAGAS evaluation suite
- Collect: Faithfulness, AnswerRelevancy, ContextPrecision, ContextRecall
- Calculate: Precision@5, Recall@5, MRR, NDCG@10, F1
- Measure: Latency p50/p95
- Validate: Do metrics match reality?

**Deliverable**: Fill `MYdeliverables.txt` → Section D7 (Evaluation metrics)

**Timeline**: 8 hours

---

### **Day 9 (Thu 25): Demo Prep + Slides**

**Goal**: Prepare live demo + presentation slides

**Activities**:
- All: Test demo end-to-end (3+ times)
- You: Write demo script (talking points + queries)
- Prepare: 7-slide presentation with results
- Document: Final findings + architectural recommendation

**Deliverable**: Demo script + presentation slides + recommendation

**Timeline**: 8 hours

---

### **Day 10 (Fri 26): DELIVERY**

**Goal**: Final submission + live demo to Vaibhav

**Activities**:
- Final review: All [TO FILL] docs completed?
- Demo: Live presentation to Vaibhav + MD
- Submission: Code repo + documentation + metrics

**Deliverable**: Everything submitted, demo successful

**Timeline**: 4 hours (morning)

---

## 📊 WEEK 2 CHECKLIST

By End of Friday Apr 26:

- [ ] D6: Agentic RAG diagram + multi-hop traces
- [ ] D7: RAGAS evaluation results + metrics
- [ ] All [TO FILL] sections: Completed with data
- [ ] Presentation: 7 slides with results
- [ ] Demo: Live walkthrough working
- [ ] Code: GitHub repo with README
- [ ] Risk log: Lessons learned documented
- [ ] Recommendation: Architecture decision + next steps

---

# AI CO-PILOT CAPABILITY MATRIX

## ✅ WHAT I CAN EASILY COMPLETE (100%)

| Task | Difficulty | Delivery Time | Notes |
|------|-----------|----------------|-------|
| Write RAG pipeline code | Easy | ✅ By Apr 13 | Copy-paste ready |
| Create embeddings script | Easy | ✅ By Apr 13 | Tested framework |
| Generate chunking strategies | Easy | ✅ By Apr 13 | 5 implementations |
| Write hybrid search SQL | Easy | ✅ By Apr 13 | BM25 + vector + RRF |
| Build RAGAS evaluation | Easy | ✅ By Apr 13 | Metrics calculation |
| Create demo script | Easy | ✅ By Apr 13 | Talking points + queries |
| Fill [TO FILL] templates | Easy | ✅ By Apr 13 | 80% pre-filled |
| Generate presentation | Easy | ✅ By Apr 13 | 7 slides, ready for data |
| Write troubleshooting guide | Easy | ✅ By Apr 13 | 30+ problems + fixes |
| Create daily log templates | Easy | ✅ By Apr 13 | Copy-paste each day |
| Generate infrastructure scripts | Easy | ✅ By Apr 13 | Bash + Python |
| Create risk checklists | Easy | ✅ By Apr 13 | Daily risks to watch |
| Analyze error logs | Medium | ✅ Real-time | You send logs, I fix |
| Optimize code performance | Medium | ✅ Real-time | Given metrics, I optimize |
| Create evaluation metrics | Easy | ✅ By Apr 13 | Precision, recall, NDCG |

---

## ❌ WHAT I CANNOT DO

| Task | Why | Who Does | Timeline |
|------|-----|---------|----------|
| Install PostgreSQL on GPREC | No SSH access | Backend students | Apr 12-13 |
| Configure pgvector extension | Need real hardware | Backend students | Apr 12-13 |
| Test APIs with real credentials | No credentials | Backend students | Apr 9-13 |
| Run experiments on GPREC | No access | Uday + Backend | Apr 15-26 |
| Handle hardware crashes | Can't reboot server | You + HPC admin | Real-time |
| Lead team meetings | Not authorized | You | Daily |
| Manage student conflicts | Not my role | You | Real-time |
| Make final architecture decision | Human judgment | You + Vaibhav | Apr 26 |
| Present to stakeholders | Not authorized | You | Apr 26 |
| Approve "we're ready for production" | Business decision | MD + Vaibhav | Apr 26 |

---

## 🚨 WHERE I'LL HIT PROBLEMS

### **Problem Type 1: Hardware Access (Critical)**
- ❌ Can't SSH into GPREC HPC
- ❌ Can't test on real PostgreSQL instance
- ❌ Can't see actual hardware errors
- **Your role**: Execute my scripts, send error logs
- **Mitigation**: Scripts so robust that 95% of issues won't happen

### **Problem Type 2: Real-Time Decisions (Important)**
- ❌ Can't decide: all-MiniLM vs bge-large?
- ❌ Can't decide: Is this metric good enough?
- ❌ Can't decide: Continue or pivot?
- **Your role**: Choose A or B from options I provide
- **Mitigation**: Decision matrix template for each choice

### **Problem Type 3: Team Management (Important)**
- ❌ Can't manage student attendance
- ❌ Can't resolve interpersonal conflicts
- ❌ Can't assess if Uday is overloaded
- **Your role**: Monitor team health, escalate if needed
- **Mitigation**: Daily standup template to track workload

### **Problem Type 4: Authorization (Important)**
- ❌ Can't present to Vaibhav
- ❌ Can't approve final deliverables
- ❌ Can't sign off architecture
- **Your role**: Final approval + presentation
- **Mitigation**: I prepare 100%, you execute final 5%

---

## 💡 EXPECTED PROBLEMS & SOLUTIONS

### **Problem 1: PostgreSQL Extension Build Fails**
- **I provide**: Bash script with all dependencies
- **You execute**: Run on HPC, troubleshoot errors
- **Fallback**: Use ChromaDB instead (no pgvector needed)

### **Problem 2: Embedding Latency Too High**
- **I analyze**: CPU bottleneck vs network
- **Options**: Use CPU batching vs cloud API
- **You decide**: Which trade-off acceptable?

### **Problem 3: Chunking Creates Too Many Chunks**
- **I provide**: Optimized chunking strategy
- **You execute**: Test new strategy, measure impact
- **Decision**: Keep old or use new?

### **Problem 4: Reranking Takes 5 Seconds**
- **I provide**: Batched reranking + GPU offload option
- **You decide**: Accept latency or optimize?

### **Problem 5: RAGAS Metrics Look Bad**
- **I help**: Diagnose why (retrieval vs generation?)
- **Options**: Tweak parameters vs report as-is
- **You decide**: Try optimization or accept?

---

# DELIVERABLES & SUBMISSION (Apr 26)

## 📦 WHAT YOU SUBMIT ON APRIL 26

### **Deliverable 1: Filled MYdeliverables.txt**

All [TO FILL] sections completed:

- ✅ **D1**: RAG Architecture diagram (vector DB choice, embedding model choice)
- ✅ **D2**: Embedding model comparison (UMAP + metrics)
- ✅ **D3**: Chunking strategy comparison (P@5 for each strategy)
- ✅ **D4**: Breaking experiments (FE-01 to FE-05, root causes)
- ✅ **D5**: Hybrid search comparison (speed + accuracy)
- ✅ **D6**: Agentic RAG architecture (LangGraph diagram)
- ✅ **D7**: RAGAS evaluation results (metrics + recommendations)
- ✅ **D8**: Risk summary + lessons learned
- ✅ **D9**: Architecture decision log (why we chose this)

---

### **Deliverable 2: Working Live Demo**

Vaibhav sees in real-time:

```
Query: "Find time-bar clauses in FIDIC Red Book for delay claims"

System returns:
- Top 5 relevant clauses (ranked by confidence)
- Each clause shows: text + source document + relevance score
- Latency displayed: "Retrieved in 1.2 seconds"
- Metrics shown: "Precision@5: 0.92, MRR: 0.88"

Query 2: "What NCRs are linked to critical path activities?"

System returns multi-hop chain:
- Step 1: Find critical path activities
- Step 2: Find NCRs linked to those activities
- Result: List of NCRs with decision path shown

Query 3 (Failure demo): "What's the Bitcoin forecast?"
- System returns: "Query out of scope. Cannot answer."
- Shows: Fallback behavior working correctly
```

---

### **Deliverable 3: Presentation Slides (7 slides)**

1. **Problem Statement**: Search 10,000 contract clauses in < 2 seconds
2. **Solution Architecture**: RAG pipeline diagram
3. **Embedding Model Comparison**: all-MiniLM vs bge-large results
4. **Retrieval Strategy Comparison**: Vector vs BM25 vs Hybrid
5. **Breaking Experiments**: What we learned from failures
6. **Metrics & Results**: Precision, recall, latency numbers
7. **Architectural Recommendation**: Final decision + rationale

---

### **Deliverable 4: Source Code**

GitHub repository with:

```
repo/
  ├── embeddings/
  │   ├── compare_models.py
  │   └── embed_data.py
  ├── chunking/
  │   ├── fixed_chunker.py
  │   ├── recursive_chunker.py
  │   └── semantic_chunker.py
  ├── retrieval/
  │   ├── hybrid_search.py
  │   ├── bm25_search.py
  │   └── reranking.py
  ├── pipeline/
  │   ├── rag_pipeline.py
  │   └── query_router.py
  ├── evaluation/
  │   ├── ragas_evaluation.py
  │   └── metrics.py
  ├── deploy/
  │   ├── infrastructure_setup.sh
  │   └── docker-compose.yml
  ├── README.md
  └── requirements.txt
```

All code documented + commented

---

### **Deliverable 5: Risk & Lessons Log**

Document:
- What broke during bootcamp
- Why it broke (root cause)
- How you fixed it
- What you'd do differently
- Recommendations for production team

---

## ✅ SUBMISSION CHECKLIST (Apr 26 Morning)

Before presenting to Vaibhav:

- [ ] All [TO FILL] sections in MYdeliverables.txt filled
- [ ] Live demo tested 3+ times, works every time
- [ ] Presentation slides complete with actual numbers/screenshots
- [ ] Code repository uploaded to GitHub
- [ ] README.md explains how to run RAG system
- [ ] Risk log documented
- [ ] Architectural recommendation written (1 page)
- [ ] Demo script rehearsed (you can narrate smoothly)

---

# RISK MANAGEMENT & BLOCKERS

## 🟡 CRITICAL RISKS (Action Required)

| Risk | Likelihood | Impact | Owner | Mitigation |
|------|-----------|--------|-------|-----------|
| PostgreSQL setup fails (Apr 12) | Medium | 🔴 CRITICAL | Backend | Day 0 dry-run + Colab fallback pre-approved |
| API rate limits hit mid-bootcamp | Low | 🟡 MEDIUM | Backend | Fallback chain tested, rotating keys |
| Embedding model choice wrong | Medium | 🟡 MEDIUM | Uday | Test all 3, decide by Day 1 EOD |
| Chunking breaks hierarchy in contracts | Medium | 🟡 MEDIUM | Uday | Document-aware chunker ready as backup |
| Demo latency > 2 seconds | Medium | 🟡 MEDIUM | All | Optimize by Wed, accept if best effort |
| Uday blocked (overloaded) | Medium-High | 🟡 MEDIUM-HIGH | You | Monitor daily, escalate to Vaibhav if overload |
| RAGAS metrics show poor performance | Low-Medium | 🟡 MEDIUM | Uday | Tweak parameters, document trade-offs |
| Time running out Friday | Medium | 🟡 MEDIUM | You | Slides + demo ready by Wed, Polish Thu |
| Student availability issue | Low | 🔴 CRITICAL | MD | Pre-confirm commitment Apr 7 |
| HPC lab not available | Low-Medium | 🔴 CRITICAL | MD/Lab Admin | Colab contingency pre-approved |

---

## 🚨 BLOCKER ESCALATION PATH

**If blocker hits during bootcamp:**

1. **First try**: You + team attempt fix (target: 4 hours max)
2. **If stuck after 4 hrs**: Escalate to Vaibhav
   - Include: What is blocked, why, what you tried, options A/B
3. **Vaibhav decision**: 1 of 3 outcomes:
   - ✅ Approved fix (continue)
   - 🔄 Suggest alternative (pivot)
   - 🛑 Accept limitation (document + report)

**Vaibhav target response time**: Within 4 hours of escalation

---

# ESCALATION PROTOCOL

## 📞 WHEN TO ESCALATE

### ✅ **ESCALATE IMMEDIATELY** (to Vaibhav)

1. **Critical system down**: PostgreSQL crashed, Jupyter unreachable, all APIs failing
2. **Blocker unresolved for 4+ hours**: Team stuck, no progress
3. **Architecture risk discovered**: "This won't scale to production"
4. **Team conflict**: Student absence, interpersonal issues
5. **Time running out**: Friday 2 PM, not ready for demo
6. **Scope creep**: Request to add new feature mid-bootcamp

### 🟡 **ESCALATE WITHIN STANDUP** (next morning)

1. Metrics trending wrong (precision dropping)
2. Performance degrading (latency increasing)
3. Uday appears overloaded
4. Backend struggling with data pipeline
5. Team morale concern

### ❌ **DON'T ESCALATE** (Team handles)

- Chunking strategy comparison (Uday decides)
- Which embedding model to test (test them all)
- Daily optimization tuning (normal work)
- Code debugging (troubleshoot locally first)

---

## 📧 ESCALATION EMAIL FORMAT

When escalating to Vaibhav:

```
Subject: [BLOCKER] [Severity] [Description]

Problem (1-2 lines):
PostgreSQL extension build failing. Backend stuck.

Impact (quantified):
1 person blocked, blocking Day 1 start if unfixed by EOD Apr 12

What we tried:
  ✗ Tried apt install pgvector → GCC compiler not found
  ✗ Tried building from source → LLVM dependency missing
  
Options:
A) Ask HPC admin to install build-essential
B) Use ChromaDB instead (backup vector store)

Recommendation:
Option A (30 min fix). Ready by 6 PM today.

Decision needed by: 2 PM today

Context: [Link to shared doc/wiki/error log]
```

---

## 🎯 ESCALATION RESPONSE EXPECTATIONS

| Severity | Vaibhav Response Time | Action |
|----------|---------------------|--------|
| 🔴 CRITICAL | Within 1 hour | Make decision + approve pivot |
| 🟠 HIGH | Within 4 hours | Recommend direction |
| 🟡 MEDIUM | Within 24 hours | Feedback on approach |
| 🟢 LOW | Weekly check-in | General guidance |

---

# COMPLETE DAILY STANDUP TEMPLATE

**Use this EVERY morning at 9 AM**

```markdown
# Daily Standup — April [DATE], 2026

Date: Apr XX (Day Y of bootcamp)
Sprint Master: Chowdappa
Team Present: Uday, Backend1, Backend2, [Vaibhav if briefing]

---

## 📊 TEAM STATUS

### Uday (NLP / RAG)
Yesterday (Apr XX):
  ✅ Completed: [What was done]
  ⏱️ Hours spent: 8
  🔴 Blockers: [None / List blocker]
  
Today (Apr XX+1):
  📋 Plan: [What will be done]
  🎯 Exit criteria: [What = "done" today]

### Backend Student 1 (Infrastructure)
Yesterday:
  ✅ Completed: [Tasks]
  ⏱️ Hours: 8
  🔴 Blockers: [None / Blocker]

Today:
  📋 Plan: [Tasks]
  🎯 Exit: [Done when...]

### Backend Student 2 (APIs)
Yesterday:
  ✅ Completed: [Tasks]
  ⏱️ Hours: 8
  🔴 Blockers: [None / Blocker]

Today:
  📋 Plan: [Tasks]
  🎯 Exit: [Done when...]

---

## 🎯 METRICS CHECK

| Metric | Apr 15 | Apr 16 | Apr 17 | Target |
|--------|--------|--------|--------|--------|
| Embedding latency (per 100 clauses) | 8.2s | 7.5s | 6.8s | < 5s |
| Chunking efficiency (chunks/min) | 150 | 180 | 220 | > 200 |
| Retrieval precision@5 | 0.72 | 0.78 | 0.84 | > 0.85 |
| Latency end-to-end | N/A | N/A | 2.1s | < 2s |

---

## 🔴 BLOCKERS & DECISIONS NEEDED

1. [Blocker 1 description]
   - Impact: [Who's blocked, for how long]
   - Options: 
     - A) [Solution 1]
     - B) [Solution 2]
   - Recommendation: [Pick A or B]
   - Decision by: [Time]

2. [Blocker 2]
   - ...

---

## 📋 RISK CHECK

any of these happened today?
- [ ] PostgreSQL latency degrading?
- [ ] API rate limits hit?
- [ ] Someone working > 10 hrs (burnout)?
- [ ] Metrics trending wrong?
- [ ] Team conflict detected?
- [ ] Time slipping vs plan?

If any ✅ → Flag for Vaibhav

---

## 📅 TOMORROW'S FOCUS

Priority 1: [Must finish]
Priority 2: [Should finish]
Priority 3: [Nice-to-have]

---

## 🚀 NEXT STANDUP
Date: Apr [DATE+1], 9 AM
Location: [Zoom link]
```

---

# 📝 FINAL SUMMARY

## 🎯 YOUR ROLE (Chowdappa)

✅ **Before Bootcamp (Apr 4-14)**:
- Confirm students & get MD approval
- Visit HPC lab, check resources
- Coordinate team prep
- Send emails to Vaibhav/Krishna

✅ **During Bootcamp (Apr 15-26)**:
- Daily 9 AM standup (15 mins)
- Monitor team health
- Log blockers + fixes
- Flag to Vaibhav if critical
- Ensure delivery stays on track

✅ **After Bootcamp (Apr 26)**:
- Final presentation + demo
- Submit filled documents
- Hand over to production team

---

## 🤖 MY ROLE (AI Co-Pilot)

✅ **Before Bootcamp (Apr 4-14)**:
- Create all code templates (RAG, embeddings, chunking, evaluation)
- Fill 80% of `MYdeliverables.txt`
- Generate presentation slides
- Create troubleshooting guide
- Provide infrastructure scripts

✅ **During Bootcamp (Apr 15-26)**:
- Real-time code debugging (you send errors, I fix)
- Performance optimization advice
- Decision analysis (A vs B options)
- Update docs with your results

✅ **After Bootcamp (Apr 26)**:
- Final [TO FILL] section auto-completion
- Metrics report generation
- Recommendation summary

---

## 🏁 SUCCESS CRITERIA (Apr 26 EOF)

- ✅ All [TO FILL] sections in deliverables document filled with evidence
- ✅ Live demo works smoothly (queries return results in < 2 seconds)
- ✅ Presentation explains architecture + recommendations
- ✅ Code repository documented + usable
- ✅ Risk log captures lessons learned
- ✅ Vaibhav + MD both approve architecture
- ✅ Team exhausted but satisfied (learned a ton)

---

## 🚀 IF YOU WANT ME TO START RIGHT NOW

**I can deliver by April 13:**

1. ✅ Complete bash script for infrastructure setup
2. ✅ Day 1-5 RAG code (embeddings, chunking, retrieval)
3. ✅ Day 6-8 RAG code (agentic, evaluation)
4. ✅ All code copy-paste ready (no Python import errors)
5. ✅ MYdeliverables.txt 80% auto-filled
6. ✅ 7-slide presentation template
7. ✅ 30+ problem troubleshooting guide
8. ✅ Daily standup templates (10 days)
9. ✅ Risk checklists for each day
10. ✅ Evaluation metrics dashboard

**Total: ~2500 lines of production code + 60 pages of docs**

---

**Ready to start? Say "YES" and I'll begin building everything today.**

**Questions? Ask anything specific to your constraints.**

---

*End of Master Playbook*
