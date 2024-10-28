import json
import pandas as pd
from pandas import json_normalize


with open('./taylor_swift_original.json', 'r') as file:
    data = json.load(file)

# Print the data
#print(data)

df = pd.read_json('taylor_swift_original.json')

#df = pd.read_json(data)

print(df.head(5))

df_c=df.columns
print(df_c)

# Normalizar la estructura
tracks_normalized = json_normalize(
    data,
    record_path=['albums', 'tracks'],
    meta=[
        'artist_id',
        'artist_name',
        'artist_popularity',
        ['albums', 'album_id'],
        ['albums', 'album_name'],
        ['albums', 'album_release_date'],
        ['albums', 'album_total_tracks']
    ]
)
print(tracks_normalized)
print(tracks_normalized.columns)

tracks_normalized.columns = tracks_normalized.columns.str.replace('albums.', 'album_', regex=False)
print(tracks_normalized)
print(tracks_normalized.columns)
# Renombrar las columnas directamente
tracks_normalized.rename(columns={
    'album_album_id': 'album_id',
    'album_album_name': 'album_name',
    'album_album_release_date': 'album_release_date',
    'album_album_total_tracks': 'album_total_tracks'
}, inplace=True)

# Mostrar el resultado
print(tracks_normalized)
print(tracks_normalized.columns)

# Guardar el DataFrame como CSV
csv_file_path = './tracks_data.csv'  # Ruta donde quieres guardar el archivo
tracks_normalized.to_csv(csv_file_path, index=False)
print(f"DataFrame guardado como CSV en: {csv_file_path}")
