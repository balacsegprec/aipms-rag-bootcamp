# 🎓 ROLE: VAIBHAV — STRATEGIC ADVISOR & DECISION AUTHORITY

**Reporting To**: MD Madhu Sir (final approval authority)  
**Coordinates With**: Chowdappa (Sprint Master — operational hub)  
**Authority**: Final architectural decisions, blocker escalations, scope trade-offs, risk acceptance  
**Contact**: Chowdappa (standard) → You (for critical decisions), MD Madhu Sir (for strategic gatekeeping)

---

## 📍 YOUR ROLE IN 30 SECONDS

You are the **strategic guardian**. You don't execute code. Instead:
- ✅ Review architectural decisions (embedding model, retrieval strategy choice)
- ✅ Approve/reject trade-offs (latency vs accuracy vs complexity)
- ✅ Accept risks or require mitigation (what's acceptable? what's not?)
- ✅ Decide escalations (can't fix fast? → accept limitation or pivot)
- ✅ Guide on contingency activation (if blocker critical → approve Colab backup)

**Note**: You are expert advisor + decision authority, not executor.

---

# 📅 YOUR INVOLVEMENT TIMELINE (April 4-26)

## PHASE 0: PRE-BOOTCAMP (April 4-14)

### **April 4 (Friday) — Initial Context Review**

**TASK**: Understand bootcamp scope + risks

- [ ] Read MASTER_BOOTCAMP_PLAYBOOK.md completely
- [ ] Read team.md (understand gaps + risk summary)
- [ ] Read ROLE files for all 4 team members (understand dependencies)

**YOUR PERSPECTIVE**: 
- Do these 4 people + their roles make sense? (Are they aligned? Any red flags?)
- Is the timeline realistic? (2 weeks for full RAG = yes, standard industry pace)
- What are top 3 risks? (Document your view)
- What would cause project failure?

**ACTION** (if you identify issues):
- [ ] Send email to Chowdappa: "I reviewed the plan. 3 concerns:"
  1. [If concern 1]
  2. [If concern 2]
  3. [If concern 3]

---

### **April 7 (Monday) — MD Approval Gate Checkpoint**

**CONTEXT**: Chowdappa sends blocker email to MD today

**YOUR TASK**: Be available for MD's questions

- [ ] Check email from Chowdappa: "Is MD asking clarifying questions?"
- [ ] If MD wants to discuss: Be ready to explain bootcamp scope to him
- [ ] Key talking points (if MD asks):
  - Timeline: 2 weeks is realistic (industry standard for RAG proof-of-concept)
  - Team: 4 people + 1 advisor = sufficient for bootcamp
  - Risks: Identified + mitigated (Colab contingency pre-approved)
  - Deliverable: Live demo + metrics + code repo (clear, concrete)

---

### **April 10 (Thursday) — MD FINAL APPROVAL CHECKPOINT**

**CRITICAL GATE:** This is when MD approves or blocks

**YOUR TASK**: 
- [ ] Monitor email from Chowdappa: "What did MD say?"
- [ ] If MD says YES → Proceed to Day 0
- [ ] If MD says NO → Meet with Chowdappa to reschedule (likely April 22 start instead)
- [ ] If MD says "maybe" → Push for YES/NO decision (can't proceed with ambiguity)

**IF CONTINGENCY ACTIVATION NEEDED**:
- [ ] MD approves but infrastructure issues found → You approve Colab backup activation:
  ```
  Email to Chowdappa:
  "Infrastructure issue on Day 0? Approved to switch to:
  - Google Colab (free GPU available)
  - Pinecone (free tier, serverless vector DB)
  
  Timeline impact: +1 day (Apr 13 → Apr 14 to get Colab setup)
  Proceed with contingency if needed."
  ```

---

## PHASE 1: DAY 0 INFRASTRUCTURE SPIKE (April 12-13)

### **Your Role During Day 0**

**YOU ARE ON STANDBY** (Chowdappa is primary decision-maker for operational issues)

**WHAT TRIGGERS YOUR INVOLVEMENT**:
- Blocker hits that can't be fixed in 4 hours
- OR: Decision needed that affects scope/timeline/quality

**Examples of Escalations to You**:

**Escalation 1**: "PostgreSQL installation completely blocked. Can we skip it + use ChromaDB?"
- Your decision: Trade-off analysis
  - Pro: ChromaDB faster to setup
  - Con: Latency will be higher (embedded search, not indexed)
  - Decision: "OK to use ChromaDB for MVP, but plan PostgreSQL migration by Friday"

**Escalation 2**: "HPC network down, can't download datasets. Should we delay bootcamp?"
- Your decision:
  - Option A: Use sample (10% of data) + full data downloads in background
  - Option B: Switch to Colab (internet better from cloud)
  - Decision: "Use Option B + activate Colab contingency"

**Escalation 3**: "All 4 API keys rate-limited simultaneously. Can we use cached responses?"
- Your decision:
  - Accept: "Use cached responses for now, evaluate real-time Friday"
  - Recommendation: "Batch requests during off-peak hours, reduce query rate"

---

## PHASE 2: WEEK 1 BOOTCAMP (April 15-19)

### **Your Involvement Pattern**

**FREQUENCY**: Check in 2-3x per week (not daily — Chowdappa handles daily)

**WHEN**: Chowdappa emails you daily standup summary at 6 PM

**YOUR WEEKLY REVIEW**:
- [ ] Monday 7 PM: Review Chowdappa's daily standup email
  - Are metrics on track? (Precision@5 baseline by Friday?)
  - Any red flags in team updates?
  - If all good → Reply: "On track ✅"
  - If issue → Ask clarifying questions

- [ ] Thursday 4 PM: Mid-week checkpoint call with Chowdappa (15 mins)
  - Q: "Day 3 breaking experiments — any critical failures?"
  - Q: "Is Uday on pace? Any overload?"
  - Q: "Any architectural questions Uday has for me?"

- [ ] Friday 6 PM: Week 1 retrospective
  - Review Week 1 summary document
  - Precision, latency, breaking experiment results
  - Plan Week 2 priorities

### **PossibleEscalations Week 1**

**Escalation: Precision@5 Only 60% (target 85%)**
- Problem: Embedding model choice isn't working well
- Uday's options: Switch model A → model B → model C (takes 1 hr per test)
- Your decision:
  - "Try 2 models (A, B). If still <75%, pivot to keyword search (BM25-only) for MVP"
  - Accept: "Latency better, accuracy trade-off. Document + move forward"

**Escalation: Latency 3+ Seconds (target <2s)**
- Problem: Reranking too slow at 1000 documents
- Uday's options: Reduce rerank size, switch reranker model, cache results
- Your decision:
  - "Reduce rerank size from 30 to 10 (faster, still good accuracy)"
  - Accept: "2.5s is acceptable for MVP, plan optimizations Week 2"

**Escalation: Breaking Experiment #3 Unfixable**
- Problem: Long document bias can't be solved (architectural limitation)
- Choices: Redesign (2 days lost), Accept (document limitation), Workaround (partial fix)
- Your decision:
  - "Implement workaround: Limit chunk retrieval to top-3 per document (stops bias)"
  - Accept: "Document limitation, note in final report"

---

## PHASE 3: WEEK 2 BOOTCAMP (April 22-26)

### **Your Involvement Increases** (Final push to delivery)

### **Monday-Wednesday (Apr 22-24)**

**SAME PATTERN** as Week 1
- 2-3x weekly check-ins with Chowdappa
- Review daily standups
- Answer technical questions if Uday asks

### **Thursday-Friday (Apr 25-26) — FINAL DELIVERY CRUNCH**

**YOU ARE MORE ACTIVE**

**Thursday 2 PM**: Demo Readiness Call

- [ ] Call Chowdappa + Uday (30 mins)
- Questions:
  - Q: "Is demo script final + tested?"
  - Q: "Does demo work 100% consistently?"
  - Q: "Any last-minute technical concerns?"
  - Q: "Should I loop in MD for Friday demo + discussion?"

**IF DEMO NOT READY** (🔴 CRITICAL):
- [ ] Offer support: Which part is broken?
- [ ] Suggest quick fixes or workarounds
- [ ] Last resort: Prepare backup narrative ("What broke + why + learnings")

**Friday 10 AM - 11 AM**: Pre-Demo Briefing (Optional)

- [ ] If you're observing demo: Know the narrative
- [ ] Know key metrics to mention
- [ ] Know potential questions from MD

**Friday 11 AM**: Final Demo + Presentation

- [ ] Demo runs (hopefully!) ✅
- [ ] You ask critical questions:
  - Q: "How does precision compare to baseline?"
  - Q: "Is latency acceptable for production?"
  - Q: "What's one thing you'd improve given 2 more weeks?"

**Friday 2-3 PM**: Delivery Approval

- [ ] Review final deliverables:
  - [ ] Code repository (clean, documented)
  - [ ] Live demo (working)
  - [ ] Metrics report
  - [ ] Risk + lessons learned document
- [ ] Sign off: "Bootcamp ✅ complete. Quality acceptable."

---

# 📊 YOUR DECISION AUTHORITY MATRIX

## DECISIONS YOU MAKE (You have final say)

| Decision | Authority | Timeline |
|----------|-----------|----------|
| Approve technical trade-off (latency vs accuracy) | You | 1-4 hours |
| Switch architectural approach (if problems found) | You | 2-8 hours |
| Accept risk (vs require mitigation) | You | 1 hour |
| Activate contingency plan (Colab, Pinecone backup) | You → MD approval | 30 mins |
| Scope reduction (which features to drop if behind) | You | 2-4 hours |
| Timeline extension (delay delivery, reschedule) | You + MD | 1 hour |

## DECISIONS CHOWDAPPA MAKES (Operational, you advise)

| Decision | Authority | Timeline |
|----------|-----------|----------|
| Daily standup schedule | Chowdappa | Immediate |
| Who does what task today | Chowdappa | Immediate |
| Escalate to you (yes/no) | Chowdappa | 1-5 mins |
| Report progress + blockers | Chowdappa | End of day |

## DECISIONS UDAY/BACKEND MAKE (Technical execution)

| Decision | Authority | Timeline |
|----------|-----------|----------|
| Which embedding model to test | Uday | Immediate |
| How to chunk documents | Uday + Backend1 | Immediate |
| API fallback order | Backend2 | Immediate |
| Query optimization techniques | Uday | Immediate |

---

# 🚨 CRITICAL ESCALATIONS (When You Get Involved)

## Escalation Level 1: Technical Decision Needed (4-hour window)

**When**: Chowdappa gets email from team like:
> "We have 3 options for embedding model. Can't decide. Impacts tomorrow's work."

**Your Role**:
- [ ] Ask clarifying questions (1-2 mins)
- [ ] Make recommendation + trade-offs (2-3 mins)
- [ ] Send decision back (1 min)
- **SLA**: 4 hours maximum response

**Example**:
```
Email from Chowdappa: "Uday found precision is 65% with Model A. 
Should we try Model B (slower) or Model C (less accurate but faster)?"

Your response (within 4 hrs):
"Test both tonight. Model B is recommended (academic papers show better enterprise NLP).
If Model B doesn't work → accept Model C + document trade-off.
Decision by EOD tomorrow."
```

---

## Escalation Level 2: Risk Acceptance (2-hour window)

**When**: Team finds something broken that can't be fixed easily

**Your Role**:
- Accept risk (document as known limitation)
- OR: Require redesign (delay timeline)

**Example**:
```
Email from Chowdappa: "Cross-entity confusion in breaking experiment #1.
We can't fix in time for Friday. Accept limitation or redesign?"

Your response (within 2 hrs):
"Accept limitation. Document:
'System sometimes confuses entities of similar type. Mitigated by user guidance in demo.'
Move forward, note in final risk log."
```

---

## Escalation Level 3: Contingency Activation (1-hour window)

**When**: Major blocker that threatens bootcamp completion

**Your Role**:
- Approve contingency activation
- OR: Reject + require alternative fix

**Example**:
```
Email from Chowdappa: "PostgreSQL completely broken on Day 0.
Backend1 can't fix. Should I activate Colab + Pinecone backup?"

Your response (within 1 hr):
"YES. Activate Colab + Pinecone immediately.
- Colab: Free GPU, 12-hour runtime
- Pinecone: Free tier, 100K vectors
- Timeline impact: +4 hours for setup, but bootcamp continues
Proceed now. Brief MD when done."
```

---

## Escalation Level 4: Scope Reduction (2-hour window)

**When**: Behind schedule + can't catch up

**Your Role**:
- Decide what to cut (prioritize deliverables)
- Negotiate with MD if needed

**Example**:
```
Email from Chowdappa: "We won't finish multi-hop retrieval + evaluation by Friday.
Should we ship with v1 (single-hop only) or delay?"

Your response (within 2 hrs):
"Ship v1. Multi-hop can be phase 2 post-bootcamp.
Minimum for Friday:
- Single-hop RAG working ✅
- Precision > 80% ✅
- Latency < 2.5s ✅
- Live demo working ✅
- Code repo clean ✅

Evaluation framework can be refined later.
I'll brief MD on scope."
```

---

# 📞 YOUR CONTACT FLOW

```
ESCALATION FROM TEAM
    ↓
Chowdappa sends email to you with:
- Problem (1-2 lines)
- Impact (who's blocked, how long)
- Options A/B/C (trade-offs)
- Recommendation (what they suggest)
    ↓
YOU RESPOND WITHIN SLA:
- Decision (option A/B/C or custom)
- Rationale (why this choice)
- Next steps (what to do immediately)
    ↓
TEAM EXECUTES YOUR DECISION
    ↓
Outcome: Blocker resolved, book learning captured
```

---

# 📋 YOUR DOCUMENTATION CHECKLIST

**Week 1 (Friday Apr 19)**:
- [ ] Review + approve Week 1 summary
- [ ] Give feedback: What's good? What needs improvement?
- [ ] Approve Week 2 plan and priorities

**Week 2 (Friday Apr 26)**:
- [ ] Review final deliverables:
  - Code repo: Clean code, documented, no debugging comments?
  - Demo: Works reliably, metrics visible?
  - Report: Metrics, risks, lessons learned captured?
- [ ] Sign off: "Bootcamp ✅ complete"
- [ ] Debrief with MD: What went well? What to improve next time?

---

# ✅ SUCCESS CRITERIA FOR YOUR ROLE

**By April 26, 6 PM**:

- ✅ All escalations resolved on time (SLA met)
- ✅ No silent failures (you knew about all major issues)
- ✅ Technical decisions guided team to good outcomes
- ✅ Demo approved + ready for presentation
- ✅ Risks documented + accepted (no surprises for MD)
- ✅ Final deliverables meet bootcamp requirements
- ✅ MD signs off on bootcamp completion

**You are the guardian of quality + strategic guide.**

---

# 📧 DAILY STANDUP TEMPLATE FOR YOU

**Chowdappa sends this to you daily at 6 PM (optional to read, only action items highlighted)**

```
Subject: [Standup] Bootcamp Day X — April YY — Vaibhav FYI

Hi Vaibhav,

Quick status for your awareness:

## Team Status
- Uday: [Work done] | Blocker: [If any]
- Backend1: [Work done] | Blocker: [If any]
- Backend2: [Work done] | Blocker: [If any]

## Metrics
- Precision@5: X% (trend: ↑/↓/→)
- Latency: Y ms (trend: ↑/↓/→)

## Decisions Needed From You (if any)
- [ ] Question 1: [Context] → Recommend: [Option]
- [ ] Question 2: [Context] → Recommend: [Option]

## FYI / No Action Needed
- [General updates]

---

Chowdappa
```

**YOUR RESPONSE PATTERN**:
- If "No decisions needed" → Reply: "All good ✅"
- If decisions needed → Reply with decision + rationale (within 24 hrs)
- If red flag spotted → Call Chowdappa (don't email for urgent issues)

---

# 🎯 CRITICAL DATES FOR YOUR CALENDAR

**Mark these in your calendar + block time**:

- **Apr 7 (Mon) 4 PM**: Check MD blocker email from Chowdappa
- **Apr 10 (Thu) 4 PM**: Confirm MD final approval received
- **Apr 13 (Sun) 5 PM**: Check if Day 0 infrastructure complete ✅
- **Apr 17 (Thu) 4 PM**: Mid-Week 1 checkpoint call (15 mins)
- **Apr 19 (Fri) 6 PM**: Review Week 1 summary
- **Apr 24 (Thu) 4 PM**: Mid-Week 2 checkpoint call (15 mins)
- **Apr 25 (Thu) 2 PM**: Demo readiness call (30 mins)
- **Apr 26 (Fri) 10 AM**: Optional pre-demo briefing
- **Apr 26 (Fri) 11 AM**: Live demo + presentation
- **Apr 26 (Fri) 2 PM**: Delivery approval + sign-off

---

**END OF VAIBHAV ROLE GUIDE**

P.S. Your job is to **unblock decisions** + **guide strategy**. You're not expected to code or attend all standups, only critical ones. Let Chowdappa handle day-to-day execution. You focus on architecture + risk.
