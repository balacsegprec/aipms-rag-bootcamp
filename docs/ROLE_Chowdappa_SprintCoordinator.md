# 🎯 ROLE: CHOWDAPPA — SPRINT COORDINATOR + QA LEAD

**Reporting To**: Vaibhav (Strategic Advisor)  
**Coordinates With**: Uday (NLP), Backend1 (Infrastructure), Backend2 (APIs)  
**Approval Authority**: MD Madhu Sir  
**Contact Emergency**: Vaibhav (within 4 hours)

---

## 📍 YOUR ROLE IN 30 SECONDS

You are the **hub of the wheel**. Everyone works independently, but you ensure:
- ✅ Team is on schedule
- ✅ Blockers get escalated fast
- ✅ Daily standups happen
- ✅ Documentation gets filled
- ✅ Demo is ready by Friday

**You don't write code. You unblock people.**

---

# 📅 YOUR DAILY CHECKLIST (April 4-26)

## PHASE 0: PRE-BOOTCAMP (April 4-14)

### **April 4 (Friday) — TODAY**

**MORNING (9 AM - 12 PM)**
- [ ] Read entire MASTER_BOOTCAMP_PLAYBOOK.md (45 mins)
- [ ] Understand your role vs others (30 mins)
- [ ] Create folder: `/aipms-rag-bootcamp/daily-logs/`

**AFTERNOON (1 PM - 5 PM)**
- [ ] Send blocker email to MD Madhu Sir (from team.md section)
- [ ] Send Info email to Vaibhav (status update)
- [ ] Send Info email to Krishna (request DMRC dataset)
- [ ] **Blockers awaiting**:
  - ⏳ Student confirmation from MD (April 7)
  - ⏳ HPC lab approval from MD (April 8)
  - ⏳ MD final approval (April 10)

**EXIT CRITERIA**: All 3 emails sent, awaiting responses

---

### **April 5 (Saturday)**

**STATUS**: Weekend — No bootcamp work (but you can prep)

- [ ] Review MASTER_BOOTCAMP_PLAYBOOK sections 4-6
- [ ] Print daily standup template (save as template.md)
- [ ] Create Slack/WhatsApp group: "RAG-Bootcamp-Team"
- [ ] Optional: Download Kaggle account setup guide

---

### **April 6 (Sunday)**

**STATUS**: Weekend — No bootcamp work

- [ ] Create shared Google Sheet: "Bootcamp_Metrics_Dashboard"
  - Columns: Date | Latency (p95) | Precision@5 | Metric | Notes
- [ ] Set up meeting calendar (9 AM daily standup, 4 PM check-in if needed)

---

### **April 7 (Monday) — CRITICAL DAY**

**MORNING (9 AM - 12 PM)**
- [ ] **CRITICAL**: Confirm students MUST meet MD today
  - [ ] Send reminder to Backend Student 1 & 2
  - [ ] Template: "Hi, today is your confirmation meeting with Madhu Sir for bootcamp. Please meet him by 11 AM. Confirm once done."
  - [ ] If students don't confirm → **ESCALATE to Vaibhav immediately** (blocker: no backend team)

**AFTERNOON (1 PM - 5 PM)**
- [ ] Receive confirmation from students or get rejection
- [ ] **If YES**: Mark ✅ in your log
- [ ] **If NO**: Contact Vaibhav → Need alternative plan (timeline slips to April 22)
- [ ] Send Vaibhav update email

**BLOCKERS TO WATCH**:
- 🔴 Students say "maybe later" → You push for YES/NO TODAY
- 🔴 No response from students → Call them directly
- 🔴 MD doesn't have bandwidth → Escalate to Vaibhav

**EXIT CRITERIA**: Both students send written YES or blocker escalated

---

### **April 8 (Tuesday) — YOU VISIT HPC LAB**

**MORNING (8 AM - 12 PM)**
- [ ] **Go to GPREC HPC lab yourself** (with or without Backend students)
- [ ] Checklist from MASTER_BOOTCAMP_PLAYBOOK:
  - [ ] CPU: 4+ cores? (8+ better?)
  - [ ] RAM: 16+ GB?
  - [ ] Storage: 75+ GB free?
  - [ ] OS: Linux/Ubuntu? (or Windows WSL?)
  - [ ] Internet: Can reach Groq, Google, HuggingFace?
  - [ ] Multi-user: Can 4 people login Jupyter simultaneously?
- [ ] **Take screenshots** of HPC specs
- [ ] **Get lab admin contact info** (phone, email)
- [ ] Ask: "Can we use this for 2 weeks starting Apr 12?"

**AFTERNOON (1 PM - 5 PM)**
- [ ] Return to office
- [ ] Document findings: `/daily-logs/apr8_hpc_lab_visit.txt`
  - Format: CPU cores: X | RAM: Y GB | Storage: Z GB | Issues: ...
- [ ] Send Vaibhav findings email
- [ ] **IF ISSUES FOUND**: Escalate immediately

**BLOCKERS TO WATCH**:
- 🔴 Lab doesn't have 16 GB RAM → Option A: Use Colab; Option B: Ask admin to clear space
- 🔴 Storage < 75 GB → Option A: Delete old data; Option B: Create new partition
- 🔴 Internet can't reach APIs → Option A: Configure firewall whitelist; Option B: Use VPN
- 🔴 Can't multi-login Jupyter → Option A: Use multiple Jupyter instances; Option B: Use Google Colab instead

**CONTACTS IF BLOCKED**:
- Lab admin (for hardware/network issues)
- Vaibhav (if major blocker, approve Colab contingency)

**EXIT CRITERIA**: HPC specs documented, plan confirmed

---

### **April 9 (Wednesday) — DATA PREP DAY**

**MORNING (9 AM - 12 PM)**
- [ ] **Verify datasets downloaded**:
  - [ ] Kaggle: `/data/datasets/kaggle-enterprise-rag/` → ~100 markdown files present?
  - [ ] GCC: `/data/datasets/indian-railways-gcc-2022/` → PDF has text (not scanned)?
  - [ ] DMRC: `/data/datasets/synthetic-dmrc/` → All doc types present?
- [ ] Check with Backend2 if all datasets accessible from HPC
- [ ] Take inventory screenshot

**AFTERNOON (1 PM - 5 PM)**
- [ ] Verify API keys created (you ask, don't do it):
  - [ ] Groq API key: Created? Saved securely?
  - [ ] Google API key: Created? Saved securely?
  - [ ] HuggingFace token: Created? Saved securely?
  - [ ] OpenRouter API key: Created? Saved securely?
- [ ] **DO NOT store real API keys.** Just verify they exist (Backend2 stores them)
- [ ] Document: `/daily-logs/apr9_api_keys_status.txt`

**BLOCKERS TO WATCH**:
- 🔴 Kaggle download still in progress → Estimate: when done? (>6 hours? Warn Vaibhav)
- 🔴 GCC PDF corrupted → Option: Download from different source (IRICEN or DFCCIL links provided)
- 🔴 DMRC data not accessible → Option: Request from Vaibhav / Krishna
- 🔴 API signup slow (email verification pending) → Option: Resend email or use backup email

**CONTACTS IF BLOCKED**:
- Krishna (for DMRC dataset)
- Vaibhav (if any block critical)

**EXIT CRITERIA**: All 3 datasets accessible, 4 API keys created

---

### **April 10 (Thursday) — MD APPROVAL CHECKPOINT**

**MORNING (9 AM - 12 PM)**
- [ ] Compile pre-bootcamp status:
  - ✅ Students confirmed (names + yes)
  - ✅ HPC lab checked (specs OK)
  - ✅ Datasets ready (3 verified)
  - ✅ API keys created (4 done)

**AFTERNOON (1 PM - 5 PM)**
- [ ] **Send final approval email to MD:**

```
Subject: RAG Bootcamp Ready — Final Approval Request (April 10)

Hi Madhu Sir,

All pre-bootcamp items complete. 4 confirmations needed:

✓ Backend Students: [Name1] & [Name2] confirmed for Apr 15-26 (full-time)
✓ GPREC HPC: CPU [X cores], RAM [Y GB], Storage [Z GB] — OK
✓ Datasets: Kaggle ✓ + GCC ✓ + DMRC ✓ (ready)
✓ APIs: Groq + Google + HF + OpenRouter (all created)

Ready to proceed with infrastructure spike Apr 12-13?

YES → Infrastructure Day 0 starts Saturday Apr 12
NO → We delay to April 22

Your approval by EOD today?

Chowdappa
```

- [ ] **AWAIT CONFIRMATION** (target: by 5 PM same day)

**IF YES**: Proceed to Day 0  
**IF NO**: Reschedule, update all dates

**EXIT CRITERIA**: MD approval received (written)

---

### **April 11 (Friday) — PRE-DAY-0 FINAL PREP**

**MORNING (9 AM - 12 PM)**
- [ ] **Confirm Day 0 is READY** (infrastructure spike tomorrow):
  - [ ] Backend1 & Backend2: Are you ready to execute infrastructure scripts? (Confirm)
  - [ ] Backend1: Do you have HPC login credentials? (Confirm)
  - [ ] Backend2: Do you have API keys saved securely? (Confirm)
  - [ ] All: Do you have emergency contact for lab admin? (Confirm)

**AFTERNOON (1 PM - 5 PM)**
- [ ] Final checklist email to team:

```
Subject: Day 0 Infrastructure Spiking Tomorrow (Apr 12-13) — Final Checklist

Hi Team,

**Tomorrow starts Day 0 (Apr 12-13, Fri-Sat). Infrastructure spiking.**

Backend1 & Backend2:
  ✓ Have HPC login? (SSH working?)
  ✓ Have infrastructure scripts? (AI will send by tonight)
  ✓ Have lab admin contact? (for emergencies)
  ✓ Sleep well today (you'll be online 48 hrs with breaks)

Uday:
  ✓ Review script templates (I'll send)
  ✓ Prepare test queries for Monday
  ✓ Have Jupyter login ready

Chowdappa (me):
  ✓ On standby Sat 9 AM - 6 PM for escalations
  ✓ Monitoring: PostgreSQL, APIs, Jupyter setup
  ✓ Ready to contact Vaibhav if blocker hit

**EXIT CRITERIA (by 6 PM Apr 13)**:
  - PostgreSQL running on GPREC ✓
  - pgvector extension installed ✓
  - Jupyter accessible to all 4 users ✓
  - All 4 APIs tested (working) ✓
  - All 3 datasets verified ✓

If ANY item incomplete → Trigger Colab contingency.

See you tomorrow!
Chowdappa
```

- [ ] Send infrastructure scripts to Backend1 (bash + SQL)
- [ ] Send Jupyter setup guide to Backend2
- [ ] Send API test script to Backend2
- [ ] Send test queries checklist to Uday

**EXIT CRITERIA**: All team members confirmed ready

---

## PHASE 1: DAY 0 INFRASTRUCTURE SPIKE (April 12-13)

### **April 12 (Saturday) — INFRASTRUCTURE DAY 1**

**9 AM START**
- [ ] **9:00 AM**: Check-in call with Backend1 & Backend2
  - Q: "Have you SSHed into GPREC HPC successfully?"
  - Q: "Infrastructure scripts downloaded?"
  - Setup expectations: Work till 6 PM (check-in at 12 PM, 3 PM, 6 PM)

**12 PM CHECK-IN**
- [ ] Call Backend1: "Progress on PostgreSQL?"
- [ ] Call Backend2: "Progress on APIs?"
- [ ] Log status: `/daily-logs/apr12_day0_morning.txt`
- [ ] **IF BLOCKED**: Escalate to Vaibhav (target: resolve within 1 hour)

**3 PM CHECK-IN**
- [ ] Same check-in questions
- [ ] Update: `/daily-logs/apr12_day0_afternoon.txt`

**6 PM CHECK-IN**
- [ ] Same check-in questions
- [ ] Document blockers (if any)
- [ ] Plan for Sunday (Day 2 of infrastructure spike)

**BLOCKERS TO WATCH** (Apr 12):
- 🔴 PostgreSQL install fails → Troubleshoot: GCC missing? Dependencies?
- 🔴 pgvector build takes too long → Option: Use ChromaDB as fallback
- 🔴 Jupyter not multi-user capable → Option: Separate Jupyter instances per user
- 🔴 API keys don't work → Option: Regenerate or use different provider

**IF CRITICAL BLOCKER (can't fix in 1 hr)**: Call Vaibhav by 7 PM

---

### **April 13 (Sunday) — INFRASTRUCTURE DAY 2 (FINAL)**

**9 AM START**
- [ ] Same check-in call with Backend1 & Backend2
- [ ] Goal: **ALL infrastructure ready by 6 PM today**

**12 PM CHECK-IN**
- [ ] "PostgreSQL working? Vectors can insert + search?"
- [ ] "APIs all tested?"
- [ ] "Jupyter accessible to all 4 users?"

**3 PM CHECK-IN**
- [ ] "Any blockers remaining?"
- [ ] "On track for 6 PM completion?"

**5:30 PM FINAL CHECK**
- [ ] Backend1: "PostgreSQL ready for Uday?"
  - Test: Can Uday query vectors?
- [ ] Backend2: "Jupyter + APIs ready?"
  - Test: Uday can login + test API call?
- [ ] Uday: "Test queries ready for Monday?"

**6 PM SIGN-OFF**
- [ ] **SUCCESS CHECKLIST**:
  - [ ] PostgreSQL + pgvector ✓
  - [ ] Apache AGE + pg_trgm ✓
  - [ ] Jupyter accessible ✓
  - [ ] APIs working ✓
  - [ ] Datasets verified ✓
- [ ] Document: `/daily-logs/apr13_day0_completed.txt`
- [ ] **IF ALL ✅**: Bootcamp ready for Monday
- [ ] **IF ANY ❌**: Trigger Colab contingency (delay to Apr 22)

**ESCALATION CHECKPOINT** (Apr 13, 5 PM):
- If ANY item not 100% → **CALL VAIBHAV IMMEDIATELY**
- Option A: Fix by 6 PM
- Option B: Use Colab + Pinecone fallback (pre-approved)
- Option C: Delay bootcamp to April 22

---

## PHASE 2: WEEK 1 BOOTCAMP (April 15-19)

### **April 15 (Monday) — BOOTCAMP DAY 1**

**PRE-STANDUP (before 9 AM)**
- [ ] Check: All team members present in HPC lab?
- [ ] Check: PostgreSQL running?
- [ ] Check: Jupyter accessible?
- [ ] All APIs up?

**9:00 AM STANDUP (15 mins)**
- [ ] Run daily standup (template provided at end of file)
- [ ] Uday: "Day 1 plan: Embedding comparison"
- [ ] Backend: "Day 1 support: Data loading, monitor APIs"
- [ ] You: "I'm documenting findings. Report blockers by 12 PM"

**DURING DAY (9 AM - 6 PM)**
- [ ] 12 PM check-in: Any blockers mid-day?
- [ ] 3 PM check-in: Progress on path?
- [ ] 5 PM check-in: On track for Day 1 exit criteria?

**6 PM EXIT CRITERIA CHECK**:
- [ ] Uday: "Embedding comparison done? UMAP plot generated?"
- [ ] Metrics: Latency for each model captured?
- [ ] Decision: Which embedding model to use going forward?
- [ ] Document: `/daily-logs/apr15_day1_completed.txt`

**DAILY LOGS** (commit to shared folder):
- Query count completed
- Latency baseline
- Any errors encountered
- Metrics captured
- Next day blockers

---

### **April 16 (Tuesday) — BOOTCAMP DAY 2**

**9:00 AM STANDUP**
- Run standup (Uday: chunking strategies, Backend: data prep)

**DURING DAY**
- 12 PM, 3 PM, 5 PM check-ins (same as Monday)

**6 PM EXIT CRITERIA CHECK**:
- [ ] 5 chunking strategies tested?
- [ ] Metrics: P@5 for each?
- [ ] Decision: Best chunking strategy?
- [ ] Document: `/daily-logs/apr16_day2_completed.txt`

---

### **April 17 (Wednesday) — BOOTCAMP DAY 3**

**9:00 AM STANDUP**
- Uday: "Breaking experiments plan (5 tests)"

**DURING DAY**
- 12 PM, 3 PM, 5 PM check-ins

**6 PM EXIT CRITERIA CHECK** (CRITICAL DAY):
- [ ] FE-01 (cross-entity confusion): Logged + fix documented?
- [ ] FE-02 (wrong contract version): Logged + fix documented?
- [ ] FE-03 (long document bias): Logged + fix documented?
- [ ] FE-04 (adversarial query): Logged + fix documented?
- [ ] FE-05 (tenant leakage): Logged + fix documented?
- [ ] Document: `/daily-logs/apr17_day3_completed.txt`

**IF BLOCKER HIT** (breaking experiment fails badly):
- Option A: Debug + fix same day (target: 2 hrs)
- Option B: Document + move forward, fix next day
- Option C: Escalate to Vaibhav (if architecture risk)

---

### **April 18 (Thursday) — BOOTCAMP DAY 4**

**9:00 AM STANDUP**
- Uday: "Hybrid search implementation"

**6 PM EXIT CRITERIA CHECK**:
- [ ] BM25 search working?
- [ ] Vector search working?
- [ ] RRF fusion working?
- [ ] Reranking implemented?
- [ ] Latency < 2 seconds?
- [ ] Document: `/daily-logs/apr18_day4_completed.txt`

---

### **April 19 (Friday) — BOOTCAMP DAY 5**

**9:00 AM STANDUP**
- Uday: "End-to-end RAG v1 integration"

**6 PM EXIT CRITERIA CHECK** (CRITICAL):
- [ ] Complete RAG pipeline working?
- [ ] 20 test queries ran successfully?
- [ ] Demo script tested 3+ times?
- [ ] All metrics captured?
- [ ] **Document**: `/daily-logs/apr19_day5_completed.txt`

**WEEK 1 SUMMARY**:
- [ ] Document: `/weekly-summaries/week1_summary.md`
  - What went well?
  - What broke + how fixed?
  - Metrics achieved?
  - Next week priorities?

---

## PHASE 3: WEEK 2 BOOTCAMP (April 22-26)

### **April 22 (Monday) — BOOTCAMP DAY 6**

Same daily rhythm as Week 1 (9 AM standup, 12/3/5 PM check-ins, 6 PM exit criteria)

**6 PM EXIT CRITERIA**:
- [ ] Query router implemented?
- [ ] Multi-hop logic tested on 2 sample queries?
- [ ] Document: `/daily-logs/apr22_day6_completed.txt`

---

### **April 23 (Tuesday) — BOOTCAMP DAY 7**

**6 PM EXIT CRITERIA**:
- [ ] LangGraph agent working?
- [ ] Multi-hop traces logged?
- [ ] Document: `/daily-logs/apr23_day7_completed.txt`

---

### **April 24 (Wednesday) — BOOTCAMP DAY 8**

**6 PM EXIT CRITERIA**:
- [ ] RAGAS evaluation complete on 50+ queries?
- [ ] Metrics calculated (Precision, Recall, F1, BLEU)?
- [ ] Document: `/daily-logs/apr24_day8_completed.txt`

---

### **April 25 (Thursday) — BOOTCAMP DAY 9**

**6 PM EXIT CRITERIA** (CRITICAL FOR DEMO):
- [ ] Presentation slides complete (7 slides)?
- [ ] Demo script finalized (ready to narrate)?
- [ ] Rehearsal run complete (30 mins)?
- [ ] All [TO FILL] docs filled?
- [ ] Document: `/daily-logs/apr25_day9_completed.txt`

**IF DEMO NOT READY** (🔴 CRITICAL):
- Call Vaibhav immediately
- Friday morning emergency fix session

---

### **April 26 (Friday) — DELIVERY DAY**

**9 AM FINAL STANDUP**
- Quick check: Everyone ready? Demo works?

**10 AM DEMO REHEARSAL** (final 30 mins)
- Run demo 1 more time
- Practice narration

**11:00 AM PRESENTATION**
- Live demo to Vaibhav + MD Madhu Sir
- You narrate (slide-by-slide)
- Uday available for technical Qs
- Demo walkthrough

**POST-DEMO (1-2 PM)**
- Collect feedback
- Document: `/daily-logs/apr26_delivery_notes.txt`
- Final submissions checklist

**EXIT CRITERIA** (DELIVERY COMPLETE):
- [ ] Vaibhav signed off architecture
- [ ] MD approved results
- [ ] All deliverables submitted
- [ ] Code repository uploaded
- [ ] Final documentation handed over

---

# ⚠️ BLOCKERS YOU'LL FACE & HOW TO RESOLVE

## Blocker Category 1: Team Issues (Most Common)

### **Blocker 1A: Backend Students Not Responding**

**When**: Any day, if student doesn't show up

**Impact**: 🔴 CRITICAL — Entire infrastructure blocked

**Resolution Steps**:
1. Call student directly (within 1 hour)
2. Ask: "What's the issue? Can you be online in 1 hour?"
3. If YES: Good, continue
4. If NO: Get reason
   - Sick? → Escalate to Vaibhav (need replacement)
   - Personal emergency? → Reschedule task, adjust timeline
   - Lack of clarity? → Re-brief on task, ensure they understand

**Whom to Contact**: Vaibhav (if replacement needed)

---

### **Blocker 1B: Uday Appears Overloaded**

**When**: Mid-week, Uday takes > 10 hrs/day or misses standup

**Impact**: 🟡 MEDIUM — Code quality degrades, bugs increase

**Resolution Steps**:
1. During standup, ask: "Uday, are you confident you'll finish today's work?"
2. If unsure: Offer to reassign 1 task
   - Option: Backend2 handles RAGAS config setup
   - Option: You handle some documentation
3. If overloaded still: Escalate to Vaibhav

**Whom to Contact**: Vaibhav (if need to reassign work)

---

### **Blocker 1C: Metrics Trending Worse**

**When**: Apr 17-19, if precision drops or latency increases

**Impact**: 🟡 MEDIUM — Architecture decision needed

**Resolution Steps**:
1. Ask Uday: "What's causing this degradation?"
2. Options:
   - A) Tuning issue (tweakable)
   - B) Design issue (needs rethinking)
   - C) Data issue (data quality problem)
3. Pick solution path with Uday
4. If unable to improve: Escalate to Vaibhav (accept limitation vs pivot)

**Whom to Contact**: Vaibhav (if architectural decision needed)

---

## Blocker Category 2: Technical Issues (Common on Day 0-2)

### **Blocker 2A: PostgreSQL Installation Fails**

**When**: April 12, morning

**Impact**: 🔴 CRITICAL — All data persistence blocked

**Resolution Steps**:
1. Get error message from Backend1 (full stack trace)
2. Common errors:
   - GCC compiler missing? → Ask HPC admin to `sudo apt-get install build-essential`
   - Dependencies missing? → Install: `libreadline-dev libz-dev`
   - Port 5432 in use? → Kill old process or use port 5433
3. If backend can't troubleshoot → You contact HPC admin
4. If still failing after 2 hrs → Switch to Docker PostgreSQL container

**Alternatives**:
- Option A: Use ChromaDB (no PostgreSQL needed) — affects latency but works
- Option B: Use Google Colab + Pinecone (cloud-based)

**Whom to Contact**: Backend1 → HPC lab admin → Vaibhav

---

### **Blocker 2B: Jupyter Not Multi-User Accessible**

**When**: April 12, afternoon

**Impact**: 🟡 MEDIUM — Only one person can access Jupyter at a time

**Resolution Steps**:
1. Backend2 tries: Launch separate Jupyter instance per user on different ports (8888, 8889, 8890, 8891)
2. If firewall blocks ports → Ask HPC admin to whitelist
3. If security policy prohibits → Use Google Colab instead (3 separate Colab instances)

**Whom to Contact**: Backend2 → HPC lab admin → Vaibhav

---

### **Blocker 2C: API Rate Limits Hit**

**When**: Any day, mid-bootcamp

**Impact**: 🟡 MEDIUM — LLM calls fail temporarily

**Resolution Steps**:
1. Check which API hit limit (Groq most likely, 30 req/min)
2. Options:
   - A) Wait 1 minute, retry
   - B) Switch to Google AI Studio (fallback provider)
   - C) Batch requests (LLM calls in groups, not individually)
   - D) Use lower rate (fewer evaluations, sample-based)

**Whom to Contact**: Backend2 (manages API fallback chain)

---

### **Blocker 2D: Latency > 2 Seconds**

**When**: April 18-19

**Impact**: 🟡 MEDIUM — Doesn't meet NFR-04 requirement

**Resolution Steps**:
1. Uday diagnoses: Which step is slow?
   - Embedding: 0.5s?
   - Chunking/retrieval: 1.2s?
   - Reranking: 0.8s?
   - LLM generation: 3s?
2. Options:
   - A) Use batch embedding (CPU faster in batch mode)
   - B) Reduce reranking from top-30 to top-10
   - C) Cache embeddings (pre-compute frequently queried chunks)
   - D) Accept 2.5s as best effort, document trade-off

**Whom to Contact**: Uday (optimization), then Vaibhav (if trade-off acceptance needed)

---

## Blocker Category 3: Data Issues

### **Blocker 3E: Dataset Download Too Slow**

**When**: April 9-11

**Impact**: 🟡 MEDIUM — Delays Day 1 work

**Resolution Steps**:
1. Check: Is Kaggle download still running? (ETA?)
2. If > 24 hrs remaining → Switch to sample dataset (1000 samples instead of 10,000)
3. Continue bootcamp with sample, full dataset loads in background

**Whom to Contact**: Backend2 (dataset manager)

---

### **Blocker 3F: GCC PDF Corrupted**

**When**: April 9-11

**Impact**: 🟡 MEDIUM — Can't use Government of India contract

**Resolution Steps**:
1. Try download from alternate source:
   - IRICEN: https://www.iricen.gov.in/...
   - DFCCIL: https://dfccil.com/...
   - IREPS: https://www.ireps.gov.in/... (primary, most reliable)
2. If all sources fail → Use sample FIDIC clauses instead (bootcamp continues, less realistic)

**Whom to Contact**: Backend2, then Vaibhav (if need to pivot dataset)

---

## Blocker Category 4: Critical Path (Demo-Related)

### **Blocker 4G: Demo Still Not Working on Friday 2 PM**

**When**: April 26, 2 PM (2 hrs before presentation!)

**Impact**: 🔴 CRITICAL — Presentation will fail

**Resolution Steps**:
1. **EMERGENCY MODE**: All hands on deck
2. Uday: Focus on making ANY demo work (even if not perfect)
3. Backend: Ensure APIs respond
4. You: Prepare alternate narrative (what didn't work + why)
5. **Options**:
   - A) Show pre-recorded demo (have backup video from Apr 25)
   - B) Show architecture + metrics (slides), acknowledge demo issue
   - C) Reschedule presentation to Apr 27 (get Vaibhav + MD approval)

**Whom to Contact**: Vaibhav (immediately, 5-10 PM Apr 25)

---

# 📊 DAILY STANDUP EMAIL TEMPLATE

**Send EVERY morning at 9:00 AM to team + Vaibhav**

```
Subject: [Standup] Bootcamp Day X — April YY

Team Status: Chowdappa (Sprint Master) → Uday, Backend1, Backend2

---

## 📍 CURRENT STATUS

**Yesterday (Apr YY-1)**:
✅ Completed: [what was done]
🔴 Blockers: [any issues]
📊 Metrics: [capture latency, precision, accuracy]

TODAY (Apr YY):
📋 Plan: [what will be attacked]
🎯 Exit Criteria: [definition of "done"]
⏰ Checkpoints: 12 PM, 3 PM, 5 PM

---

## 👥 TEAM UPDATES

**Uday (NLP)**:
- Yesterday: [Work done]
- Blocker: [If any]
- Today: [Plan]

**Backend1 (Infrastructure)**:
- Yesterday: [Work done]
- Blocker: [If any]
- Today: [Plan]

**Backend2 (APIs)**:
- Yesterday: [Work done]
- Blocker: [If any]
- Today: [Plan]

---

## 📊 METRICS

| Metric | Yesterday | Today Target |
|--------|-----------|--------------|
| Latency (p95) | X sec | < 2 sec |
| Precision@5 | X | > 0.85 |
| Accuracy | X | Improving |

---

## 🚨 BLOCKERS

[List any blockers, impact, resolution by when]

---

## 🎯 PRIORITY TODAY

1. [Priority 1 — must finish]
2. [Priority 2 — should finish]
3. [Priority 3 — nice-to-have]

---

Chowdappa
Sprint Master | RAG Bootcamp
```

---

# 📞 ESCALATION CHART (WHO TO CONTACT WHEN)

```
YOU HIT BLOCKER
    ↓
Can team + you fix in 4 hrs?
    ↓
[YES] → Fix + document
[NO]  → Escalate to Vaibhav
         • Problem (1-2 lines)
         • Impact (who blocked, how long)
         • Options A/B
         • Recommendation
         ↓
Vaibhav Response (target: 1-4 hrs)
    ↓
[APPROVE FIX] → Continue
[SUGGEST ALT] → Try alternative
[ACCEPT LIMITATION] → Document + proceed
```

---

# 💾 YOUR DOCUMENTATION FOLDER STRUCTURE

```
/aipms-rag-bootcamp/
  ├── daily-logs/
  │   ├── apr4_blockers_email.txt
  │   ├── apr8_hpc_lab_visit.txt
  │   ├── apr12_day0_morning.txt
  │   ├── apr12_day0_afternoon.txt
  │   ├── apr12_day0_evening.txt
  │   ├── apr15_day1_completed.txt
  │   ├── apr16_day2_completed.txt
  │   ├── apr17_day3_completed.txt
  │   ├── apr18_day4_completed.txt
  │   ├── apr19_day5_completed.txt
  │   └── ... (and so on Apr 22-26)
  ├── weekly-summaries/
  │   ├── week1_summary.md
  │   └── week2_summary.md
  ├── metrics-dashboard/
  │   ├── latency_tracking.csv
  │   ├── precision_tracking.csv
  │   └── team_workload.csv
  └── blockers-log/
      └── blockers_resolution_timeline.md
```

---

# ✅ SUCCESS CRITERIA FOR YOUR ROLE

**By April 26, 6 PM, you will have**:

- ✅ Zero blocked dependencies (all escalated on time)
- ✅ All daily standups conducted (10 standups, 10 emails sent)
- ✅ Zero silent failures (all blockers documented)
- ✅ Demo running (rehearsed 3+ times)
- ✅ All [TO FILL] sections team filled (you verified)
- ✅ Vaibhav approves architecture
- ✅ MD approves delivery

**Your grade**: Good team coordination = successful bootcamp = happy Vaibhav 🎯

---

**END OF CHOWDAPPA ROLE GUIDE**
