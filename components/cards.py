import streamlit as st

from components.api import explain


def movie_card(movie):

    with st.container(border=True):

        st.subheader(movie.get("title", "Unknown"))

        c1, c2 = st.columns(2)

        with c1:
            st.write("🎬", movie.get("type", "-"))
            st.write("⭐", movie.get("rating", "-"))

        with c2:
            st.write("🎭", movie.get("genre", "-"))

            similarity = movie.get("similarity", 0)
            st.progress(float(similarity))
            st.caption(f"{similarity:.1%} Similar")

        imdb_url = movie.get("imdb_url")

        st.write("DEBUG:", imdb_url)

        if imdb_url:
             st.link_button("🎬 View on IMDb", imdb_url)
        
        with st.expander("🧠 Why recommended?"):

            try:
                x = explain(movie["title"])

                st.write(f"**Cluster:** {x['cluster']}")
                st.write(f"**Genre:** {x['genre']}")
                st.write(f"**Rating:** {x['rating']}")
                st.write(f"**Reason:** {x['reason']}")

            except Exception:
                st.warning("Explanation unavailable.")