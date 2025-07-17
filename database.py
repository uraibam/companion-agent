# database.py
import sqlite3
from datetime import datetime

DB_NAME = "companion_agent.db"

# Get today's date in consistent format
def today():
    return datetime.now().strftime("%Y-%m-%d")

# Database connection helper
def get_connection():
    return sqlite3.connect(DB_NAME)

# Initialize database with schema
def init_db():
    conn = get_connection()
    with open("schema.sql", "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

# ========== USERS ==========
def add_user(email, traits):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO users (email, traits, onboarded_date)
        VALUES (?, ?, ?)
    """, (email, traits, today()))
    conn.commit()
    conn.close()

def get_user(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()
    return result

# ========== TASKS ==========
def save_task(email, task_text):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (user_email, task_date, task)
        VALUES (?, ?, ?)
    """, (email, today(), task_text))
    conn.commit()
    conn.close()

def get_today_task(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM tasks
        WHERE user_email = ? AND task_date = ?
    """, (email, today()))
    result = cursor.fetchone()
    conn.close()
    return result

def mark_task_done(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET is_done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def get_all_tasks(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE user_email = ? ORDER BY task_date DESC", (email,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# ========== REFLECTIONS ==========
def save_reflection(email, soul, mind, body, trust, value):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reflections (user_email, reflection_date, soul, mind, body, trust, value)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (email, today(), soul, mind, body, trust, value))
    conn.commit()
    conn.close()

def get_reflections(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reflections WHERE user_email = ?", (email,))
    data = cursor.fetchall()
    conn.close()
    return data
