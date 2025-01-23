import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Spotify API credentials
CLIENT_ID = ''
CLIENT_SECRET = ''

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

# Function to fetch tracks by genre
def fetch_songs_by_genre(genre, limit=50):
    """
    Fetch songs from Spotify based on genre.
    :param genre: Spotify-supported genre
    :param limit: Number of songs to fetch (max 50 per API call)
    :return: List of songs with details
    """
    results = sp.recommendations(seed_genres=[genre], limit=limit)
    songs = []
    for track in results['tracks']:
        songs.append({
            "Artist": track['artists'][0]['name'],
            "Song": track['name'],
            "Album": track['album']['name'],
            "Popularity": track['popularity'],
            "Genre": genre
        })
    return songs

# List of genres (example subset, you can expand this)
genres = ["indie", "rock", "pop"]

# Fetch songs for each genre and compile into a dataset
all_songs = []
for genre in genres:
    print(f"Fetching songs for genre: {genre}")
    all_songs.extend(fetch_songs_by_genre(genre))

# Convert to DataFrame
df = pd.DataFrame(all_songs)

# Save to CSV
df.to_csv("songs_by_genre.csv", index=False)

print("Dataset saved to 'songs_by_genre.csv'")
