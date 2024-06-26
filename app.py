import streamlit as st
import pickle
import pandas as pd
import bz2
# import requests
similarity=pickle.load(open('similarity.pkl','rb'))
# def fetch_poster(movie_id):
#     response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6c393321353ae8a6acb30f39092585ba&language=en-US'.format(movie_id))
#     data=response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    # recommended_movies_posters=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetching poster from API
        # recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    "Select a movie for system to recommend other movies",
    movies['title'].values)

st.write("You selected:", selected_movie_name)
if st.button("Recommend"):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
