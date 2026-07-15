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
        cur.execute("ALTER ROLE rag_user NOSUPERUSER NOBYPASSRLS;")
        conn.commit()
        print("Successfully altered role rag_user to NOSUPERUSER NOBYPASSRLS.")
    except Exception as e:
        print(f"Error altering role: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    main()
