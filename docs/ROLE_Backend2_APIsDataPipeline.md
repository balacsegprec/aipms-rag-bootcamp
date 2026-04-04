# 🔗 ROLE: BACKEND2 — APIs & DATA PIPELINE ENGINEER

**Reporting To**: Chowdappa (Sprint Master)  
**Coordinates With**: Backend1 (Infrastructure), Uday (NLP — data consumer)  
**Technical Authority**: Data downloads, API provisioning, data loading pipeline, dataset versioning  
**Contact Emergency**: Chowdappa (within 1 hour), Uday (if pipeline issue blocking)

---

## 📍 YOUR ROLE IN 30 SECONDS

You are the **data gatekeeper**. Your job:
- ✅ Download + stage 3 datasets (Kaggle, GCC, DMRC)
- ✅ Setup + test 4 free API keys (Groq, Google, HF, OpenRouter)
- ✅ Create data loading pipeline (files → PostgreSQL)
- ✅ Manage dataset versions + metadata
- ✅ Monitor API rate limits + fallbacks

**Note**: You don't write ML algorithms. You make data accessible.

---

# 📅 YOUR DAILY CHECKLIST (April 4-26)

## PHASE 0: PRE-BOOTCAMP (April 4-14)

### **April 4 (Friday) — TODAY**

**YOUR TASK**: Understand data requirements

- [ ] Read MASTER_BOOTCAMP_PLAYBOOK.md (sections 1-3, 5)
- [ ] Read ROLE_Uday_NLPEngineer.md (understand what data Uday needs)
- [ ] Read ROLE_Backend1_Infrastructure.md (understand PostgreSQL schema)

**PREP WORK**:
- [ ] Download Kaggle CLI to laptop:
  ```bash
  pip install kaggle
  ```
- [ ] Setup Kaggle credentials:
  - Go to https://www.kaggle.com/settings/account
  - Download API token (json)
  - Save to `~/.kaggle/kaggle.json`
  - Run: `kaggle datasets list` (test authentication)

---

### **April 5 (Saturday)**

**STATUS**: Weekend

- [ ] Prep API keys setup:
  - [ ] Groq account + API key generation (free)
  - [ ] Google AI Studio account + key (free Gemini access)
  - [ ] HuggingFace token (free account)
  - [ ] OpenRouter API account (free tier available)

- [ ] Create `.env` template file (for storing API keys securely):
  ```
  GROQ_API_KEY=xxxxx
  GOOGLE_API_KEY=xxxxx
  HUGGINGFACE_TOKEN=xxxxx
  OPENROUTER_API_KEY=xxxxx
  KAGGLE_USERNAME=xxxxx
  KAGGLE_KEY=xxxxx
  ```

---

### **April 6 (Sunday)**

**STATUS**: Weekend

- [ ] Research dataset sources:
  - [ ] **Kaggle**: Enterprise RAG datasets (download details)
  - [ ] **GCC**: Government of India contracts (PDF links)
  - [ ] **DMRC**: Delhi Metro/Railway datasets (synthetic URLs)

- [ ] Create download roadmap: `/docs/data_download_roadmap.txt`
  ```
  Dataset 1: Kaggle Enterprise RAG
  - URL: https://www.kaggle.com/...
  - Size: ~500 MB
  - Files: Multiple markdown documents
  - Estimated download time: 30 mins (broadband)
  
  Dataset 2: GCC (Government Contracts)
  - URL: https://www.ireps.gov.in/... or DFCCIL
  - Size: ~100 MB
  - Files: PDF contract documents
  - Estimated download time: 15 mins
  
  Dataset 3: DMRC (Synthetic)
  - URL: https://synthetic-dmrc-*
  - Size: ~50 MB
  - Files: YAML policy documents
  - Estimated download time: 10 mins
  
  TOTAL ESTIMATED: 55 mins
  ```

---

### **April 7 (Monday)**

**YOUR TASK**: Start API key provisioning

- [ ] Create Groq account:
  - [ ] Sign up: https://console.groq.com/keys
  - [ ] Create API key
  - [ ] Test: `curl https://api.groq.com/openai/v1/models -H "Authorization: Bearer [KEY]"` (should list models)
  - [ ] Save key securely

- [ ] Create Google API key:
  - [ ] Go to https://aistudio.google.com/app/apikey
  - [ ] Create new API key
  - [ ] Test access to Gemini API
  - [ ] Save key

- [ ] Status update to Chowdappa: "Groq + Google keys created, 2 more to go"

---

### **April 8 (Tuesday)**

**YOUR TASK**: Finish API key provisioning

- [ ] Create HuggingFace token:
  - [ ] Sign up: https://huggingface.co
  - [ ] Generate API token (Settings → API tokens → Create new token)
  - [ ] Save token

- [ ] Create OpenRouter API key:
  - [ ] Sign up: https://openrouter.ai
  - [ ] Create API key
  - [ ] Add payment method (optional, free tier available)
  - [ ] Save key

- [ ] Document: `/docs/api_keys_setup.txt`
  ```
  ✅ Groq API Key: [Date created]
  ✅ Google API Key: [Date created]  
  ✅ HuggingFace Token: [Date created]
  ✅ OpenRouter API Key: [Date created]
  
  All 4 keys provisioned and tested.
  Ready to load into environment variables.
  ```

- [ ] Status to Chowdappa: "All 4 API keys created ✅"

---

### **April 9 (Wednesday) — CRITICAL DATA DOWNLOAD DAY**

**YOUR MAIN TASK**: Download all 3 datasets to HPC

**NOTE**: This might be slow (depends on internet speed). Start early. If not done by 6 PM, OK — can continue into evening.

**MORNING (9 AM - 12 PM)**

**Step 1: Verify HPC Disk Space**
- [ ] SSH into HPC
  ```bash
  df -h | grep /home
  # Need: 75 GB free (target: have 75GB minimum)
  ```
- [ ] Create data directory structure on HPC:
  ```bash
  mkdir -p /data/datasets/kaggle-enterprise-rag
  mkdir -p /data/datasets/indian-railways-gcc-2022
  mkdir -p /data/datasets/synthetic-dmrc
  ```

**Step 2: Download Kaggle Dataset**
- [ ] On HPC, configure Kaggle credentials:
  - [ ] Copy Kaggle API token from local machine to HPC
  - [ ] Place at `~/.kaggle/kaggle.json` on HPC
  ```bash
  kaggle datasets download -d [dataset-id] -p /data/datasets/kaggle-enterprise-rag --unzip
  ```
- [ ] Monitor download progress (might take 10-30 mins depending on speed)
- [ ] Verify: `ls -la /data/datasets/kaggle-enterprise-rag/` (should see markdown files)
- [ ] Status: Log download time + file count

**AFTERNOON (1 PM - 4 PM)**

**Step 3: Download GCC Dataset**
- [ ] Download from IREPS (Indian Railway eProcurement System) or alternate:
  ```bash
  cd /data/datasets/indian-railways-gcc-2022
  # Option A: Direct link (if available)
  wget https://www.ireps.gov.in/... -O gcc_contracts.pdf
  
  # Option B: Manual download from web
  # (If download not possible, use fallback PDF from Git)
  ```
- [ ] If download fails → Fallback: Use sample GCC PDF from GitHub/IRICEN
- [ ] Verify: `ls -la /data/datasets/indian-railways-gcc-2022/` (should see PDF(s))

**Step 4: Download DMRC Dataset**
- [ ] Download synthetic DMRC data:
  ```bash
  cd /data/datasets/synthetic-dmrc
  git clone https://github.com/... dmrc-synthetic  # if available
  # OR
  wget https://synthetic-dmrc-dataset... -O dmrc_data.zip
  unzip dmrc_data.zip
  ```
- [ ] Verify: `ls -la /data/datasets/synthetic-dmrc/` (should see YAML/JSON files)

**LATE AFTERNOON/EVENING (4 PM - 7 PM)**

**Step 5: Verify All Datasets**
- [ ] Count files + check sizes:
  ```bash
  echo "Kaggle files:" && ls /data/datasets/kaggle-enterprise-rag/ | wc -l
  echo "GCC files:" && ls /data/datasets/indian-railways-gcc-2022/ | wc -l
  echo "DMRC files:" && ls /data/datasets/synthetic-dmrc/ | wc -l
  echo "Total disk used:"
  du -sh /data/datasets/
  ```

- [ ] Spot-check validity:
  - Kaggle: Can you open a .md file? (should be readable text)
  - GCC: Is PDF readable? (try: `file gcc_contracts.pdf`)
  - DMRC: Are files valid YAML? (try: `python -c "import yaml; yaml.safe_load(open('sample.yaml'))"`)

- [ ] Document: `/daily-logs/apr9_data_download_verification.txt`
  ```
  Kaggle Enterprise RAG: ✅ [X files, Y GB size]
  GCC Contracts: ✅ [X files, Y GB size]
  DMRC Synthetic: ✅ [X files, Y GB size]
  
  Total dataset size: Z GB
  Download time: A hours
  Status: Ready for bootcamp
  ```

- [ ] Status to Chowdappa: "All 3 datasets downloaded ✅ + verified"

---

### **April 10 (Thursday)**

**YOUR TASK**: Wait for MD approval + finalize environment setup

- [ ] Check with Chowdappa: "Has MD approved bootcamp start?"
- [ ] If YES: Prepare Day 0
- [ ] If NO: Wait

**PREP FOR DAY 0**:
- [ ] Create `.env` file for HPC (with all 4 API keys + data paths):
  ```
  GROQ_API_KEY=xxxxx
  GOOGLE_API_KEY=xxxxx
  HUGGINGFACE_TOKEN=xxxxx
  OPENROUTER_API_KEY=xxxxx
  DATA_PATH=/data/datasets
  ```
- [ ] Upload `.env` to HPC `/home/bootcamp_user/` (secure: `chmod 600 .env`)
- [ ] Create Python test script for API access:
  ```python
  # File: /scripts/test_apis.py
  import os
  from groq import Groq
  from google.generativeai import configure
  
  # Test 1: Groq
  client = Groq(api_key=os.getenv("GROQ_API_KEY"))
  response = client.chat.completions.create(
    model="llama-3.3-70b-specdec",
    messages=[{"role": "user", "content": "Hi"}]
  )
  print("✅ Groq API working")
  
  # Test 2: Google
  configure(api_key=os.getenv("GOOGLE_API_KEY"))
  print("✅ Google API working")
  ```

---

### **April 11 (Friday)**

**YOUR TASK**: Final pre-Day-0 checks

- [ ] Confirm with Chowdappa: "Ready for Day 0 data setup?"
- [ ] Final checklist:
  - [ ] All datasets downloaded?
  - [ ] All API keys created?
  - [ ] Environment variables ready?
  - [ ] Test scripts prepared?

- [ ] Prepare Day 0 task list:
  ```
  Day 0 (Apr 12-13) Data Tasks:
  1. Load sample Kaggle data into PostgreSQL
  2. Test API connectivity (all 4 providers)
  3. Create data loading pipeline (for Days 1-5)
  4. Setup dataset versioning + metadata
  ```

---

## PHASE 1: DAY 0 INFRASTRUCTURE SPIKE (April 12-13)

### **April 12 (Saturday) — INFRASTRUCTURE DAY 1**

**YOU + BACKEND1 ARE ACTORS IN PARALLEL.**

**9:00 AM START** (with Backend1 installing PostgreSQL)

- [ ] While Backend1 installs infrastructure, you test APIs:

**9:15 AM - 11:00 AM**: API Testing

- [ ] SSH into HPC
- [ ] Load `.env` file:
  ```bash
  source /home/bootcamp_user/.env
  ```
- [ ] Run API test script:
  ```bash
  python /scripts/test_apis.py
  ```
- [ ] Check results:
  - [ ] Groq ✅ or ❌?
  - [ ] Google ✅ or ❌?
  - [ ] HuggingFace ✅ or ❌?
  - [ ] OpenRouter ✅ or ❌?

- [ ] If any API fails:
  - [ ] Check: Is API key correct? (print first 10 chars: `echo $GROQ_API_KEY | head -c 10`)
  - [ ] Check: Is internet working from HPC? (try: `curl https://api.groq.com`)
  - [ ] Regenerate API key if needed

- [ ] Status to Chowdappa: "All 4 APIs ✅ working"

**11:00 AM - 12:00 PM**: Data Loading Preparation

- [ ] Wait for Backend1 to create PostgreSQL tables
- [ ] Write data loading script: `/scripts/load_kaggle_data.py`
  ```python
  import os
  import json
  import psycopg2
  from pathlib import Path
  
  # Connect to PostgreSQL
  conn = psycopg2.connect(
    dbname="bootcamp_rag",
    user="bootcamp_user",
    password="...",
    host="localhost"
  )
  cursor = conn.cursor()
  
  # Load first 10 Kaggle documents (sample)
  data_path = "/data/datasets/kaggle-enterprise-rag"
  files = sorted(Path(data_path).glob("*.md"))[:10]  # First 10 only
  
  for file in files:
    content = file.read_text()
    # Insert into PostgreSQL (will do chunking + embedding in Day 1)
    cursor.execute(
      "INSERT INTO documents (filename, content, source) VALUES (%s, %s, %s)",
      (file.name, content, "kaggle")
    )
  conn.commit()
  ```

**12:00 PM - 1:00 PM**: Lunch

**1:00 PM - 3:00 PM**: Load Sample Data into PostgreSQL

- [ ] Run data loading script:
  ```bash
  python /scripts/load_kaggle_data.py
  ```
- [ ] Verify data in PostgreSQL:
  ```bash
  psql -U bootcamp_user -d bootcamp_rag -c "SELECT COUNT(*) FROM documents;"
  # Should show: 10 (if loaded 10 sample docs)
  ```

- [ ] Status: "Sample data ✅ loaded into PostgreSQL"

**3:00 PM - 5:00 PM**: API Rate Limit Documentation

- [ ] Create rate limit tracking document: `/docs/api_rate_limits.txt`
  ```
  Groq (free tier):
  - 30 requests per minute
  - 4,000 tokens per minute
  - Fallback: Use Google if Groq rate limited
  
  Google AI Studio (free tier):
  - 60 requests per minute
  - 900,000 tokens per month
  - Fallback: Use HuggingFace if Google limited
  
  HuggingFace (community):
  - Inference API: ~100 requests per hour (varies)
  - Community models: No strict limit
  - Fallback: Use Groq if offline
  
  OpenRouter (free tier):
  - Varies by model (20-100 req/min typically)
  - Good for multi-model evaluation
  - Fallback: Last resort (most restricted)
  
  STRATEGY:
  1. Try Groq (fastest, most reliable free tier)
  2. If rate limited → Wait 1 min OR switch to Google
  3. If Google limited → Switch to HuggingFace
  4. If all limited → Cache results + batch requests
  ```

- [ ] Status to Chowdappa: "Day 0 data + API setup ✅"

**5:00 PM - 6:00 PM**: Document + Signoff

- [ ] Document: `/daily-logs/apr12_data_pipeline_day1.txt`
  ```
  ✅ All 4 APIs tested + working
  ✅ Sample Kaggle data (10 docs) loaded into PostgreSQL
  ✅ Rate limits documented
  ✅ Data pipeline ready for scaling
  
  Status: Ready for Day 1 embedding operations
  ```

---

### **April 13 (Sunday) — INFRASTRUCTURE DAY 2**

**YOU + UDAY ARE ACTORS IN PARALLEL.**

**9:00 AM - 11:00 AM**: Full Data Load

- [ ] Modify data loading script to load ALL Kaggle data (not just 10):
  ```python
  # Load ALL Kaggle files (full dataset)
  files = sorted(Path(data_path).glob("*.md"))  # No [:10] limit
  for file in files:
    # ... same loading logic
  ```

- [ ] Run full load:
  ```bash
  time python /scripts/load_kaggle_data.py  # Time it
  ```

- [ ] Monitor PostgreSQL:
  ```bash
  # In separate terminal, watch progress
  watch -n 5 'psql -U bootcamp_user -d bootcamp_rag -c "SELECT COUNT(*) FROM documents;"'
  ```

- [ ] Verify final count (should be 100-1000+ depending on dataset size):
  ```bash
  psql -U bootcamp_user -d bootcamp_rag -c "SELECT COUNT(*) FROM documents;"
  ```

**11:00 AM - 12:00 PM**: Load GCC + DMRC Data

- [ ] Similar scripts for GCC:
  ```python
  # /scripts/load_gcc_data.py
  # Load PDF contracts (if readable) or plaintext
  ```

- [ ] Similar scripts for DMRC:
  ```python
  # /scripts/load_dmrc_data.py
  # Load YAML policy documents
  ```

- [ ] Run all loads in sequence:
  ```bash
  python /scripts/load_kaggle_data.py
  python /scripts/load_gcc_data.py
  python /scripts/load_dmrc_data.py
  ```

**12:00 PM - 1:00 PM**: Lunch

**1:00 PM - 4:00 PM**: Data Inventory + Quality Check

- [ ] Create data inventory:
  ```bash
  psql -U bootcamp_user -d bootcamp_rag << EOF
  SELECT source, COUNT(*) as document_count, SUM(LENGTH(content)) as total_chars
  FROM documents
  GROUP BY source;
  EOF
  ```
  
  Expected output:
  ```
  source    | document_count | total_chars
  kaggle    | 100            | 50M
  gcc       | 5              | 5M
  dmrc      | 50             | 20M
  ```

- [ ] Quality checks:
  - [ ] Any documents with NULL content? (should be 0)
    ```sql
    SELECT COUNT(*) FROM documents WHERE content IS NULL;
    ```
  - [ ] Any duplicate filenames? (should be 0)
    ```sql
    SELECT filename, COUNT(*) FROM documents GROUP BY filename HAVING COUNT(*) > 1;
    ```
  - [ ] Any docs > 1MB? (might cause tokenization issues)
    ```sql
    SELECT filename, LENGTH(content) FROM documents WHERE LENGTH(content) > 1000000;
    ```

- [ ] Document: `/daily-logs/apr13_data_inventory.txt`
  ```
  Total Documents: X
  Kaggle: X docs (Y MB)
  GCC: X docs (Y MB)
  DMRC: X docs (Y MB)
  
  Quality: No NULLs, no duplicates, no megadocs
  Status: ✅ Data ready for Day 1 bootcamp
  ```

**4:00 PM - 5:00 PM**: Metadata Setup

- [ ] Add metadata to documents (for filtering):
  ```sql
  ALTER TABLE documents ADD COLUMN contract_type VARCHAR(50);
  ALTER TABLE documents ADD COLUMN contract_owner VARCHAR(50);
  ALTER TABLE documents ADD COLUMN source_document_id VARCHAR(100);
  
  UPDATE documents SET contract_type = 'enterprise' WHERE source = 'kaggle';
  UPDATE documents SET contract_type = 'government' WHERE source = 'gcc';
  UPDATE documents SET contract_type = 'metro' WHERE source = 'dmrc';
  ```

**5:00 PM - 6:00 PM**: Final Signoff

- [ ] Message to Chowdappa:
  ```
  Data pipeline READY ✅
  
  Loaded:
  ✅ Kaggle Enterprise: X documents
  ✅ GCC Government Contracts: X documents
  ✅ DMRC Metro/Railway: X documents
  
  APIs:
  ✅ All 4 working (Groq, Google, HF, OpenRouter)
  
  Quality:
  ✅ No corruption, duplicates, or quality issues
  ✅ Metadata properly configured
  
  We're ready for Day 1 bootcamp (Monday 9 AM).
  ```

---

## PHASE 2: WEEK 1 BOOTCAMP (April 15-19)

**YOUR TASK**: Monitor data pipeline + API health (background role, Uday is foreground)

### **April 15 (Monday) — BOOTCAMP DAY 1**

**9:00 AM STANDUP**
- Your update: "All APIs healthy. Data pipeline ready."
- Uday: "Running embedding comparison"

**DURING DAY**:
- [ ] Monitor API performance (3x daily: 9 AM, 12 PM, 4 PM):
  - [ ] Test Groq: ~50ms response time?
  - [ ] Test Google: ~100ms response time?
  - [ ] Any rate limit errors in logs?

- [ ] Monitor data queries (track slow queries):
  ```bash
  # Check PostgreSQL slow query log
  grep "duration:" /var/log/postgresql/postgresql.log | tail -20
  ```

**IF ISSUE**: API returning errors
- [ ] Check: Rate limit hit?
  ```
  If "429 Too Many Requests" → Wait 1 min, use fallback API
  If "401 Unauthorized" → Re-check API key, regenerate if needed
  If "500 Server Error" → Try different model or provider
  ```

**6:00 PM**: Document
- [ ] Log: `/daily-logs/apr15_data_api_monitor.txt`
  ```
  Groq: ✅ Healthy (avg response: 50ms, 0 errors)
  Google: ✅ Healthy (avg response: 100ms, 0 errors)
  HuggingFace: ✅ Healthy
  OpenRouter: ✅ Healthy
  
  Data pipeline: ✅ No issues
  ```

---

### **April 16-19 (Tuesday - Friday)**

**SAME MONITORING** as Day 1:
- 3x daily API health checks
- Monitor slow queries
- Report any issues to Chowdappa

**SCALING TASK** (mid-week):
- [ ] Data scales from 10 docs → 100 → 1000 (as Uday tests)
- [ ] Monitor: Does data loading still work? Any indexing delays?

---

## PHASE 3: WEEK 2 BOOTCAMP (April 22-26)

**SAME MONITORING** as Week 1 (APIs + data pipeline)

**ADDITIONAL TASK** (Week 2):
- [ ] If Uday needs more data (evaluation phase) → Load additional datasets
- [ ] If API switching needed → Manage fallback logic

---

# ⚠️ BLOCKERS YOU'LL FACE

## **Blocker 1: Kaggle Dataset Download Too Slow**

**When**: April 9-11

**Impact**: Dataset not ready by Day 0

**Resolution**:
1. Check download speed: `wget --spider` to estimate
2. Options:
   - A) Wait (might take 1-2 hours if slow internet)
   - B) Download in background, continue prep work
   - C) Use smaller sample dataset instead (first 100 files only)
3. Fallback: Start with smaller dataset, full one loads overnight

**Whom to Contact**: Chowdappa (if impacts timeline), you manage retry

---

## **Blocker 2: GCC PDF Not Accessible**

**When**: April 9-11

**Impact**: Missing government contracts dataset

**Resolution**:
1. Try alternate sources:
   - IREPS: https://www.ireps.gov.in/...
   - IRICEN: https://www.iricen.gov.in/...
   - DFCCIL: https://dfccil.com/...
   - GitHub: Sample PDFs available
2. If all fail → Use sample FIDIC clauses (generic contract terms)
3. Document: Use fallback, note limitation

**Whom to Contact**: Chowdappa (if need to pivot dataset)

---

## **Blocker 3: An API Key Stops Working**

**When**: Any day during bootcamp

**Impact**: That LLM provider unavailable

**Resolution**:
1. Check: Is quota exceeded? (regenerate new key if needed)
2. Check: Is account still active? (login to verify)
3. Regenerate new API key:
   - Delete old key from provider portal
   - Create new key
   - Update `.env` on HPC
   - Test with `/scripts/test_apis.py`
4. Update fallback chain if permanent issue

**Whom to Contact**: You can fix this (1-5 mins), notify Uday if key was primary

---

## **Blocker 4: Rate Limit Hit (429 Error)**

**When**: Week 2, when evaluation queries scale (50+ queries)

**Impact**: LLM calls throttled, evaluation slow

**Resolution**:
1. Strategy:
   - Batch requests (wait between groups)
   - Use different API providers in rotation
   - Cache results (don't re-query same thing)
   - Reduce query rate (spread across 2 days instead of 1)

2. Implement fallback chain automatically:
   ```python
   apis = [Groq, Google, HuggingFace, OpenRouter]
   for api in apis:
     try:
       response = api.generate(query)
       return response
     except RateLimitError:
       continue  # Try next API
     except Exception:
       break  # No more fallbacks
   ```

**Whom to Contact**: Uday (to reduce query volume), you manage API fallbacks

---

## **Blocker 5: PostgreSQL Data Ingestion Slow**

**When**: April 13, when loading all Kaggle data

**Impact**: Loading takes > 2 hours, Day 1 starts without data

**Resolution**:
1. Check: Is it INSERT-bound or NETWORK-bound?
   - Monitor: `watch 'ps aux | grep python'` (CPU running?)
   - Monitor: `iostat -x 1` (disk busy?)
   - Monitor: `iftop` (network utilized?)

2. Optimize:
   - A) Batch inserts (insert 1000 rows per transaction vs 1 per transaction)
   - B) Disable indexes during load (enable after)
   - C) Use COPY command instead of INSERT
   - D) Split load across 2-3 processes in parallel

3. Example optimized loader:
   ```python
   # Batch 1000 inserts
   conn.autocommit = False
   cursor = conn.cursor()
   batch = []
   for file in files:
     batch.append((file.name, file.content))
     if len(batch) >= 1000:
       cursor.executemany("INSERT ...", batch)
       conn.commit()
       batch = []
   ```

**Whom to Contact**: You optimize code, Backend1 optimizes indexes, Chowdappa if timeline critical

---

## **Blocker 6: DMRC Dataset Unavailable**

**When**: April 9

**Impact**: Missing metro/railway dataset (1/3 of data)

**Resolution**:
1. Check sources:
   - DMRC official: http://www.delhimetrorail.com
   - IREPS: https://www.ireps.gov.in
   - GitHub: Community repos with synthetic data
2. If really unavailable → Use 2X more GCC+Kaggle docs (substitute)
3. Document: Use fallback, note in final report

**Whom to Contact**: Chowdappa (if need to substitute dataset)

---

# 📞 ESCALATION CHART

```
YOU HIT DATA/API BLOCKER
    ↓
Is it API auth issue?
    ↓
[YES] → Regenerate key, update .env, test
[NO]  → Is it data availability issue?
    ↓
[YES] → Find alternate source / use fallback
[NO]  → Escalate to Chowdappa
```

---

# 💾 YOUR DOCUMENTATION FOLDER

```
/aipms-rag-bootcamp/
  ├── scripts/
  │   ├── test_apis.py
  │   ├── load_kaggle_data.py
  │   ├── load_gcc_data.py
  │   ├── load_dmrc_data.py
  │   └── monitor_apis.py
  ├── docs/
  │   ├── data_download_roadmap.txt
  │   ├── api_keys_setup.txt
  │   ├── api_rate_limits.txt
  │   └── data_pipeline_architecture.txt
  ├── daily-logs/
  │   ├── apr9_data_download_verification.txt
  │   ├── apr12_data_pipeline_day1.txt
  │   ├── apr13_data_inventory.txt
  │   ├── apr15_data_api_monitor.txt
  │   ├── apr16_data_api_monitor.txt
  │   ├── apr17_data_api_monitor.txt
  │   ├── apr18_data_api_monitor.txt
  │   ├── apr19_data_api_monitor.txt
  │   ├── apr22_data_scale_monitor.txt
  │   ├── apr23_data_api_monitor.txt
  │   ├── apr24_data_api_monitor.txt
  │   ├── apr25_data_api_monitor.txt
  │   └── apr26_data_final_status.txt
  └── .env (secure, not committed to git)
```

---

# ✅ SUCCESS CRITERIA FOR YOUR ROLE

**By April 26, 6 PM**:

- ✅ All 3 datasets downloaded + staged
- ✅ 100+ documents in PostgreSQL ready for embedding
- ✅ All 4 APIs provisioned + tested
- ✅ Data loading pipeline working
- ✅ Zero data corruption
- ✅ APIs never rate-limited (or gracefully fallback)
- ✅ All daily monitoring logs created
- ✅ Zero unplanned data downtime

**You are the data engineer. Everyone depends on your data.**

---

**END OF BACKEND2 ROLE GUIDE**
