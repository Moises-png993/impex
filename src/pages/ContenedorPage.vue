<template>
  <q-page>
    <div class="row">
      <div class="col-4 table-container">
        <h6>
          Contenedor: SEGU4889430 <br />
          Pedido Asociado: SEGU4889430 <br />
          MK: SEGU4889430
        </h6>
      </div>
      <div class="col-2">
        <q-btn
          label="Agregar Campaña"
          color="primary"
          @click="showPopup = true"
          class="q-mt-xl"
        />

        <!-- El Pop-up usando QDialog -->
        <q-dialog v-model="showPopup" persistent>
          <q-card>
            <div class="q-pa-md">
              <div class="q-gutter-md row items-start">
                <!-- Solo se deja el calendario -->
                <q-date v-model="model" mask="YYYY-MM-DD" color="purple" />
              </div>
            </div>
            <q-card-actions align="right">
              <q-btn flat label="Cerrar" color="primary" v-close-popup />
            </q-card-actions>
          </q-card>
        </q-dialog>
      </div>

      <!-- Mostrar los estados con badges -->
      <div class="col-4">
        <h6>Estado de Campaña</h6>
        <div class="q-gutter-xs q-mb-lg">
          <q-badge
            v-for="(estado, index) in estados"
            :key="index"
            :color="estado.color"
            size="lg"
          >
            {{ estado.label }}
          </q-badge>
        </div>
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
        <q-table
          :rows="moreInfoData"
          :columns="moreInfoColumns"
          row-key="label"
          class="q-pa-sm"
          no-data-label="No hay datos disponibles"
        >
        </q-table>

        <!-- Nueva tabla: Estilo y Cantidad de Pares -->
        <q-table
          :rows="styleData"
          :columns="styleColumns"
          row-key="style"
          class="q-pa-sm q-mt-lg"
          no-data-label="No hay datos disponibles"
        >
        </q-table>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  data() {
    return {
      model: "",
      showPopup: false,
      estados: [
        { label: "Fuera de Tiempo", color: "red" },
        { label: "A Tiempo", color: "green" },
        { label: "Casi a Tiempo", color: "yellow" },
      ],
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

      moreInfoData: [
        { label: "Puerto de Origen", value: "Puerto de Shanghái" },
        { label: "Puerto de Destino", value: "Puerto de Acajutla" },
        { label: "País de Origen", value: "China" },
        { label: "Puerto Transbordo", value: "Puerto de Manzanillo" },
        { label: "Forwarder", value: "Expeditors" },
        { label: "Naviera", value: "Maersk" },
        { label: "Destino", value: "San Salvador, El Salvador" },
      ],

      moreInfoColumns: [
        { name: "label", label: "Descripción", align: "left", field: "label" },
        { name: "value", label: "Detalle", align: "left", field: "value" },
      ],

      // Datos de la nueva tabla: Estilo y Cantidad de Pares
      styleData: [
        { style: "Estilo 001", cantidad: 100 },
        { style: "Estilo 002", cantidad: 200 },
        { style: "Estilo 003", cantidad: 150 },
      ],

      styleColumns: [
        { name: "style", label: "Estilo", align: "left", field: "style" },
        {
          name: "cantidad",
          label: "Cantidad de Pares",
          align: "left",
          field: "cantidad",
        },
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
.q-badge {
  font-size: 16px;
  font-weight: bold;
  padding: 10px;
}
</style>
