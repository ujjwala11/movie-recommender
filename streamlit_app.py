import streamlit as st

from components.sidebar import sidebar
from components.api import recommend, titles
from components.cards import movie_card


def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


st.set_page_config(
    page_title="Netflix Content Intelligence",
    page_icon="🎬",
    layout="wide"
)

load_css()

sidebar()

st.title("🎬 Netflix Content Intelligence")
st.caption("AI-powered Netflix Recommendation Engine")

title = st.selectbox(
    "Choose a title",
    titles()
)

top_n = st.slider(
    "Number of recommendations",
    5,
    20,
    10
)

if st.button("🔍 Recommend", use_container_width=True):

    with st.spinner("Finding similar content..."):

        response = recommend(title, top_n)

    # Handle backend error response
    if response.get("error"):
        st.error(response["message"])

        if response.get("suggestions"):
            st.write("Did you mean:")
            for s in response["suggestions"]:
                st.write(f"• {s}")

    else:
        st.success(f"Found {len(response['recommendations'])} recommendations")

        for movie in response["recommendations"]:
            movie_card(movie)