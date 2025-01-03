<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container>
      <q-page>
        <q-table
          :rows="rows"
          :columns="columns"
          row-key="_id"
          dense
          bordered
          separator="horizontal"
          :filter="filter"
        >
          <template v-slot:body-cell="props">
            <q-td :props="props">
              <div
                v-if="isEditable && props.col.field === 'comentario'"
                contenteditable
                @blur="updateRow(props.row, props.col.field, $event)"
              >
                {{ props.row[props.col.field] }}
              </div>
              <div v-else>
                {{ props.row[props.col.field] }}
              </div>
            </q-td>
          </template>
        </q-table>
      </q-page>
    </q-page-container>

    <!-- Filtros -->
    <q-dialog v-model="showFilters">
      <q-card>
        <q-card-section>
          <div>Seleccionar Columnas:</div>
        </q-card-section>
        <q-card-section>
          <q-checkbox
            v-for="col in columns"
            :key="col.name"
            v-model="col.visible"
            :label="col.label"
          />
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="Cerrar" @click="showFilters = false" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-layout>
</template>

<script>
export default {
  data() {
    return {
      isEditable: false,
      showFilters: false,
      selectedWeek: 1,
      filter: "",
      rows: [
        {
          _id: "67784952eec1f0c050b8c587",
          pais: "sv",
          semana: 1,
          expediente: "SV25L7-001",
          tamano: "48´",
          fechaDespacho: "2025-01-02",
          status: "Pendiente de LE",
          transporte: "CROWLEY",
          comentario: "OK",
          fts: "Pendiente",
          sap: "Cerrado",
          agente: "Moisés",
        },
      ],
      columns: [
        {
          name: "pais",
          label: "PAIS",
          align: "left",
          field: "pais",
          visible: true,
        },
        {
          name: "semana",
          label: "Semana",
          align: "left",
          field: "semana",
          visible: true,
        },
        {
          name: "expediente",
          label: "Expediente",
          align: "left",
          field: "expediente",
          visible: true,
        },
        {
          name: "tamano",
          label: "Tamaño",
          align: "left",
          field: "tamano",
          visible: true,
        },
        {
          name: "fechaDespacho",
          label: "Fecha Despacho",
          align: "left",
          field: "fechaDespacho",
          visible: true,
        },
        {
          name: "status",
          label: "Status",
          align: "left",
          field: "status",
          visible: true,
        },
        {
          name: "transporte",
          label: "Transporte",
          align: "left",
          field: "transporte",
          visible: true,
        },
        {
          name: "comentario",
          label: "Comentario",
          align: "left",
          field: "comentario",
          visible: true,
        },
        {
          name: "fts",
          label: "FTS",
          align: "left",
          field: "fts",
          visible: true,
        },
        {
          name: "sap",
          label: "SAP",
          align: "left",
          field: "sap",
          visible: true,
        },
        {
          name: "agente",
          label: "Agente",
          align: "left",
          field: "agente",
          visible: true,
        },
      ],
    };
  },
  methods: {
    toggleEdit() {
      this.isEditable = !this.isEditable;
    },
    updateRow(row, field, event) {
      row[field] = event.target.innerText;
    },
  },
};
</script>
