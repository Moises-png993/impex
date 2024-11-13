"""
Endpoint de prueba para el equipo de planning
"""

from fastapi import APIRouter, HTTPException, Query
from database.connection import db

router = APIRouter()

@router.get("/api/eta-semana")
async def obtener_eta_semana(estilo: str = Query(..., description="Estilo para buscar")):
    try:
        results = list(db["import"].aggregate([
            {"$match": {"ESTILO": estilo}},
            {
                "$group": {
                    "_id": {"semana": "$ETA PUERTO (SEMANA)", "contenedor": "$CONTENEDOR"},
                    "totalCantidad": {"$sum": "$CANTIDAD"}
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "ETA PUERTO (SEMANA)": "$_id.semana",
                    "CONTENEDOR": "$_id.contenedor",
                    "Total CANTIDAD": "$totalCantidad"
                }
            }
        ]))
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/estilo-cantidad")
async def obtener_estilo_cantidad(contenedor: str = Query(..., description="Contenedor para buscar")):
    try:
        results = list(db["import"].aggregate([
            {"$match": {"CONTENEDOR": contenedor}},
            {"$group": {"_id": "$ESTILO", "totalCantidad": {"$sum": "$CANTIDAD"}}},
            {"$project": {"_id": 0, "ESTILO": "$_id", "CANTIDAD": "$totalCantidad"}}
        ]))
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
