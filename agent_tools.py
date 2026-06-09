import streamlit as st
import platform
import socket

from datetime import datetime

st.set_page_config(
    page_title="AI Agent Tools",
    page_icon="🤖",
    layout="wide"
)

st.title(
    "🤖 AI Agent Tools"
)

tool = st.sidebar.selectbox(
    "Select Agent",
    [
        "Calculator",
        "Current Time",
        "System Info",
        "Hostname",
        "PDF Summarizer",
        "Resume Analyzer",
        "CSV Analyzer",
        "Email Writer",
        "Code Generator",
        "SQL Agent",
        "File Explorer",
        "Web Search Agent"
    ]
)

# -----------------------------------
# Calculator
# -----------------------------------

if tool == "Calculator":

    st.header(
        "🧮 Calculator"
    )

    expression = st.text_input(
        "Enter Expression"
    )

    if st.button(
        "Calculate"
    ):

        try:

            result = eval(
                expression
            )

            st.success(
                result
            )

        except Exception as e:

            st.error(
                str(e)
            )

# -----------------------------------
# Current Time
# -----------------------------------

elif tool == "Current Time":

    st.header(
        "⏰ Current Time"
    )

    if st.button(
        "Get Time"
    ):

        st.info(
            datetime.now()
        )

# -----------------------------------
# System Info
# -----------------------------------

elif tool == "System Info":

    st.header(
        "💻 System Info"
    )

    if st.button(
        "Get System Info"
    ):

        st.write(
            f"OS: {platform.system()}"
        )

        st.write(
            f"Version: {platform.version()}"
        )

        st.write(
            f"Machine: {platform.machine()}"
        )

        st.write(
            f"Processor: {platform.processor()}"
        )

# -----------------------------------
# Hostname
# -----------------------------------

elif tool == "Hostname":

    st.header(
        "🌐 Hostname"
    )

    if st.button(
        "Get Hostname"
    ):

        st.success(
            socket.gethostname()
        )
