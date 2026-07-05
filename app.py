import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="JARVIS-X", layout="centered")

# --- ดึง API Key แบบระมัดระวัง ---
api_key = st.secrets.get("GOOGLE_API_KEY", "").strip() # .strip() ช่วยลบช่องว่างที่อาจติดมา

if not api_key:
    st.error("บอสยังไม่ได้ใส่ API Key ใน Secrets!")
    st.stop()

# พยายามเชื่อมต่อโมเดล
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"การตั้งค่าโมเดลผิดพลาด: {e}")
    st.stop()

# --- CSS โฮโลแกรมเหมือนเดิม ---
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

# --- UI ---
st.markdown('<div class="holo-box"><h1>JARVIS-X SYSTEM</h1><p>PROTOCOL ONLINE</p></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center;"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJw_EJsDjFwVDtWxMW0nTQ_A5r4mxFrEWpa4Xe9inoeQ&s=10" width="120" style="border-radius:50%; border:2px solid #00e5ff;"></div>', unsafe_allow_html=True)

# --- Chat Logic ---
if "messages" not in st.session_state: st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]): st.write(msg["content"])

if prompt := st.chat_input("Input Command..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.write(prompt)
    
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"API Key หรือโปรเจกต์นี้ใช้งานไม่ได้ (Error: {e})")
