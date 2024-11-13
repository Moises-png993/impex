<template>
  <q-page class="flex flex-center bg-yellow-50">
    <q-card class="login-card">
      <q-card-section class="text-center q-pt-lg">
        <div class="text-h4 text-weight-bold text-yellow-9">SIMPEX</div>
        <div class="text-subtitle1 text-grey-7">Iniciar Sesión</div>
      </q-card-section>

      <q-card-section>
        <q-form @submit.prevent="onSubmit" class="q-gutter-y-md">
          <q-input
            outlined
            v-model="username"
            label="Usuario"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Por favor ingrese un usuario']"
            color="yellow-9"
            class="input-field"
          >
            <template v-slot:prepend>
              <q-icon name="person" color="yellow-9" />
            </template>
          </q-input>

          <q-input
            outlined
            type="password"
            v-model="password"
            label="Contraseña"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Por favor ingrese una contraseña']"
            color="yellow-9"
            class="input-field"
          >
            <template v-slot:prepend>
              <q-icon name="lock" color="yellow-9" />
            </template>
          </q-input>

          <div>
            <q-btn 
              label="Iniciar Sesión" 
              type="submit" 
              color="yellow-9" 
              class="full-width q-py-sm"
              :loading="loading"
              unelevated
            />
          </div>
        </q-form>
      </q-card-section>

      <q-card-section class="text-center q-pt-none">
        <q-btn flat color="grey-7" label="¿Olvidaste tu contraseña?" />
      </q-card-section>

      <q-dialog v-model="showErrorDialog">
        <q-card>
          <q-card-section class="row items-center">
            <q-avatar icon="error" color="red" text-color="white" />
            <span class="q-ml-sm">{{ errorMessage }}</span>
          </q-card-section>
          <q-card-actions align="right">
            <q-btn flat label="Cerrar" color="primary" v-close-popup />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const username = ref('')
const password = ref('')
const loading = ref(false)
const showErrorDialog = ref(false)
const errorMessage = ref('')

const onSubmit = async () => {
  loading.value = true
  try {
    const response = await axios.post('http://127.0.0.1:3000/login', {
      username: username.value,
      password: password.value
    })

    if (response.data.access_token) {
      console.log("Login exitoso")
      const token = response.data.access_token
      const tokenType = response.data.token_type
     
      localStorage.setItem('access_token', token)
      localStorage.setItem('token_type', tokenType)
       router.push('/menu')

      // Aquí puedes redirigir al usuario o realizar otras acciones después del login exitoso
    } else {
      throw new Error('Token no recibido')
    }
  } catch (error) {
    console.log(error)

    if (error.response && error.response.status === 401) {
      errorMessage.value = 'Usuario o contraseña incorrectos'
      showErrorDialog.value = true
    } else if (error.response) {
      console.log('Error en la respuesta del servidor', error.response)
      errorMessage.value = 'Error en el servidor. Por favor, intente más tarde.'
      showErrorDialog.value = true
    } else if (error.request) {
      console.log('No hubo respuesta del servidor', error.request)
      errorMessage.value = 'No se pudo conectar con el servidor. Verifique su conexión.'
      showErrorDialog.value = true
    } else {
      console.log('Error en la solicitud', error.message)
      errorMessage.value = 'Ocurrió un error inesperado. Por favor, intente de nuevo.'
      showErrorDialog.value = true
    }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-card {
  width: 100%;
  max-width: 400px;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  background-color: white;
}

.input-field {
  margin-bottom: 16px;
}

.q-btn {
  font-weight: bold;
  letter-spacing: 1px;
  border-radius: 8px;
}

.bg-yellow-50 {
  background-color: #FFFDE7;
}

:deep(.q-field--outlined .q-field__control) {
  border-radius: 8px;
}

:deep(.q-field--outlined .q-field__control:hover:before) {
  border-color: #F57F17;
}

:deep(.q-field--focused .q-field__control:before) {
  border-color: #F57F17 !important;
}
</style>