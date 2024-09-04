<template>
  <q-page class="form-page">
    <!-- Formulario Actual -->
    <div class="row q-col-gutter-md">
      <div class="col-4">
        <h6 class="label">Orden de Compra:</h6>
        <q-input filled v-model="ordenCompra" class="input-style" />
      </div>
      <div class="col-4">
        <h6 class="label">Contenedor:</h6>
        <q-input filled v-model="contenedor" class="input-style" />
      </div>
      <div class="col-4">
        <h6 class="label">Pedido Asociado:</h6>
        <q-input filled v-model="pedidoAsociado" class="input-style" />
      </div>
    </div>
    <div class="row justify-end">
      <div class="col-3">
        <q-btn color="primary" label="Buscar" class="btn-custom" />
      </div>
    </div>

    <OrdenCompra class="q-ma-none q-pa-none" />
    <PedidoAsociado class="q-ma-none q-pa-none" />
    <ContenedorComponente class="q-ma-none q-pa-none" />
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

<style scoped>
.form-page {
  padding: 20px;
  background-color: #f8f9fa; /* Fondo suave */
  border-radius: 8px; /* Bordes redondeados */
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Sombra sutil */
}

.label {
  font-weight: 600;
  color: #495057; /* Color de texto oscuro */
  margin-bottom: 4px; /* Espacio debajo del título */
}

.input-style {
  margin-bottom: 16px; /* Espacio entre los inputs */
  --q-color-primary: #027be3; /* Color principal personalizado */
  --q-input-padding: 12px; /* Padding personalizado dentro del input */
}

.q-input__inner {
  border-radius: 4px; /* Bordes redondeados para los inputs */
}

.btn-custom {
  padding: 12px 24px; /* Aumenta el tamaño del botón con padding */
  font-size: 16px; /* Aumenta el tamaño del texto del botón */
  border-radius: 8px; /* Bordes redondeados */
  margin-left: 0; /* Asegura que el botón esté alineado a la izquierda */
  min-width: 120px; /* Establece un ancho mínimo para que se vea más grande */
}
</style>
