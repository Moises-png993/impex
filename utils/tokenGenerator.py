from fastapi import Header,  HTTPException
from datetime import datetime, timedelta
import jwt
import os
from dotenv import load_dotenv

 # Definir clave secreta y algoritmo para JWT
load_dotenv("variables.env")
SECRET_KEY = "Elcieloesrojo98"

SECRET_KEY = SECRET_KEY.encode()
  # Cambia esto por una clave más segura en producción
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=1)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]  # Extraer el token del encabezado
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except (jwt.PyJWTError, IndexError):
        raise HTTPException(status_code=401, detail="Token inválido")