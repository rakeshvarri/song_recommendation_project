import streamlit as st
import pandas as pd
import pickle

# Streamlit UI
st.title('Song Recommendation System')

df = pickle.load(open(r"C:\Users\Rakesh varri\Downloads\song_recommendation_project\songs.pkl", 'rb'))

# Load the pickle file
# Use raw string for file path or double backslashes
similarity = pickle.load(open(r"C:\Users\Rakesh varri\Downloads\song_recommendation_project\song_clustering_model.pkl", 'rb'))

# Input for song title
user_song = st.text_input("Enter the song title:")

if st.button('Get Recommendations'):
    if user_song in df['Title'].values:
        # Find the cluster of the user song
        cluster = df[df['Title'] == user_song]['cluster'].values[0]
        st.write(f'The song is in cluster {cluster}')

        # Get all songs in the same cluster
        recommended_songs = df[df['cluster'] == cluster][['Title', 'Genre', 'Popularity']]

        # Sort by popularity and select the top 10 songs
        top_10_songs = recommended_songs.sort_values(by='Popularity', ascending=False).head(10)

        st.write('Top 10 Popular Songs in the Same Cluster:')
        st.dataframe(top_10_songs)
    else:
        st.write("Invalid song title. Please enter a valid song.")
