<template>
  <q-page class="flex flex-center q-pa-md">
    <q-card class="q-pa-md q-ma-md" flat bordered>
      <div class="text-h5 text-center q-mb-md">
        {{ saludo }} <q-icon :name="emoji" size="30px" />
      </div>
      <q-table :rows="articulos" :columns="columns" row-key="_id">
        <template v-slot:body-cell-upper="props">
          <q-td :props="props">{{ props.row.upper }}</q-td>
        </template>
        <template v-slot:body-cell-forro="props">
          <q-td :props="props">{{ props.row.forro }}</q-td>
        </template>
        <!-- Agrega más templates personalizados para otras columnas si es necesario -->
      </q-table>
    </q-card>
  </q-page>
</template>

<script>
export default {
  data() {
    return {
      saludo: "",
      emoji: "",
      columns: [
        {
          name: "numeroArticulo",
          align: "left",
          label: "N° Artículo",
          field: "numeroArticulo",
        },
        {
          name: "proveedor",
          align: "left",
          label: "Proveedor",
          field: "proveedor",
        },
        {
          name: "partida",
          align: "left",
          label: "Partida Arancelaria Sugerida",
          field: "partida",
        },
        {
          name: "descripcion",
          align: "left",
          label: "Descripción",
          field: "descripcion",
        },
        { name: "upper", align: "left", label: "Upper", field: "upper" },
        {
          name: "forro",
          align: "left",
          label: "Forro/Plantilla",
          field: "forro",
        },
        { name: "origen", align: "left", label: "Origen", field: "origen" },
        {
          name: "informacionAdicional",
          align: "left",
          label: "Información adicional",
          field: "informacionAdicional",
        },
      ],
      articulos: [],
    };
  },
  methods: {
    obtenerSaludo() {
      const horas = new Date().getHours();
      if (horas >= 6 && horas < 12) {
        this.saludo = "Buenos días";
        this.emoji = "local_cafe";
      } else if (horas >= 12 && horas < 18) {
        this.saludo = "Buenas tardes";
        this.emoji = "wb_sunny";
      } else {
        this.saludo = "Buenas noches";
        this.emoji = "nightlight_round";
      }
    },
    async obtenerArticulos() {
      try {
        const response = await this.$axios.get("/api/articulos");
        console.log("Datos recibidos:", response.data);
        this.articulos = response.data;
      } catch (error) {
        console.error("Error al obtener los artículos:", error);
      }
    },
  },
  mounted() {
    this.obtenerSaludo();
    this.obtenerArticulos();
  },
};
</script>

<style scoped>
.q-page {
  background-color: #f4f4f9;
}

.q-card {
  max-width: 1200px;
  width: 100%;
}

.text-h5 {
  color: #555;
}
</style>
