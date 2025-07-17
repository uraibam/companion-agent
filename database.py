import sqlite3
from datetime import datetime

DB_NAME = "companion_agent.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    with open("schema.sql", "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

def add_user(email, traits):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users (email, traits, onboarded_date) VALUES (?, ?, ?)",
                   (email, traits, datetime.now().strftime("%Y-%m-%d")))
    conn.commit()
    conn.close()

def get_user(email):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()
    return result

def save_task(email, task_text):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (user_email, task_date, task) VALUES (?, ?, ?)",
                   (email, datetime.now().strftime("%Y-%m-%d"), task_text))
    conn.commit()
    conn.close()

def get_today_task(email):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE user_email = ? AND task_date = ?", 
                   (email, datetime.now().strftime("%Y-%m-%d")))
    result = cursor.fetchone()
    conn.close()
    return result

def mark_task_done(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET is_done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

