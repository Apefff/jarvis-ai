import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่า API ให้ชัดเจนที่สุด
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("บอสยังไม่ได้ใส่ API Key ในช่อง Secrets ในหน้าตั้งค่าของ Streamlit ครับ!")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. UI ตกแต่ง
st.set_page_config(page_title="JARVIS AI", layout="centered")
st.markdown("<h2 style='text-align:center; color:#00e5ff;'>JARVIS AI SYSTEM</h2>", unsafe_allow_html=True)

# 3. Chat Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

# แสดงแชท
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ช่องพิมพ์คำสั่ง
if prompt := st.chat_input("สั่งการ JARVIS..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
        
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.write(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
