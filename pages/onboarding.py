import streamlit as st
import sqlite3

def show():
    st.title("🛍 Onboarding")
    st.write("Let's personalize your journey as a founder.")

    email = st.text_input("📧 Enter your email:")
    traits = st.text_area("🧠 What traits do you want to improve?", height=100)

    if st.button("🚀 Submit"):
        if email and traits:
            try:
                conn = sqlite3.connect("companion.db")
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO users (email, traits)
                    VALUES (?, ?)
                """, (email, traits))
                conn.commit()
                conn.close()
                st.success("✅ Onboarding complete! You're all set.")
            except Exception as e:
                st.error(f"❌ Error saving data: {e}")
        else:
            st.warning("Please enter both email and traits to continue.")
