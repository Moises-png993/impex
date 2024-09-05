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
          <q-input v-model="filter" label="Filtrar" />
          <q-btn flat color="red" @click="handleClose" class="close-btn">
            <img src="/filtrar.png" alt="Ícono" class="btn-icon" />
          </q-btn>
          <h6>MK: 4400051383</h6>
          <q-btn icon="close" flat color="red" @click="handleClose" />
        </div>
      </template>
    </q-table>
  </q-page>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  setup() {
    const tableData = ref([
      {
        articulo: "30056776002",
        booking: "14-000823AD",
        bl: "SHHT24080051SZN",
        contenedor: "SEGU4889430",
        factura: "X54NL26B",
      },
      {
        articulo: "30056776004",
        booking: "14-000823AD",
        bl: "SHHT24080051SZN",
        contenedor: "SEGU4889430",
        factura: "X54NL26B",
      },
      {
        articulo: "30056777002",
        booking: "14-000823AD",
        bl: "SHHT24080051SZN",
        contenedor: "SEGU4889430",
        factura: "X54NL26B",
      },
      {
        articulo: "30056777003",
        booking: "14-000823AD",
        bl: "SHHT24080051SZN",
        contenedor: "SEGU4889430",
        factura: "X54NL26B",
      },
      {
        articulo: "30056777004",
        booking: "14-000823AD",
        bl: "SHHT24080051SZN",
        contenedor: "SEGU4889430",
        factura: "X54NL26B",
      },
      {
        articulo: "30056777005",
        booking: "14-000823AD",
        bl: "SHHT24080051SZN",
        contenedor: "SEGU4889430",
        factura: "X54NL26B",
      },
    ]);

    const columns = [
      { name: "articulo", label: "Artículo", align: "left", field: "articulo" },
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
        // Reemplaza esta sección con la lógica para cargar datos si es necesario
      } catch (error) {
        console.error("Error fetching data:", error);
      } finally {
        loading.value = false;
      }
    };

    const handleClose = () => {
      console.log("Cerrar tabla");
      // Implementa la lógica para cerrar la tabla si es necesario
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
  padding: 0; /* Elimina el padding del contenedor de la página si es necesario */
}

.top-bar {
  display: flex;
  align-items: center;
  margin-bottom: 10px; /* Espacio entre la barra superior y la tabla */
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
  margin: 10px 0; /* Agrega margen vertical alrededor de las tablas */
  padding: 0; /* Agrega padding alrededor del contenido de las tablas */
  border-radius: 8px;
}
</style>
