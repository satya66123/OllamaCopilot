import streamlit as st
import ollama

st.title("🤖 OllamaCopilot")

user_input = st.text_input("Ask something")

if st.button("Send"):
    response = ollama.chat(
        model="phi3",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    st.write(response["message"]["content"])