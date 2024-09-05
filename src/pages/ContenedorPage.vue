<template>
  <q-page>
    <div class="row">
      <div class="col-4 table-container">
        <h6>Contenedor: SEGU4889430</h6>
      </div>
    </div>

    <div class="row q-col-gutter-lg">
      <div class="col-4 table-container">
        <q-table
          :rows="tableData"
          :columns="columns"
          row-key="label"
          :loading="loading"
          :pagination="pagination"
          :filter="filter"
          class="q-pa-sm"
          no-data-label="No hay datos disponibles"
        >
        </q-table>
      </div>

      <div class="col-8">
        <h6>Más Información</h6>
        <p>Aquí va la información adicional que deseas mostrar.</p>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  data() {
    return {
      tableData: [
        { label: "ETA ACTUALIZADO", value: "2024-09-10" },
        { label: "ETA AJUSTADO IMPEX", value: "2024-09-12" },
        { label: "ETA PUERTO SEMANA", value: "Semana 37" },
        { label: "ETA BLUE SAP", value: "2024-09-15" },
        { label: "ETA CD SV/NI/HN/GT", value: "2024-09-13" },
        { label: "ETA CD CR", value: "2024-09-14" },
        { label: "ETA/ATA PUERTO TRANSBORDO", value: "2024-09-11" },
        { label: "ETD/ATD PUERTO TRANSBORDO", value: "2024-09-09" },
      ],

      columns: [
        { name: "label", label: "Descripción", align: "left", field: "label" },
        { name: "value", label: "Fecha", align: "left", field: "value" },
      ],
      pagination: { rowsPerPage: 10 },
      filter: "",
      loading: false,
    };
  },
};
</script>

<style scoped>
.table-container {
  padding-left: 50px; /* Ajusta el margen izquierdo según tus necesidades */
}
</style>
