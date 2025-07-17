import streamlit as st
import sqlite3
from datetime import date
from email_utils import send_email

def show():
    st.title("🛠 Admin Panel (POC)")
    st.write("Trigger notifications and plans manually.")

    # Simulate sending reminder
    st.subheader("📧 Send Email Reminder")
    recipient = st.text_input("Recipient Email")
    subject = st.text_input("Subject", "You missed a habit yesterday")
    body = st.text_area("Body", "Let's get back on track today!")

    if st.button("Send Reminder"):
        if recipient and subject and body:
            success = send_email(recipient, subject, body)
            if success:
                st.success("✅ Email sent!")
            else:
                st.error("❌ Failed to send email.")
        else:
            st.warning("Please fill in all fields.")

    st.markdown("---")

    # Simulate task plan generation
    st.subheader("🧠 Generate 3-day Plan")
    email = st.text_input("Generate plan for user email")

    if st.button("Generate Plan Now"):
        if not email:
            st.warning("Please enter an email.")
            return

        try:
            conn = sqlite3.connect("companion.db")
            cursor = conn.cursor()

            sample_tasks = [
                "Review calendar for 15 mins",
                "Write down 1st principles about today's goal",
                "Reflect on biggest win this week"
            ]
            today = date.today()

            for i, task in enumerate(sample_tasks):
                task_date = str(today)
                cursor.execute(
                    "INSERT INTO tasks (email, task, date, done) VALUES (?, ?, ?, ?)",
                    (email, task, task_date, 0)
                )

            conn.commit()
            conn.close()
            st.success("✅ Plan generated and saved!")
        except Exception as e:
            st.error(f"Error: {e}")

