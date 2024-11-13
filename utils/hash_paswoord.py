from pymongo import MongoClient
from passlib.context import CryptContext

# Contexto de encriptación
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Conectar a la base de datos
client = MongoClient("mongodb+srv://root:Elcieloesrojo98@cluster0.dyswr.mongodb.net/data-impex?retryWrites=true&w=majority")
db = client["data-impex"]
users_collection = db["usuarios"]

# Actualizar las contraseñas de los usuarios ya registrados
for user in users_collection.find():
    if not user.get("password_hashed"):  # Verificar si la contraseña no está hasheada
        hashed_password = pwd_context.hash(user["password"])  # Hashear la contraseña
        users_collection.update_one(
            {"_id": user["_id"]},
            {"$set": {"password": hashed_password, "password_hashed": True}}  # Marcar que la contraseña ha sido hasheada
        )

print("Todas las contraseñas se han actualizado.")