<template>
  <q-page class="flex flex-center q-pa-md">
    <q-card class="q-pa-md q-ma-md" flat bordered>
      <div class="text-h5 text-center q-mb-md">
        {{ saludo }} <q-icon :name="emoji" size="30px" />
      </div>
      <q-table
        :rows="articulos"
        :columns="columns"
        row-key="id"
        flat
        bordered
        rows-per-page-options="[5, 10, 20]"
      >
        <template v-slot:body-cell-upper="props">
          <q-td :props="props">{{ props.row.upper }}</q-td>
        </template>
        <!-- Más templates personalizados según sea necesario -->
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
        { name: "id", align: "left", label: "N° Artículo", field: "id" },
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
          name: "forroPlantilla",
          align: "left",
          label: "Forro/Plantilla",
          field: "forroPlantilla",
        },
        { name: "suela", align: "left", label: "Suela", field: "suela" },
        { name: "origen", align: "left", label: "Origen", field: "origen" },
        {
          name: "infoAdicional",
          align: "left",
          label: "Información adicional",
          field: "infoAdicional",
        },
      ],
      articulos: [
        {
          id: "001",
          proveedor: "Proveedor A",
          partida: "12345678",
          descripcion: "Descripción del artículo",
          upper: "Material Upper",
          forroPlantilla: "Material Forro/Plantilla",
          suela: "Material Suela",
          origen: "País de Origen",
          infoAdicional: "Información adicional sobre el artículo",
        },
        // Más artículos según sea necesario
      ],
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
  },
  mounted() {
    this.obtenerSaludo();
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
