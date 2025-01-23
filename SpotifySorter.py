import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

# Spotify API credentials
CLIENT_ID = 'f3b759b378fa42118fc1819833f65b06'  # Replace with your Spotify Client ID
CLIENT_SECRET = 'c4aab459f4ca4f3e8b5b1d705b921499'  # Replace with your Spotify Client Secret

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

# Function to fetch song popularity
def get_song_data(artist, song):
    """
    Fetches the popularity of a song by an artist from Spotify.
    :param artist: Name of the artist
    :param song: Name of the song
    :return: Popularity score (0-100) or None if not found
    """
    try:
        results = sp.search(q=f"track:{song} artist:{artist}", type='track', limit=1)
        if results['tracks']['items']:
            track_info = results['tracks']['items'][0]
            return track_info['popularity']
    except Exception as e:
        print(f"Error fetching data for {song} by {artist}: {e}")
    return None

# Load your dataset
songs = 'indie_alt_music_data.csv'  # Replace with your dataset file path
df = pd.read_csv(songs)

print("Columns in dataset:", df.columns)

# Ensure the dataset has the required columns
if 'Song' not in df.columns or 'Artist' not in df.columns:
    raise ValueError("Dataset must have 'Song' and 'Artist' columns")

# Add a column for popularity, with a delay to avoid hitting API rate limits
df['Popularity'] = df.apply(lambda row: get_song_data(row['Artist'], row['Song']), axis=1)
time.sleep(0.05)  # Add delay between requests

# Drop rows where popularity is None (optional)
df = df.dropna(subset=['Popularity'])

# Sort the dataset by popularity (highest first)
df_sorted = df.sort_values(by='Popularity', ascending=False)

# Save the updated and sorted dataset to a new CSV file
output_path = 'sorted_dataset_with_popularity.csv'
df_sorted.to_csv(output_path, index=False)

print(f"Updated and sorted dataset saved to '{output_path}'")