# recommendation_engine/preprocess.py

import pandas as pd
import numpy as np

def preprocess(data_dir):
    # Load the raw data files
    interactions = pd.read_csv(data_dir / 'raw/user_song_interactions.csv')
    songs = pd.read_csv(data_dir / 'raw/songs.csv')
    users = pd.read_csv(data_dir / 'raw/users.csv')

    # Merge the interactions and songs data.
    interactions = interactions.merge(songs, on='song_id')

    # Convert the song_release_date column to a datetime object
    interactions['song_release_date'] = pd.to_datetime(interactions['song_release_date'])

    # Create a year column from the song_release_date column
    interactions['year'] = interactions['song_release_date'].dt.year

    # Filter the interactions data to only include songs released after 2010
    interactions = interactions[interactions['year'] > 2010]

    # Create a user-item interaction matrix
    user_item_matrix = interactions.pivot_table(index='user_id', columns='song_id', values='play_count', fill_value=0)

    # Create a song feature matrix
    song_features = songs.set_index('song_id')[['artist', 'duration', 'year']]

    # Create a user feature matrix
    user_features = users.set_index('user_id')[['age', 'gender']]

    # Save the processed data to files
    np.savez(data_dir / 'processed/user_item_matrix.npz', user_item_matrix)
    np.savez(data_dir / 'processed/song_features.npz', song_features)
    np.savez(data_dir / 'processed/user_features.npz', user_features)
