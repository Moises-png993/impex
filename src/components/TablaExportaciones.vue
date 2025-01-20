<template>
  <div class="table-container full-width">
    <h1 class="page-title">Semana Actual</h1>
    <q-table
      :rows="rows"
      :columns="columns"
      row-key="id"
      :pagination="pagination"
      :loading="loading"
      flat
      bordered
      class="editable-table"
    >
      <template v-slot:body="props">
        <q-tr :props="props" class="row-style">
          <q-td v-for="col in props.cols" :key="col.name" :props="props">
            <div v-if="props.row.editable">
              <!-- Input para edición -->
              <q-input v-model="props.row[col.name]" dense outlined />
            </div>
            <div v-else>
              <!-- Valor normal -->
              {{ props.row[col.name] }}
            </div>
          </q-td>
        </q-tr>
      </template>
    </q-table>

    <div class="actions-container">
      <q-btn
        color="primary"
        icon="edit"
        label="Editar Todo"
        @click="editAllRows"
      />
      <q-btn
        color="positive"
        icon="save"
        label="Guardar Todo"
        @click="saveAllRows"
      />
      <q-btn
        color="negative"
        icon="cancel"
        label="Cancelar"
        @click="cancelAllEdits"
      />
    </div>
  </div>
</template>

<script>
import { ref, reactive } from "vue";

export default {
  setup() {
    const loading = ref(false);

    const pagination = reactive({
      sortBy: "semana",
      descending: false,
      page: 1,
      rowsPerPage: 10,
    });

    const columns = [
      { name: "pais", label: "País", field: "pais", align: "center" },
      { name: "semana", label: "Semana", field: "semana", align: "center" },
      {
        name: "expediente",
        label: "Expediente",
        field: "expediente",
        align: "center",
      },
      { name: "tamano", label: "Tamaño", field: "tamano", align: "center" },
      {
        name: "fecha",
        label: "Fecha de Despacho",
        field: "fecha",
        align: "center",
      },
      { name: "status", label: "Estado", field: "status", align: "center" },
      {
        name: "transporte",
        label: "Transporte",
        field: "transporte",
        align: "center",
      },
      {
        name: "comentario",
        label: "Comentario",
        field: "comentario",
        align: "left",
      },
    ];

    const rows = ref([
      {
        id: 1,
        pais: "SV",
        semana: "1",
        expediente: "SV25L7-001",
        tamano: "8T",
        fecha: "2025-01-02",
        status: "Pendiente LE",
        transporte: "CROWLEY",
        comentario: "Todo en orden",
        editable: false, // Estado de edición
      },
      {
        id: 2,
        pais: "GT",
        semana: "2",
        expediente: "GT25L7-002",
        tamano: "20'",
        fecha: "2025-01-09",
        status: "Notificado",
        transporte: "MAERSK",
        comentario: "Pendiente documentación",
        editable: false, // Estado de edición
      },
      {
        id: 3,
        pais: "HN",
        semana: "3",
        expediente: "HN25L7-003",
        tamano: "40'",
        fecha: "2025-01-16",
        status: "Despachado",
        transporte: "MSC",
        comentario: "Entregado al cliente",
        editable: false, // Estado de edición
      },
    ]);

    const editAllRows = () => {
      rows.value.forEach((row) => {
        row.editable = true; // Activa el modo de edición para todas las filas
      });
    };

    const saveAllRows = () => {
      rows.value.forEach((row) => {
        row.editable = false; // Guarda cambios y desactiva edición
      });
    };

    const cancelAllEdits = () => {
      // Cancela la edición restaurando los valores iniciales
      rows.value.forEach((row) => {
        row.editable = false; // Desactiva edición sin guardar
      });
    };

    return {
      loading,
      pagination,
      columns,
      rows,
      editAllRows,
      saveAllRows,
      cancelAllEdits,
    };
  },
};
</script>

<style lang="scss">
.table-container {
  width: 100%;
  padding: 16px;
}

.page-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 16px;
  text-align: center;
}

.editable-table {
  width: 100%;
  border-spacing: 0;
}

.q-tr {
  text-align: center;
}

.cell-content {
  padding: 8px 16px;
  text-align: center;
  vertical-align: middle;
}

.row-style {
  &:hover {
    background-color: #f9f9f9;
  }
}

.actions-container {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 16px;
}
</style>
