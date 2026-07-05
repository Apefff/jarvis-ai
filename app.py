import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="JARVIS AI Live", layout="centered")

if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("ตั้งค่า API Key ใน Secrets ด้วย!")
    st.stop()

# --- CSS & JS สำหรับคลื่นเสียงแบบ Live ---
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] { background: #00040a; color: #00e5ff; }
        .live-pulse {
            width: 100px; height: 100px; border-radius: 50%;
            background: radial-gradient(circle, #00e5ff, transparent);
            margin: 20px auto; animation: pulse 1.5s infinite;
        }
        @keyframes pulse { 0% { transform: scale(0.8); opacity: 0.5; } 50% { transform: scale(1.2); opacity: 1; } 100% { transform: scale(0.8); opacity: 0.5; } }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div style="text-align:center;"><h2>JARVIS LIVE MODE</h2><div class="live-pulse"></div></div>', unsafe_allow_html=True)

# ส่วนการสั่งการ
st.write("---")
user_input = st.text_input("สั่งการ JARVIS (กดไมค์ที่คีย์บอร์ดแล้วพูด):")

if user_input:
    response = model.generate_content(user_input)
    st.markdown(f'<div style="background:#1e3a69; padding:15px; border-radius:10px;">{response.text}</div>', unsafe_allow_html=True)
    st.rerun()
