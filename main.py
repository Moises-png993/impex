from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.connection import connect_to_mongo
from controllers import  cumplimiento_controller, contenedor_controller, upload_controller, e_controller, login_controller

app = FastAPI()

# Configuración de CORS
allowed_origins = [
    "http://localhost:9000",
    "http://localhost:9001",
    "http://localhost:9002",
    "https://simpex.netlify.app",
    "https://formulario-proveedores.netlify.app",
    "https://supply-form.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conectar a la base de datos
connect_to_mongo()

# Incluir rutas desde los controladores
app.include_router(cumplimiento_controller.router)
app.include_router(contenedor_controller.router)
app.include_router(upload_controller.router)
app.include_router(e_controller.router)
app.include_router(login_controller.router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
