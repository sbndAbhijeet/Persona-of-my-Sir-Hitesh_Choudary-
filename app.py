import streamlit as st
from backend.chat_handler import get_gemini_response
import base64

st.set_page_config(page_title="Gemini-Chat", layout="wide")  # Wide layout for side-by-side view

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

# CSS styles for chat bubbles and typing dots animation
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
    @keyframes blink {
        0% { opacity: 0.2; }
        20% { opacity: 1; }
        100% { opacity: 0.2; }
    }
    .dots::after {
        content: '...';
        animation: blink 1.4s infinite;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💬 Chat with Hitesh")

# Initialize session state variables
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'pending_prompt' not in st.session_state:
    st.session_state.pending_prompt = None

if 'thinking_steps' not in st.session_state:
    st.session_state.thinking_steps = []

# Layout with two columns: Chat (left), Thinking steps (right)
col_chat, col_thinking = st.columns([4, 1])

# Chat area
with col_chat:
    # Show chat messages
    for msg in st.session_state.messages:
        if msg['role'] == 'user':
            c1, c2 = st.columns([1, 9])
            with c1:
                st.image("images/user.png", width=64)
            with c2:
                st.markdown(f'<div class="message-bubble user-bubble">{msg["parts"]}</div>', unsafe_allow_html=True)
        else:
            c1, c2 = st.columns([9, 1])
            with c1:
                st.markdown(f'<div class="message-bubble bot-bubble">{msg["parts"]}</div>', unsafe_allow_html=True)
            with c2:
                st.image("images/hitesh.png", width=64)

    # Input box for new prompt
    prompt = st.chat_input("Ask anything to sir...")

    if prompt:
        st.session_state.messages.append({'role': 'user', 'parts': prompt})
        st.session_state.pending_prompt = prompt
        st.session_state.thinking_steps = []  # Clear previous thinking steps
        st.rerun()

    # Show typing indicator and get response
    if st.session_state.pending_prompt:
        typing_placeholder = st.empty()
        typing_placeholder.markdown(
            '<div class="message-bubble bot-bubble">Hitesh is typing<span class="dots"></span></div>',
            unsafe_allow_html=True
        )

        # Call backend to get thinking steps and final answer
        thinking, response = get_gemini_response(st.session_state.pending_prompt)

        typing_placeholder.empty()  # Remove typing indicator

        # Save thinking steps and final response
        st.session_state.thinking_steps = thinking
        st.session_state.messages.append({'role': 'model', 'parts': response})
        st.session_state.pending_prompt = None
        st.rerun()

# Thinking steps area
with col_thinking:
    st.markdown("### 🧠 Model's Thought Process")
    if st.session_state.thinking_steps:
        for step in st.session_state.thinking_steps:
            st.markdown(f"- {step}")
    else:
        st.markdown("_Thinking steps will appear here..._")
