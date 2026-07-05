import streamlit as st
import google.generativeai as genai

st.title("🦜 JARVIS AI: Urgent Task Protocol")

api_key = st.text_input("Enter your Google API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.generativeai.GenerativeModel('gemini-1.5-flash')
    user_input = st.text_input("สั่งงาน JARVIS:")
    if user_input:
        response = model.generate_content(user_input)
        st.write(f"**JARVIS:** {response.text}")
