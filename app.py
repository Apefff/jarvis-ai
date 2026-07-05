import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="JARVIS AI", layout="centered")

# API Setup
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("ใส่ API Key ใน Secrets ด้วย!")
    st.stop()

# --- CSS ที่มีคลื่นเสียงแบบ Live ---
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] { background: #00040a; color: #00e5ff; }
        /* Waveform Animation */
        .wave-container { display: flex; align-items: center; justify-content: center; gap: 5px; height: 50px; margin: 20px 0; }
        .bar { width: 5px; height: 20px; background: #00e5ff; animation: pulse 1s infinite; }
        @keyframes pulse { 0%, 100% { height: 20px; } 50% { height: 50px; } }
        .bar:nth-child(2) { animation-delay: 0.1s; }
        .bar:nth-child(3) { animation-delay: 0.2s; }
        .bar:nth-child(4) { animation-delay: 0.3s; }
    </style>
""", unsafe_allow_html=True)

# UI
st.markdown("<h2 style='text-align:center;'>JARVIS SYSTEM</h2>", unsafe_allow_html=True)

# แสดงคลื่นเสียง
st.markdown("""
    <div class='wave-container'>
        <div class='bar'></div><div class='bar'></div><div class='bar'></div><div class='bar'></div>
    </div>
""", unsafe_allow_html=True)

# Chat Logic
if "messages" not in st.session_state: st.session_state.messages = []
for msg in st.session_state.messages:
    st.write(f"**{msg['role']}:** {msg['content']}")

prompt = st.chat_input("สั่งการ JARVIS...")
if prompt:
    st.session_state.messages.append({"role": "BOSS", "content": prompt})
    response = model.generate_content(prompt)
    st.session_state.messages.append({"role": "JARVIS", "content": response.text})
    st.rerun()
