import requests
import streamlit as st

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

def query_groq(messages, model="mixtral-8x7b-32768"):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": messages,
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def generate_plan(traits):
    prompt = f"A founder wants to improve the following traits: {traits}. Create a personalized 3-day plan with practical steps aligned to startup life. Be realistic and focused."
    messages = [{"role": "user", "content": prompt}]
    return query_groq(messages)

def smb_tv_reflection(soul, mind, body, trust, value):
    prompt = f"""
A founder is reflecting on their day. Their inputs:
Soul: {soul}
Mind: {mind}
Body: {body}
Trust: {trust}
Value: {value}

Based on this, provide thoughtful analysis. Where are they aligned? What should they focus on more? What are they neglecting?
"""
    messages = [{"role": "user", "content": prompt}]
    return query_groq(messages)

