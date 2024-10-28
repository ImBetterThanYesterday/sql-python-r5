# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Obtener variables de entorno
db_params = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME")
}

# Construir URL de conexión
db_url = f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}'

Base = declarative_base()

def creating_engine():
    """Crear y retornar una instancia del motor de base de datos"""
    engine = create_engine(db_url)
    return engine

def creating_session(engine):
    """Crear y retornar una sesión de base de datos"""
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def closing_session(session):
    """Cerrar la sesión de base de datos"""
    session.close()

def disposing_engine(engine):
    """Cerrar el motor de base de datos"""
    engine.dispose()
    print("Engine cerrado")