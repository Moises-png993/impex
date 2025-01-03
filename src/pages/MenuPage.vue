<template>
  <q-page class="bg-yellow-50 flex flex-center">
    <q-card flat class="menu-grid">
      <div class="text-center q-pb-lg">
        <div class="text-h4 text-weight-bold text-yellow-9">Bienvenido</div>
      </div>

      <div class="grid-container">
        <q-btn flat class="menu-card" @click="goTo('exportaciones')">
          <q-icon name="flight_takeoff" size="56px" color="yellow-9" />
          <div class="text-h6 text-yellow-9 q-mt-sm">Exportaciones</div>
        </q-btn>

        <q-btn flat class="menu-card" @click="goTo('trafico-contenedores')">
          <q-icon name="local_shipping" size="56px" color="yellow-9" />
          <div class="text-h6 text-yellow-9 q-mt-sm">Tráfico Contenedores</div>
        </q-btn>

        <q-btn flat class="menu-card" @click="goTo('aforo')">
          <q-icon name="scale" size="56px" color="yellow-9" />
          <div class="text-h6 text-yellow-9 q-mt-sm">Aforo</div>
        </q-btn>

        <q-btn flat class="menu-card" @click="goTo('fast-email')">
          <q-icon name="email" size="56px" color="yellow-9" />
          <div class="text-h6 text-yellow-9 q-mt-sm">Fast Email</div>
        </q-btn>
      </div>
    </q-card>
  </q-page>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const goTo = (route) => {
  router.push(`/${route}`);
};
</script>

<style scoped>
.menu-grid {
  width: 100%;
  max-width: 600px;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 16px;
}

.menu-card {
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
  padding: 16px;
  transition: transform 0.2s, box-shadow 0.2s;
}

.menu-card:hover {
  transform: scale(1.05);
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
}
</style>
