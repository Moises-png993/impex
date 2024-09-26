<template>
  <q-page class="bg-yellow-50">
    <q-btn
      color="yellow-9"
      icon="add"
      label="Nuevo Embarque"
      class="q-ma-md"
      @click="showPopup = true"
    />

    <q-dialog v-model="showPopup" persistent>
      <q-card style="min-width: 350px">
        <q-card-section class="bg-yellow-9 text-white">
          <div class="text-h6">Nuevo Embarque</div>
        </q-card-section>

        <q-card-section class="q-pt-md">
          <q-form @submit="onSubmit" class="q-gutter-md">
            <q-input
              filled
              v-model="formData.embarque"
              label="Embarque"
              hint="Ejemplo: GT24L7-043"
              :rules="[val => !!val || 'El campo es requerido']"
            />

            <q-input
              filled
              v-model="formData.expediente"
              label="Expediente"
              hint="Ejemplo: 10022345"
              :rules="[val => !!val || 'El campo es requerido']"
            />

            <q-input
              filled
              v-model="formData.transporte"
              label="Transporte"
              hint="Ejemplo: 991221"
              :rules="[val => !!val || 'El campo es requerido']"
            />

            <q-select
              filled
              v-model="formData.checkpoint"
              :options="['L1', 'L7', 'CB']"
              label="Checkpoint"
              :rules="[val => !!val || 'El campo es requerido']"
            />

            <q-input
              filled
              v-model="formData.comentario"
              type="textarea"
              label="Comentario"
            />

            <q-file
              filled
              v-model="formData.documentos"
              label="Documentos"
              multiple
              hint="Seleccione uno o más archivos"
              :rules="[val => val && val.length > 0 || 'Debe subir al menos un documento']"
            >
              <template v-slot:prepend>
                <q-icon name="attach_file" />
              </template>
            </q-file>

            <div class="row justify-end q-mt-md">
              <q-btn label="Cancelar" color="grey-7" v-close-popup class="q-mr-sm" />
              <q-btn label="Guardar" type="submit" color="yellow-9" />
            </div>
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()
const showPopup = ref(false)

const formData = ref({
  embarque: '',
  expediente: '',
  transporte: '',
  checkpoint: null,
  comentario: '',
  documentos: null
})

const onSubmit = () => {
  // Aquí puedes manejar el envío del formulario
  console.log('Datos del formulario:', formData.value)
  
  // Mostrar notificación de éxito
  $q.notify({
    color: 'positive',
    message: 'Formulario enviado con éxito',
    icon: 'check'
  })

  // Cerrar el popup
  showPopup.value = false

  // Reiniciar el formulario
  formData.value = {
    embarque: '',
    expediente: '',
    transporte: '',
    checkpoint: null,
    comentario: '',
    documentos: null
  }
}
</script>

<style scoped>
.bg-yellow-50 {
  background-color: #FFFDE7;
}

.bg-yellow-9 {
  background-color: #F57F17;
}
</style>