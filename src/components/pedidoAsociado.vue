<template>
  <q-page>
    <q-table
      :rows="tableData"
      :columns="columns"
      row-key="articulo"
      :loading="loading"
      :pagination="pagination"
      :filter="filter"
      no-data-label="No hay datos disponibles"
      class="table-content"
    >
      <template v-slot:top>
        <div class="top-bar">
          <q-input v-model="filter" label="Filtrar" class="q-mb-md" />
          <q-btn flat color="red" @click="handleClose" class="close-btn">
            <img src="/filtrar.png" alt="Ícono" class="btn-icon" />
          </q-btn>
          <h6>Pedido Asociado: 4400051383</h6>
          <q-btn
            icon="close"
            flat
            color="red"
            @click="handleClose"
            class="close-btn"
          />
        </div>
      </template>
    </q-table>
  </q-page>
</template>

<script>
import { ref, onMounted } from "vue";
import axios from "axios";

export default {
  setup() {
    const tableData = ref([
      {
        mk: "4400051383",
        articulo: "30056776002",
        textoBreve: "Zapato de cuero",
        booking: "14-000823AD",
        bl: "SHHT24080051SZN",
        contenedor: "SEGU4889430",
        factura: "X54NL26B",
      },
      {
        mk: "4400051384",
        articulo: "30056776004",
        textoBreve: "Botas de lluvia",
        booking: "14-000823AD",
        bl: "SHHT24080051SZN",
        contenedor: "SEGU4889430",
        factura: "X54NL26B",
      },
      {
        mk: "4400051385",
        articulo: "30056777002",
        textoBreve: "Sandalias de playa",
        booking: "14-000823AD",
        bl: "SHHT24080051SZN",
        contenedor: "SEGU4889430",
        factura: "X54NL26B",
      },
    ]);

    const columns = [
      { name: "mk", label: "MK", align: "left", field: "mk" },
      { name: "articulo", label: "Artículo", align: "left", field: "articulo" },
      {
        name: "textoBreve",
        label: "Texto Breve",
        align: "left",
        field: "textoBreve",
      },
      { name: "booking", label: "Booking", align: "left", field: "booking" },
      { name: "bl", label: "BL", align: "left", field: "bl" },
      {
        name: "contenedor",
        label: "Contenedor",
        align: "left",
        field: "contenedor",
      },
      { name: "factura", label: "Factura", align: "left", field: "factura" },
    ];

    const pagination = ref({ rowsPerPage: 10 });
    const filter = ref("");
    const loading = ref(false);

    const fetchData = async () => {
      loading.value = true;
      try {
        // Reemplaza con tu URL de API si es necesario
        // const response = await axios.get("https://api.example.com/data");
        // tableData.value = response.data;
      } catch (error) {
        console.error("Error fetching data:", error);
      } finally {
        loading.value = false;
      }
    };

    const handleClose = () => {
      console.log("Cerrar tabla");
    };

    onMounted(() => {
      fetchData();
    });

    return {
      tableData,
      columns,
      pagination,
      filter,
      loading,
      handleClose,
    };
  },
};
</script>

<style scoped>
.q-page {
  padding: 20px;
}

.top-bar {
  display: flex;
  align-items: center;
  margin-bottom: 16px; /* Añadido para dar un poco de espacio entre la barra superior y la tabla */
}

.close-btn {
  margin-left: 8px;
}

.btn-icon {
  width: 16px;
  height: 16px;
  margin-right: 4px;
}

.table-content {
  margin: 1px 0; /* Agrega margen vertical alrededor de las tablas */
  padding: 0; /* Agrega padding alrededor del contenido de las tablas */
  border-radius: 8px;
}
</style>
