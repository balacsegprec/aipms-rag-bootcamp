import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.database.connection import get_connection

def main():
    conn = get_connection()
    if not conn:
        print("Failed to connect to database.")
        return
    
    try:
        cur = conn.cursor()
        
        # 1. Current user
        cur.execute("SELECT current_user;")
        user = cur.fetchone()[0]
        print(f"Current User: {user}")
        
        # 2. User attributes
        cur.execute("SELECT rolsuper, rolbypassrls FROM pg_roles WHERE rolname = %s;", (user,))
        row = cur.fetchone()
        if row:
            print(f"Is Superuser: {row[0]}, Has BypassRLS: {row[1]}")
        else:
            print("User role attributes not found in pg_roles.")
            
        # 3. Table security attributes
        cur.execute("""
            SELECT relrowsecurity, relforcerowsecurity 
            FROM pg_class 
            WHERE relname = 'rag_documents';
        """)
        row = cur.fetchone()
        if row:
            print(f"Table relrowsecurity (RLS Enabled): {row[0]}")
            print(f"Table relforcerowsecurity (RLS Forced): {row[1]}")
        else:
            print("Table 'rag_documents' not found in pg_class.")
            
        # 4. Existing policies
        cur.execute("""
            SELECT policyname, roles, cmd, qual 
            FROM pg_policies 
            WHERE tablename = 'rag_documents';
        """)
        policies = cur.fetchall()
        print(f"Active Policies count: {len(policies)}")
        for p in policies:
            print(f"  Policy Name: {p[0]}")
            print(f"    Roles: {p[1]}")
            print(f"    Cmd: {p[2]}")
            print(f"    Qual: {p[3]}")
            
    except Exception as e:
        print(f"Error checking RLS status: {e}")
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    main()
