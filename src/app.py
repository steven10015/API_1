import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()


# Spotify API credentials
client_id = os.environ.get("SPOTIFY_CLIENT")
client_secret = os.environ.get("SPOTIFY_SECRET")

# Configura la autenticación con Spotify usando las credenciales de la app.
# auth_manager se encarga de obtener el token de acceso para la API.
# spotify es el objeto que usamos para hacer todas las llamadas a la API de Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

# Buscar el artista por nombre en la API de Spotify.
# spotify.search devuelve un diccionario con resultados de artistas, álbumes o tracks según el tipo.
# Tomamos el primer artista de la lista de resultados y obtenemos su ID único en Spotify.
artist_name = "jesus adrian romero"
result = spotify.search(q=f"artist:{artist_name}", type="artist")
artist = result['artists']['items'][0]
artist_id = artist['id']
print(f"Artist: {artist['name']} | ID: {artist_id}")

# Top tracks (en US)
top_tracks = spotify.artist_top_tracks(artist_id, country='US')


# Guardar en lista de diccionarios
tracks_list = []
for track in top_tracks['tracks']:
    tracks_list.append({
        "name": track['name'],
        "album": track['album']['name'],
        "popularity": track['popularity'],
        "duration_ms": track['duration_ms']
    })

# Crear un DataFrame de pandas a partir de la lista de tracks obtenida de Spotify
df_tracks = pd.DataFrame(tracks_list)

# Convertir la duración de milisegundos a segundos para facilitar el análisis
df_tracks["duration_sec"] = df_tracks["duration_ms"] / 1000

# Mostrar el DataFrame resultante con la información de los tracks
print(df_tracks)

# Graficar un scatter plot para analizar la relación entre duración y popularidad de los tracks
# Cada punto representa una canción: eje X → duración en segundos, eje Y → popularidad
# s=100 define el tamaño de los puntos y alpha=0.6 hace los puntos semi-transparentes
plt.figure(figsize=(10,6))
plt.scatter(df_tracks["duration_sec"], df_tracks["popularity"], color="green", s=100, alpha=0.6)
plt.xlabel("Duración (segundos)")
plt.ylabel("Popularidad")
plt.title(f"Duración vs Popularidad de Top Tracks de {artist_name}")
plt.grid(True)
plt.show()