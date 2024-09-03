<template>
  <q-page>
    <q-table
      :rows="tableData"
      :columns="columns"
      row-key="id"
      :loading="loading"
      :pagination="pagination"
      :filter="filter"
      no-data-label="No hay datos disponibles"
    >
      <template v-slot:top>
        <q-input v-model="filter" label="Filtrar" class="q-mb-md" />
      </template>
    </q-table>
    <p>hola</p>
  </q-page>
</template>

<script>
import DataTable from "src/components/ordenCompra.vue"; // Ajusta la ruta según tu estructura de proyecto
import { ref, onMounted } from "vue";
import axios from "axios";

export default {
  setup() {
    const tableData = ref([]);
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
        const response = await axios.get("https://api.example.com/data"); // Reemplaza con tu URL de API
        tableData.value = response.data;
      } catch (error) {
        console.error("Error fetching data:", error);
      } finally {
        loading.value = false;
      }
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
    };
  },
};
</script>

<style scoped>
.q-page {
  padding: 20px;
}
</style>
