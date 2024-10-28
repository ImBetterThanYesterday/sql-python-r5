from sqlalchemy import text
from database import creating_engine, creating_session, closing_session, disposing_engine

# Función para obtener la canción más larga
def get_longest_song():
    engine = creating_engine()
    session = creating_session(engine)
    
    try:
        ########## Nombre de la canción mas larga  ################
        longest_song_query = text("""
            SELECT track_name, duration_ms
            FROM dataset
            ORDER BY duration_ms DESC
            LIMIT 1;
        """)
        
        result = session.execute(longest_song_query)
        longest_song = result.fetchone()  # Obtenemos solo la primera fila
        print(f"La canción más larga es: {longest_song.track_name} con duración de {longest_song.duration_ms} ms   \n \n")
    
    finally:
        closing_session(session)
        disposing_engine(engine)

"""
POR CADA ALBUM LA CANCION MAS POPULAR
PERO ES POSIBLE DE QUE HAYA 2 CANCIONES CON LAS POPULARIDAD
ENTRE LAS 2 VOY A ELEGIR LA DE MENOR DURACION
"""
def get_most_popular_song_per_album():
    engine = creating_engine()
    session = creating_session(engine)
    
    try:
        # Consulta para obtener la canción más popular por álbum
        most_popular_song_query = text("""
            WITH ranked_songs AS (
                SELECT 
                    album_id, 
                    track_name, 
                    track_popularity, 
                    duration_ms,
                    ROW_NUMBER() OVER (
                        PARTITION BY album_id 
                        ORDER BY track_popularity DESC, duration_ms ASC
                    ) AS rank
                FROM dataset
            )
            SELECT album_id, track_name, track_popularity, duration_ms
            FROM ranked_songs
            WHERE rank = 1
            ORDER BY track_popularity DESC;
        """)
        
        result = session.execute(most_popular_song_query)
        most_popular_songs = result.fetchall()  # Obtenemos todas las filas
        
        print("\n CANCION MAS POPULAR POR CADA ALBUM : \n ")
        for song in most_popular_songs:
            print(f" Álbum ID: {song.album_id}, Canción: {song.track_name}, Popularidad: {song.track_popularity}, Duración: {song.duration_ms} ms")
    
    finally:
        closing_session(session)
        disposing_engine(engine)

# Ejecutar las funciones
get_longest_song()
get_most_popular_song_per_album()
