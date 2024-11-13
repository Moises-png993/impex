from fastapi import FastAPI, APIRouter, HTTPException, Depends, Form, File, UploadFile
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from pymongo import MongoClient
from bson import ObjectId
from cryptography.fernet import Fernet
from utils.tokenGenerator import verify_token
from database.connection import db
import os
from dotenv import load_dotenv
import json
from typing import List

# Cargar las variables de entorno
load_dotenv("variables.env")

# Obtener la clave de cifrado de Fernet desde el archivo .env
fernet_key = os.getenv("FERNET_KEY").encode()
cipher = Fernet(fernet_key)

# Colección de usuarios en la base de datos MongoDB
users_collection = db["usuarios"]

# Inicializa el router de FastAPI
router = APIRouter()

# Modelo para la solicitud de correo electrónico
class EmailRequest(BaseModel):
    user_id: str  
    recipient_email: List[str]  # Cambiado a lista
    cc_email: List[str]          # Cambiado a lista
    subject: str
    body: str

async def send_email(sender_email: str, sender_password: str, recipient_email: List[str], cc_email: List[str], subject: str, body: str, full_name: str, position: str, attachments: List[UploadFile]):
    # Crear el mensaje MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipient_email)
    msg['Cc'] = ", ".join(cc_email)
    msg['Subject'] = subject

    # Crear la parte HTML con la firma y el cuerpo del mensaje
    html_body = f"""
    <div style="font-family: Arial, sans-serif; font-size: 14px; color: #000;">
        <p>{body}</p>  <!-- Cuerpo del correo enviado por el usuario -->
        <div style="margin-top: 20px;">
            <img src="cid:logo" alt="Logo Empresas ADOC" width="200" 
                 style="float: left; margin-right: 10px; margin-top: 20px;">
            <div style="overflow: hidden;">
                <p><strong>{full_name}</strong><br>
                {position}</p>
                <p>KM. 24 CARRETERA A SANTA ANA,<br> 
                PARQUE DE SERVICIOS EXPORTSALVA, EDIF. 18-C<br>
                COLÓN, LA LIBERTAD. EL SALVADOR</p>
                <p>
                    <a href="http://www.empresasadoc.com" style="color: #0078D4; text-decoration: none;">
                    www.empresasadoc.com</a>
                </p>
            </div>
        </div>
    </div>
    """

    # Adjuntar la parte HTML al mensaje
    msg.attach(MIMEText(html_body, 'html'))

    # Adjuntar la imagen del logo desde la carpeta /images
    with open("images/logo_adoc.png", "rb") as img_file:
        logo = MIMEImage(img_file.read())
        logo.add_header('Content-ID', '<logo>')
        msg.attach(logo)

    # Adjuntar archivos
    for file in attachments:
        file_content = await file.read()  # Leer el contenido del archivo
        attachment = MIMEText(file_content, 'plain', 'utf-8')  # Puedes cambiar 'plain' a 'application/octet-stream'
        attachment.add_header('Content-Disposition', f'attachment; filename="{file.filename}"')
        msg.attach(attachment)

    try:
        # Configurar el servidor SMTP
        with smtplib.SMTP('smtp.office365.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email + cc_email, msg.as_string())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al enviar el correo: {e}")

@router.post("/send-email/")
async def send_email_route(
    email_request: str = Form(...),  # Recibe como string
    attachments: List[UploadFile] = File(None)  # Cambiado para ser opcional
):
    try:
        # Convertir el string a un objeto JSON
        email_request_data = json.loads(email_request)
        email_data = EmailRequest(**email_request_data)  # Crear el objeto EmailRequest

        # Buscar al usuario en la base de datos usando su ID
        user = users_collection.find_one({"_id": ObjectId(email_data.user_id)})

        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        sender_email = user.get("correo")
        if not sender_email:
            raise HTTPException(status_code=404, detail="Correo del usuario no encontrado")

        # Descifrar el token_out del usuario desde la base de datos
        encrypted_token_out = user.get("token_out")
        if not encrypted_token_out:
            raise HTTPException(status_code=404, detail="token_out no encontrado")

        sender_password = cipher.decrypt(encrypted_token_out.encode()).decode()

        # Obtener el nombre completo y el puesto del usuario
        full_name = f"{user.get('nombre')} {user.get('apellido')}"
        position = user.get('puesto')

        # Enviar el correo electrónico con la firma y los archivos adjuntos
        await send_email(
            sender_email=sender_email,
            sender_password=sender_password,
            recipient_email=email_data.recipient_email,
            cc_email=email_data.cc_email,
            subject=email_data.subject,
            body=email_data.body,
            full_name=full_name,
            position=position,
            attachments=attachments
        )

        return {"message": "Correo enviado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al enviar el correo: {e}")

# Inicializar la aplicación FastAPI y añadir el router
app = FastAPI()
app.include_router(router)
