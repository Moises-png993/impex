const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');  
const { findMostSimilar } = require('./hamming');

const app = express();
const port = 3000;

const allowedOrigins = ['http://localhost:9000','http://localhost:9001', 'http://localhost:9002', 'https://mi-dominio.com'];

const corsOptions = {
  origin: function (origin, callback) {
    // Permite solicitudes sin origen (por ejemplo, desde herramientas como Postman)
    if (!origin) return callback(null, true);

    // Verifica si el origen está en la lista de permitidos
    if (allowedOrigins.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Origen no permitido por CORS'));
    }
  },
  optionsSuccessStatus: 200,
};

app.use(cors(corsOptions));
app.use(express.json());  // Añadido para analizar JSON

mongoose.connect('mongodb+srv://root:Elcieloesrojo98@cluster0.dyswr.mongodb.net/data-impex?retryWrites=true&w=majority&appName=Cluster0', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('Conectado a MongoDB Atlas'))
.catch((error) => console.error('Error al conectar a MongoDB Atlas:', error));

const articuloSchema = new mongoose.Schema({
  numeroArticulo: Number,
  proveedor: String,
  partida: Number,
  descripcion: String,
  upper: String,
  forro: String,
  suela: String,
  origen: String,
  informacionAdicional: String
}, { collection: 'articulos' });

const Articulo = mongoose.model('Articulo', articuloSchema);

// Endpoint POST para recibir los datos
app.post('/api/articulo', async (req, res) => {
  try {
    const {
      numeroArticulo,
      proveedor,
      partida,
      descripcion,
      upper,
      forro,
      suela,
      origen,
      informacionAdicional
    } = req.body;

    const nuevoArticulo = new Articulo({
      numeroArticulo,
      proveedor,
      partida,
      descripcion,
      upper,
      forro,
      suela,
      origen,
      informacionAdicional
    });

    await nuevoArticulo.save();

    res.status(201).json(nuevoArticulo);
  } catch (error) {
    console.error('Error al subir datos:', error);
    res.status(500).json({ error: error.message });
  }
});

const contenedorSchema = new mongoose.Schema({
  ESTILO: String,
  "ETA PUERTO (SEMANA)": Number,
  CONTENEDOR: String,
  CANTIDAD: Number,
}, { collection: 'import' });

const CodigoSchemaPartida = new mongoose.Schema({
  codigo: String,
  atributo: String
}, { collection: 'partidas' });

const Contenedor = mongoose.model('Contenedor', contenedorSchema);
const Partida = mongoose.model('Partida', CodigoSchemaPartida);

app.get('/api/partida', async (req, res) => {
  const { cadena } = req.query;

  if (!cadena) {
    return res.status(400).send('La cadena es requerida');
  }

  try {
    const resultado = await Partida.findOne({ atributo: cadena });
    if (resultado) {
      res.json({ partida: resultado.codigo });
    } else {
      let partidaSugerida = findMostSimilar(cadena);
      const resultado2 = await Partida.findOne({ atributo: partidaSugerida });
      console.log(partidaSugerida);
      res.json({ partida: resultado2.codigo });
    }
  } catch (err) {
    res.status(500).send('Error en el servidor');
  }
});

app.get('/api/articulos', async (req, res) => {
  try {
    // Utiliza el modelo Articulo para obtener todos los documentos de la colección
    const articulos = await Articulo.find();

    // Envía los artículos como respuesta en formato JSON
    res.status(200).json(articulos);
  } catch (error) {
    console.error('Error al obtener los artículos:', error);
    res.status(500).json({ error: 'Error al obtener los artículos' });
  }
});

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