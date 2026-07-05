import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="JARVIS AI", layout="centered")

# ตั้งค่า API
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # ใช้รุ่นนี้ที่เสถียรที่สุด
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("ไม่ได้ตั้งค่า API Key ใน Secrets!")
    st.stop()

# --- UI ---
st.markdown('<div style="background:rgba(0,20,40,0.7); border:1px solid #00e5ff; padding:20px; border-radius:15px; text-align:center;"><h2>JARVIS AI SYSTEM</h2></div>', unsafe_allow_html=True)

# ช่องพิมพ์คำสั่ง (เอาไว้ก่อนเพื่อความชัวร์)
user_input = st.text_input("INPUT COMMAND:", placeholder="พิมพ์คำสั่งที่นี่...")

if user_input:
    try:
        response = model.generate_content(user_input)
        st.success(f"JARVIS: {response.text}")
    except Exception as e:
        st.error(f"ระบบขัดข้อง: {e}")

# --- CSS ไฮเทค ---
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] { background: #00040a; color: #00e5ff; }
        .holo-screen { background: rgba(0, 20, 40, 0.7); border: 1px solid #00e5ff; border-radius: 15px; padding: 20px; text-align: center; }
        .chat-boss { background: rgba(0, 100, 255, 0.2); color: #fff; padding: 10px; border-radius: 10px; margin: 5px 0; border-left: 4px solid #00e5ff; }
        .chat-jarvis { background: rgba(255, 215, 0, 0.1); color: #ffd700; padding: 10px; border-radius: 10px; margin: 5px 0; border-left: 4px solid #ffd700; }
    </style>
""", unsafe_allow_html=True)

# --- UI & LOGIC ---
st.markdown('<div class="holo-screen"><h2>JARVIS AI SYSTEM</h2></div>', unsafe_allow_html=True)

# ปุ่มไมค์ (Mic Recorder)
st.write("กดปุ่มเพื่อเริ่มบันทึกเสียง:")
audio = mic_recorder(start_prompt="🎙️ พูดเลย", stop_prompt="⏹️ หยุด", just_once=False)

# ช่องพิมพ์สำรอง
user_input = st.text_input("หรือพิมพ์คำสั่ง:", placeholder="Command to JARVIS...")

# ประมวลผล
if user_input:
    response = model.generate_content(user_input)
    st.markdown(f'<div class="chat-jarvis">JARVIS: {response.text}</div>', unsafe_allow_html=True)
