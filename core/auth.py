import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from core.database import get_connection
def authenticate(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, role
        FROM users
        WHERE username=? AND password=? AND is_active=1
    """, (username, password))

    user = cursor.fetchone()
    conn.close()

    return user  # None یا (id, role)

