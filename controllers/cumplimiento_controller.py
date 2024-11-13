"""
EndPoint para la automatizacion y obtencion de partidas Arancelarias
para el departamento de cumpliento Liderado hasta el momento por Raquel Flores
Funcionamiento: 
Primero debera hacer una Peticion GET al EndPoint /api/partida en donde se debe enviar una cadena
el EndPoint valida que la queda sea valida con el numero de caractares que se debe tener que debe ser
13 caracteres en dado caso no se cumpla alguna con alguna de las posibles 29 opciones de cadena, si 
nose encuentra ninguna cadena se ejecuta un algoritmo llamado Hamming el cual encuentra la cadena mas
cercana a la partida, luego el from debe obtener ese partida y formar un esquemA de un JSON para enviar al
Enpoint Partida en una peticion Post, el EndPoint Partidas sirve para listar todas las partidas subidas.

ing. Moises Perez 
Edit 19-09-2024
"""

from fastapi import APIRouter, HTTPException,  Query
from models.models import ArticuloModel
from database.connection import db
from utils.hamming import find_most_similar

router = APIRouter()

#EndPoint para obtener una partida sugerida dada la respuesta de un formualario despues de obtener una cadena.
@router.get("/api/partida")
async def obtener_partida(cadena: str = Query(..., description="Cadena para buscar la partida")):
    try:
        resultado = db["partidas"].find_one({"atributo": cadena})
        if resultado:
            return {"partida": resultado["codigo"]}
        else:
            # Usa la función find_most_similar importada
            partida_sugerida = find_most_similar(cadena)
            resultado2 = db["partidas"].find_one({"atributo": partida_sugerida})
            return {"partida": resultado2["codigo"] if resultado2 else "No encontrada"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint para crear un artículo luego de obtener la partida correcta y subirlo a la base de datos.
@router.post("/api/partida", response_model=ArticuloModel)
async def crear_articulo(articulo: ArticuloModel):
    try:
        nuevo_articulo = articulo.dict()
        result = db["articulos"].insert_one(nuevo_articulo)
        if result.inserted_id:
            return nuevo_articulo
        else:
            raise HTTPException(status_code=500, detail="Error al guardar el artículo")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para obtener todos los articulos con las partidas correctas. 
@router.get("/api/partidas", response_model=list[ArticuloModel])
async def obtener_articulos():
    try:
        articulos = list(db["articulos"].find())
        return articulos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

