// src/boot/axios.js
import axios from "axios";

// Crear una instancia de axios con la configuración base
const api = axios.create({
  baseURL: "https://impex-zctt.onrender.com", // URL base de la API
  timeout: 10000000, // Tiempo máximo de espera en milisegundos
});

// Exportar la instancia para ser utilizada en el proyecto
export default ({ app }) => {
  app.config.globalProperties.$axios = api; // Configura axios globalmente en la aplicación Vue 3
};
