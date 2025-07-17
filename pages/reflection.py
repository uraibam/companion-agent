import streamlit as st
import openai

def ask_llm(prompt):
    import os
    openai.api_key = os.getenv("GROQ_API_KEY", st.secrets["GROQ_API_KEY"])

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Replace with groq's model if needed
        messages=[
            {
                "role": "system",
                "content": (
                    "You're a helpful reflective agent that guides founders "
                    "to align their Soul, Mind, Body, Trust, and Value through deep thinking."
                ),
            },
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]

def show():
    st.title("🧘 SMBTV Reflection")
    st.write("Check in with your inner compass.")

    soul = st.text_input("🌌 How is your Soul aligned?")
    mind = st.text_input("🧠 How is your Mind aligned?")
    body = st.text_input("💪 How is your Body aligned?")
    trust = st.text_input("🤝 How is your Trust aligned?")
    value = st.text_input("🎯 How is your Value aligned?")

    if st.button("🔍 Reflect with AI"):
        if any([soul, mind, body, trust, value]):
            user_input = f"Soul: {soul}\nMind: {mind}\nBody: {body}\nTrust: {trust}\nValue: {value}"
            st.info("Thinking...")
            result = ask_llm(user_input)
            st.text_area("🧭 Your Companion Agent says:", result, height=250)
        else:
            st.warning("Please fill at least one reflection input.")
