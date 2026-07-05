import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="JARVIS AI", layout="centered")

# ดึงค่าจาก Secrets
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("บอสลืมตั้งค่า GOOGLE_API_KEY ในหน้า Secrets ของ Streamlit Cloud ครับ!")
    st.stop()

# ตั้งค่าโมเดลแบบมาตรฐานที่สุด (Flash 1.5)
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"ตั้งค่าโมเดลผิดพลาด: {e}")
    st.stop()

st.title("JARVIS AI SYSTEM")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("สั่งการ JARVIS..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        try:
            # จุดเกิด Error เดิมคือตรงนี้
            response = model.generate_content(prompt)
            st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"JARVIS เชื่อมต่อไม่ได้: {e}")
            st.info("คำแนะนำ: ลองสร้าง API Key ใหม่ในโปรเจกต์เดิม หรือใช้รุ่น 'gemini-1.5-flash' เท่านั้น")
