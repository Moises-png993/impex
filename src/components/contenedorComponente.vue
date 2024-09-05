<template>
  <q-page>
    <q-table
      :rows="tableData"
      :columns="columns"
      row-key="mk"
      :loading="loading"
      :pagination="pagination"
      :filter="filter"
      no-data-label="No hay datos disponibles"
      class="table-content"
    >
      <template v-slot:top>
        <q-input v-model="filter" label="Filtrar" />
        <q-btn flat color="red" @click="handleClose" class="close-btn">
          <img src="public/filtrar.png" alt="Ícono" class="btn-icon" />
        </q-btn>
        <h6>Contenedor: SEGU4889430</h6>
        <q-btn
          icon="close"
          flat
          color="red"
          @click="handleClose"
          class="close-btn"
        />
      </template>
      <template v-slot:body-cell-action="props">
        <q-td :props="props">
          <q-btn flat color="primary" @click="handleDetails(props.row)">
            Más detalle
          </q-btn>
        </q-td>
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
        zimp: "Z123456",
        crd: "2024-09-01",
        cfs: "2024-09-03",
        etd: "2024-09-05",
        eta: "2024-09-10",
        etaImpex: "2024-09-12",
        etaBlueSap: "2024-09-15",
      },
      {
        mk: "4400051384",
        zimp: "Z654321",
        crd: "2024-09-02",
        cfs: "2024-09-04",
        etd: "2024-09-06",
        eta: "2024-09-11",
        etaImpex: "2024-09-13",
        etaBlueSap: "2024-09-16",
      },
    ]);

    const columns = [
      { name: "mk", label: "MK", align: "left", field: "mk" },
      { name: "zimp", label: "ZIMP", align: "left", field: "zimp" },
      { name: "crd", label: "CRD", align: "left", field: "crd" },
      { name: "cfs", label: "CFS", align: "left", field: "cfs" },
      { name: "etd", label: "ETD", align: "left", field: "etd" },
      { name: "eta", label: "ETA", align: "left", field: "eta" },
      {
        name: "etaImpex",
        label: "ETA IMPEX",
        align: "left",
        field: "etaImpex",
      },
      {
        name: "etaBlueSap",
        label: "ETA BLUE/SAP",
        align: "left",
        field: "etaBlueSap",
      },
      {
        name: "action",
        label: "Acciones",
        align: "center",
        field: "action",
        sortable: false,
      },
    ];

    const pagination = ref({ rowsPerPage: 10 });
    const filter = ref("");
    const loading = ref(false);

    const fetchData = async () => {
      loading.value = true;
      try {
        // const response = await axios.get("https://api.example.com/data"); // Reemplaza con tu URL de API
        // tableData.value = response.data;
      } catch (error) {
        console.error("Error fetching data:", error);
      } finally {
        loading.value = false;
      }
    };

    const handleDetails = (row) => {
      console.log("Más detalle:", row);
      // Implementa la lógica para mostrar más detalles aquí
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
      handleDetails,
      handleClose,
    };
  },
};
</script>

<style scoped>
.q-page {
  padding: 0;
  background-color: transparent;
}

.top-bar {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.close-btn {
  margin-left: 8px;
  padding: 6px 12px;
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
