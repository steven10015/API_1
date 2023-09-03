#%%
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt

# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Inicialize Spotify library
client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Make API Request
artist_ID = '6qqNVTkY8uBg9cP3Jd7DAH'
artist_top_tracks_request = spotify.artist_top_tracks(artist_ID)

if artist_top_tracks_request:
    tracks = artist_top_tracks_request["tracks"]
    tracks = [{i: (v/(1000*60))%60 if i == 'duration_ms' else v for i, v in track.items() if i in ['name', 'popularity', 'duration_ms']} for track in tracks]

#Transform to Pandas DataFrame
tracks_df = pd.DataFrame.from_records(tracks)
tracks_df.sort_values('popularity', ascending = False)
print(tracks_df.head(3))

#Analyze statistical relationship
x = tracks_df['duration_ms']
y = tracks_df['popularity']
plt.scatter(x, y,)
plt.xlabel('Duration (ms)')
plt.ylabel('Popularity')
plt.title('Popularity vs Duration')
plt.show()

print("We can infer from the fig that there is not relationship between\npopularity and duration of the track. We can see that different durations\nof the songs has the same popularity and the less popular and the most popular\nare outsiders")
# %%
