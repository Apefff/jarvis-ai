import streamlit as st
import google.generativeai as genai

st.title("🦜 JARVIS AI: Live Protocol")

# ช่องใส่ API Key
api_key = st.sidebar.text_input("Enter API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # [จุดสำคัญ] ใส่บรรทัดนี้เพื่อให้ปุ่มไมค์กลับมาครับ
    audio_value = st.audio_input("กดไมโครโฟนเพื่อคุยกับ JARVIS")
    
    if audio_value:
        st.write("ได้รับเสียงแล้ว! (กำลังรอการพัฒนาฟังก์ชันถอดเสียง)")
    
    # ช่องพิมพ์เผื่อไว้ด้วย
    user_input = st.text_input("หรือพิมพ์คำสั่งที่นี่:")
    if user_input:
        response = model.generate_content(user_input)
        st.write(f"**JARVIS:** {response.text}")
