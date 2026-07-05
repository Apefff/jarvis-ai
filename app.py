import streamlit as st
import google.generativeai as genai

st.title("🦜 JARVIS AI: Urgent Task Protocol")

api_key = st.text_input("Enter your Google API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # เพิ่มปุ่มรับเสียง
    audio_value = st.audio_input("กดไมโครโฟนเพื่อคุยกับ JARVIS")
    
    if audio_value:
        st.write("JARVIS กำลังประมวลผล...")
        # หมายเหตุ: การแปลงเสียงเป็นข้อความต้องใช้ Whisper API 
        # แต่เบื้องต้นลองพิมพ์ทดสอบในช่องนี้ได้ครับ
        user_input = st.text_input("หรือพิมพ์คำสั่งที่นี่:")
        if user_input:
            response = model.generate_content(user_input)
            st.write(f"**JARVIS:** {response.text}")
