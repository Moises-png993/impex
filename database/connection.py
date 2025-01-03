# database/connection.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

 

# Función para conectar a MongoDB Atlas
def connect_to_mongo():
    mongo_password = "Xv7buNmL7bgIG1Tn" # Obtén la contraseña de la variable de entorno
    client = MongoClient(
        f"mongodb+srv://root:{mongo_password}@cluster0.dyswr.mongodb.net/data-impex?retryWrites=true&w=majority&appName=Cluster0"
    )
    print("Conectado a MongoDB Atlas")
    return client["data-impex"]

# Llama a la función para conectar y asigna la base de datos a 'db'
db = connect_to_mongo()
