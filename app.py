import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="JARVIS AI", layout="centered")

# ตั้งค่า API จาก Secrets
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("ตั้งค่า API Key ใน Secrets ให้เรียบร้อยก่อน!")
    st.stop()

# --- CSS จัดเต็ม ---
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] { background: #00040a; color: #00e5ff; }
        .holo-screen { background: rgba(0, 20, 40, 0.7); border: 1px solid #00e5ff; border-radius: 15px; padding: 20px; text-align: center; }
        .chat-boss { background: rgba(0, 100, 255, 0.2); color: #fff; padding: 10px; border-radius: 10px; margin: 5px 0; border-left: 4px solid #00e5ff; float: right; clear: both;}
        .chat-jarvis { background: rgba(255, 215, 0, 0.1); color: #ffd700; padding: 10px; border-radius: 10px; margin: 5px 0; border-left: 4px solid #ffd700; float: left; clear: both;}
    </style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# แสดง UI
st.markdown('<div class="holo-screen"><h2>JARVIS AI SYSTEM</h2><p>TACTICAL PROTOCOL ACTIVE</p></div>', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-boss">BOSS: {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-jarvis">JARVIS: {msg["content"]}</div>', unsafe_allow_html=True)

# --- เทคนิคใช้เสียงบนมือถือ ---
# บอสไม่ต้องกดปุ่มไมค์ในเว็บให้รวนครับ
# ให้บอสกดที่ "ไอคอนไมโครโฟน" บนคีย์บอร์ดของมือถือ (Dictation) แล้วพูดใส่ช่องนี้ได้เลย
user_input = st.text_input("สั่งการ JARVIS:", placeholder="พูดใส่ไมค์มือถือหรือพิมพ์ที่นี่...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = model.generate_content(user_input)
    st.session_state.messages.append({"role": "jarvis", "content": response.text})
    st.rerun()
