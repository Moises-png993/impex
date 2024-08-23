const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');  // Importa el paquete cors

const app = express();
const port = 3000;

// Configura CORS para permitir solicitudes desde localhost:9000
app.use(cors({
  origin: 'http://localhost:9000'
}));

// Conexión a MongoDB
mongoose.connect('mongodb+srv://root:Elcieloesrojo98@cluster0.dyswr.mongodb.net/data-impex?retryWrites=true&w=majority&appName=Cluster0', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('Conectado a MongoDB Atlas'))
.catch((error) => console.error('Error al conectar a MongoDB Atlas:', error));

// Define el esquema para la colección 'import'
const contenedorSchema = new mongoose.Schema({
  ESTILO: String,
  "ETA PUERTO (SEMANA)": Number,
  CONTENEDOR: String,
  CANTIDAD: Number,
}, { collection: 'import' });

const Contenedor = mongoose.model('Contenedor', contenedorSchema);

// Ruta para obtener la información mediante la agregación
app.get('/api/eta-semana', async (req, res) => {
  try {
    const estilo = req.query.estilo;
    console.log(`Estilo recibido: ${estilo}`);

    const count = await Contenedor.countDocuments({ ESTILO: estilo });
    console.log(`Número de documentos que coinciden con ESTILO "${estilo}": ${count}`);

    const results = await Contenedor.aggregate([
      {
        $match: { ESTILO: estilo }
      },
      {
        $group: {
          _id: {
            semana: "$ETA PUERTO (SEMANA)",
            contenedor: "$CONTENEDOR"
          },
          totalCantidad: { $sum: "$CANTIDAD" }
        }
      },
      {
        $project: {
          _id: 0,
          "ETA PUERTO (SEMANA)": "$_id.semana",
          CONTENEDOR: "$_id.contenedor",
          "Total CANTIDAD": "$totalCantidad"
        }
      }
    ]);

    console.log('Resultados:', results);
    res.json(results);
  } catch (error) {
    console.error('Error en la agregación:', error);
    res.status(500).json({ error: error.message });
  }
});

app.get('/api/estilo-cantidad', async (req, res) => {
  try {
    const contenedor = req.query.contenedor; 
    console.log(`Contenedor recibido: ${contenedor}`);

    const results = await Contenedor.aggregate([
      {
        $match: { CONTENEDOR: contenedor }  
      },
      {
        $group: {
          _id: "$ESTILO", 
          totalCantidad: { $sum: "$CANTIDAD" }  
        }
      },
      {
        $project: {
          _id: 0, 
          ESTILO: "$_id",  
          CANTIDAD: "$totalCantidad"  
        }
      }
    ]);

    console.log('Resultados:', results);
    res.json(results);
  } catch (error) {
    console.error('Error en la agregación:', error);
    res.status(500).json({ error: error.message });
  }
});

app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});
