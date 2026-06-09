import streamlit as st

from database.db import (
    get_total_users,
    get_all_users,
    get_total_chats_admin
)

from database.vector_db import (
    get_document_count_admin
)

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="👑",
    layout="wide"
)

st.title(
    "👑 Admin Dashboard"
)

col1, col2, col3 = (
    st.columns(3)
)

with col1:

    st.metric(
        "Users",
        get_total_users()
    )

with col2:

    st.metric(
        "Chats",
        get_total_chats_admin()
    )

with col3:

    st.metric(
        "Documents",
        get_document_count_admin()
    )

st.divider()

import pandas as pd

st.subheader(
    "👥 All Users"
)

users = get_all_users()

if users:

    df = pd.DataFrame(
        users,
        columns=[
            "ID",
            "Username",
            "Role"
        ]
    )

    st.dataframe(
        df.drop(
            columns=["ID"]
        ),
        hide_index=True,
        use_container_width=True
    )

else:

    st.info(
        "No Users Found"
    )