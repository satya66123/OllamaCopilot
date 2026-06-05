import streamlit as st
import ollama
from datetime import datetime
import os

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="OllamaCopilot",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# Create Chats Folder
# --------------------------------------------------

if not os.path.exists("chats"):
    os.makedirs("chats")

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_title" not in st.session_state:
    st.session_state.chat_title = "New Conversation"

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("🤖 OllamaCopilot")

model = st.sidebar.selectbox(
    "Select Model",
    [
        "phi3:latest",
        "llama3:8b",
        "llama3:instruct",
        "llama3.1:8b",
        "qwen3:8b",
        "gemma3:4b",
        "mistral:latest",
        "deepseek-coder:latest"
    ],
    index=0
)

# Statistics
st.sidebar.subheader("📊 Statistics")

total_messages = len(st.session_state.messages)

user_messages = len(
    [m for m in st.session_state.messages
     if m["role"] == "user"]
)

st.sidebar.write(f"Total Messages: {total_messages}")
st.sidebar.write(f"User Messages: {user_messages}")

# Current Chat
st.sidebar.subheader("💬 Current Chat")
st.sidebar.write(st.session_state.chat_title)

# Export Chat
st.sidebar.subheader("📤 Export")

chat_text = ""

for msg in st.session_state.messages:
    chat_text += (
        f"{msg['role'].upper()}:\n"
        f"{msg['content']}\n\n"
    )

st.sidebar.download_button(
    label="⬇ Download Chat",
    data=chat_text,
    file_name="conversation.txt",
    mime="text/plain"
)

# Save Chat
if st.sidebar.button("💾 Save Chat"):

    filename = (
        f"chats/chat_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        for msg in st.session_state.messages:

            f.write(
                f"{msg['role'].upper()}:\n"
            )

            f.write(
                f"{msg['content']}\n\n"
            )

    st.sidebar.success("Chat Saved Successfully")

# History
st.sidebar.subheader("📝 History")

history_items = [
    m for m in st.session_state.messages
    if m["role"] == "user"
]

if history_items:

    for i, msg in enumerate(
            history_items[-10:],
            start=1):

        st.sidebar.write(
            f"{i}. {msg['content'][:30]}"
        )

else:
    st.sidebar.write("No history yet")

# New Conversation
if st.sidebar.button("🆕 New Conversation"):

    st.session_state.messages = []
    st.session_state.chat_title = "New Conversation"

    st.rerun()

# --------------------------------------------------
# Main Screen
# --------------------------------------------------

st.title("🤖 OllamaCopilot")

# Display Messages

for message in st.session_state.messages:

    with st.chat_message(
            message["role"]):

        st.markdown(
            message["content"]
        )

# --------------------------------------------------
# User Input
# --------------------------------------------------

prompt = st.chat_input(
    "Ask anything..."
)

if prompt:

    # Set Title
    if len(st.session_state.messages) == 0:

        st.session_state.chat_title = (
            prompt[:40]
        )

    # User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    try:

        with st.spinner("Thinking..."):

            response = ollama.chat(
                model=model,
                messages=st.session_state.messages
            )

            ai_response = (
                response["message"]["content"]
            )

    except Exception as e:

        ai_response = (
            f"Error: {str(e)}"
        )

    # Assistant Message

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_response
        }
    )

    with st.chat_message(
            "assistant"):

        st.markdown(
            ai_response
        )

    st.rerun()