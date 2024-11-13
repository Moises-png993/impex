"""
EndPoint para subir los datos a mongoDb.
"""
from fastapi import FastAPI, UploadFile, File, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from database.connection import db
import pandas as pd



# Inicializar FastAPI y el enrutador
app = FastAPI()
router = APIRouter()

# Colecciones de MongoDB
collection_me3n = db['me3n']
collection = db['tungya2']
collection_resultado = db['me3n_tungya']  # Nueva colección para almacenar los resultados de la agregación

app = FastAPI()
router = APIRouter()

@router.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):
    # Validar que el archivo tenga extensión .csv
    if not file.filename.endswith('.csv'):
        return JSONResponse({'error': 'Invalid file format'}, status_code=400)

    try:
        # Leer el archivo CSV usando pandas
        content = await file.read()
        df = pd.read_csv(StringIO(content.decode('utf-8')))  # Decodificar bytes a string

        # Convertir DataFrame a diccionarios para insertar en MongoDB
        records = df.to_dict(orient='records')

        # Insertar los registros en MongoDB
        if records:
            collection.insert_many(records)

        return JSONResponse({'message': 'File processed and uploaded to MongoDB successfully'}, status_code=200)

    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

# Registrar el router en la aplicación FastAPI
app.include_router(router)

def ejecutar_agregacion():
    """
    Ejecuta la agregación en MongoDB para combinar los datos de `me3n` y `tungya`
    y guarda los resultados en la colección `me3n_tungya`.
    """
    pipeline = [
        {
            "$match": {
                "mk": {"$exists": True},
                "line": {"$exists": True}
            }
        },
        {
            "$lookup": {
                "from": "tungya",
                "localField": "mk",
                "foreignField": "mk",
                "as": "tungya_docs"
            }
        },
        {
            "$unwind": {
                "path": "$tungya_docs",
                "preserveNullAndEmptyArrays": False
            }
        },
        {
            "$addFields": {
                "NumeroBooking": "$tungya_docs.NumeroBooking",
                # Agrega aquí todos los campos necesarios del documento tungya_docs
            }
        },
        {
            "$project": {
                "tungya_docs": 0
            }
        },
        {
            "$merge": {
                "into": "me3n_tungya",
                "whenMatched": "merge",
                "whenNotMatched": "insert"
            }
        }
    ]
    try:
        collection_me3n.aggregate(pipeline)
        print('Agregación ejecutada con éxito y resultados almacenados en la colección `me3n_tungya`.')
    except Exception as e:
        print(f'Error al ejecutar la agregación: {e}')

# Registrar el router en la aplicación FastAPI
app.include_router(router)
