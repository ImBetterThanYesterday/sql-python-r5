from sqlalchemy import create_engine ,text
from dotenv import load_dotenv
import os

def test_db_connection():
    try:
        # Cargar variables de entorno
        load_dotenv()
        
        # Obtener credenciales del .env
        db_params = {
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "host": os.getenv("DB_HOST"),
            "port": os.getenv("DB_PORT"),
            "database": os.getenv("DB_NAME")
        }
        
        # Construir URL de conexión
        db_url = f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}'
        
        # Intentar crear el engine y conectar
        engine = create_engine(db_url)
        with engine.connect() as connection:
            print("¡Conexión exitosa!")
            # Obtener versión de PostgreSQL
            result = connection.execute(text("SELECT version()"))
            version = result.scalar()
            print(f"Versión de PostgreSQL: {version}")
            
        engine.dispose()
        
    except Exception as e:
        print("Error de conexión:")
        print(str(e))

if __name__ == "__main__":
    test_db_connection()