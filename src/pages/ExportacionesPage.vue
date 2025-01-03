<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <!-- Botón para abrir el Drawer -->
        <q-btn flat round icon="menu" @click="toggleDrawer" />

        <!-- Título -->
        <q-toolbar-title>Reporte de Exportaciones</q-toolbar-title>

        <!-- Botón para redirigir -->
        <q-btn
          flat
          round
          dense
          icon="open_in_new"
          @click="goToMenu"
          class="q-ml-auto"
          label="Ir al menú"
        />
      </q-toolbar>
    </q-header>

    <q-page-container>
      <q-page>
        <div v-if="selectedOption === 'semanaActual'">
          <h2>Semana Actual</h2>
          <p>Este es el contenido de la semana actual.</p>
        </div>
        <div v-else-if="selectedOption === 'porSemana'">
          <h2>Por Semana</h2>
          <p>Este es el contenido por semana.</p>
        </div>
        <div v-else-if="selectedOption === 'kanban'">
          <h2>Kanban</h2>
          <p>Este es el contenido del tablero Kanban.</p>
        </div>
        <div v-else-if="selectedOption === 'todo'">
          <h2>Todo</h2>
          <p>Este es el contenido de todo.</p>
        </div>
        <div v-else>
          <h2>Bienvenido</h2>
          <p>Selecciona una opción en el menú para ver el contenido.</p>
        </div>
      </q-page>
    </q-page-container>

    <!-- Drawer lateral -->
    <q-drawer v-model="rightDrawer" side="left" elevated>
      <q-list>
        <q-item clickable v-ripple @click="selectOption('semanaActual')">
          <q-item-section>Semana Actual</q-item-section>
        </q-item>
        <q-item clickable v-ripple @click="selectOption('porSemana')">
          <q-item-section>Por semana</q-item-section>
        </q-item>
        <q-item clickable v-ripple @click="selectOption('kanban')">
          <q-item-section>Kanban</q-item-section>
        </q-item>
        <q-item clickable v-ripple @click="selectOption('todo')">
          <q-item-section>Todo</q-item-section>
        </q-item>
      </q-list>
    </q-drawer>
  </q-layout>
</template>

<script>
export default {
  data() {
    return {
      rightDrawer: false,
      selectedOption: "", // Almacena la opción seleccionada
    };
  },
  methods: {
    toggleDrawer() {
      this.rightDrawer = !this.rightDrawer;
    },
    goToMenu() {
      // Redirige al menú
      window.location.href = "http://localhost:9000/#/menu";
    },
    selectOption(option) {
      // Actualiza la opción seleccionada y cierra el drawer
      this.selectedOption = option;
      this.rightDrawer = false;
    },
  },
};
</script>
