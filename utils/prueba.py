import os

# Acceder a la variable de entorno
secret_key = os.getenv("SECRET_KEY")  # Devuelve None si no existe
fernet_key = os.getenv("FERNET_KEY") # Devuelve None si no existe

# Verificar si las variables están disponibles
if secret_key is None:
    print("La variable de entorno SECRET_KEY no está configurada.")
else:
    print(f"Secret Key: {secret_key}")

if fernet_key is None:
    print("La variable de entorno FERNET_KEY no está configurada.")
else:
    print(f"Fernet Key: {fernet_key}")
