import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def fetch_info(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    info = []
    info.append(data['original_title'])
    info.append(data['overview'])
    info.append(data['release_date'])
    info.append(data['vote_average'])
    return info
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:11]
    recommended_movies = []
    recommended_movies_poster = []
    recommended_movies_info=[]
    for i in movies_list:
        movie_id = movies.movie_id[i[0]]
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_info.append(fetch_info(movie_id))
        # Fetch Poster from API
        recommended_movies.append(movies.title[i[0]])
    return recommended_movies, recommended_movies_poster, recommended_movies_info

movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

st.image('https://getwallpapers.com/wallpaper/full/9/9/a/1283451-movie-wallpapers-for-desktop-1920x1080-free-download.jpg')

selected_movie_name = st.selectbox(
    'Which Movies Do you want to Watch?',
    movies['title'].values)

if st.button('Recommend Similar Movies'):
    names, poster, info = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(names[0])
        st.image(poster[0])
        with st.expander("Movie Info"):
            st.write(info[0][0])
            st.write(info[0][1])
            st.write(info[0][2])
            st.write(info[0][3])
    with col2:
        st.header(names[1])
        st.image(poster[1])
        with st.expander("Movie Info"):
            st.write(info[1][0])
            st.write(info[1][1])
            st.write(info[1][2])
            st.write(info[1][3])
    with col3:
        st.header(names[2])
        st.image(poster[2])
        with st.expander("Movie Info"):
            st.write(info[2][0])
            st.write(info[2][1])
            st.write(info[2][2])
            st.write(info[2][3])
    with col4:
        st.header(names[3])
        st.image(poster[3])
        with st.expander("Movie Info"):
            st.write(info[3][0])
            st.write(info[3][1])
            st.write(info[3][2])
            st.write(info[3][3])
    with col5:
        st.header(names[4])
        st.image(poster[4])
        with st.expander("Movie Info"):
            st.write(info[4][0])
            st.write(info[4][1])
            st.write(info[4][2])
            st.write(info[4][3])
    col6, col7, col8, col9, col10 = st.columns(5)
    with col1:
        st.header(names[5])
        st.image(poster[5])
        with st.expander("Movie Info"):
            st.write(info[5][0])
            st.write(info[5][1])
            st.write(info[5][2])
            st.write(info[5][3])
    with col2:
        st.header(names[6])
        st.image(poster[6])
        with st.expander("Movie Info"):
            st.write(info[6][0])
            st.write(info[6][1])
            st.write(info[6][2])
            st.write(info[6][3])
    with col3:
        st.header(names[7])
        st.image(poster[7])
        with st.expander("Movie Info"):
            st.write(info[7][0])
            st.write(info[7][1])
            st.write(info[7][2])
            st.write(info[7][3])
    with col4:
        st.header(names[8])
        st.image(poster[8])
        with st.expander("Movie Info"):
            st.write(info[8][0])
            st.write(info[8][1])
            st.write(info[8][2])
            st.write(info[8][3])
    with col5:
        st.header(names[9])
        st.image(poster[9])
        with st.expander("Movie Info"):
            st.write(info[9][0])
            st.write(info[9][1])
            st.write(info[9][2])
            st.write(info[9][3])

st.title("Thanks You for visiting")


