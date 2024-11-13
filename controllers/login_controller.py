from fastapi import FastAPI, HTTPException, APIRouter, Header, Depends
from pydantic import BaseModel
from passlib.context import CryptContext
from pymongo import MongoClient
from bson import ObjectId  # Importar para trabajar con ObjectId de MongoDB
from database.connection import db
from utils.tokenGenerator import verify_token, create_access_token

# Conjunto de usuarios en la base de datos
users_collection = db["usuarios"]
router = APIRouter()

# Contexto de encriptación de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Esquema para registrar y autenticar usuarios
class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

# Endpoint para registrar nuevos usuarios
@router.post("/register")
async def register(user: UserCreate):
    # Verifica si el usuario ya existe
    db_user = users_collection.find_one({"username": user.username})
    if db_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe.")
    
    # Hashear la contraseña
    hashed_password = pwd_context.hash(user.password)
    
    # Crear el nuevo usuario
    new_user = {
        "username": user.username,
        "password": hashed_password
    }
    
    # Insertar el nuevo usuario en la base de datos
    users_collection.insert_one(new_user)
    return {"message": "Usuario creado exitosamente."}

# Ruta de login
@router.post("/login")
async def login(user: UserLogin):
    db_user = users_collection.find_one({"username": user.username})
    
    if not db_user or not pwd_context.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    # Crear el token JWT
    access_token = create_access_token(data={"sub": user.username})
    
    # Devolver el token y el _id del usuario
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": str(db_user["_id"])  # Convertir ObjectId a string para poder enviarlo en la respuesta
    }

# Incluir las rutas en la aplicación principal
app = FastAPI()
app.include_router(router)

# Ruta protegida de ejemplo
@router.get("/protected")
async def protected_route(payload: dict = Depends(verify_token)):
    return {"message": "Tienes acceso a esta ruta protegida."}
