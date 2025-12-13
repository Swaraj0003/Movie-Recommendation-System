import streamlit as st

def display_movie_card(title, genres, plot, img_url):
    st.image(f"https://image.tmdb.org/t/p/w500{img_url}", width=200)
    st.subheader(title)
    st.caption(", ".join(genres))
    st.write(plot)
