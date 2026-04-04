# YOUR ACTION PLAN — Bala Chowdappa

## 🎯 WHAT YOU NEED TO DO (Simple Version)

---

## 📅 KEY DATES (Remember These!)

### **BEFORE BOOTCAMP STARTS (By April 10)**
- Get students to confirm YES with MD
- Check GPREC HPC lab (visit yourself, check CPU/storage)
- Download all 3 datasets
- Register free API keys (Groq, Google, HuggingFace)
- Get approval from MD for these

### **DURING BOOTCAMP (April 15 - April 26)**
- **2 WEEKS INTENSIVE** = 10 working days (Mon-Fri only)
- Run experiments, break things, learn from failures
- Track everything in shared log
- Daily 15-min standup at 9 AM

### **AFTER BOOTCAMP (April 26 Friday)**
- Fill the deliverables document (all the [TO FILL] sections)
- Prepare live demo
- Hand over to production team

---

## 📋 YOUR CHECKLIST RIGHT NOW (April 4-10)

### **STEP 1: CONFIRM STUDENTS (By April 7 - Monday)**
☐ Call the 2 backend students  
☐ Ask them: "Will you commit full-time for April 15-26?"  
☐ Ask them: "Have you used PostgreSQL + pgvector before?"  
☐ Get their names + email IDs  
☐ Have them meet MD on Monday to confirm  
☐ **REQUIRED**: Both MUST say YES. No maybes.

**What to tell them if they ask**:
- "2-week project, Mon-Fri only"
- "Infrastructure setup (databases, APIs)"
- "Free to learn, no payment issues"
- "We have full support from Vaibhav"

---

### **STEP 2: VISIT GPREC HPC LAB (By April 8)**
☐ Go to the lab yourself  
☐ Check equipment: **Do they have server/CPU machine?**  
☐ Ask lab admin: "Can we run PostgreSQL + Jupyter for 2 weeks?"  
☐ Check: **Storage available? At least 75 GB?**  
☐ Check: **Internet access fast enough for APIs?** (Free Groq, Google, HuggingFace APIs need good connection)  
☐ Check: **Can 4 people login to same Jupyter Lab server?**  
☐ Get contact info of lab admin (you'll need to ask them for access)

**HPC SPECS TO CHECK (Minimum)**:
- ✓ CPU: At least 4 cores (8+ is better)
- ✓ RAM: At least 16 GB
- ✓ Storage: At least 75 GB free
- ✓ OS: Linux/Ubuntu (best) or Windows with WSL
- ✓ Internet: Can reach outside (Groq, Google, etc.)
- ✓ Access: Can lab students login? How many can login at once?

---

### **STEP 3: DOWNLOAD DATASETS (By April 9)**
You can do this yourself or ask students to help:

☐ **Dataset 1**: Kaggle Enterprise RAG  
   - Go to: https://www.kaggle.com/datasets/rrr3try/enterprise-rag-markdown
   - Make free Kaggle account
   - Download (2 GB, takes 10 mins)
   - Save to: `/data/datasets/kaggle-enterprise-rag/`

☐ **Dataset 2**: Indian Railways GCC 2022  
   - Go to: https://www.ireps.gov.in (pick this one)
   - Search for "GCC 2022" or copy link: https://www.ireps.gov.in/ireps/upload/repository/railway/3482/456083/private/GCC-2022.pdf
   - Download (3 MB, takes 1 min)
   - Save to: `/data/datasets/indian-railways-gcc-2022/`

☐ **Dataset 3**: Synthetic DMRC (internal)  
   - Email Vaibhav or Krishna: "Send us synthetic DMRC dataset"
   - They will give you folder/link
   - Save to: `/data/datasets/synthetic-dmrc/`

---

### **STEP 4: CREATE FREE API KEYS (By April 9)**
Students should do this (or you do it):

☐ **Groq API** (Main one): https://console.groq.com  
   - Gmail login, get API key (takes 2 mins)
   - Save it safely

☐ **Google AI Studio**: https://aistudio.google.com  
   - Google login, get API key (takes 2 mins)

☐ **HuggingFace**: https://huggingface.co  
   - Email signup, create token (takes 3 mins)

☐ **OpenRouter**: https://openrouter.ai  
   - Email signup, get API key (takes 2 mins)

**All these are FREE. No credit card. No cost.**

---

### **STEP 5: GET APPROVAL FROM MD (By April 10)**
Send MD simple message:

```
Hi Madhu Sir,

4 things need your approval to start bootcamp on April 15:

1. ✓ Students [Name1] & [Name2] confirmed for April 15-26
2. ✓ GPREC HPC lab available (I checked it on April 8)
3. ✓ Datasets downloaded (3 ready)
4. ✓ Free APIs registered (no cost, just checked)

Can you confirm yes/no by April 10?

If no = we delay to April 22.

Thanks,
Chowdappa
```

---

## 📚 DOCUMENTS YOU NEED TO FILL (After Bootcamp Starts)

### **DOCUMENT 1: Deliverables File** (Fill during bootcamp, submit April 26)
Location: `docs/MYdeliverables.txt`

What to fill (sections marked [TO FILL]):

🔵 **Section D1** — RAG Architecture diagram  
   - What vector database did you use? (pgvector? ChromaDB?)
   - What LLM embedding model did you pick? (all-MiniLM? bge-large?)
   - Decision: Why did you pick this one?

🔵 **Section D2** — Embedding model comparison  
   - Compare 3 models: all-MiniLM vs bge-large vs nomic-embed
   - UMAP plot (visual)
   - Which one is best for contracts? Why?

🔵 **Section D3** — Chunking strategy comparison  
   - Test 5 ways to chunk: Fixed, Recursive, Semantic, Document-aware, Parent-child
   - Which works best for contracts? For NCRs? For DPRs?

🔵 **Section D4** — Breaking experiments (5 tests)  
   - FE-01: Cross-entity confusion (NCR + contract mixed)
   - FE-02: Wrong contract version (Red vs Yellow Book confusion)
   - FE-03: Long document bias (hard to summarize)
   - FE-04: Adversarial query (ask about Bitcoin, not in corpus)
   - FE-05: Tenant leakage (data privacy test)

🔵 **Section D5** — Hybrid search comparison  
   - Compare speed: Vector-only vs BM25-only vs Hybrid
   - Which is fastest? Which is most accurate?

🔵 **Section D6** — Agentic RAG  
   - Show multi-hop query examples
   - LangGraph flow diagram

🔵 **Section D7** — Evaluation metrics  
   - Precision@5, MRR, NDCG scores
   - Latency measurements
   - Final recommendation: Which retrieval strategy wins?

---

### **DOCUMENT 2: Live Demo Script** (Prepare Week 2)
What Vaibhav will see on April 26:

- Start with problem: "Search 10,000 contract clauses in < 2 seconds"
- Show query: "Find time-bar clauses in FIDIC Red Book"
- Show result: Top 5 relevant clauses + confidence scores
- Show failure case: "Here's what breaks and how we fixed it"
- Show metrics: "We achieved 0.87 precision@5"
- End with: "This will save DMRC 100+ hours of manual search"

---

## 🎓 STUDENT REQUIREMENTS (Specs to Check)

### **Backend Student 1 & 2 Need:**

✓ **Mandatory Skills**:
- PostgreSQL experience (or willing to learn fast)
- Linux command line (basic)
- Python basics (can write simple scripts)
- API integration (REST/JSON)

✓ **Nice-to-have**:
- Docker (not required, but helps)
- Database indexing (pgvector is similar)

✓ **Time commitment**:
- Full-time April 15-26 (2 weeks, Mon-Fri)
- ~8 hours/day in HPC lab

✓ **Deliverables they own**:
- Infrastructure setup (Day 0: Apr 12-13)
- API fallback chain working
- Data pipeline (cleaning, formatting)
- Deployment scripts

---

## 📆 WHAT HAPPENS DURING 2 WEEKS

### **WEEK 1 (Apr 15-19): Build & Break**
- Mon: Embedding comparison, UMAP plots
- Tue: Chunking strategy tests, naive RAG pipeline launch
- Wed: Run 5 breaking experiments, find problems
- Thu: Hybrid search (BM25 + vector), reranking tests
- Fri: First full RAG pipeline working end-to-end

**Your job**: Document findings daily in shared failure log

### **WEEK 2 (Apr 22-26): Polish & Demo**
- Mon-Tue: Multi-hop retrieval, LangGraph agents
- Wed-Thu: RAGAS evaluation, live demo script ready
- Fri: Final demo + hand over deliverables

**Your job**: Ensure all [TO FILL] docs are filled, demo script ready

---

## ✉️ EMAILS YOU NEED TO SEND

### **Email 1: To Students (Today - April 4)**
```
Hi [Name1] & [Name2],

Quick update on bootcamp project:

Dates: April 15-26, 2026 (Mon-Fri only, 2 weeks)
Work: Database setup, API integration, infrastructure
Location: GPREC HPC lab
Commitment: Full-time (8 hrs/day)
Pay: [Check with Madhu Sir]

Need to confirm:
1. Can you commit full-time?
2. Have you used PostgreSQL?
3. Can you meet Madhu Sir on Monday (April 7)?

Reply by April 7 EOD.

Thanks,
Chowdappa
```

### **Email 2: To Vaibhav (April 5)**
```
Hi Vaibhav Sir,

Pre-bootcamp status:

✓ Team structure ready
✓ Blockers identified (students, HPC, datasets)
- Students confirming on Monday
- I'm visiting HPC lab on April 8
- Datasets downloading by April 9
- API keys registered by April 9

Waiting for MD approval by April 10.

If approved, infrastructure spiking = April 12-13.
Bootcamp starts April 15.

Questions: Should we have contingency (Colab) plan ready?

Thanks,
Chowdappa
```

### **Email 3: To Krishna (April 5)**
```
Hi Krishna Sir,

Sharing synthetic DMRC dataset access needed for bootcamp.

Team: Uday (NLP), 2 backend students, Chowdappa (me)
Start date: Targeting April 15
Datasets: Kaggle + GCC 2022 + Synthetic DMRC

Can you send link/access to synthetic DMRC data?

Thanks,
Chowdappa
```

### **Email 4: To MD Madhu Sir (April 10)**
(Send when all prep is done)

```
Hi Madhu Sir,

Bootcamp status - Ready to go!

Completed:
✓ Students [Names] confirmed for April 15-26
✓ GPREC HPC lab checked (resources OK)
✓ Datasets downloaded (3 ready)
✓ Free APIs registered

Need your approval to start infrastructure spike on April 12.

Timeline:
- April 12-13: Backend infrastructure setup
- April 15-26: 2-week bootcamp
- April 26 Friday: Final demo + deliverables

Yes/No?

Chowdappa
```

---

## 📊 AFTER 2 WEEKS - WHAT YOU SUBMIT (April 26)

**TO SUBMIT TO MD/VAIBHAV:**

1. ✅ **Filled Deliverables Document**
   - All [TO FILL] sections completed
   - Diagrams + metrics tables
   - Architecture recommendation

2. ✅ **Live Demo Working**
   - Query: "Find me time-bar clauses"
   - System returns top 5 with confidence scores
   - Shows metrics (speed, accuracy)

3. ✅ **Demo Script (slides + talking points)**
   - Problem statement
   - Solution architecture
   - Results & metrics
   - Limitations & next steps

4. ✅ **Code Repository**
   - GitHub repo with all code
   - README with setup instructions
   - Comments explaining key decisions

5. ✅ **Risk Log & Findings**
   - What broke? Why?
   - How did you fix it?
   - What would you do differently?

---

## 🚀 QUICK SUMMARY (What You Tell People)

**If Madhu Sir asks**: "What do you need?"
```
1. Students to confirm by Monday
2. GPREC HPC access by April 10
3. Your approval to proceed
That's it. We'll handle the rest.
```

**If students ask**: "What's the project?"
```
2-week RAG bootcamp.
Learn how to build smart search (like Google but for contracts).
Infrastructure setup + RAG pipeline + live demo.
Full-time, Mon-Fri, April 15-26.
```

**If Vaibhav asks**: "Are we on track?"
```
Yes. Blockers identified, solutions ready.
Waiting on MD approval by April 10.
If yes → infrastructure April 12-13 → bootcamp April 15.
If any blocker hits during bootcamp, I escalate to you within 4 hours.
```

---

## 💾 FILES TO KEEP READY

- `docs/team.md` — Read this to understand roles + escalation
- `docs/TwoWeekplan.txt` — Read for day-by-day schedule
- `docs/MYdeliverables.txt` — This is what you fill during bootcamp
- `docs/chowdappa_email_to_md.md` — Your status to MD

---

## 🔥 CRITICAL DATES (Pin These!)

| Date | What | Your Action |
|------|------|-------------|
| **Apr 7 (Mon)** | Students meet MD | Confirm YES/NO |
| **Apr 8 (Tue)** | Visit HPC lab | Check CPU/storage/network |
| **Apr 9 (Wed)** | Download datasets | Verify 3 datasets ready |
| **Apr 10 (Thu)** | File ready for MD approval | Send summary, get approval |
| **Apr 12-13 (Fri-Sat)** | Infrastructure spiking | Test PostgreSQL, APIs, Jupyter |
| **Apr 15 (Mon)** | BOOTCAMP STARTS | Day 1: Embeddings |
| **Apr 26 (Fri)** | BOOTCAMP ENDS | Submit deliverables + demo |

---

**BOTTOM LINE:**

- **Start prep**: TODAY (April 4)
- **Confirmation deadline**: April 10
- **Bootcamp dates**: April 15-26
- **What you submit**: Filled docs + working demo + code
- **Who approves**: MD (Madhu), then Vaibhav

**You are the Sprint Coordinator + QA Lead. Your job is to:**
1. Keep team on track
2. Document everything
3. Flag blockers early
4. Make sure demo works

**If something breaks during bootcamp: Escalate to Vaibhav within 4 hours.**

---

That's it. Simple. Clear. You got this! 🙌
