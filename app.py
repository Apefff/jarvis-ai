import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="JARVIS AI: Tactical Protocol", layout="centered")

# 2. ตั้งค่า API
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("ไม่ได้ตั้งค่า API Key ใน Secrets โปรดตั้งค่าก่อน!")
    st.stop()

# --- HI-TECH CSS (เน้นเรืองแสงและดีไซน์แบบ AR) ---
st.markdown("""
    <style>
        /* พื้นหลังธีม Cyber-Dark */
        [data-testid="stAppViewContainer"] { background: #00040a; color: #00e5ff; font-family: 'Orbitron', sans-serif; }
        
        /* กล่องหลักแบบ Holo-Screen */
        .holo-screen {
            background: rgba(0, 20, 40, 0.7);
            border: 1px solid #00e5ff;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 0 20px rgba(0, 229, 255, 0.2);
            text-align: center;
        }

        /* ตกแต่งแชท */
        .chat-boss { background: rgba(0, 100, 255, 0.2); color: #fff; padding: 10px; border-radius: 10px; margin: 5px 0; border-left: 4px solid #00e5ff; }
        .chat-jarvis { background: rgba(255, 215, 0, 0.1); color: #ffd700; padding: 10px; border-radius: 10px; margin: 5px 0; border-left: 4px solid #ffd700; }
        
        /* ช่องใส่ Input ให้ดูไฮเทค */
        .stTextInput input { border: 1px solid #00e5ff !important; background: #000 !important; color: #00e5ff !important; }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- HEADER (ตามภาพ reference) ---
st.markdown('<div class="holo-screen"><h2 style="color:#00e5ff;">JARVIS AI SYSTEM</h2><p style="font-size:12px;">TACTICAL PROTOCOL ONLINE</p></div>', unsafe_allow_html=True)

# ส่วนแสดงนกแก้วเรืองแสง
st.markdown('<div style="text-align:center; padding: 20px;"><img src="https://cdn-icons-png.flaticon.com/512/6165/6165557.png" width="120" style="filter: drop-shadow(0 0 10px #00e5ff);"></div>', unsafe_allow_html=True)

# แสดงแชท
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-boss">BOSS: {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-jarvis">JARVIS: {msg["content"]}</div>', unsafe_allow_html=True)

# --- INPUT AREA (ด้านล่าง) ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
user_input = st.text_input("INPUT COMMAND:", placeholder="Waiting for instructions...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = model.generate_content(user_input)
    st.session_state.messages.append({"role": "jarvis", "content": response.text})
    st.rerun()
