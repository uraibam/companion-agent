import streamlit as st
from database import init_db
from pages import onboarding, dashboard, reflection, admin

st.set_page_config(page_title="Founder Companion Agent", layout="centered")

# ✅ Initialize the database once app starts
init_db()

PAGES = {
    "🛍 Onboarding": onboarding.show,
    "📋 Dashboard": dashboard.show,
    "🧘 SMBTV Reflection": reflection.show,
    "🛠 Admin Panel": admin.show,
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
PAGES[selection]()


