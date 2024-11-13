from cryptography.fernet import Fernet
from pymongo import MongoClient

# Generar o usar una clave Fernet existente
fernet_key = b'mj_g-BGvtHopfDK2_h9QrDyKvxptG8Gi5TkRgVyIGY4='  # Reemplaza con tu clave de cifrado
cipher = Fernet(fernet_key)

# Conectar a la base de datos
client = MongoClient("mongodb+srv://root:Elcieloesrojo98@cluster0.dyswr.mongodb.net/data-impex?retryWrites=true&w=majority")
db = client["data-impex"]
users_collection = db["usuarios"]

# Buscar usuarios que tienen un token_out sin cifrar
users_to_update = users_collection.find({
    "$or": [
        {"token_out_hashed": {"$exists": False}},  # Campo no existe
        {"token_out_hashed": False}  # Campo es false
    ]
})

# Iterar sobre los usuarios y cifrar el token_out
for user in users_to_update:
    # Cifrar el token
    if "token_out" in user:
        encrypted_token = cipher.encrypt(user["token_out"].encode()).decode()
        
        # Actualizar en la base de datos
        users_collection.update_one(
            {"_id": user["_id"]},
            {
                "$set": {
                    "token_out": encrypted_token,
                    "token_out_hashed": True  # Marcar como cifrado
                }
            }
        )
        print(f"Token cifrado para el usuario: {user['username']}")

print("Proceso de cifrado completado para los tokens.")
