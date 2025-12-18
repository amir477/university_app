import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from core.database import get_connection

def create_user_role(username, password, role):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (username, password, role)
        VALUES (?, ?, ?)
    """, (username, password, role))

    conn.commit()
    conn.close()

def block_user(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET is_active = 0
        WHERE username = ?
    """, (username,))

    conn.commit()
    conn.close()

def unblock_user(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET is_active = 1
        WHERE username = ?
    """, (username,))

    conn.commit()
    conn.close()

def delete_user(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM users
        WHERE username = ?
    """, (username,))

    conn.commit()
    conn.close()

def exists_user(username):
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
        SELECT COUNT(*) FROM users
        WHERE username = ?
    """, (username,))


    count = cursor.fetchone()[0]
    conn.close()

    return count > 0

def is_block(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT is_active FROM users
        WHERE username = ?
    """, (username,))

    is_active = cursor.fetchone()[0]
    conn.close()

    return not is_active

def is_unblock(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT is_active FROM users
        WHERE username = ?
    """, (username,))

    is_active = cursor.fetchone()[0]
    conn.close()

    return is_active