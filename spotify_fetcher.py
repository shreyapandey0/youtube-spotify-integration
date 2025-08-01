# spotify_fetcher.py

import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import re

# It's better to use environment variables for credentials
client_id = os.getenv("SPOTIFY_CLIENT_ID", "068bf5abd6cc43d9b1cbd8444c954967")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", "7b2863aff86544089af1e6403f88e4ef")

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
))

def clean_title(title):
    """Clean YouTube title to improve Spotify search results"""
    # Remove anything in brackets or parentheses - these often confuse the search
    title = re.sub(r'[\(\[].*?[\)\]]', '', title)
    # Remove common suffixes that are usually not part of the song title
    for suffix in ['official video', 'official music video', 'lyrics', 'mv', 'hd']:
        title = title.lower().replace(suffix, '')
    return title.strip()

def search_spotify_track(query, retries=3):
    """Search for a track on Spotify with retry logic"""
    cleaned_query = clean_title(query)
    
    for attempt in range(retries):
        try:
            result = sp.search(q=cleaned_query, type='track', limit=1, market='US')
            if result['tracks']['items']:
                track = result['tracks']['items'][0]
                return {
                    "Spotify Title": track['name'],
                    "Artist": track['artists'][0]['name'],
                    "Album": track['album']['name'],
                    "Release Date": track['album']['release_date'],
                    "Spotify URL": track['external_urls']['spotify'],
                    "Popularity": track['popularity'],
                    "Duration (ms)": track['duration_ms']
                }
            else:
                # Try again with original query if cleaned version didn't work
                if attempt < retries - 1 and cleaned_query != query:
                    time.sleep(1)
                    continue
                return {
                    "Spotify Title": "Not Found",
                    "Artist": "",
                    "Album": "",
                    "Release Date": "",
                    "Spotify URL": "",
                    "Popularity": "",
                    "Duration (ms)": ""
                }
        except Exception as e:
            print(f"Uh-oh, Spotify search error (attempt {attempt + 1}): {str(e)}")
            time.sleep(2)
            continue
    
    return {
        "Spotify Title": "Error",
        "Artist": "",
        "Album": "",
        "Release Date": "",
        "Spotify URL": "",
        "Popularity": "",
        "Duration (ms)": ""
    }
