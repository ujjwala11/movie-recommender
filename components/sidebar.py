import streamlit as st
from components.api import stats
from components.api import history

def sidebar():

    st.sidebar.title("🎬 Netflix")

    data = stats()

    st.sidebar.metric(
        "Movies",
        data["movies"]
    )

    st.sidebar.metric(
        "TV Shows",
        data["tv_shows"]
    )

    st.sidebar.metric(
        "Clusters",
        data["clusters"]
    )

    st.sidebar.divider()

    st.sidebar.subheader("Recent Searches")

    searches = history()["recent_searches"]

    if searches:

        for title in searches:

            st.sidebar.write("•", title)

    else:

        st.sidebar.info("No history yet.")