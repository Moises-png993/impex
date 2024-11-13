from pydantic import BaseModel

class ArticuloModel(BaseModel):
    numeroArticulo: int
    proveedor: str
    partida: int
    descripcion: str
    upper: str
    forro: str
    suela: str
    origen: str
    informacionAdicional: str


class ContenedorModel(BaseModel):
    ESTILO: str
    ETA_SEMANA: int
    CONTENEDOR: str
    CANTIDAD: int


class PartidaModel(BaseModel):
    codigo: str
    atributo: str
