<template>
  <q-layout view="lHh Lpr lFf">
    <table>
      <thead>
        <tr>
          <th id="thPais">PAIS</th>
          <th id="thSemana">Semana</th>
          <th id="thExpediente">EXPEDIENTE</th>
          <th id="thTamano">Tamaño</th>
          <th id="thFechaDespacho">FECHA DESPACHO</th>
          <th id="thStatus">Status</th>
          <th id="thTransporte">TRANSPORTE</th>
          <th id="thComentario">Comentario</th>
          <th id="thFts">FTS</th>
          <th id="thSap">SAP</th>
          <th id="thAgente">AGENTE</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td id="tdPais">
            <select disabled>
              <option value="SV" selected>SV</option>
              <option value="GT">GT</option>
              <option value="HN">HN</option>
              <option value="NI">NI</option>
              <option value="CR">CR</option>
            </select>
          </td>
          <td id="tdSemana" contenteditable="false">1</td>
          <td id="tdExpediente" contenteditable="false">SV25L7-001</td>
          <td id="tdTamano">
            <select disabled>
              <option value="8T">8T</option>
              <option value="20'">20'</option>
              <option value="40'">40'</option>
              <option value="48'">48'</option>
              <option value="53'">53'</option>
            </select>
          </td>
          <td id="tdFechaDespacho">
            <input type="date" value="2025-01-02" disabled />
          </td>
          <td id="tdStatus">
            <select disabled>
              <option value="Pendiente LE">Pendiente LE</option>
              <option value="Pendiente Prep">Pendiente Prep</option>
              <option value="Pendiente Notificación">
                Pendiente Notificación
              </option>
              <option value="Notificado">Notificado</option>
              <option value="Despachado">Despachado</option>
            </select>
          </td>
          <td id="tdTransporte">
            <select disabled>
              <option value="CROWLEY">CROWLEY</option>
              <option value="ACOAVANZAR">ACOAVANZAR</option>
              <option value="Transportes Continental">
                Transportes Continental
              </option>
            </select>
          </td>
          <td id="tdComentario" contenteditable="false">Todo en orden</td>
          <td id="tdFts">
            <select disabled>
              <option value="Pendiente">Pendiente</option>
              <option value="Verificar">Verificar</option>
              <option value="Notificado">Notificado</option>
            </select>
          </td>
          <td id="tdSap" contenteditable="false">Cerrado</td>
          <td id="tdAgente">
            <select disabled>
              <option value="Mauricio">Mauricio</option>
              <option value="Moises">Moises</option>
              <option value="Robert">Robert</option>
            </select>
          </td>
        </tr>
        <!-- Más filas pueden ir aquí -->
      </tbody>
    </table>
  </q-layout>
</template>
<style>
body {
  font-family: Arial, sans-serif;
  margin: 20px;
  background-color: #f4f4f4;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  background-color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
th,
td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: left;
}
th {
  background-color: #007bff;
  color: white;
  font-weight: bold;
}
tr:nth-child(even) {
  background-color: #f9f9f9;
}
tr:hover {
  background-color: #f1f1f1;
}
button {
  margin: 10px 0;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}
button:hover {
  background-color: #0056b3;
}
button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}
td[contenteditable="true"] {
  font-weight: normal;
}
td[contenteditable="false"] {
  font-weight: bold;
}
select,
input[type="date"] {
  width: 100%;
  padding: 5px;
  font-weight: bold;
  background-color: white;
  border: none;
  outline: none;
  pointer-events: none; /* Deshabilitar interacciones */
}
select:enabled,
input[type="date"]:enabled {
  pointer-events: auto;
  cursor: pointer;
}
.filter-container {
  margin-bottom: 20px;
}
.filter-container label {
  margin-right: 10px;
}

/* Estilo del Modal */
.modal {
  display: none;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0, 0, 0);
  background-color: rgba(0, 0, 0, 0.4);
  padding-top: 60px;
}
.modal-content {
  background-color: #fefefe;
  margin: 5% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  max-width: 500px;
}
.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}
.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
</style>
