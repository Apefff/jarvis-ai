import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="JARVIS PARROT AI", layout="centered")

# 2. ตั้งค่า API
api_key = st.secrets.get("GOOGLE_API_KEY")
if not api_key:
    st.error("บอสยังไม่ได้ใส่ GOOGLE_API_KEY ในหน้า Secrets ครับ!")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. CSS ไฮเทค (คลื่นเสียงขยับได้ + แชทสวย)
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] { background: #00040a; color: #00e5ff; }
        .wave { display: flex; justify-content: center; gap: 5px; height: 30px; margin: 20px 0; }
        .bar { width: 5px; height: 10px; background: #00e5ff; animation: move 1s infinite alternate; }
        @keyframes move { from { height: 10px; } to { height: 30px; } }
        .stChatMessage { border-radius: 10px; border: 1px solid #1e3a69; background: rgba(11, 22, 38, 0.6); }
    </style>
""", unsafe_allow_html=True)

# 4. UI
st.markdown("<h2 style='text-align:center; color:#00e5ff;'>JARVIS AI SYSTEM</h2>", unsafe_allow_html=True)
st.markdown("<div class='wave'><div class='bar'></div><div class='bar'></div><div class='bar'></div><div class='bar'></div></div>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;'><img src='https://cdn-icons-png.flaticon.com/512/6165/6165557.png' width='120'></div>", unsafe_allow_html=True)

# 5. Chat Logic (แบบมาตรฐาน)
if "messages" not in st.session_state:
    st.session_state.messages = []

# แสดงข้อความเดิม
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# รับคำสั่ง
if prompt := st.chat_input("สั่งการ JARVIS..."):
    # แสดงคำสั่งทันที
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # JARVIS ตอบ
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
