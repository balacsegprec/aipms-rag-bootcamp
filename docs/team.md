# Team Validation & Gap Analysis
**AI-PMS RAG Bootcamp** | March 2026 | 2-Week Intensive

---

## 1. TEAM SUFFICIENCY ANALYSIS

### Critical Project Requirements vs. Team Coverage

#### Requirement Area: **Embedding & Model Selection**
- **Deliverable**: UMAP analysis comparing 3+ models, domain-term clustering validation
- **Assignment**: Uday (NLP Engineer)
- **Coverage**: ✓ **Fully Covered**
- **Risk Level**: None

#### Requirement Area: **Chunking Strategy Testing**
- **Deliverable**: 5 chunking approaches tested across 4 document types (contracts, NCRs, DPRs, correspondence), comparative metrics table
- **Assignment**: Uday (NLP Engineer)
- **Coverage**: ✓ **Fully Covered**
- **Risk Level**: None

#### Requirement Area: **Infrastructure & DevOps Setup**
- **Deliverable**: PostgreSQL + pgvector running on GPREC HPC by Day 1 afternoon; Apache AGE, pg_trgm configured; shared Jupyter Lab; free API keys (Groq, Google, OpenRouter, Cerebras) configured
- **Assignment**: Sathwika + Harshitha (Backend & Pipeline)
- **Coverage**: 🟡 **Partially Covered — HIGH DEPENDENCY**
- **Risk Level**: **MEDIUM-HIGH**
- **Why**: This is not a simple task. Requires:
  - PostgreSQL + pgvector extension compilation/installation
  - Apache AGE complex setup from source or package
  - GPREC HPC environment specific configurations
  - Free API key rotation fallback chain implementation
  - Jupyter Lab shared server configuration with proper auth
  - vLLM local serving setup (if used as fallback)
- **Mitigation**: Backend team should have **Day 0 (before bootcamp starts)** fully dedicated to infrastructure. If either Sathwika or Harshitha has NOT done PostgreSQL + pgvector before, escalate immediately.

#### Requirement Area: **Vector Search & Retrieval Implementation**
- **Deliverable**: Hybrid search (BM25 + vector + RRF), reranking pipeline, top-K retrieval logic
- **Assignment**: Uday (NLP Engineer)
- **Coverage**: ✓ **Fully Covered**
- **Risk Level**: None — Uday owns this end-to-end

#### Requirement Area: **Agentic RAG & LangGraph**
- **Deliverable**: Query router, multi-hop retrieval logic, agent decision traces
- **Assignment**: Uday (NLP Engineer)
- **Coverage**: ✓ **Fully Covered**
- **Risk Level**: None — Expected competency area for RAG engineer

#### Requirement Area: **Data Pipeline & Preprocessing**
- **Deliverable**: Download Kaggle + Indian Railways GCC datasets, organize synthetic DMRC data, structure for vector ingestion with metadata tagging (tenant_id, entity_type, package_id, etc.)
- **Assignment**: Sathwika + Harshitha (Backend & Pipeline)
- **Coverage**: ✓ **Fully Covered**
- **Risk Level**: None — Explicit role ownership

#### Requirement Area: **Free LLM API Integration & Fallback Chain**
- **Deliverable**: Groq primary + Google AI + OpenRouter + Cerebras fallback working; rate limit handling; fallback chain tested
- **Assignment**: Sathwika + Harshitha (Backend) + Uday (LLM integration)
- **Coverage**: 🟡 **Partially Covered — COORDINATION REQUIRED**
- **Risk Level**: **LOW-MEDIUM**
- **Why**: Backend handles API setup, but Uday must validate integration in LLM inference loops. Requires handoff testing.
- **Mitigation**: Joint spike on Day 1 morning (1 hr) to validate fallback chain. Both Backend + Uday sign off.

#### Requirement Area: **Evaluation Framework & RAGAS**
- **Deliverable**: RAGAS integration, manual evaluation system for 50+ queries, metrics calculation (P@5, P@10, MRR, NDCG@10, latency), structured logging
- **Assignment**: Uday (evaluation metrics) + Chowdappa (test design)
- **Coverage**: 🟡 **Partially Covered — COORDINATION RISK**
- **Risk Level**: **LOW-MEDIUM**
- **Why**: No single owner of the "evaluation orchestration." Uday knows metrics, Chowdappa knows testing, but who ensures:
  - Evaluation dataset is versioned and consistent?
  - RAGAS is configured correctly for all experiments?
  - Results are logged in retrievable format for deliverables?
- **Mitigation**: Day 1 — Uday + Chowdappa jointly design evaluation spec. Uday owns RAGAS config, Chowdappa owns test dataset creation + manual scoring.

#### Requirement Area: **Breaking Experiments & Failure Analysis**
- **Deliverable**: 5 experiments (cross-entity confusion, wrong contract version, long-doc bias, adversarial queries, tenant leakage) run + documented with root cause analysis + fixes implemented + re-tested
- **Assignment**: Uday (run experiments) + Chowdappa (find bugs) + Backend (implement metadata/security fixes)
- **Coverage**: 🟡 **Partially Covered — WORKFLOW GAP**
- **Risk Level**: **MEDIUM**
- **Why**: This is the critical "learn from failure" phase. Requires tight debugging loop across 3 team members. Without a clear workflow, experiments could run but findings get lost in the shuffle.
- **Mitigation**: Day 3 — Create shared failure log template (experiment name, query, expected failure, observed failure, root cause, fix owner, re-test result). Uday runs, logs immediately. Chowdappa validates, Backend fixes. Daily standup to unblock.

#### Requirement Area: **Experiment Tracking, Reproducibility & Metrics Logging**
- **Deliverable**: MLflow (or equivalent) tracking all experiments, hyperparameter versions, latency measurements, model checkpoints retrievable for future reference
- **Assignment**: **UNASSIGNED**
- **Coverage**: 🔴 **NOT COVERED**
- **Risk Level**: **MEDIUM**
- **Why**: The bootcamp emphasis is on "observable, testable pipelines." Without centralized experiment tracking:
  - Results from Day 1 embedding comparison might not be reproducible on Day 3
  - Hyperparameters used in chunking tests can't be easily compared to Day 5 results
  - Latency measurements from different dates/hardware can't be correlated
  - Deliverables document asks for "evidence-based architecture recommendations" — evidence needs to be trackable
- **Mitigation Options**:
  - **Option B (Stretch)**: Backend team adds MLflow setup as part of infrastructure. Takes ~2 hrs on Day 0. Then Uday + Chowdappa log their own experiments manually. Works but adds responsibility to already-loaded team.
  - **Option C (Hire)**: See hiring recommendation below.

#### Requirement Area: **Documentation & Deliverables Compilation**
- **Deliverable**: Filled-in deliverables document with 9+ diagrams, metrics tables, observation forms, finding reports; all [TO FILL] sections completed with evidence
- **Assignment**: **DISTRIBUTED (No clear owner)**
- **Coverage**: 🟡 **Partially Covered — BOTTLENECK RISK**
- **Risk Level**: **MEDIUM**
- **Why**: 
  - Uday generates RAG results → must write findings
  - Backend generates infrastructure + latency data → must document decisions
  - Chowdappa generates test results + demo script → must document QA findings
  - Nobody owns the "keeper of the deliverables" role. Last-minute scramble on Day 14 very likely.
- **Mitigation**: Designate **one person as "Deliverables Owner"** (recommend: Chowdappa, since he owns QA + demo anyway). Owners of each section must provide raw data to Deliverables Owner by EOD each relevant day. Deliverables Owner compiles daily, flags missing evidence immediately.

#### Requirement Area: **Live Demo Preparation & Stakeholder Readiness**
- **Deliverable**: Working end-to-end RAG system demonstrated; demo script; stakeholder presentation
- **Assignment**: Chowdappa (Testing & Demo)
- **Coverage**: ✓ **Fully Covered**
- **Risk Level**: None — Explicit role

#### Requirement Area: **Day-to-Day Sprint Coordination & Dependency Management**
- **Deliverable**: Daily standup decisions, blocking dependency resolution, timeline adherence on parallel tracks (Uday on retrieval, Backend on APIs, Chowdappa on QA), escalation clarity
- **Assignment**: **UNASSIGNED**
- **Coverage**: 🔴 **NOT COVERED**
- **Risk Level**: **MEDIUM-HIGH**
- **Why**: The 2-week plan is heavily parallel:
  - **Day 1 Afternoon (parallel)**: Uday running UMAP embedding comparison while Backend sets up Jupyter Lab + PostgreSQL
  - **Day 2 (parallel)**: Uday testing chunking strategies while Backend configuring API fallbacks
  - **Day 3-4 (parallel)**: Multiple breaking experiments need debugging + fixes from different team members
  - **Day 5 end (parallel)**: Final integration + demo prep requires tight coordination
  - **No sprint master**: Uday can't unblock Backend if PostgreSQL fails. Backend can't escalate LLM integration to Vaibhav if needed. Chowdappa doesn't know if demo should wait for retrieval improvements.
- **Impact if uncovered**: High likelihood of:
  - Blocking dependencies found too late (Day 5 realization that PostgreSQL latency kills NFR-04)
  - Rework cycles because teams didn't coordinate on data formats
  - Demo prep starting on Day 13 (only 1 day before delivery)

---

## 2. ROLE GAP DECISIONS

### Gap 1: Infrastructure & DevOps (PostgreSQL + pgvector + free APIs)
**Decision: OPTION B — STRETCH**
- Covered by: Sathwika + Harshitha (Backend & Pipeline)
- Added Risk: Medium — IF team has done this before, proceed. IF new to PostgreSQL extensions + API orchestration, escalate.
- Mitigation: Backend team claims **full Day 0 (before bootcamp)** for infrastructure spiking. Joint sign-off with Uday on Day 1 morning that all systems are working.
- Contingency: If infrastructure is not ready by EOD Day 1, bootcamp start date slips. Build 1-day buffer into schedule.

### Gap 2: Experiment Tracking & Reproducibility (MLflow / equivalent)
**Decision: OPTION B → OPTION C (escalation point)**
- **Start with OPTION B**: Backend adds MLflow setup as Day 0 task (~2 hrs config). Uday + Chowdappa log experiments manually.
- **Escalate to OPTION C if**: By EOD Day 2, it's clear that manual logging is creating duplicate work or missing data. Then hire dedicated role (see below).
- Why escalate possible: "Observable, testable pipelines" is a core bootcamp goal. Half-implemented experiment tracking undermines this.

### Gap 3: Evaluation Framework Orchestration (RAGAS + Manual Scoring)
**Decision: OPTION A — COVERED via tight coordination**
- Covered by: Uday (RAGAS config) + Chowdappa (test dataset + manual scoring)
- Coordination required: Joint design spec on Day 1, daily sync during Days 2-5.
- Risk level: **Low** if coordination happens; **Medium** if no handoff protocol defined upfront.

### Gap 4: Breaking Experiments Workflow (Debugging + Root Cause + Fixes)
**Decision: OPTION A — COVERED via clear workflow**
- Covered by: Uday (runs), Chowdappa (validates), Backend (implements fixes)
- Critical requirement: Shared failure log + daily standup during Days 3-4.
- Risk level: **Low** if workflow is written down; **High** if ad-hoc.

### Gap 5: Documentation & Deliverables Compilation
**Decision: OPTION B — STRETCH**
- Covered by: Distributed ownership (Uday writes findings, Backend writes infra decisions, Chowdappa writes QA results)
- Added Risk: **Medium** — Without a "Deliverables Owner," last-minute scramble very likely.
- Mitigation: Designate Chowdappa as Deliverables Owner. He compiles daily from other team members' submissions. Non-negotiable.

### Gap 6: Day-to-Day Sprint Coordination & Blocking Dependencies
**Decision: OPTION B → OPTION C (escalation approach)**

**Phase 1 (Days 1–8): Try Chowdappa as Dual-Role Sprint Coordinator**
- **Rationale**: Chowdappa is already Deliverables Owner. His testing role has natural breathing room in Days 1–8 (testing happens after things are built). Days 1–8 are infrastructure + setup heavy; Chowdappa can own sprint coordination with minimal conflict.
- **Promotion to**: "QA Lead + Sprint Coordinator" (temporary, Days 1–8 only)
- **Responsibilities** (same as Scrum Master role, Section 3)
- **Load assessment**: Medium. If Chowdappa reports overload by EOD Day 3, escalate immediately.

**Phase 2 (Days 9–14): Demo Prep Takes Over**
- Chowdappa drops coordination duties entirely
- Focus shifts to live demo + stakeholder readiness
- If parallel tracks are still actively running in Days 9–14, coordination reverts to ad-hoc standups

**Escalation to OPTION C (External Hire)**
- **Trigger**: If EOD Day 3 shows Chowdappa cannot juggle both roles, or if parallel dependency work continues past Day 8
- **Then**: Hire external Scrum Master for remaining days (Days 9–14)
- **Cost impact**: Lower than full 2-week hire (~₹20–30K)
- **Not covered by** any existing role if this escalation is needed. Vaibhav is advisor-only, not operational.
- **Why critical**: 2-week intensive with 4 people on parallel tracks. Without sprint coordination:
  - Uday waits on Backend for PostgreSQL, doesn't escalate fast enough
  - Backend doesn't know if their API setup matches Uday's integration expectations
  - Chowdappa starts demo prep without knowing if Uday has final RAG results
  - Vaibhav gets surprised on Day 13 that something is blocked since Day 7
- **Kill criteria**: If any team member spends > 1 day blocked waiting for another team member's deliverable, the lack of sprint coordination is hurting the project.

---

## 3. SPRINT COORDINATOR ROLE DEFINITION

**Primary Approach: Chowdappa (Days 1–8)**  
**Fallback Approach: External Hire (Days 9–14, if needed)**

**Role Title**: Sprint Master / RAG Bootcamp Coordinator

**Duration**: Full-time, 2 weeks (Days 1–14, March 18–31, 2026)  
**Reporting To**: Vaibhav (advisor approval); day-to-day coordination owns all 4 team members

**Must-Have Skills**:
1. **Agile / Scrum facilitation** — Daily standups, dependency tracking, blocker resolution
2. **Technical literacy** (not expertise, but literacy):
   - Understands what a RAG pipeline is
   - Knows why PostgreSQL + pgvector matters for this project
   - Can read a pull request and ask intelligent follow-up questions
   - Can interpret experiment metrics (P@5, latency, MRR)
3. **Delivery mindset** — Ruthless prioritization; willing to say "this can slip" vs. "this is critical path"
4. **Documentation discipline** — Keeps the shared failure log, metrics dashboard, blockers board updated in real-time

**Nice-to-Have Skills**:
- Prior experience with ML/NLP projects (even if not hands-on)
- Familiarity with free LLM APIs (Groq, Google, etc.) — context-setting only
- Experience with PostgreSQL or vector databases — to have informed conversations

**Does NOT Need To**:
- Write code — all technical work belongs to Uday/Backend/Chowdappa
- Know RAG deeply — Vaibhav is the strategic advisor
- Do ML — Uday is the ML person

**Primary Responsibilities**:
1. **Daily standup facilitation** (15 mins each morning at 9 AM)
   - What did you complete?
   - What are you starting today?
   - What blockers do you have?
2. **Blockers dashboard** — Maintains visible list of all blockers, owner, expected resolution
3. **Deliverables tracking** — Ensures all [TO FILL] sections of deliverables doc are assigned and have deadlines
4. **Metrics logging** — Ensures MLflow / experiment log is being filled in daily (doesn't do the logging, just audits)
5. **Risk escalation** — If any task looks like it will slip, flag to Vaibhav by EOD
6. **Demo readiness** — Works with Chowdappa to ensure demo script + data are ready by Day 13
7. **Meeting notes & decisions** — Keeps the shared Slack/wiki updated on architectural decisions made each day

**Closest Collaboration Partner**: All 4 team members, but daily sync with Chowdappa (QA intersection) and Backend (schedule risk highest there)

**Cost Estimate** (for budgeting):
- Junior Scrum Master / Coordinator: ~₹40–60K for 2 weeks (India rate, estimated)
- Alternative: Senior intern with delivery experience, lower cost

---

## 4. FINAL VERDICT

### � **IF Chowdappa Accepts Sprint Coordinator Role (Days 1–8) → Proceed**

**Justification** (3–5 sentences):

The team is structurally sound — Uday owns RAG complexity, Backend owns infrastructure, Chowdappa owns QA/demo + now sprint coordination (Days 1–8), Vaibhav provides strategic oversight. By promoting Chowdappa to dual role early (his testing work is light until Day 9), coordination stays internal and context-aware without external hire. Infrastructure setup (PostgreSQL + pgvector + free API fallback chain) is the critical path; Backend claims full Day 0 for spiking. If Chowdappa reports overload by EOD Day 3, escalate to external hire immediately for Days 9–14. **Recommendation:** Confirm Chowdappa's willingness to Sprint Coordinate for first 8 days; Backend completes Day 0; Vaibhav approves contingency hiring authority if needed.

### 🔴 **IF Nobody Takes Sprint Coordinator Role → Do NOT Proceed**

Without day-to-day sprint coordination, the team will experience blocked dependencies, mishandoffs, and last-minute panics. This is not a "nice-to-have." A 2-week intensive with 4 people on parallel tracks **requires** active coordination. If Chowdappa cannot take it, hire external Scrum Master **before Day 1 starts.** Proceeding without either option is a path to failure.

---

## 5. RISK SUMMARY TABLE

| Risk Area | Likelihood | Impact | Owner | Mitigation |
|-----------|------------|--------|-------|-----------|
| PostgreSQL + pgvector not ready by EOD Day 1 | Medium | **CRITICAL** — blocks all ingestion | Backend | Day 0 dry-run + sign-off |
| API fallback chain fails mid-bootcamp (hits rate limits) | Low | Medium — have manual LLM script as backup | Backend + Uday | Test fallback chain on Day 1 afternoon |
| Breaking experiments findings get lost (no central log) | Medium | Medium — deliverables incomplete | Uday + Chowdappa | Shared failure log template, daily standup review |
| Demo prep starts on Day 13 (bleeding into Day 14) | Medium | Medium — rushed presentation | Chowdappa | Assign Chowdappa to Deliverables Owner role; demo script started by EOD Day 10 |
| Uday blocked waiting for Backend API setup (no escalation) | Medium-High | Medium-High — parallel work stalls | Sprint Master | Chowdappa escalates within 4 hrs; Vaibhav unblocks if needed |
| Experiment metrics not reproducible (no MLflow) | Low-Medium | Low — affects future tuning, not immediate demo | Backend + Uday | MLflow setup on Day 0; manual logging if time short |
| **Uday single-point-of-failure (overloaded NLP tasks)** | **High** | **CRITICAL** — if Uday blocked for 1 day, 3 tracks slip | **Uday + Sathwika/Harshitha** | Identify 2 offloadable tasks by Day 1 (RAGAS setup config, MLflow logging). Sathwika absorbs if Uday overloaded. |

---

## 6. APPROVAL CHECKLIST BEFORE BOOTCAMP STARTS

**Role Confirmations**
- [ ] Chowdappa confirmed as Deliverables Owner + Sprint Coordinator (Days 1–8 dual role)
- [ ] Vaibhav confirmed as Strategic Advisor (see escalation protocol in Section 7)
- [ ] Day 0 Lead: Sathwika (primary), Harshitha (support)
      - Primary Task: PostgreSQL + pgvector + Apache AGE + Jupyter Lab
      - Success Criteria: Uday can run a test embedding query by 6 PM Day 0
      - **If infrastructure fails by 6 PM Day 0 → Trigger contingency**: Use Google Colab Pro + Pinecone free tier as temporary fallback. Do NOT delay Day 1 start.
- [ ] Contingency decision authority: Vaibhav has pre-approved Colab + Pinecone pivot if Day 0 PostgreSQL fails

**Infrastructure & Setup**
- [ ] Backend team completes Day 0 infrastructure spike; Uday sign-off on all systems
- [ ] Free API keys (Groq, Google, OpenRouter, Cerebras) generated and tested
- [ ] Kaggle + Indian Railways GCC + synthetic DMRC datasets downloaded and staged in shared storage
- [ ] Jupyter Lab server running on GPREC HPC, all 4 team members can log in
- [ ] MLflow server started OR manual logging protocol defined

**Process & Coordination**
- [ ] Shared failure log template created and linked in team wiki
- [ ] Evaluation spec jointly designed by Uday + Chowdappa (Day 1)
- [ ] Break experiments workflow documented: Uday runs → logs → Chowdappa validates → Backend fixes
- [ ] Uday's offloadable tasks identified: RAGAS config setup + MLflow logging (Sathwika/Harshitha absorb if needed)
- [ ] Calendar blocked: Daily 9 AM standup (15 mins), Daily 4 PM check-in (if blockers exist)
- [ ] Vaibhav availability confirmed for escalation (see Section 7 triggers)

---

## 7. Vaibhav Engagement Protocol

**Vaibhav's Role**: Strategic Advisor (NOT operational, NOT daily contributor)

**Consulted IN These Situations** (and ONLY these):
1. **Scope or deliverable impact** — A decision will change what's in the final demo/document
2. **Blocker unresolved for >4 hours** — Chowdappa has attempted resolution within team; needs external input
3. **Risk triggered (not feared)** — One of the Section 5 risks has **actually occurred**, not just been anticipated
4. **Demo readiness in question** — By EOD Day 12, if demo readiness is uncertain
5. **Parallel track decision** — If both Uday + Backend are blocked waiting on each other; Vaibhav breaks tie
6. **Contingency approval** — Day 0 infrastructure failure → Colab + Pinecone pivot decision

**NOT Consulted For** (team owns these):
- Daily technical decisions (Uday owns RAG architecture + LLM integration)
- Infrastructure choices (Backend owns PostgreSQL + APIs)
- Test case design (Chowdappa owns QA strategy)
- Experiment hyperparameter tuning (Uday owns RAG tuning)
- API provider selection (Backend owns API strategy)

**Escalation Format** (ensures Vaibhav can respond fast):
```
When escalating to Vaibhav, ALWAYS include:
  → Problem (1–2 lines, no jargon)
  → Impact (how many people blocked? how many days?)
  → Option A vs Option B (team's recommendation included)
  → Decision needed by: [HH:MM format]
  → Your context link (wiki page / GitHub PR / Slack thread)

Example:
  "PostgreSQL setup failing. Backend stuck. Recommend Colab 
   fallback approved in advance. Approval needed by 6 PM today.
   Wiki: [link]"
```

**Response Expectation**:
- Vaibhav targets: Response within 4 hours of escalation
- If unavailable: Chowdappa has pre-approved authority to implement recommended option (document decision)

**NOT an Escalation** (Chowdappa + team resolve):
- Chunking strategy debate (technical tradeoff, not scope-changing)
- Which embedding model to test (all get tested per plan)
- Whether a failing experiment needs rerun (Chowdappa decides)

---

**Document Owner**: Vaibhav (approver). **Operational Owner**: Chowdappa (Days 1–8 sprint coordination). **Next Update**: EOD Day 1 (post infrastructure validation).
