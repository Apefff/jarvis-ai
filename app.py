import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="JARVIS-X", layout="centered")

# 2. API Config
api_key = st.secrets.get("GOOGLE_API_KEY")
if not api_key:
    st.error("บอสยังไม่ได้ใส่ API Key ใน Secrets!")
    st.stop()

genai.configure(api_key=api_key)
# เปลี่ยนมาใช้รุ่นนี้แทน ถ้าอันเดิมหาไม่เจอ
model = genai.GenerativeModel('gemini-1.0-pro')

# 3. CSS โฮโลแกรม
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] { 
            background: #050a12; color: #00e5ff; 
            background-image: linear-gradient(rgba(0,229,255,0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(0,229,255,0.05) 1px, transparent 1px);
            background-size: 40px 40px;
        }
        .holo-box { border: 1px solid #00e5ff; padding: 20px; background: rgba(10,25,47,0.8); text-align: center; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# 4. UI
st.markdown('<div class="holo-box"><h1>JARVIS-X SYSTEM</h1><p>PROTOCOL ONLINE</p></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center;"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJw_EJsDjFwVDtWxMW0nTQ_A5r4mxFrEWpa4Xe9inoeQ&s=10" width="120" style="border-radius:50%; border:2px solid #00e5ff;"></div>', unsafe_allow_html=True)

# 5. Chat Logic แบบเสถียรสุดๆ
if "messages" not in st.session_state: st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]): st.write(msg["content"])

if prompt := st.chat_input("Input Command..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.write(prompt)
    
    with st.chat_message("assistant"):
        try:
            # ใช้ model.generate_content แบบนี้เสถียรที่สุด
            response = model.generate_content(prompt)
            st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("โมเดลขัดข้อง ลองเช็ค API Key ในโปรเจกต์ว่าเปิดใช้งาน Gemini Pro หรือยัง?")
