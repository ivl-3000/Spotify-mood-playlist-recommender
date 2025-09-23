import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from dotenv import load_dotenv

# Load credentials
load_dotenv(".env")
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

# Auth manager
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Example: Get track info
track_id = "3n3Ppam7vgaVa1iaRUc9Lp"  # Mr. Brightside - The Killers
track = sp.track(track_id)

print("Track Name:", track["name"])
print("Artist:", track["artists"][0]["name"])
print("Album:", track["album"]["name"])
print("Release Date:", track["album"]["release_date"])
print("Duration (ms):", track["duration_ms"])
print("Explicit:", track["explicit"])
print("Popularity:", track["popularity"])
