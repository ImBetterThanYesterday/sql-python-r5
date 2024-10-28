import pandas as pd
from database import creating_engine, disposing_engine

def load_csv_to_database(csv_file_path: str, table_name: str) -> None:
    """
    Carga un archivo CSV a la base de datos usando las configuraciones
    existentes en database.py
    
    Args:
        csv_file_path (str): Ruta al archivo CSV
        table_name (str): Nombre de la tabla donde se cargarán los datos
    """
    try:
        # Crear el engine usando la función existente
        engine = creating_engine()
        
        # Leer el CSV
        print(f"Leyendo archivo CSV: {csv_file_path}")
        df = pd.read_csv(csv_file_path)
        
        # Mostrar información del DataFrame
        print("\nInformación del DataFrame:")
        print(f"Columnas: {df.columns.tolist()}")
        print(f"Número de filas: {len(df)}")
        
        # Cargar datos a PostgreSQL
        print(f"\nCargando datos a la tabla '{table_name}'...")
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists='replace',
            index=False
        )
        
        # Cerrar el engine usando la función existente
        disposing_engine(engine)
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo CSV en la ruta: {csv_file_path}")
    except Exception as e:
        print(f"Error al cargar datos:", str(e))
        # Asegurar que el engine se cierre incluso si hay error
        disposing_engine(engine)

if __name__ == "__main__":
    # Configuración
    CSV_FILE_PATH = 'tracks_data.csv'  # Ajusta la ruta según necesites
    TABLE_NAME = 'dataset'
    
    # Ejecutar la carga
    load_csv_to_database(CSV_FILE_PATH, TABLE_NAME)