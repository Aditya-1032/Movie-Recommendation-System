import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}'

    params = {
        'api_key': st.secrets["TMDB_API_KEY"],
        'language': 'en-US'
    }

    try:
        response = requests.get(url, params=params, timeout=30)

        print("Movie ID:", movie_id)
        print("Status:", response.status_code)

        response.raise_for_status()

        data = response.json()

        if data.get('poster_path'):
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

        return None

    except requests.exceptions.RequestException as e:
        print("TMDB Error:", repr(e))
        return None



def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    recommended_indices = recommendations[movie_index]

    recommended_movies = []
    recommended_movies_posters = []

    for index in recommended_indices:

        movie_id = movies.iloc[index].movie_id

        recommended_movies.append(
            movies.iloc[index].title
        )

        recommended_movies_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

recommendations = pickle.load(
    open('recommendations.pkl', 'rb')
)

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    '🎬 Choose a movie to get recommendations',
    movies['title'].values
)


if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)

            if poster:
                st.image(poster)
            else:
                st.write("Poster unavailable")
