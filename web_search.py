import streamlit as st

from ddgs import DDGS

# ------------------------------------
# PAGE CONFIG
# ------------------------------------

st.set_page_config(
    page_title="Web Search",
    page_icon="🌐",
    layout="wide"
)

# ------------------------------------
# SEARCH FUNCTION
# ------------------------------------

def search_web(
        query,
        max_results=10
):

    results = []

    try:

        with DDGS() as ddgs:

            for item in ddgs.text(
                    query,
                    max_results=max_results
            ):

                results.append(
                    item
                )

    except Exception as e:

        st.error(
            f"Search Error: {e}"
        )

    return results


# ------------------------------------
# UI
# ------------------------------------

st.title(
    "🌐 Web Search"
)

query = st.text_input(
    "Search Internet"
)

max_results = st.slider(
    "Results",
    1,
    20,
    5
)

if st.button(
    "Search"
):

    if query:

        results = search_web(
            query,
            max_results
        )

        st.success(
            f"Found {len(results)} results"
        )

        for i, result in enumerate(
                results,
                start=1
        ):

            with st.expander(
                    f"{i}. {result['title']}"
            ):

                st.write(
                    result["body"]
                )

                st.link_button(
                    "Open Website",
                    result["href"]
                )

    else:

        st.warning(
            "Enter a search query"
        )