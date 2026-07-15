import sys
import os

os.environ["DB_USER"] = "rag_app_user"
os.environ["DB_PASSWORD"] = "rag_password"

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.security.database import setup_database_hardening, load_documents_idempotent, retrieve_with_rls
from src.core.pipeline import embed_model

def main():
    print("=== STARTING MANUAL RLS TEST ===")
    
    # 1. Setup/Verify database hardening is enabled
    print("Enabling database hardening...")
    hardened = setup_database_hardening()
    print(f"Database hardened: {hardened}")
    if not hardened:
        print("[ERROR] Database hardening could not be set up.")
        sys.exit(1)
        
    # 2. Insert test document for tenant_a
    tenant_a = "tenant_a"
    tenant_b = "tenant_b"
    doc_text = "This is a highly confidential document for Tenant A only."
    q_emb = embed_model.encode([doc_text])[0].tolist()
    
    print(f"Loading document for {tenant_a}...")
    inserted = load_documents_idempotent([doc_text], [q_emb], entity_type="contract", tenant_id=tenant_a)
    print(f"Documents inserted: {inserted}")
    
    # 3. Query as tenant_a
    print(f"Querying as {tenant_a}...")
    res_a = retrieve_with_rls(q_emb, tenant_id=tenant_a, entity_type="contract", k=5)
    print(f"Results for {tenant_a}: count={len(res_a)}")
    for r in res_a:
        print(f" - [{r['tenant_id']}] {r['content']}")
        
    # 4. Query as tenant_b against tenant_a's docs
    print(f"Querying as {tenant_b}...")
    res_b = retrieve_with_rls(q_emb, tenant_id=tenant_b, entity_type="contract", k=5)
    print(f"Results for {tenant_b}: count={len(res_b)}")
    for r in res_b:
         print(f" - [{r['tenant_id']}] {r['content']}")
         
    # 5. Assert isolation
    assert len(res_a) > 0, f"Tenant A should be able to retrieve its own document (found {len(res_a)})."
    # Ensure no rows leak to Tenant B
    leakage = [r for r in res_b if r['tenant_id'] == tenant_a]
    assert len(leakage) == 0, f"Leakage detected! Tenant B retrieved Tenant A's document: {leakage}"
    
    print("SUCCESS: RLS tenant isolation verified! No leakage occurred.")

if __name__ == "__main__":
    main()
