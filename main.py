import streamlit as st
import pickle
import pandas as pd


def getMovie(movie):
    movie = movie_dict[movie_dict['title'] == movie.lower()].index[0]
    distance = similairity[movie]
    movie_list = sorted(list(enumerate(distance)),
                        reverse=True, key=lambda x: x[1])[1:6]
    recommended = []
    for i in movie_list:
        recommended.append(movie_dict.iloc[i[0]].title)
    return recommended


movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similairity = pickle.load(open('similairity.pkl', 'rb'))
movie_dict = pd.DataFrame(movie_dict)
movie_name = movie_dict['title'].apply(lambda x: x.title()).values

st.title("Movie Recommendation")
option = st.selectbox(
    'Write Movie Name',
    movie_name)

if st.button("Recommend"):
    recommended = getMovie(option)
    for i in recommended:
        st.write(i)
