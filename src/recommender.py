from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def create_similarity_matrix(df):
    # Combine genres and plot for similarity
    df['content'] = df['genres'].apply(lambda x: ' '.join(x)) + ' ' + df['plot']
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['content'])
    return cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_movies(title, df, similarity_matrix, top_n=5):
    idx = df[df['title'].str.lower() == title.lower()].index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]
    return df.iloc[movie_indices]
