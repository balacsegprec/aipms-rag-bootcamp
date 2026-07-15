### ROADMAP
## ROLE: You are a full-stack engineer building a frontend for an already-hardened RAG backend, then deploying the full stack for a CSE final year project demo.

## CONTEXT: 
Backend hardening is complete and verified (RLS with FORCE ROW LEVEL SECURITY + non-superuser 
app role, CORS, /health endpoint reading real DB connectivity, llm_provider tracking in QueryResponse, 
Gemini import safety, Docker port/command fixes, startup auto-init of pgvector/hardening).

## HARD CONSTRAINT: Do NOT modify any backend logic, security configuration, database roles, or RLS 
policies in this phase. If you find a backend issue while building the frontend, STOP, report it, 
and wait for explicit approval before touching backend code. This phase is frontend + deployment only.

## STEP 0: CONFIRM THE REAL API CONTRACT (before writing any UI code)

Before building anything, inspect the current, actual QueryResponse model in src/api/main.py and the 
/health endpoint response shape. Do not assume the shape from earlier reports — confirm it fresh, since 
tuple-unpacking refactors across multiple files (query_router.py, pipeline.py, etc.) may have shifted 
field names. Report the exact current QueryResponse schema and /health schema before proceeding.


## STEP 1: FRONTEND SCAFFOLD
Stack: Vite + React (state management for tenant switching + trace display will be cleaner than vanilla 
JS given 4 interacting panels).

Build exactly these 4 panels, wired only to fields confirmed to actually exist in Step 0:

1. Chat Panel
   - Query input, X-API-Key input (session-only storage, never persisted to disk/localStorage)
   - Markdown-rendered answer
   - Status bar: confidence, llm_provider, latency_ms vs latency_budget_ms as a colored meter 
     (green if latency_status == "PASSED", red if "FAILED")
   - "Server waking up..." loading state if no response within ~3s (handles Render cold starts)

2. Sidebar Config Panel
   - tenant_id dropdown (hardcode metro_tenant / dfcc_tenant — no discovery endpoint exists)
   - entity_type_filter dropdown (contract_clause / ncr / dpr / correspondence / none)

3. Source Explorer (collapsible)
   - Render retrieval_trace: content (redacted), distance, entity_type, source (pgvector/fallback)
   - Visually flag any [REDACTED_*] tokens distinctly (e.g. highlighted background)

4. Diagnostic Panel
   - Show llm_provider as "Answered by: X" — label honestly, do NOT imply a multi-step failover 
     trace unless a failover_trace field actually exists in the confirmed schema from Step 0
   - If entity_type_filter blocked something or confidence is "low", surface that plainly rather 
     than hiding it — a visible low-confidence flag is more credible to examiners than a system 
     that always looks certain

Do NOT build: an audit ledger viewer, an adversarial-block visualizer, or a tenant-discovery UI — 
none of these have backing endpoints yet. If asked "should we add these," answer "needs a new backend 
endpoint, out of scope for this phase" rather than mocking fake data for them.

## STEP 2: LOCAL INTEGRATION TEST (before any deployment)

Run frontend + backend + DB locally together. Manually verify, and report each result explicitly:
   - Query as metro_tenant, then dfcc_tenant, confirm different/isolated retrieval_trace results
   - Trigger a deliberately out-of-scope query, confirm the UI shows the block clearly rather than 
     erroring or showing a blank screen
   - Kill one LLM provider's API key temporarily (or simulate) and confirm llm_provider in the UI 
     reflects the actual fallback provider, not a stale value
   - Confirm CORS actually works from the browser (not just curl) — open browser devtools network 
     tab and confirm no CORS errors

Do not proceed to deployment until all four checks above pass with actual evidence (screenshots or 
console output), not just "should work."

## STEP 3: DEPLOYMENT
1. Provision Neon.tech or Supabase Postgres, confirm pgvector + pg_trgm extensions enabled
2. Run migrations + ingestion against the remote DB using the non-superuser app role credentials 
   (confirm the admin-only operations like init_pgvector still correctly use the admin role even 
   when pointed at the remote DB)
3. Deploy backend to Render, set env vars matching remote DB + at least one LLM key
4. Update CORS allowlist in backend to include the actual deployed frontend URL (not just localhost)
5. Deploy frontend to Vercel/Netlify, point API base URL at the deployed Render backend
6. Re-run the Step 2 checklist against the DEPLOYED stack, not just local — cold start behavior, 
   CORS, tenant isolation, all need re-verification in the real deployed environment since 
   local-vs-deployed behavior can differ (e.g. CORS misconfigurations often only show up once 
   origins actually differ)

## OUTPUT
After each step, report concretely: what was built/deployed, what was tested, and paste actual 
evidence (terminal output, screenshots, network tab state) rather than asserting success. If Step 0 
reveals the schema doesn't match what earlier reports claimed, stop and report the discrepancy before 
building UI against assumptions.