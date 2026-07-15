import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.database.connection import get_connection

def main():
    conn = get_connection()
    if not conn:
        print("Failed to connect.")
        return
    try:
        cur = conn.cursor()
        
        # Check if user already exists
        cur.execute("SELECT 1 FROM pg_roles WHERE rolname = 'rag_app_user';")
        exists = cur.fetchone()
        
        if not exists:
            cur.execute("CREATE ROLE rag_app_user WITH LOGIN PASSWORD 'rag_password';")
            print("Role rag_app_user created.")
        else:
            print("Role rag_app_user already exists.")
            
        # Grant privileges
        cur.execute("GRANT CONNECT ON DATABASE rag_bootcamp TO rag_app_user;")
        cur.execute("GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO rag_app_user;")
        cur.execute("GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO rag_app_user;")
        cur.execute("ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO rag_app_user;")
        conn.commit()
        print("Privileges granted to rag_app_user.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    main()
