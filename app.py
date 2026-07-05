import streamlit as st
import base64

# --- SET PAGE CONFIG ---
st.set_page_config(page_title="JARVIS AI: Tactical Protocol", layout="wide")

# --- CUSTOM CSS FOR HI-TECH LOOK ---
st.markdown("""
    <style>
        /* Overall Theme */
        [data-testid="stAppViewContainer"] {
            background-color: #050a12; /* Very dark navy/black */
            background-image: 
                radial-gradient(circle at 50% 50%, rgba(14, 39, 79, 0.4) 0%, rgba(5, 10, 18, 0.5) 80%);
            color: #e0e6ed;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #0b1626;
            border-right: 1px solid #1e3a69;
        }
        .stTextInput > div > div > input {
            background-color: #050a12;
            color: #60a5fa; /* Neon Blue */
            border: 1px solid #1e3a69;
            font-family: 'Courier New', Courier, monospace;
        }

        /* Main Title */
        h1.main-title {
            font-family: 'Impact', Charcoal, sans-serif;
            color: #f5e1a4; /* Gold */
            text-align: center;
            text-shadow: 0 0 15px #f5e1a4, 0 0 5px #b59410;
            margin-bottom: -10px;
        }
        p.subtitle {
            color: #9ca3af; /* Grey */
            text-align: center;
            font-size: 0.9rem;
            margin-bottom: 30px;
        }

        /* Digital Overlay Container */
        .digital-container {
            border: 2px solid #1e3a69;
            padding: 20px;
            background-color: rgba(11, 22, 38, 0.6);
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(30, 58, 105, 0.3);
            position: relative;
            text-align: center;
        }
        .digital-overlay-text {
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.7rem;
            color: #60a5fa;
        }
        .overlay-top-left { position: absolute; top: 10px; left: 10px; text-align: left;}
        .overlay-top-right { position: absolute; top: 10px; right: 10px; text-align: right;}

        /* Chat Bubbles */
        .chat-bubble-boss {
            background-color: #1e3a69;
            color: #e0e6ed;
            padding: 10px 15px;
            border-radius: 15px 15px 0 15px;
            margin-bottom: 15px;
            max-width: 80%;
            float: right;
            clear: both;
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.9rem;
        }
        .chat-bubble-jarvis {
            background-color: #374151; /* Medium Grey */
            color: #f5e1a4; /* Gold text for Jarvis */
            padding: 10px 15px;
            border-radius: 15px 15px 15px 0;
            margin-bottom: 15px;
            max-width: 80%;
            float: left;
            clear: both;
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.9rem;
            border-left: 3px solid #f5e1a4;
        }
        .avatar {
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 10px;
        }

        /* Input Area */
        .input-area {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            width: 60%;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
        }
        .stAudioInput > div > button {
            background-color: #1e3a69;
            border: 1px solid #60a5fa;
            color: #60a5fa;
            box-shadow: 0 0 15px rgba(96, 165, 250, 0.5);
        }
        .stAudioInput > div > button:hover {
            background-color: #3b82f6;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# --- DUMMY PARROT IMAGE ---
# (In a real app, you would use an actual image file or generate it)
parrot_image_url = "https://cdn-icons-png.flaticon.com/512/6165/6165557.png" # Placeholder

# --- SIDEBAR ---
api_key = st.sidebar.text_input("Enter API Key", type="password")

# --- MAIN CONTENT ---
st.markdown('<h1 class="main-title">JARVIS AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Urgent Task Protocol</p>', unsafe_allow_html=True)

# Create 3 columns for layout
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    # Digital Overlay Container
    st.markdown(f"""
        <div class="digital-container">
            <div class="digital-overlay-text overlay-top-left">
                Location: Active GPS<br>
                Urgent Status: PENDOT
            </div>
            <div class="digital-overlay-text overlay-top-right">
                Urgent Status: PENDING<br>
                Booking Progress: Ready
            </div>
            <img src="{parrot_image_url}" width="200" style="filter: drop-shadow(0 0 20px #60a5fa);">
            <div class="digital-overlay-text" style="margin-top: 10px;">SYSTEM LINK ACTIVE [GLOBAL]</div>
        </div>
    """, unsafe_allow_html=True)

    st.write("") # Spacer

    # Chat History Simulation
    st.markdown("""
        <div>
            <div>
                <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" class="avatar" style="float:right;">
                <div class="chat-bubble-boss">
                    **BOSS:** "Jarvis, I need an AC tech near me *immediately* for a critical cleaning."
                </div>
            </div>
            <div>
                <img src="https://cdn-icons-png.flaticon.com/512/6165/6165557.png" class="avatar" style="float:left;">
                <div class="chat-bubble-jarvis">
                    **JARVIS:** "Searching local databases, Boss. Locating closest certified urgent AC service... Found 3 technicians with immediate availability within 2 miles."
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.write("") # Spacer
st.write("") # Spacer

# --- FIXED INPUT AREA ---
with st.container():
    st.markdown('<div class="input-area">', unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 5])
    with c1:
        audio_input = st.audio_input(" ", label_visibility="collapsed")
    with c2:
        user_input = st.text_input(" ", placeholder="Command to Book...", label_visibility="collapsed")

    st.markdown('</div>', unsafe_allow_html=True)

if audio_input or user_input:
    st.toast("JARVIS Protocol Engaged. Processing...")
