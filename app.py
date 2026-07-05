import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="JARVIS AI", layout="centered")

# ตั้งค่า API
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("ไม่ได้ตั้งค่า API Key!")
    st.stop()

# --- CSS ไฮเทค ---
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] { background: #00040a; color: #00e5ff; font-family: 'Courier New', monospace; }
        .holo-screen { background: rgba(0, 20, 40, 0.7); border: 1px solid #00e5ff; border-radius: 15px; padding: 20px; text-align: center; margin-bottom: 20px; }
        .chat-boss { background: rgba(0, 100, 255, 0.2); color: #fff; padding: 10px; border-radius: 10px; margin: 5px 0; border-left: 4px solid #00e5ff; float: right; clear: both;}
        .chat-jarvis { background: rgba(255, 215, 0, 0.1); color: #ffd700; padding: 10px; border-radius: 10px; margin: 5px 0; border-left: 4px solid #ffd700; float: left; clear: both;}
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- UI ---
st.markdown('<div class="holo-screen"><h2>JARVIS AI SYSTEM</h2><p>TACTICAL PROTOCOL ONLINE</p></div>', unsafe_allow_html=True)

# แสดงประวัติแชท
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-boss">BOSS: {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-jarvis">JARVIS: {msg["content"]}</div>', unsafe_allow_html=True)

# ช่องพิมพ์คำสั่ง
user_input = st.text_input("INPUT COMMAND:", placeholder="พิมพ์คำสั่งที่นี่...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = model.generate_content(user_input)
    st.session_state.messages.append({"role": "jarvis", "content": response.text})
    st.rerun()
