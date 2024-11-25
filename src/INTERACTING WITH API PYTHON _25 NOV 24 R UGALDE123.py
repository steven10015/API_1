# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:09:53 2024
INTERACTING WITH API-PYTHON PROJECT.


@author: rober ugalde



client ID

0fc0c0f47f394ed890bf5501fbc48bc6

client secret

8c674905b81c48a0bfca4f16e58164d6
"""

import subprocess
import sys

# List of libraries with versions
libraries = [
    "sqlalchemy==1.4.37",
    "pymysql==1.0.2",
    "pandas>=1.4.2",
    "python-dotenv==0.20.0",
    "psycopg2-binary==2.9.3",
    "requests==2.27.1",
    "spotipy==2.23.0",
    "numpy>=1.18.5",
    "opencv-python>=4.1.2",
    "matplotlib>=3.2.2",
    "ipyleaflet>=0.14.0",
    "sympy>=1.10.1",
    "scikit-learn"
]

def install_library(library):
    """
    Installs a Python library using pip.
    """
    try:
        print(f"Installing {library}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])
        print(f"{library} installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {library}: {e}")

# Install each library
for lib in libraries:
    install_library(lib)

print("All libraries have been installed!")


XXXXXX

import os
from dotenv import load_dotenv
load_dotenv()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')


XXXXX


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

con = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = 0fc0c0f47f394ed890bf5501fbc48bc6,
                                                              client_secret = 8c674905b81c48a0bfca4f16e58164d6))



import spotipy as sp

spotify = sp.Spotify(auth_manager=...)
results = spotify.search(q='track', type='track', limit=10)




artist_id = "3TVXtAsR1Inumwj472S9r4"

response = sp.artist_top_tracks("3TVXtAsR1Inumwj472S9r4")
if response:
  # We keep the "tracks" object of the answer
  tracks = response["tracks"]
  # We select, for each song, the data we are interested in and discard the rest
  tracks = [{k: (v/(1000*60))%60 if k == "duration_ms" else v for k, v in track.items() if k in ["name", "popularity", "duration_ms"]} for track in tracks]




import requests
print(requests.__file__)


conda remove requests
conda install requests


import requests
file_path = r"C:\Users\rober ugalde\anaconda3\Lib\site-packages\requests\__init__.py"
print(file_path)


import requests
file_path = r"C:\Users\rober ugalde\anaconda3\Lib\site-packages\requests\__init__.py"
print(file_path)



artist_id = "3TVXtAsR1Inumwj472S9r4"

response = sp.artist_top_tracks("3TVXtAsR1Inumwj472S9r4")
if response:
  # We keep the "tracks" object of the answer
  tracks = response["tracks"]
  # We select, for each song, the data we are interested in and discard the rest
  tracks = [{k: (v/(1000*60))%60 if k == "duration_ms" else v for k, v in track.items() if k in ["name", "popularity", "duration_ms"]} for track in tracks]



import pandas as pd

tracks_df = pd.DataFrame.from_records(tracks)
tracks_df.sort_values(["popularity"], inplace = True)

print(tracks_df.head(3))



for track in tracks:
    print(track)
    
    

import pkg_resources

installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
if "spotipy" in installed_packages:
    print(f"Spotipy version: {installed_packages['spotipy']}")
else:
    print("Spotipy is not installed.")


pip install spotipy



xxxxx
this one works.


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace with your Spotify API credentials
client_id = "0fc0c0f47f394ed890bf5501fbc48bc6"
client_secret = "8c674905b81c48a0bfca4f16e58164d6"

# Initialize Spotipy
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))

# Test fetching Spotify's featured playlists
results = sp.featured_playlists(limit=5)
for playlist in results['playlists']['items']:
    print(f"Playlist Name: {playlist['name']}")



out:
    
    Playlist Name: Éxitos México
    Playlist Name: Viva Latino
    Playlist Name: La Reina: Éxitos de la Música Mexicana
    Playlist Name: Corridos Tumbados
    Playlist Name: Christmas Hits
    
    
    
xxxx


artist_id = "3TVXtAsR1Inumwj472S9r4"

response = sp.artist_top_tracks("3TVXtAsR1Inumwj472S9r4")
if response:
  # We keep the "tracks" object of the answer
  tracks = response["tracks"]
  # We select, for each song, the data we are interested in and discard the rest
  tracks = [{k: (v/(1000*60))%60 if k == "duration_ms" else v for k, v in track.items() if k in ["name", "popularity", "duration_ms"]} for track in tracks]
  
  
  
xxxx


import pandas as pd

tracks_df = pd.DataFrame.from_records(tracks)
tracks_df.sort_values(["popularity"], inplace = True)

print(tracks_df.head(3))


xxxxx


import seaborn as sns

scatter_plot = sns.scatterplot(data = tracks_df, x = "popularity", y = "duration_ms")
fig = scatter_plot.get_figure()
fig.savefig("scatter_plot.png")


