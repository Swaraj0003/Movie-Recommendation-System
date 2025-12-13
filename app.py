import streamlit as st
from src.data_loader import load_data
from src.recommender import create_similarity_matrix, recommend_movies
from src.ui_components import display_movie_card

st.set_page_config(page_title="Movie Recommender", layout="wide")


df = load_data(r"C:\Users\USER\Desktop\swaraj_data_science_project\Movie_recommentation_system\data\movies_with_posters.csv")
similarity_matrix = create_similarity_matrix(df)


st.title("🎬 Movie Recommendation System")

col1, col2, col3 = st.columns([1, 2, 1])  
with col2:
    selected_movie = st.selectbox("Select a Movie", df['title'].values)
    top_n = st.slider("Number of Recommendations", 1, 10, 5)

st.markdown("---")  


if selected_movie:
    st.subheader(f"Because you liked **{selected_movie}**, you may also enjoy:")
    recommendations = recommend_movies(selected_movie, df, similarity_matrix, top_n=top_n)

    
    cols_per_row = 4
    for i in range(0, len(recommendations), cols_per_row):
        row_cols = st.columns(cols_per_row)
        for j, (_, row) in enumerate(recommendations.iloc[i:i+cols_per_row].iterrows()):
            with row_cols[j]:
                display_movie_card(row['title'], row['genres'], row['plot'], row['img'])
