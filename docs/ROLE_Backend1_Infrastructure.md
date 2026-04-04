# ⚙️ ROLE: BACKEND1 — INFRASTRUCTURE ENGINEER

**Reporting To**: Chowdappa (Sprint Master)  
**Coordinates With**: Backend2 (APIs/Data), Uday (NLP — data consumer)  
**Technical Authority**: PostgreSQL, pgvector, Apache AGE, Jupyter setup, HPC resources  
**Contact Emergency**: Chowdappa (within 1 hour), HPC Lab Admin (for hardware issues)

---

## 📍 YOUR ROLE IN 30 SECONDS

You are the **foundation builder**. Your job:
- ✅ Get PostgreSQL + pgvector running on GPREC HPC
- ✅ Add Apache AGE (graph DB optional, if time permits)
- ✅ Setup Jupyter for team (multi-user access)
- ✅ Monitor database performance
- ✅ Troubleshoot hardware/network issues

**Note**: You don't write NLP code. You keep the lights on.

---

# 📅 YOUR DAILY CHECKLIST (April 4-26)

## PHASE 0: PRE-BOOTCAMP (April 4-14)

### **April 4 (Friday) — TODAY**

**YOUR TASK**: Understand infrastructure requirements

- [ ] Read MASTER_BOOTCAMP_PLAYBOOK.md (sections 1-3, 5)
- [ ] Read ROLE_Backend2_APIsDataPipeline.md (understand data flow into your DB)
- [ ] Read `ai_execution_plan.md` for infrastructure specs

**PREP WORK**:
- [ ] SSH key setup: Do you have HPC credentials?
  - [ ] Can you SSH into GPREC HPC from your laptop? (test: `ssh -i [key] user@hpc-ip`)
- [ ] Network check: Can you download from internet from HPC? (important for installations)
- [ ] Disk space: Check available space on HPC
  - [ ] Target: 75GB free (for data + databases)

---

### **April 5 (Saturday)**

**STATUS**: Weekend

- [ ] Read PostgreSQL documentation (1 hr):
  - Installation on Linux
  - Basic commands (createdb, psql)
  - Permissions management (CREATE ROLE)
  
- [ ] Research pgvector extension (30 mins):
  - What it does: Stores + indexes embeddings (384-1024 dim vectors)
  - Installation requirements
  - Performance characteristics

- [ ] Optional: Download PostgreSQL 15 + pgvector build instructions locally

---

### **April 6 (Sunday)**

**STATUS**: Weekend

- [ ] Review Apache AGE (optional, depends on timeline):
  - Is it needed? (only if multi-hop reasoning needs entity relationships)
  - Can be skipped if time-constrained

- [ ] Prepare bash scripts (for automated setup):
  - `install_postgresql.sh`
  - `install_pgvector.sh`
  - `create_database.sh`
  - `setup_jupyter.sh`

---

### **April 7 (Monday)**

**YOUR TASK**: Coordinate with Chowdappa on HPC lab visit

- [ ] Message to Chowdappa: "If visiting HPC lab today, can you get me these details?"
  - CPU cores? (run: `nproc` on HPC)
  - RAM available? (run: `free -h` on HPC)
  - Disk free? (run: `df -h` on HPC)
  - Linux distro + version? (run: `cat /etc/os-release`)
  - Can I compile from source? (do we have build-essential?)
  - Can I use package manager? (apt, yum, or other?)

---

### **April 8 (Tuesday)**

**YOUR TASK**: Receive HPC details from Chowdappa

- [ ] Chowdappa sends HPC specs from lab visit
- [ ] Review: Are specs adequate for bootcamp?
  - Need: 4+ CPU cores (for parallel queries)
  - Need: 16+ GB RAM (for embeddings cache)
  - Need: 75+ GB disk (for data + vectors)
  - Need: Linux (Ubuntu preferred, CentOS OK)

- [ ] If specs marginal → Flag to Chowdappa (may need contingency)

---

### **April 9 (Wednesday)**

**YOUR TASK**: Prepare infrastructure scripts

- [ ] Create PostgreSQL installation script: `/scripts/install_postgresql.sh`
  ```bash
  sudo apt-get update
  sudo apt-get install -y postgresql postgresql-contrib postgresql-dev build-essential libreadline-dev libz-dev
  sudo systemctl start postgresql
  sudo systemctl enable postgresql
  ```

- [ ] Create pgvector installation script: `/scripts/install_pgvector.sh`
  ```bash
  git clone https://github.com/pgvector/pgvector.git
  cd pgvector
  make
  sudo make install
  ```

- [ ] Create database setup script: `/scripts/create_database.sh`
  ```sql
  CREATE ROLE bootcamp_user WITH LOGIN PASSWORD 'secure_password';
  CREATE DATABASE bootcamp_rag OWNER bootcamp_user;
  \c bootcamp_rag
  CREATE EXTENSION IF NOT EXISTS vector;
  CREATE EXTENSION IF NOT EXISTS pg_trgm;
  CREATE SCHEMA IF NOT EXISTS embeddings;
  ```

- [ ] Create Jupyter setup script: `/scripts/setup_jupyter.sh`
  ```bash
  pip install python-dotenv jupyter numpy pandas scikit-learn langchain chromadb psycopg2-binary sentence-transformers groq google-generativeai requests
  jupyter notebook --generate-config
  ```

---

### **April 10 (Thursday)**

**YOUR TASK**: Wait for MD approval + finalize setup plan

- [ ] Check with Chowdappa: "Has MD approved infrastructure spiking?"
- [ ] If YES: Prepare for Day 0 (Apr 12-13)
- [ ] If NO: Wait

**PREP FOR DAY 0**:
- [ ] Download all scripts to local laptop (backup)
- [ ] Test scripts on personal Linux machine if available (for sanity check)
- [ ] Prepare checklist: `/daily-logs/infrastructure_setup_checklist.txt`
  ```
  PostgreSQL: [ ] Installation [ ] Start service [ ] Accessible on port 5432
  pgvector: [ ] Installed [ ] Extension loadable [ ] Test table created
  Jupyter: [ ] Installation [ ] Multi-user setup [ ] 4 users can login
  Database: [ ] Bootcamp_rag created [ ] User permissions set [ ] Sample table created
  ```

---

### **April 11 (Friday)**

**YOUR TASK**: Final pre-Day-0 checks

- [ ] Confirm Chowdappa: "Ready for Day 0 infrastructure spiking tomorrow?"
- [ ] Final checklist reviewed
- [ ] All scripts backed up to HPC `/tmp/` folder (safer than email)
- [ ] Contact HPC lab admin: "We're installing PostgreSQL tomorrow. Any guidance?"

---

## PHASE 1: DAY 0 INFRASTRUCTURE SPIKE (April 12-13)

### **April 12 (Saturday) — INFRASTRUCTURE DAY 1**

**YOU ARE THE PRIMARY ACTOR TODAY.**

**9:00 AM START** (with Chowdappa + team online via Slack/email)

- [ ] **9:00 AM - 9:15 AM**: Standup
  - You: "Starting PostgreSQL installation"
  - Chowdappa: Monitoring
  - Backend2: Standby for API setup later

**9:15 AM - 11:00 AM**: PostgreSQL Installation

- [ ] SSH into GPREC HPC
  ```bash
  ssh -i [key] user@hpc-ip
  cd /tmp
  ```

- [ ] Run installation script
  ```bash
  bash /tmp/install_postgresql.sh
  ```

- [ ] Checklist:
  - [ ] PostgreSQL service running? (check: `sudo systemctl status postgresql`)
  - [ ] Accessible on port 5432? (check: `psql -U postgres -c "SELECT version();"`)
  - [ ] Respond to Chowdappa: "PostgreSQL ✅ running"

**IF BLOCKER**:
- Error: "build-essential not found"? → Contact HPC admin (need admin privileges)
- Error: "Port 5432 in use"? → Find old process: `lsof -i :5432` → kill it
- Error: "GCC not available"? → Switch to package manager instead of compile

**11:00 AM - 12:00 PM**: pgvector Installation

- [ ] Run pgvector script
  ```bash
  bash /tmp/install_pgvector.sh
  ```

- [ ] Checklist:
  - [ ] pgvector built successfully? (check: `ls /usr/lib/postgresql/15/lib/ | grep vector`)
  - [ ] Test load: `psql -U postgres -c "CREATE EXTENSION vector;"`
  - [ ] Respond: "pgvector ✅ installed"

**IF BLOCKER**:
- Build fails? → Ensure `build-essential` installed (PostgreSQL already provided dev files)
- Extension fails? → Check PostgreSQL version (pgvector should match PG version)

**12:00 PM - 1:00 PM**: Lunch

**1:00 PM - 2:30 PM**: Database Creation + Permissions

- [ ] Create database + user
  ```bash
  psql -U postgres -f /tmp/create_database.sh
  ```

- [ ] Verify:
  ```bash
  psql -U bootcamp_user -d bootcamp_rag -c "SELECT 1;"
  psql -U bootcamp_user -d bootcamp_rag -c "CREATE TABLE test (id SERIAL, embedding vector(384));"
  psql -U bootcamp_user -d bootcamp_rag -c "INSERT INTO test VALUES (1, ARRAY[0.1::float, 0.2::float]);"
  ```

- [ ] If all ✅ → Reply: "Database ✅ ready"

**2:30 PM - 3:30 PM**: Jupyter Setup (Single User First)

- [ ] Install Jupyter
  ```bash
  bash /tmp/setup_jupyter.sh
  ```

- [ ] Start Jupyter on port 8888
  ```bash
  jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser &
  ```

- [ ] Get login token (for testing)
  ```bash
  jupyter notebook list
  ```

- [ ] Test from local laptop:
  - Open browser: `http://[HPC-IP]:8888`
  - Paste token → Should see Jupyter
  - Create test notebook, import `psycopg2` → Should work ✅

- [ ] Reply: "Jupyter ✅ working (single user tested)"

**3:30 PM - 5:00 PM**: Multi-User Jupyter Setup

- [ ] Problem: Only one user can use port 8888 at a time
- [ ] Solution: Launch 4 Jupyter instances (ports 8888, 8889, 8890, 8891)
  ```bash
  nohup jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser > /logs/jupyter_8888.log 2>&1 &
  nohup jupyter notebook --ip=0.0.0.0 --port=8889 --no-browser > /logs/jupyter_8889.log 2>&1 &
  nohup jupyter notebook --ip=0.0.0.0 --port=8890 --no-browser > /logs/jupyter_8890.log 2>&1 &
  nohup jupyter notebook --ip=0.0.0.0 --port=8891 --no-browser > /logs/jupyter_8891.log 2>&1 &
  ```

- [ ] Test each port (ensure all working)

**IF BLOCKED**: Firewall not allowing ports?
- Contact HPC admin: "Need ports 8888-8891 open for Jupyter"

- [ ] Reply: "Multi-user Jupyter ✅ (4 instances on ports 8888-8891)"

**5:00 PM - 6:00 PM**: Final Documentation + Monitoring

- [ ] Create Service Monitoring Script
  ```bash
  ps aux | grep postgres
  ps aux | grep jupyter
  ```

- [ ] Create `/scripts/health_check.sh`:
  ```bash
  #!/bin/bash
  echo "PostgreSQL status:"
  sudo systemctl status postgresql
  echo "Jupyter instances:"
  ps aux | grep jupyter | grep -v grep
  echo "Disk usage:"
  df -h
  ```

- [ ] Document: `/daily-logs/apr12_infrastructure_day1.txt`
  ```
  PostgreSQL: ✅ Running on port 5432
  pgvector: ✅ Extension loadable
  Jupyter: ✅ 4 instances (ports 8888-8891)
  Database: ✅ Bootcamp_rag created
  
  Issues encountered: [None / List any]
  
  Status: Ready for Day 2
  ```

**6:00 PM**: Message to Chowdappa
- "Infrastructure Day 1 complete. PostgreSQL + pgvector + Jupyter ready. See doc."

---

### **April 13 (Sunday) — INFRASTRUCTURE DAY 2 (FINAL)**

**YOU + BACKEND2 ARE ACTORS IN PARALLEL.**

**9:00 AM START**

- [ ] **9:00 AM-10:00 AM**: Verify everything still running
  ```bash
  bash /scripts/health_check.sh
  psql -U bootcamp_user -d bootcamp_rag -c "SELECT version();"
  ```

- [ ] Confirm with Uday: "Can you test PostgreSQL + Jupyter from your laptop?"
  - Uday tests connection
  - Reports: Working ✅ or Issues ❌

**10:00 AM - 12:00 PM**: Table Schema Creation

- [ ] Create main embeddings table (that Uday will use):
  ```sql
  CREATE TABLE embeddings.chunks (
    id SERIAL PRIMARY KEY,
    document_id VARCHAR(100),
    chunk_text TEXT,
    chunk_number INT,
    embedding vector(384),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB,
    contract_type VARCHAR(50),
    contract_owner VARCHAR(50)
  );
  
  CREATE INDEX idx_embedding ON embeddings.chunks USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
  CREATE INDEX idx_text_search ON embeddings.chunks USING GIN (to_tsvector('english', chunk_text));
  ```

- [ ] Create test table + insert sample vector:
  ```sql
  INSERT INTO embeddings.chunks (document_id, chunk_text, embedding, contract_type, contract_owner)
  VALUES (
    'test_001',
    'Test paragraph about contract penalties',
    array_cat(ARRAY[0.1::float], array_fill(0.0::float, ARRAY[383])),
    'kaggle',
    'user1'
  );
  ```

- [ ] Test similarity search:
  ```sql
  SELECT id, document_id, chunk_text, embedding <=> array_cat(ARRAY[0.1::float], array_fill(0.0::float, ARRAY[383])) as distance
  FROM embeddings.chunks
  ORDER BY embedding <=> array_cat(ARRAY[0.1::float], array_fill(0.0::float, ARRAY[383]))
  LIMIT 5;
  ```

- [ ] If query returns results ✅ → Reply: "Table schema ✅ and similarity search working"

**12:00 PM - 1:00 PM**: Lunch

**1:00 PM - 2:00 PM**: Full BM25 Setup

- [ ] Enable pg_trgm for text search:
  ```sql
  CREATE EXTENSION IF NOT EXISTS pg_trgm;
  
  -- Create tsvector column for BM25
  ALTER TABLE embeddings.chunks ADD COLUMN text_search tsvector;
  UPDATE embeddings.chunks SET text_search = to_tsvector('english', chunk_text);
  CREATE INDEX idx_tsvector ON embeddings.chunks USING GIN(text_search);
  ```

- [ ] Test BM25 search:
  ```sql
  SELECT id, document_id, chunk_text, ts_rank_cd(text_search, query) as relevance
  FROM embeddings.chunks, plainto_tsquery('english', 'contract penalties') query
  WHERE text_search @@ query
  ORDER BY relevance DESC
  LIMIT 5;
  ```

- [ ] If works ✅ → Reply: "BM25 search ✅ working"

**2:00 PM - 3:00 PM**: MultiSchema Setup (Optional: Apache AGE)

- [ ] If time permits → Install Apache AGE (graph database)
  ```sql
  CREATE EXTENSION IF NOT EXISTS age;
  LOAD 'age';
  SET search_path = ag_catalog, "$user", public;
  
  SELECT create_graph('entities');
  ```

- [ ] If skip → That's fine, AGE is optional for MVP

**3:00 PM - 4:00 PM**: Backup + Monitoring

- [ ] Create backup script: `/scripts/backup_database.sh`
  ```bash
  pg_dump -U bootcamp_user bootcamp_rag > /backups/bootcamp_rag_$(date +%Y%m%d_%H%M%S).sql
  ```

- [ ] Create automated monitoring (check every hour if DB is responsive):
  ```bash
  # Add to crontab: 0 * * * * psql -U bootcamp_user -d bootcamp_rag -c "SELECT 1;" || echo "DB DOWN" | mail admin
  ```

**4:00 PM - 5:00 PM**: Final Integration Test

- [ ] Uday runs full integration test:
  - [ ] Connect to PostgreSQL ✅
  - [ ] Load 10 sample documents ✅
  - [ ] Insert 10 embeddings ✅
  - [ ] Similarity search returns results ✅
  - [ ] BM25 search returns results ✅

- [ ] If ALL ✅ → Infrastructure ready

**5:00 PM - 6:00 PM**: Document + Signoff

- [ ] Document: `/daily-logs/apr13_infrastructure_day2_complete.txt`
  ```
  PostgreSQL: ✅ Production ready
  pgvector: ✅ Indexing working (IVFFlat with 100 lists)
  BM25: ✅ Full-text search working
  Jupyter: ✅ 4 users can access
  Schema: ✅ Embeddings table created with metadata
  Backups: ✅ Automated backup scheduled
  Monitoring: ✅ Health checks in place
  
  Overall Status: 🟢 INFRASTRUCTURE READY FOR BOOTCAMP
  ```

- [ ] Message to Chowdappa:
  ```
  Infrastructure spiking COMPLETE ✅
  
  Status:
  ✅ PostgreSQL running
  ✅ pgvector ready
  ✅ BM25 search ready
  ✅ Jupyter multi-user setup
  ✅ Backups configured
  ✅ Monitoring active
  
  We're ready for Day 1 bootcamp (Monday 9 AM).
  
  Backend1
  ```

---

## PHASE 2: WEEK 1 BOOTCAMP (April 15-19)

**YOUR TASK**: Monitor + maintain infrastructure (background role, Uday is foreground)

### **April 15 (Monday) — BOOTCAMP DAY 1**

**9:00 AM STANDUP**
- Your update: "Database healthy. Monitoring active."
- Uday: "Running embedding comparison"
- Chowdappa: Coordinating

**9:15 AM - 6:00 PM**: Background Monitoring

- [ ] 3x daily health checks (9 AM, 12 PM, 4 PM):
  ```bash
  bash /scripts/health_check.sh
  # Check: PostgreSQL running? Jupyter running? Disk space OK?
  ```

- [ ] Monitor disk space (vectors can get large):
  ```bash
  du -sh /var/lib/postgresql/
  df -h | grep /
  ```

- [ ] If any issue → Report to Chowdappa immediately

**IF ISSUE**: Database becomes slow
- [ ] Check: VACUUM + ANALYZE (rebuild indexes)
  ```sql
  VACUUM ANALYZE embeddings.chunks;
  ```
- [ ] Check: Index performance
  ```sql
  EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM embeddings.chunks ORDER BY embedding <=> '[0.1,...]' LIMIT 5;
  ```

**6:00 PM**: Document
- [ ] Log: `/daily-logs/apr15_infrastructure_monitor.txt`
  ```
  Status: ✅ Healthy
  Disk used: X GB (target: <50 GB)
  Query response time: <100ms
  Jupyter availability: 100%
  ```

---

### **April 16-19 (Tuesday - Friday) — DAYS 2-5**

**SAME PROCESS** as Day 1:
- 9 AM, 12 PM, 4 PM health checks
- Monitor disk space
- Monitor query latency
- Report any issues to Chowdappa

**DURING WEEK 1**:
- [ ] Gradual data load (10 docs → 100 docs → 1000 docs)
- [ ] Monitor index performance at each scale
- [ ] Adjust IVFFlat lists if query time degrades (lists = 100 good for 1000 vectors; may need 200 for 10K)

**EXIT CRITERIA (Friday Apr 19, 6 PM)**:
- ✅ Database stable with 1000+ vectors
- ✅ Query latency <100ms (single query, not including embedding)
- ✅ Disk usage <30 GB
- ✅ No crashes or restarts

---

## PHASE 3: WEEK 2 BOOTCAMP (April 22-26)

**YOUR TASK**: Scale infrastructure (monitoring becomes more critical)

### **April 22 (Monday) — DAY 6**

- [ ] Data scales to 5K vectors
- [ ] Monitor: Query latency still <100ms?
- [ ] If latency creeping up → Optimize indexes

**IF BLOCKER**: Query latency > 200ms

**Resolution**:
1. Check: Index size + performance
2. Options:
   - A) Rebuild index with different lists parameter (IVFFlat lists = 200 or 500)
   - B) Switch to HNSW index (different algorithm, often faster)
   - C) Add read replicas (PostgreSQL streaming replication)

---

### **April 23-25 (Tuesday - Thursday)**

**SAME MONITORING** as Week 1 (3x daily health checks)

### **April 26 (Friday) — DELIVERY**

- [ ] Final infrastructure status check
- [ ] Database backup + archive
- [ ] Document infrastructure performance for handover

---

# ⚠️ BLOCKERS YOU'LL FACE

## **Blocker 1: PostgreSQL Installation Fails (GCC Missing)**

**When**: April 12, 9:15 AM

**Impact**: Can't compile pgvector

**Resolution**:
1. Check: Is build-essential available?
   ```bash
   sudo apt-get install -y build-essential
   ```
2. If permission denied → Contact HPC admin
3. Fallback: Use package manager (apt/yum) instead of compile (faster, less control)

**Whom to Contact**: HPC lab admin (for permission), Chowdappa (if critical blocking)

---

## **Blocker 2: Port 5432 Already in Use**

**When**: April 12, during PostgreSQL start

**Impact**: Can't start PostgreSQL service

**Resolution**:
1. Find what's using port:
   ```bash
   lsof -i :5432
   # or
   netstat -tulpn | grep 5432
   ```
2. Kill old process:
   ```bash
   sudo kill -9 [PID]
   ```
3. Use different port (5433) if needed:
   ```bash
   sudo nano /etc/postgresql/15/main/postgresql.conf
   # Change: port = 5433
   ```

**Whom to Contact**: You can fix this alone (IT not needed)

---

## **Blocker 3: Disk Space Running Out**

**When**: April 18-19 (when scaling to 10K vectors)

**Impact**: Database can't write, queries fail

**Resolution**:
1. Check disk:
   ```bash
   df -h
   ```
2. Options:
   - A) Delete old backups/logs (free up space quickly)
   - B) Archive vectors to different disk/mount
   - C) Request HPC admin for additional storage
3. Long-term: Implement data retention policy (delete old vectors after X days)

**Whom to Contact**: HPC lab admin (if need more storage), Chowdappa (if critical)

---

## **Blocker 4: Query Latency > 2 Seconds**

**When**: April 18-19 (during scaling)

**Impact**: RAG pipeline too slow

**Resolution**:
1. Diagnose:
   ```bash
   EXPLAIN (ANALYZE) SELECT * FROM embeddings.chunks ORDER BY embedding <=> ... LIMIT 5;
   ```
2. Check index state:
   ```sql
   SELECT * FROM pg_indexes WHERE tablename = 'chunks';
   ```
3. Options:
   - A) Rebuild index with better parameters (lists = 200 instead of 100)
   - B) Switch to HNSW index (faster neighbor search)
   - C) Reduce chunk size (fewer vectors to search)
   - D) Accept trade-off (slower = more accurate)

**Whom to Contact**: You + Uday (optimization) → Chowdappa (if trade-off decision needed)

---

## **Blocker 5: Jupyter Not Accessible on Port 8888**

**When**: April 12-13

**Impact**: Uday can't access notebook environment

**Resolution**:
1. Check: Is Jupyter running?
   ```bash
   ps aux | grep jupyter
   ```
2. Check: Is port open?
   ```bash
   sudo ufw status
   # or
   sudo firewall-cmd --list-ports
   ```
3. Open port if firewall blocking:
   ```bash
   sudo ufw allow 8888/tcp
   ```
4. Test locally:
   ```bash
   curl localhost:8888
   ```

**Whom to Contact**: HPC lab admin (if firewall), you can fix port issues

---

## **Blocker 6: PostgreSQL Crashes Mid-Day**

**When**: Any day during bootcamp

**Impact**: All Uday's work stops

**Resolution**:
1. Check logs:
   ```bash
   sudo tail -100 /var/log/postgresql/postgresql-*.log
   ```
2. Common causes:
   - Out of memory → Reduce shared_buffers or cache sizes
   - Query too expensive → Optimize query
   - Disk full → Free disk space
3. Restart PostgreSQL:
   ```bash
   sudo systemctl restart postgresql
   ```
4. Check if data corrupted:
   ```bash
   psql -U postgres -d bootcamp_rag -c "REINDEX DATABASE bootcamp_rag;"
   ```

**Whom to Contact**: You → Chowdappa if data recovery needed

---

# 📞 ESCALATION CHART

```
YOU HIT INFRASTRUCTURE BLOCKER
    ↓
Is it environment/permissions issue?
    ↓
[YES] → Contact HPC Lab Admin
[NO]  → Can you fix in 1 hour?
    ↓
[YES] → Fix + document
[NO]  → Contact Chowdappa
    ↓
Chowdappa helps + escalates if needed
```

---

# 💾 YOUR DOCUMENTATION FOLDER

```
/aipms-rag-bootcamp/
  ├── scripts/
  │   ├── install_postgresql.sh
  │   ├── install_pgvector.sh
  │   ├── create_database.sh
  │   ├── setup_jupyter.sh
  │   ├── health_check.sh
  │   ├── backup_database.sh
  │   └── optimize_indexes.sh
  ├── daily-logs/
  │   ├── apr12_infrastructure_day1.txt
  │   ├── apr13_infrastructure_day2_complete.txt
  │   ├── apr15_infrastructure_monitor.txt
  │   ├── apr16_infrastructure_monitor.txt
  │   ├── apr17_infrastructure_monitor.txt
  │   ├── apr18_infrastructure_monitor.txt
  │   ├── apr19_infrastructure_monitor.txt
  │   ├── apr22_scaling_to_5k.txt
  │   ├── apr23_infrastructure_monitor.txt
  │   ├── apr24_infrastructure_monitor.txt
  │   ├── apr25_infrastructure_monitor.txt
  │   └── apr26_final_infrastructure_status.txt
  └── backups/
      ├── bootcamp_rag_20260412_*.sql
      ├── bootcamp_rag_20260419_*.sql
      └── bootcamp_rag_20260426_*.sql
```

---

# ✅ SUCCESS CRITERIA FOR YOUR ROLE

**By April 26, 6 PM**:

- ✅ PostgreSQL stable + accessible
- ✅ pgvector + indexing working
- ✅ BM25 search working
- ✅ Jupyter multi-user access (all 4 users can log in)
- ✅ 10K+ vectors stored + queryable
- ✅ Query latency < 2 seconds
- ✅ Zero unplanned downtime (99%+ uptime)
- ✅ Automated backups running
- ✅ Zero data corruption
- ✅ All health checks passing

**You are SRE (Site Reliability Engineer). Everyone depends on your infrastructure.**

---

**END OF BACKEND1 ROLE GUIDE**
