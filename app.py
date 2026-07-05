import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="JARVIS AI", layout="centered")

# 2. ตั้งค่า API (ดึงจาก Secrets อย่างปลอดภัย)
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("บอสยังไม่ได้ใส่ API Key ในช่อง Secrets ในหน้าตั้งค่าของ Streamlit ครับ!")
    st.stop()

genai.configure(api_key=api_key)
# ใช้รุ่นนี้ที่เสถียรและรวดเร็ว
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. CSS จัดเต็มธีมไฮเทค (คงความสวยงามเดิมไว้)
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] { background: #00040a; color: #00e5ff; font-family: 'Courier New', Courier, monospace; }
        .main-title { text-align: center; color: #f5e1a4; text-shadow: 0 0 10px #f5e1a4; font-size: 2.5rem; margin-bottom: 10px;}
        .digital-container { border: 1px solid #1e3a69; padding: 15px; background-color: rgba(11, 22, 38, 0.6); border-radius: 10px; text-align: center; margin-bottom: 20px; }
        /* Chat styling */
        .stChatMessage { border-radius: 10px; }
        .stChatMessage[data-testid="stChatMessage-user"] { background-color: #1e3a69; color: #e0e6ed; border: 1px solid #60a5fa; }
        .stChatMessage[data-testid="stChatMessage-assistant"] { background-color: #374151; color: #f5e1a4; border-left: 3px solid #f5e1a4; }
    </style>
""", unsafe_allow_html=True)

# --- UI CONTENT ---
st.markdown('<h1 class="main-title">JARVIS AI</h1>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown('<div class="digital-container"><img src="https://cdn-icons-png.flaticon.com/512/6165/6165557.png" width="150" style="filter: drop-shadow(0 0 15px #60a5fa);"></div>', unsafe_allow_html=True)

# 4. Session State เก็บประวัติแชท (จำเป็นมากเพื่อให้แชทไม่หาย)
if "messages" not in st.session_state:
    st.session_state.messages = []

# แสดงประวัติแชททั้งหมด
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. ช่องรับคำสั่ง (ส่วนสำคัญที่ทำให้ Error หายไป)
if prompt := st.chat_input("สั่งการ JARVIS..."):
    # บันทึกคำถามของผู้ใช้
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # ให้ JARVIS ตอบ
    with st.chat_message("assistant"):
        with st.spinner("JARVIS กำลังประมวลผล..."):
            try:
                response = model.generate_content(prompt)
                if response and response.text:
                    st.markdown(response.text)
                    # บันทึกคำตอบของ JARVIS
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                else:
                    st.error("JARVIS ไม่สามารถตอบคำถามนี้ได้ในขณะนี้ โปรดลองใหม่อีกครั้งครับ")
            except Exception as e:
                st.error(f"เกิดข้อผิดพลาดในการเชื่อมต่อกับ Gemini: {e}")
                # ตัวช่วย Debug: ถ้า Error บ่อย ให้บอสลองใส่ print(e) ใน Terminal ของ Streamlit Cloud
