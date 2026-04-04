# 🤝 TEAM COORDINATION GUIDE

**How the 5 Independent Role Files Work Together**

---

## 📖 HOW TO USE THESE 5 ROLE FILES

Each team member has their own individual `.md` file in this folder:

1. **[ROLE_Chowdappa_SprintCoordinator.md](ROLE_Chowdappa_SprintCoordinator.md)** — You if you're Chowdappa
2. **[ROLE_Uday_NLPEngineer.md](ROLE_Uday_NLPEngineer.md)** — You if you're Uday
3. **[ROLE_Backend1_Infrastructure.md](ROLE_Backend1_Infrastructure.md)** — You if you're Backend Student 1
4. **[ROLE_Backend2_APIsDataPipeline.md](ROLE_Backend2_APIsDataPipeline.md)** — You if you're Backend Student 2
5. **[ROLE_Vaibhav_StrategicAdvisor.md](ROLE_Vaibhav_StrategicAdvisor.md)** — You if you're Vaibhav

**READ ONLY YOUR ROLE FILE.** It contains:
- Daily checklist (what to do, in what order)
- Blockers you'll face (how to handle them)
- Who to contact when stuck
- Daily logs to write
- Success criteria for your role

---

## 🔄 HOW THE 5 ROLES DEPEND ON EACH OTHER

### Dependency Map (Timeline Sequence)

```
PHASE 0: PRE-BOOTCAMP (Apr 4-14)
┌─────────────────────────────────────────────────────┐
│                                                       │
│  Chowdappa (Leads)                                   │
│  ├─ Confirm students (Apr 7)                        │
│  ├─ Visit HPC lab (Apr 8)                           │
│  ├─ Get MD approval (Apr 10)                        │
│  └─ Orchestrate Team                                │
│      │                                               │
│      ├─→ Uday (Preps offline work)                  │
│      │   ├─ Creates golden queries                  │
│      │   ├─ Writes chunking code                    │
│      │   └─ Prepares evaluation harness             │
│      │                                               │
│      ├─→ Backend2 (Downloads data)                  │
│      │   ├─ Gets Kaggle data (Apr 9)                │
│      │   ├─ Gets GCC data (Apr 9)                   │
│      │   ├─ Gets DMRC data (Apr 9)                  │
│      │   └─ Creates 4 API keys (Apr 7-9)            │
│      │                                               │
│      ├─→ Backend1 (Preps scripts)                   │
│      │   └─ Writes PostgreSQL setup scripts         │
│      │                                               │
│      └─→ Vaibhav (Advisor)                          │
│          └─ Reviews plan, available for questions   │
│                                                       │
└─────────────────────────────────────────────────────┘

      ↓ (MD approval gates all next steps)

PHASE 1: DAY 0 INFRASTRUCTURE (Apr 12-13)
┌─────────────────────────────────────────────────────┐
│                                                       │
│  Backend1 (Primary Actor)                           │
│  └─ Setup PostgreSQL + pgvector + Jupyter           │
│     (Parallel with →)                               │
│                                                       │
│  Backend2 (Parallel Actor)                          │
│  ├─ Test all 4 APIs                                │
│  └─ Load sample data into DB                       │
│     (Waits for Backend1's DB schema)                │
│                                                       │
│  Uday (Validation)                                  │
│  └─ Validates infrastructure works                  │
│     (First Jupyter test run)                        │
│                                                       │
│  Chowdappa (Monitoring)                             │
│  ├─ 3x daily check-ins (9am, 12pm, 5pm)            │
│  ├─ Reports status to Vaibhav                      │
│  └─ If blocker → Escalates to Vaibhav              │
│                                                       │
│  Vaibhav (Standby)                                  │
│  └─ If critical blocker → Approves contingency     │
│                                                       │
└─────────────────────────────────────────────────────┘

      ↓ (Infrastructure ready by Sunday 6 PM)

PHASE 2: WEEK 1 BOOTCAMP (Apr 15-19)
┌─────────────────────────────────────────────────────┐
│                                                       │
│  Uday (Primary Actor)                               │
│  ├─ Day 1: Embedding comparison                     │
│  ├─ Day 2: Chunking strategies                      │
│  ├─ Day 3: Breaking experiments                     │
│  ├─ Day 4: Hybrid search + reranking                │
│  └─ Day 5: End-to-end RAG v1                        │
│     (Depends on Backend1 DB, Backend2 APIs)         │
│                                                       │
│  Backend1 (Background)                              │
│  └─ Monitor PostgreSQL health 3x daily              │
│     (Supports Uday's data queries)                  │
│                                                       │
│  Backend2 (Background)                              │
│  └─ Monitor APIs 3x daily                           │
│     (Supports Uday's LLM calls)                     │
│                                                       │
│  Chowdappa (Hub)                                    │
│  ├─ Daily standups (9 AM each day)                 │
│  ├─ Mid-day check-ins (12 PM)                       │
│  ├─ Evening exit criteria check (6 PM)              │
│  └─ Report to Vaibhav (weekly)                      │
│                                                       │
│  Vaibhav (Strategic)                                │
│  └─ Weekly review (Thu PM + Fri AM)                 │
│     Acts on escalations only (architectural Q's)   │
│                                                       │
└─────────────────────────────────────────────────────┘

      ↓ (RAG v1 ready Friday, Week 1)

PHASE 3: WEEK 2 BOOTCAMP (Apr 22-26)
┌─────────────────────────────────────────────────────┐
│                                                       │
│  Uday (Primary Actor)                               │
│  ├─ Day 6: Query routing                            │
│  ├─ Day 7: LangGraph agentic RAG                    │
│  ├─ Day 8: RAGAS evaluation                         │
│  ├─ Day 9: Performance hardening                    │
│  └─ Day 10: Demo + presentation                     │
│     (Depends on Backend1 DB, Backend2 APIs)         │
│                                                       │
│  Backend1 + Backend2 (Background monitoring)        │
│  └─ Same as Week 1 (health checks)                 │
│                                                       │
│  Chowdappa (Hub + Demo Master)                      │
│  ├─ Daily standups (9 AM)                          │
│  ├─ Prep demo + rehearsal (Thursday)                │
│  ├─ Run demo script (Friday AM)                     │
│  └─ Present to Vaibhav + MD (Friday AM)             │
│                                                       │
│  Vaibhav (Strategic + Final Approval)               │
│  ├─ Thursday 2 PM: Demo readiness check             │
│  ├─ Friday AM: Observe demo                         │
│  └─ Friday PM: Sign off ✅ or Flag issues ❌        │
│                                                       │
└─────────────────────────────────────────────────────┘
```

---

## 📞 WHO CONTACTS WHOM (Communication Hierarchy)

### Daily Communication

```
DAILY BOTTLENECK (who reports to whom):

Uday → Chowdappa: "Day's work done? Blocker? Need something?"
Backend1 → Chowdappa: "Infrastructure healthy? Any issues?"
Backend2 → Chowdappa: "Data pipeline OK? APIs working?"
Chowdappa → Vaibhav: "Day summary + decisions needed?"

If urgency/blocker:
Team Member → Chowdappa (within 1 hour)
Chowdappa → Vaibhav (if can't fix in 4 hours)
```

### Emergency Communication (Unblock Fast)

```
IF SOMEONE BLOCKED:
1. Try to fix yourself (check your role file)
2. If can't fix in 30 mins → Contact Chowdappa directly (call, not email)
3. Chowdappa determines if need Vaibhav
4. Vaibhav responds within SLA (see ROLE_Vaibhav_StrategicAdvisor.md)
```

### Weekly Strategic Communication

```
Every Thursday 4 PM (optional call):
Chowdappa + Uday + Vaibhav call (15 mins)
Topics: Architecture questions, mid-week course corrections, blockers

Every Friday 6 PM (email summary):
Chowdappa sends week summary to Vaibhav + team
Topics: Metrics, what went well, what broke + fixed, next week plan
```

---

## 🎯 DAILY STANDUP SCHEDULE

### Same Time Every Day (9:00 AM Sharp)

**Attendees**: All 5 team members (15 mins)

**Format** (from [ROLE_Chowdappa_SprintCoordinator.md](ROLE_Chowdappa_SprintCoordinator.md#-daily-standup-email-template)):

```
Subject: [Standup] Bootcamp Day X — April YY

Team Status: Chowdappa (Sprint Master) → Uday, Backend1, Backend2

## Current Status
Yesterday's work + blockers + metrics

## Today's Plan
What will be attacked today

## Team Updates
Each person: What done | Blocker | Today's plan

## Metrics
Latency | Precision | Other KPIs

## Blockers
Any blocking work? Impact? Resolution?

## Priorities
Top 3 must-dos for today
```

**After Standup** (same 9 AM meeting):
- Chowdappa assigns tasks if any re-prioritization
- If any blocker → Flag for escalation

---

## 🚨 BLOCKER ESCALATION PROTOCOL

### When Blocker Hits (Examples)

**Scenario 1: PostgreSQL Won't Start**

```
Timeline:
- 9:30 AM: Backend1 discovers error
- 9:31 AM: Backend1 tries 3 quick fixes (30 mins)
- 10:00 AM: Still broken → Contacts Chowdappa (call, not email)
- 10:05 AM: Chowdappa + Backend1 brainstorm (30 mins)
- 10:30 AM: If still broken → Chowdappa escalates to Vaibhav
- 10:35 AM: Vaibhav decision: "Use ChromaDB as fallback" or "Fix method X" or "Accept limitation"
- 10:40 AM: Team pivots + continues
```

**Escalation SLA**:
- Blocker hits → You try fix (4 hours max)
- If can't fix → Escalate to Chowdappa (async OK, but urgent if blocking multiple people)
- If Chowdappa stuck → Escalate to Vaibhav (call preferred, 1-hour response target)

---

## 📊 SHARED METRICS DASHBOARD

**Everyone has READ access to**:
- `/metrics-dashboard/latency_tracking.csv` (filled by Uday daily)
- `/metrics-dashboard/team_workload.csv` (filled by Chowdappa)
- `/metrics-dashboard/api_health.csv` (filled by Backend2 daily)

**Format** (CSV, anyone can check):

```
latency_tracking.csv:
Date,Task,Latency_ms,Precision_at5,Notes
2026-04-15,Embedding_Comparison,50,0.72,Model1 selected
2026-04-16,Chunking_Strategy,30,0.78,Fixed-512 best
2026-04-17,Breaking_Exp,200,0.85,All 5 passed
2026-04-18,Hybrid_Search,100,0.89,RRF working
2026-04-19,RAG_E2E,950,0.92,Week1 done!

api_health.csv:
Date,API,Status,Response_Time_ms,Errors,Notes
2026-04-12,Groq,OK,50,0,All green
2026-04-12,Google,OK,100,0,All green
2026-04-12,HF,OK,150,0,All green
2026-04-12,OpenRouter,OK,200,0,Backup only
```

---

## 📁 SHARED FOLDER STRUCTURE

**Everyone has access to this structure** (in `/aipms-rag-bootcamp/`):

```
├── docs/
│   ├── MASTER_BOOTCAMP_PLAYBOOK.md (master reference)
│   ├── ROLE_Chowdappa_SprintCoordinator.md
│   ├── ROLE_Uday_NLPEngineer.md
│   ├── ROLE_Backend1_Infrastructure.md
│   ├── ROLE_Backend2_APIsDataPipeline.md
│   ├── ROLE_Vaibhav_StrategicAdvisor.md
│   ├── TEAM_COORDINATION_GUIDE.md (this file)
│   ├── data_download_roadmap.txt
│   ├── api_rate_limits.txt
│   └── api_keys_setup.txt (SECURE - .gitignore!)
│
├── daily-logs/ (everyone writes here)
│   ├── apr15_day1_embedding_decision.txt (by Uday)
│   ├── apr15_infrastructure_monitor.txt (by Backend1)
│   ├── apr15_data_api_monitor.txt (by Backend2)
│   └── (one per day per person)
│
├── weekly-summaries/ (updated Friday EOD)
│   ├── week1_summary.md
│   └── week2_summary.md
│
├── metrics-dashboard/ (updated daily)
│   ├── latency_tracking.csv
│   ├── precision_tracking.csv
│   ├── api_health.csv
│   └── team_workload.csv
│
├── blockers-log/ (Chowdappa maintains)
│   ├── blockers_resolution_timeline.md (all blockers logged here)
│   └── decision_log.md (all escalations + decisions)
│
├── scripts/
│   ├── install_postgresql.sh (Backend1)
│   ├── load_kaggle_data.py (Backend2)
│   ├── test_apis.py (Backend2)
│   ├── evaluate_rag.py (Uday)
│   └── health_check.sh (Backend1)
│
├── notebooks/
│   ├── golden_queries_v1.json (Uday)
│   ├── chunking_strategies/ (Uday)
│   ├── day1_embedding_comparison.ipynb (Uday)
│   ├── day5_rag_e2e_v1.ipynb (Uday)
│   └── demo_rag_v1.ipynb (Uday → Chowdappa presents)
│
├── data/
│   └── datasets/
│       ├── kaggle-enterprise-rag/ (Backend2)
│       ├── indian-railways-gcc-2022/ (Backend2)
│       └── synthetic-dmrc/ (Backend2)
│
├── backups/ (Backend1)
│   ├── bootcamp_rag_20260413_*.sql
│   └── bootcamp_rag_20260426_*.sql
│
└── deliverables/ (final output, Friday Apr 26)
    ├── MYdeliverables_filled.txt
    ├── code_repository.zip
    ├── live_demo_recording.mp4
    ├── presentation_slides.pdf
    ├── metrics_report.md
    └── risk_log.md
```

---

## ✅ WEEKLY SIGN-OFF CHECKLIST

### Every Friday EOD (Person → Role)

**Uday signs off**:
- [ ] Day's work complete + documented
- [ ] Daily log written (`/daily-logs/apr##_day#_completed.txt`)
- [ ] Metrics updated (`/metrics-dashboard/latency_tracking.csv`)
- [ ] Any blockers escalated (or fixed)

**Backend1 signs off**:
- [ ] Daily health check complete
- [ ] No infrastructure surprises
- [ ] Daily log written
- [ ] Backup complete

**Backend2 signs off**:
- [ ] API monitoring complete
- [ ] Data pipeline healthy
- [ ] Daily log written
- [ ] Rate limits documented

**Chowdappa signs off**:
- [ ] All 3 standups conducted + logged
- [ ] All blockers tracked/escalated
- [ ] Weekly summary written (`/weekly-summaries/week#_summary.md`)
- [ ] Team sign-offs received from all 3
- [ ] Metrics dashboard updated
- [ ] Email to Vaibhav sent (status + decisions needed)

**Vaibhav signs off**:
- [ ] Weekly review completed
- [ ] Any escalations resolved + documented
- [ ] Team feedback given (what to improve)
- [ ] Ready for next week (or final demo Friday)

---

## 🎤 DEPENDENCIES YOU MUST KNOW

### Critical Dependency #1: Backend1 → Uday

**Uday can't start coding until Backend1 provides**:
- ✅ PostgreSQL running on GPREC HPC
- ✅ Jupyter accessible on port 8888-8891
- ✅ pgvector extension loaded
- ✅ Sample test table created

**If Backend1 blocked**: Uday waits (can do offline prep, but no live coding)

### Critical Dependency #2: Backend2 → Uday

**Uday can't test on real data until Backend2 provides**:
- ✅ Kaggle data downloaded + accessible
- ✅ GCC data downloaded + accessible
- ✅ DMRC data downloaded + accessible
- ✅ All 4 API keys created + tested

**If Backend2 blocked**: Uday uses sample data (pre-computed locally)

### Critical Dependency #3: Backend1 → Backend2

**Backend2 can't load data until Backend1 provides**:
- ✅ PostgreSQL running + accepting connections
- ✅ Database schema created (columns, types)

**If Backend1 blocked**: Backend2 waits

### Critical Dependency #4: Chowdappa → All

**Everyone reports to Chowdappa daily**:
- Chowdappa aggregates status
- Identifies blockers
- Escalates if needed

**If Chowdappa doesn't get daily update**: Vaibhav has no visibility (bad!)

### Critical Dependency #5: Vaibhav → Final Demo

**Vaibhav reviews final deliverables** (Friday):
- Does demo work?
- Are metrics good?
- Is delivery acceptable?

**If Vaibhav says NO**: May delay or reduce scope (rare if weekly reviews done well)

---

## 🎯 SUCCESS = SYNCHRONIZED DEPENDENCIES

**Your team succeeds if**:

```
✅ Backend1 + Backend2 → Infrastructure ready by Sunday 6 PM
   ↓
✅ Uday → Uses infrastructure to build RAG all Week 1
   ↓
✅ Chowdappa → Tracks daily, escalates blockers, keeps team aligned
   ↓
✅ Vaibhav → Reviews weekly, makes architectural decisions fast
   ↓
✅ All → Friday demo works + Vaibhav signs off + MD approves
```

**Your team fails if**:

```
❌ Backend1 delayed → Uday can't code → Week 1 lost
OR
❌ Backend2 delayed → No data → Uday trains on nothing → Week 1 lost
OR
❌ Chowdappa not syncing → Blockers accumulate silent → Surprise failure Friday
OR
❌ Vaibhav unavailable → Architectural Qs stuck → Days lost on wrong path
OR
❌ Anyone not reporting daily → Team doesn't know what's broken
```

---

## 📞 QUICK REFERENCE: WHO TO CONTACT

| Problem | Contact | Response Time |
|---------|---------|----------------|
| "I don't have my role file" | Chowdappa | Immediate (share file) |
| "I need to understand dependencies" | Read this file + your role file | N/A |
| "PostgreSQL won't start" | Backend1 (self), then Chowdappa (if stuck >30m) | 5-30 mins |
| "API key not working" | Backend2 (self), then Chowdappa | 5-30 mins |
| "Precision only 60%" | Uday + Chowdappa, escalate to Vaibhav if unfixable | 2-4 hours |
| "Behind schedule, what should we cut?" | Vaibhav (decision authority) | 1-2 hours |
| "Demo broken Friday morning" | Chowdappa + Uday emergency, Vaibhav if critical | 30 mins - 2 hours |
| "What if PostgreSQL fails?" | See ROLE_Backend1 blocker #1 → use contingency | Planned: 4 hours to Colab switch |

---

## 🏁 FINAL SUCCESS CRITERIA (April 26, 6 PM)

**Everyone succeeded if**:

- ✅ **Chowdappa**: Team coordinated, all daily standups done, zero missed blockers
- ✅ **Uday**: RAG pipeline built, metrics > targets (precision 85%, latency <2s), demo rehearsed 3+ times
- ✅ **Backend1**: PostgreSQL stable 99%+ uptime, no data loss, indexes optimized
- ✅ **Backend2**: All datasets loaded, all 4 APIs working, zero rate-limit surprises
- ✅ **Vaibhav**: All escalations decided on time, team confident in deliverables, MD approved

**Project delivered**:
- ✅ Live demo working (demo script runs start-to-finish without errors)
- ✅ Code clean + documented (GitHub ready)
- ✅ Metrics documented (latency, precision, accuracy captured)
- ✅ Risks logged (what worked, what broke, how fixed, what to improve)
- ✅ MD approves ✅

---

**END OF TEAM COORDINATION GUIDE**
