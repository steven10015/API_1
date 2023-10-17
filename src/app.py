import os
import spotipy
import pandas as pd
import seaborn as sns
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
load_dotenv()


client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")


lz_uri = 'spotify:artist:2IMZYfNi21MGqxopj9fWx8'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(lz_uri)

def segundos_minutos(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60
    return f"{minutos}:{segundos}"

top_track = []

for track in results['tracks'][:10]:
    duracion = round(track['duration_ms']/1000)

    top_track.append(dict(track))

    print(f"Nombre de la canción: {track['name']}, popularidad: {track['popularity']}, duración: {segundos_minutos(duracion)} minutos.")

    
df = pd.DataFrame(top_track, columns=['name', 'popularity', 'duration_ms'])
df['duration_ms'] = (df['duration_ms']/1000).round()
df['duracion_min'] = df.duration_ms.apply(segundos_minutos)
df_ordenado = df.sort_values('popularity',ascending=False).head()

df_final = pd.DataFrame(df_ordenado,columns=['name', 'popularity', 'duracion_min'])

df_final

scatter_plot = sns.scatterplot(data = df_final, x= df_final['duracion_min'] , y = df_final['popularity'])
fig = scatter_plot.get_figure()
fig.savefig("scatter_plot.png")
print('A mayor duración de la canción menor es su popularidad en este caso')


"Al printarlo en python me salta error, en jupyter no"