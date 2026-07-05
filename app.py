import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="JARVIS-X Protocol", layout="centered")

# 2. ตั้งค่า API
api_key = st.secrets.get("GOOGLE_API_KEY")
if not api_key:
    st.error("ตั้งค่า GOOGLE_API_KEY ใน Secrets ครับบอส!")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. CSS ไฮเทคแบบ Hologram Grid (นี่คือหัวใจของความล้ำ!)
st.markdown("""
    <style>
        /* สร้างพื้นหลังเป็นเส้นตาราง Grid เรืองแสง */
        [data-testid="stAppViewContainer"] { 
            background-color: #050a12;
            background-image: 
                linear-gradient(rgba(0, 229, 255, 0.1) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 229, 255, 0.1) 1px, transparent 1px);
            background-size: 40px 40px;
            color: #00e5ff; font-family: 'Orbitron', sans-serif; 
        }
        .holo-frame { 
            border: 1px solid #00e5ff; padding: 25px; border-radius: 10px;
            background: rgba(10, 25, 47, 0.8); box-shadow: 0 0 20px rgba(0, 229, 255, 0.3);
            text-align: center; margin-bottom: 20px;
        }
        .parrot-img { 
            width: 150px; border-radius: 50%; border: 2px solid #00e5ff;
            filter: drop-shadow(0 0 10px #00e5ff);
        }
        /* ปรับสีช่องพิมพ์ให้เข้ากับธีม */
        .stChatInput { border: 2px solid #00e5ff !important; background: #000 !important; }
    </style>
""", unsafe_allow_html=True)

# 4. UI Layout
st.markdown('<div class="holo-frame">', unsafe_allow_html=True)
st.markdown("<h1 style='color:#64ffda; text-shadow: 0 0 10px #64ffda;'>JARVIS-X SYSTEM</h1>", unsafe_allow_html=True)
st.markdown('<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJw_EJsDjFwVDtWxMW0nTQ_A5r4mxFrEWpa4Xe9inoeQ&s=10" class="parrot-img">', unsafe_allow_html=True)
st.markdown('<p style="color:#ffffff; font-size: 0.8rem;">TACTICAL PROTOCOL: ACTIVE</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 5. Chat Logic
if "messages" not in st.session_state: st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(f"<span style='color: {'#ffffff' if msg['role']=='user' else '#00e5ff'};'>{msg['content']}</span>", unsafe_allow_html=True)

if prompt := st.chat_input("Command..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"<span style='color: #ffffff;'>{prompt}</span>", unsafe_allow_html=True)
    
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(f"<span style='color: #00e5ff;'>{response.text}</span>", unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception:
            st.error("ระบบติดขัดเล็กน้อย")
