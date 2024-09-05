<template>
  <q-page class="form-page">
    <!-- Formulario Actual -->
    <div class="row q-col-gutter-md">
      <div class="col-4">
        <h6>Orden de Compra:</h6>
        <q-input filled v-model="ordenCompra" class="input-style" />
      </div>
      <div class="col-4">
        <h6>Contenedor:</h6>
        <q-input filled v-model="contenedor" class="input-style" />
      </div>
      <div class="col-4">
        <h6>Pedido Asociado:</h6>
        <q-input filled v-model="pedidoAsociado" class="input-style" />
      </div>
    </div>
    <div class="row justify-end q-mt-md">
      <div class="col-3">
        <q-btn color="primary" label="Buscar" class="btn-custom" />
      </div>
    </div>

    <OrdenCompra class="table-content q-mt-md" />
    <PedidoAsociado class="table-content q-mt-md" />
    <ContenedorComponente class="table-content q-mt-md" />
  </q-page>
</template>

<script>
import OrdenCompra from "src/components/ordenCompra.vue";
import PedidoAsociado from "src/components/pedidoAsociado.vue";
import ContenedorComponente from "src/components/contenedorComponente.vue";

export default {
  name: "FormComponent",
  components: {
    OrdenCompra,
    PedidoAsociado,
    ContenedorComponente,
  },
  data() {
    return {
      ordenCompra: "",
      contenedor: "",
      pedidoAsociado: "",
    };
  },
};
</script>

<style>
.form-page {
  padding: 20px; /* Aumenta el padding alrededor del contenido */
  background-color: #f8f9fa;
  border-radius: 8px;
}

.input-style {
  margin-bottom: 15px;
  --q-color-primary: #027be3;
  --q-input-padding: 12px;
}

.q-input__inner {
  border-radius: 4px;
}

.btn-custom {
  padding: 12px 24px;
  font-size: 16px;
  border-radius: 8px;
  min-width: 120px;
}

.table-content {
  margin: 20px 0; /* Agrega margen vertical alrededor de las tablas */
  padding: 20px; /* Agrega padding alrededor del contenido de las tablas */
}
</style>
