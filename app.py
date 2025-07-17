from database import init_db

init_db()  # This will create the database when the app starts

import streamlit as st
from pages import onboarding, dashboard, reflection, admin

st.set_page_config(page_title="Founder Companion Agent", layout="centered")

PAGES = {
    "🛍 Onboarding": onboarding.show,
    "📋 Dashboard": dashboard.show,
    "🧘 SMBTV Reflection": reflection.show,
    "🛠 Admin Panel": admin.show,
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
PAGES[selection]()

