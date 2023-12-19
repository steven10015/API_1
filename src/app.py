import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load the .env file variables
load_dotenv()

# Retrieve CLIENT_ID and CLIENT_SECRET from environment variables
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

if not client_id or not client_secret:
    raise Exception("CLIENT_ID and CLIENT_SECRET must be set in the environment variables")

# Spotify Client Credentials Authentication
credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(client_credentials_manager=credentials_manager)

# Artist URI
artist_id = '58zz0VTpGNHn7MGTlW2cxQ'

# Fetching the top tracks of the artist
try:
    results = spotify.artist_top_tracks(artist_id)

    # Printing the top 10 tracks with their popularity and duration
    for track in results['tracks'][:10]:
        duration_min = track['duration_ms'] / 60000  # Convert milliseconds to minutes
        print('Track   :', track['name'])
        print('Popularity:', track['popularity'])
        print('Duration:', "{:.2f} minutes".format(duration_min))
        print()
except spotipy.exceptions.SpotifyException as e:
    print("An error occurred:", e)




