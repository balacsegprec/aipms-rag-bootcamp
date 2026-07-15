import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.database.connection import get_connection

def main():
    # Force connect as rag_app_user
    os.environ["DB_USER"] = "rag_app_user"
    os.environ["DB_PASSWORD"] = "rag_password"
    
    conn = get_connection()
    if not conn:
        print("Failed to connect.")
        return
        
    try:
        cur = conn.cursor()
        
        # Start transaction
        cur.execute("BEGIN;")
        
        # Set tenant to tenant_b
        cur.execute("SET LOCAL app.current_tenant_id = 'tenant_b';")
        
        # Print setting
        cur.execute("SELECT current_setting('app.current_tenant_id', true);")
        val = cur.fetchone()[0]
        print(f"Session app.current_tenant_id: {val}")
        
        # Query table
        cur.execute("SELECT id, tenant_id, content FROM rag_documents;")
        rows = cur.fetchall()
        print(f"Total rows retrieved: {len(rows)}")
        for r in rows:
            print(f" - ID: {r[0]}, Tenant: {r[1]}, Content: {r[2][:50]}...")
            
        cur.execute("COMMIT;")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    main()
