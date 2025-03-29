import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load environment variables
load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

# Initialize Spotipy with a longer timeout
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager, requests_timeout=30)

# Test connection
try:
    result = sp.search(q="Coldplay", type="artist")
    print("Connected successfully! Found artist:", result['artists']['items'][0]['name'])
except Exception as e:
    print("Error:", e)

# Get Drake's Top Tracks
artist_id = "3TVXtAsR1Inumwj472S9r4"
tracks = []

try:
    response = sp.artist_top_tracks(artist_id)
    if response:
        tracks = [{k: (v / (1000 * 60)) % 60 if k == "duration_ms" else v 
                   for k, v in track.items() 
                   if k in ["name", "popularity", "duration_ms"]} 
                  for track in response["tracks"]]
    else:
        print("No response from API.")
except Exception as e:
    print(f"Error fetching top tracks: {e}")

# Check if data was retrieved
if not tracks:
    print("No tracks found for the artist.")
    exit()

# Convert to Pandas DataFrame
tracks_df = pd.DataFrame.from_records(tracks)
tracks_df.sort_values(by="popularity", ascending=False, inplace=True)

# Print extracted data
print("Data successfully extracted! Here are the top 3 songs:")
print(tracks_df.head(3))

# Create scatter plot
plt.figure(figsize=(8,6))  
scatter_plot = sns.scatterplot(data=tracks_df, x="popularity", y="duration_ms")
scatter_plot.set_title("Song Popularity vs. Duration")
scatter_plot.set_xlabel("Popularity")
scatter_plot.set_ylabel("Duration (minutes)")

# Save the plot
fig = scatter_plot.get_figure()
fig.savefig("scatter_plot.png")

plt.show()
