# OllamaCopilot app.py
# NOTE:
# save_chat() should return cursor.lastrowid in db.py

import streamlit as st
import ollama
from database.db import save_chat, get_all_chats, get_chat_by_id, update_chat, delete_chat, get_chat_titles
import json

st.set_page_config(page_title="OllamaCopilot", page_icon="🤖", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = []
chat_text = ""

for msg in st.session_state.messages:

    chat_text += (
        f"{msg['role']} : "
        f"{msg['content']}\n\n"
    )
messages_json = json.dumps(
    st.session_state.messages
)

if "chat_title" not in st.session_state:
    st.session_state.chat_title = "New Conversation"

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = None

MODELS = [
    "phi3:latest",
    "llama3:8b",
    "llama3:instruct",
    "llama3.1:8b",
    "qwen3:8b",
    "gemma3:4b",
    "mistral:latest",
    "deepseek-coder:latest"
]

st.sidebar.title("🤖 OllamaCopilot")

model = st.sidebar.selectbox("Select Model", MODELS, index=0)

st.sidebar.subheader("📊 Statistics")
st.sidebar.write(f"Messages: {len(st.session_state.messages)}")

st.sidebar.subheader("💬 Current Chat")
st.sidebar.write(st.session_state.chat_title)

chat_text = ""
for msg in st.session_state.messages:
    chat_text += f"{msg['role']} : {msg['content']}\n\n"

st.sidebar.download_button(
    "⬇ Download Chat",
    chat_text,
    "conversation.txt",
    "text/plain"
)

st.sidebar.subheader("📚 Saved Chats")

try:
    chats = get_all_chats()

    for chat in chats:

        c1, c2, c3 = st.sidebar.columns([4, 1, 1])

        with c1:

            if st.button(
                f"{chat[0]} - {chat[1]}",
                key=f"load_{chat[0]}"
            ):

                record = get_chat_by_id(
                    chat[0]
                )

                if record:

                    st.session_state.current_chat_id = (
                        record[0]
                    )

                    st.session_state.chat_title = (
                        record[1]
                    )

                    st.sidebar.success(
                        "Chat Loaded"
                    )

        with c2:

            if st.button(
                "🔄",
                key=f"update_{chat[0]}"
            ):

                chat_text = ""

                for msg in st.session_state.messages:

                    chat_text += (
                        f"{msg['role']} : "
                        f"{msg['content']}\n\n"
                    )

                update_chat(
                    chat[0],
                    st.session_state.chat_title,
                    chat_text,
                    messages_json
                )

                st.sidebar.success(
                    "Chat Updated"
                )

        with c3:

            if st.button(
                "❌",
                key=f"delete_{chat[0]}"
            ):

                delete_chat(
                    chat[0]
                )

                st.rerun()

except Exception as e:

    st.sidebar.error(str(e))


st.sidebar.subheader("📝 History")

try:

    history = get_chat_titles()

    if history:

        for chat in history:

            if st.sidebar.button(
                f"{chat[1]}",
                key=f"history_{chat[0]}"
            ):

                record = get_chat_by_id(
                    chat[0]
                )

                st.session_state.current_chat_id = (
                    record[0]
                )

                st.session_state.chat_title = (
                    record[1]
                )

                st.sidebar.success(
                    f"Loaded {record[1]}"
                )

    else:

        st.sidebar.write(
            "No history found"
        )

except Exception as e:

    st.sidebar.error(str(e))

if st.sidebar.button("🆕 New Conversation"):

    st.session_state.messages = []

    st.session_state.chat_title = (
        "New Conversation"
    )

    st.session_state.current_chat_id = None

    st.rerun()

st.title("🤖 OllamaCopilot")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask anything...")

if prompt:

    if len(st.session_state.messages) == 0:
        st.session_state.chat_title = prompt[:40]

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.spinner("Thinking..."):
        response = ollama.chat(
            model=model,
            messages=st.session_state.messages
        )

        ai_response = response["message"]["content"]

    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })

    chat_text = ""
    for msg in st.session_state.messages:
        chat_text += f"{msg['role']} : {msg['content']}\n\n"

    try:

        if st.session_state.current_chat_id is None:

            inserted_id = save_chat(
                st.session_state.chat_title,
                chat_text,
                messages_json
            )

            st.session_state.current_chat_id = inserted_id

        else:

            update_chat(
                st.session_state.current_chat_id,
                st.session_state.chat_title,
                chat_text,
                messages_json
            )

    except Exception as e:
        st.error(f"Database Error: {e}")

    st.rerun()
