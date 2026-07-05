import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="JARVIS AI: Tactical Protocol", layout="wide")

# 2. ตั้งค่า API
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("ไม่ได้ตั้งค่า API Key ใน Secrets โปรดตั้งค่าก่อน!")
    st.stop()

# --- CUSTOM CSS (รวมของเดิม + ตกแต่งแชทให้สวยงาม) ---
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] { background-color: #050a12; color: #e0e6ed; }
        .main-title { font-family: 'Impact'; color: #f5e1a4; text-align: center; text-shadow: 0 0 15px #f5e1a4; margin-bottom: 20px;}
        .digital-container { border: 2px solid #1e3a69; padding: 20px; background-color: rgba(11, 22, 38, 0.6); border-radius: 10px; text-align: center; margin-bottom: 20px;}
        .input-area { position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%); width: 60%; display: flex; gap: 10px; z-index: 1000; background: rgba(5, 10, 18, 0.9); padding: 10px; border-radius: 10px;}
        .chat-bubble-boss { background-color: #1e3a69; color: #e0e6ed; padding: 10px 15px; border-radius: 15px 15px 0 15px; margin-bottom: 10px; float: right; width: fit-content; clear: both;}
        .chat-bubble-jarvis { background-color: #374151; color: #f5e1a4; padding: 10px 15px; border-radius: 15px 15px 15px 0; margin-bottom: 10px; float: left; width: fit-content; clear: both; border-left: 3px solid #f5e1a4;}
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE (เพื่อเก็บประวัติแชท) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- UI CONTENT ---
st.markdown('<h1 class="main-title">JARVIS AI</h1>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown('<div class="digital-container"><img src="https://cdn-icons-png.flaticon.com/512/6165/6165557.png" width="150"></div>', unsafe_allow_html=True)

# แสดงประวัติแชท
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-bubble-boss">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bubble-jarvis">{msg["content"]}</div>', unsafe_allow_html=True)

# --- INPUT AREA ---
st.markdown('<div class="input-area">', unsafe_allow_html=True)
c1, c2 = st.columns([1, 6])
with c1:
    audio_input = st.audio_input(" ")
with c2:
    user_input = st.text_input(" ", placeholder="Command to JARVIS...", key="user_input")
st.markdown('</div>', unsafe_allow_html=True)

# --- LOGIC ---
if user_input:
    # เพิ่มข้อความบอส
    st.session_state.messages.append({"role": "user", "content": user_input})
    # JARVIS ตอบ
    response = model.generate_content(user_input)
    st.session_state.messages.append({"role": "jarvis", "content": response.text})
    st.rerun()
