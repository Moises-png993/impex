<template>
  <q-page>
    <div class="row q-mt-md">
      <div class="col-6 q-pl-md">
        <p>Busqueda por estilo</p>
        <div class="row items-center">
          <q-input v-model="estilo" dense style="width: 25%" />
          <q-btn
            color="white"
            text-color="black"
            label="Buscar"
            class="q-ml-sm"
            @click="buscarEstilo"
          />
        </div>
        <q-table
          :rows="tableData"
          :columns="columns"
          row-key="contenedor"
          class="q-mx-lg q-mt-lg"
          :dense="true"
          :striped="true"
          :bordered="true"
        />
      </div>
      <div class="col-6 q-pl-md">
        <p>Busqueda por contenedor</p>
        <div class="row items-center">
          <q-input v-model="contenedor" dense style="width: 25%" />
          <q-btn
            color="white"
            text-color="black"
            label="Buscar"
            class="q-ml-sm"
            @click="buscarContenedor"
          />
          <div class="col-10">
            <q-table
              :rows="tableData2"
              :columns="columns2"
              row-key="estilo"
              class="q-mx-lg q-mt-lg"
              :dense="true"
              :striped="true"
              :bordered="true"
            />
          </div>
        </div>
      </div>
    </div>
    <DataTable></DataTable>
  </q-page>
</template>

<script>
import DataTable from "src/components/ordenCompra.vue"; // Ajusta la ruta según tu estructura de proyecto

export default {
  components: {
    DataTable,
  },
  data() {
    return {
      estilo: "",
      contenedor: "",
      columns: [
        {
          name: "contenedor",
          label: "Contenedor",
          align: "left",
          field: "contenedor",
        },
        {
          name: "eta_semana",
          label: "ETA PUERTO (SEMANA)",
          align: "center",
          field: "eta_semana",
        },
        {
          name: "total_cantidad",
          label: "Total CANTIDAD",
          align: "right",
          field: "total_cantidad",
        },
      ],
      tableData: [],
      columns2: [
        { name: "estilo", label: "Estilo", align: "left", field: "ESTILO" },
        {
          name: "cantidad",
          label: "Cantidad",
          align: "right",
          field: "CANTIDAD",
        },
      ],
      tableData2: [],
    };
  },
  methods: {
    buscarEstilo() {
      const url = `https://impex-zctt.onrender.com/api/eta-semana?estilo=${encodeURIComponent(
        this.estilo
      )}`;
      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          if (data.length > 0) {
            this.tableData = data.map((item) => ({
              contenedor: item.CONTENEDOR,
              eta_semana: item["ETA PUERTO (SEMANA)"],
              total_cantidad: item["Total CANTIDAD"],
            }));
          }
          console.log(data);
          console.log(data.CONTENEDOR);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    buscarContenedor() {
      const url = `https://impex-zctt.onrender.com/api/estilo-cantidad?contenedor=${encodeURIComponent(
        this.contenedor
      )}`;
      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          if (data.length > 0) {
            this.tableData2 = data.map((item) => ({
              ESTILO: item.ESTILO,
              CANTIDAD: item.CANTIDAD,
            }));
          }
          console.log(data);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
  },
};
</script>

<style>
.custom-table-margin {
  margin-top: 16px; /* Ajusta este valor según sea necesario */
}
</style>
