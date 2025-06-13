import streamlit as st
import pickle
import pandas as pd
import requests

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")
st.markdown("Get recommendations based on your favorite movie! 🍿")

OMDB_API_KEY = "dd5d7e0e"


def fetch_movie_details(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data.get("Response") == "True":
        return {
            "poster": data.get("Poster", "https://via.placeholder.com/200x300.png?text=No+Image"),
            "plot": data.get("Plot", "Plot not available."),
            "rating": data.get("imdbRating", "N/A")
        }
    else:
        return {
            "poster": "https://via.placeholder.com/200x300.png?text=No+Image",
            "plot": "Plot not available.",
            "rating": "N/A"
        }

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:]

    recommended = []
    for i in movie_list:
        title = movies.iloc[i[0]].title
        details = fetch_movie_details(title)
        recommended.append({
            "title": title,
            "poster": details["poster"],
            "plot": details["plot"],
            "rating": details["rating"]
        })
        if len(recommended) == 8:  # Show max 8 results
            break
    return recommended

# Dropdown for movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox("👥 Choose a movie to get recommendations:", movie_list)

if st.button("🎯 Recommend"):
    
    recommendations = recommend(selected_movie)

    if not recommendations:
        st.warning("No matching movies found for the selected genre.")
    else:
        st.subheader("📽️ Recommended Movies")
        for i in range(0, len(recommendations), 4):
            cols = st.columns(4)
            for col, movie in zip(cols, recommendations[i:i+4]):
                with col:
                    st.image(movie["poster"], use_container_width=True)
                    st.markdown(f"**{movie['title']}**")
                    st.markdown(f"⭐ {movie['rating']}")
                    st.caption(movie["plot"])

# Trending section (static for demo, can be dynamic)
st.markdown("---")
st.subheader("🔥 Trending Movies")
trending_titles = ["Inception", "The Dark Knight", "Interstellar", "The Shawshank Redemption"]
trending_data = [fetch_movie_details(title) | {"title": title} for title in trending_titles]

cols = st.columns(4)
for col, movie in zip(cols, trending_data):
    with col:
        st.image(movie["poster"], use_container_width=True)
        st.markdown(f"**{movie['title']}**")
        st.markdown(f"⭐ {movie['rating']}")
