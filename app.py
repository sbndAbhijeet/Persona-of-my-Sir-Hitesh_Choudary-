import streamlit as st
from backend.chat_handler import get_gemini_response
import base64


st.set_page_config(page_title="Gemini-Chat", layout="centered")

def set_background(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white;
        }}
        </style>
    """, unsafe_allow_html=True)

set_background("images/whatsapp_dark_bg.jpg")

st.markdown("""
    <style>
    .message-bubble {
        padding: 12px 18px;
        border-radius: 18px;
        margin-bottom: 12px;
        max-width: 80%;
        word-wrap: break-word;
        font-size: 16px;
        line-height: 1.5;
        color: white;
    }
    .user-bubble {
        background-color: #2e7d32;
        margin-left: auto;
        text-align: left;
    }
    .bot-bubble {
        background-color: #424242;
        margin-right: auto;
        text-align: left;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💬 Chat with Hitesh")

# Init session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'pending_prompt' not in st.session_state:
    st.session_state.pending_prompt = None

# Display messages
for msg in st.session_state.messages:
    if msg['role'] == 'user':
        col1, col2 = st.columns([1, 9])
        with col1:
            st.image("images/user.png", width=64)
        with col2:
            st.markdown(f'<div class="message-bubble user-bubble">{msg["parts"]}</div>', unsafe_allow_html=True)
    else:
        col1, col2 = st.columns([9, 1])
        with col1:
            st.markdown(f'<div class="message-bubble bot-bubble">{msg["parts"]}</div>', unsafe_allow_html=True)
        with col2:
            st.image("images/hitesh.png", width=64)

prompt = st.chat_input("Ask anything to sir...")

if prompt:
    st.session_state.messages.append({'role': 'user', 'parts': prompt})
    st.session_state.pending_prompt = prompt
    st.rerun()

if st.session_state.pending_prompt:
    response = get_gemini_response(st.session_state.pending_prompt)
    st.session_state.messages.append({'role': 'model', 'parts': response})
    st.session_state.pending_prompt = None
    st.rerun()

