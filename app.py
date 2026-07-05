import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

st.title("🦜 JARVIS AI: Live Protocol")

api_key = st.sidebar.text_input("API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # ส่วนพิมพ์คุย (เร็วที่สุด)
    user_input = st.text_input("สั่งการ JARVIS:")
    if user_input:
        response = model.generate_content(user_input)
        reply = response.text
        st.write(f"**JARVIS:** {reply}")
        
        # แปลงเป็นเสียง
        tts = gTTS(text=reply, lang='th')
        tts.save("reply.mp3")
        st.audio("reply.mp3", autoplay=True)
