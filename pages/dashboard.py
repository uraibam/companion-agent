import streamlit as st
import sqlite3
from datetime import date

def show():
    st.title("📋 Your Dashboard")

    today = str(date.today())

    try:
        conn = sqlite3.connect("companion.db")
        cursor = conn.cursor()

        st.subheader("📝 Today's Tasks")

        tasks = cursor.execute(
            "SELECT id, task, done FROM tasks WHERE date = ?", (today,)
        ).fetchall()

        if not tasks:
            st.info("No tasks for today. Admin might not have generated them yet.")
        else:
            for task_id, task, done in tasks:
                checked = st.checkbox(task, value=bool(done))
                if checked != bool(done):
                    cursor.execute(
                        "UPDATE tasks SET done = ? WHERE id = ?",
                        (int(checked), task_id)
                    )
                    conn.commit()

        st.markdown("---")

        st.subheader("💡 Missed a task?")
        st.write("Don’t worry. Here's a motivational nudge: ")
        st.info("Progress is built one small habit at a time. Recommit and go again today.")

        conn.close()

    except Exception as e:
        st.error(f"Database error: {e}")
