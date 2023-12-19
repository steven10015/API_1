import os
import pandas as pd
import matplotlib.pyplot as plt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv


#import matplotlib
#matplotlib.use('TkAgg')


# Load the .env file variables
load_dotenv()

# Retrieve CLIENT_ID and CLIENT_SECRET from environment variables
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

#if not client_id or not client_secret:
#    raise Exception("CLIENT_ID and CLIENT_SECRET must be set in the environment variables")

# Spotify Client Credentials Authentication
credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(client_credentials_manager=credentials_manager)

# Artist URI
artist_Id = '58zz0VTpGNHn7MGTlW2cxQ'

# Fetching the top tracks of the artist
try:
    results = spotify.artist_top_tracks(artist_Id)

    # Extract track data - Transform to Pandas DataFrame
    tracks_data = [{
        'Name': track['name'],
        'Popularity': track['popularity'],
        'Duration (Minutes)': track['duration_ms'] / 60000,  # Convert milliseconds to minutes
    } for track in results['tracks']]

    # Create a DataFrame and sort by popularity
    df_tracks = pd.DataFrame(tracks_data)
    df_sorted = df_tracks.sort_values(by='Popularity') #sort the songs by increasing popularity
    # display the resulting top 3
    print(df_sorted.tail(3))

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(df_tracks['Duration (Minutes)'], df_tracks['Popularity'])
    plt.title('Track Duration vs. Popularity')
    plt.xlabel('Duration (Minutes)')
    plt.ylabel('Popularity')
    plt.grid(True)

    # Save the plot as an image file
    plt.savefig('scatter_plot.png')
    plt.show()

except spotipy.exceptions.SpotifyException as e:
    print("An error occurred:", e)