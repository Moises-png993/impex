<template>
  <q-page class="flex flex-center bg-container">
    <div class="form-container">
      <h4>Formulario Proveedores</h4>
      <h6>Datos Generales:</h6>
      <div class="form-group">
        <label for="name">Proveedor</label>
        <input
          type="text"
          id="name"
          class="custom-input"
          placeholder="Ingrese el nombre del Proveedor"
        />
        <label for="name">Numero de articulo</label>
        <input
          type="number"
          id="name"
          class="custom-input"
          placeholder="Ingresa Numero de articulo"
        />
        <label for="name">Descripcion</label>
        <input
          type="text"
          id="name"
          class="custom-input"
          placeholder="Ingrese Descripcion del Producto"
        />
        <h6>Construccion</h6>
        <div class="row">
          <div class="col-6">
            <q-radio
              v-model="selectedOption"
              val="opcion1"
              label="Adhesive only (cement)"
            ></q-radio>
            <q-radio
              v-model="selectedOption"
              val="option2"
              label="Adhesive with stitching, nails, staples, etc"
            ></q-radio>
            <q-radio
              v-model="selectedOption"
              val="option3"
              label="Cement"
            ></q-radio>
            <q-radio
              v-model="selectedOption"
              val="option4"
              label="Espadrille"
            ></q-radio>
            <q-radio
              v-model="selectedOption"
              val="option5"
              label="Glued and stitched"
            ></q-radio>
            <q-radio
              v-model="selectedOption"
              val="option6"
              label="Goodyear welt"
            ></q-radio>
            <q-radio
              v-model="selectedOption"
              val="option13"
              label="Injected"
            ></q-radio>
          </div>
          <div class="col-6">
            <q-radio
              v-model="selectedOption"
              val="option7"
              label="Mock welt (welt)"
            ></q-radio>
            <q-radio
              v-model="selectedOption"
              val="option8"
              label="One piece molded (injection molded)"
            ></q-radio>
            <q-radio
              v-model="selectedOption"
              val="option9"
              label="Stitch & Turn"
            ></q-radio>
            <q-radio
              v-model="selectedOption"
              val="option10"
              label="Stitched"
            ></q-radio>
            <q-radio
              v-model="selectedOption"
              val="option11"
              label="Vulcanized"
            ></q-radio>
            <q-radio
              v-model="selectedOption"
              val="option12"
              label="Welts"
            ></q-radio>
          </div>
        </div>
        <h6>Caracteristicas</h6>
        <div class="row">
          <div class="col-6">
            <q-field label="Water Proof?" stack-label>
              <q-radio v-model="answer" val="yes" label="Sí"></q-radio>
              <q-radio v-model="answer" val="no" label="No"></q-radio>
            </q-field>
            <q-field label="Cover Ankle?" stack-label>
              <q-radio v-model="answer2" val="yes" label="Sí"></q-radio>
              <q-radio v-model="answer2" val="no" label="No"></q-radio>
            </q-field>
            <q-field label="Wedge?" stack-label>
              <q-radio v-model="answer3" val="yes" label="Sí"></q-radio>
              <q-radio v-model="answer3" val="no" label="No"></q-radio>
            </q-field>
          </div>

          <div class="col-6">
            <q-field label="Metal Toe Cap?" stack-label>
              <q-radio v-model="answer4" val="yes" label="Sí"></q-radio>
              <q-radio v-model="answer4" val="no" label="No"></q-radio>
            </q-field>
            <q-field label="Over Ankle?" stack-label>
              <q-radio v-model="answer5" val="yes" label="Sí"></q-radio>
              <q-radio v-model="answer5" val="no" label="No"></q-radio>
            </q-field>
          </div>
        </div>
        <h5>Materiales del Calzado</h5>
        <p>Upper:</p>
        <div class="row">
          <div class="col-6">
            <q-select v-model="model1" :options="options" label="Material" />
          </div>
          <div class="col-6">
            <input
              type="number"
              id="name"
              class="custom-input"
              placeholder="Porcentaje del Material"
            />
          </div>
        </div>
        <p>Lining:</p>
        <div class="row">
          <div class="col-6">
            <q-select v-model="model2" :options="options2" label="Material" />
          </div>
          <div class="col-6">
            <input
              type="number"
              id="name"
              class="custom-input"
              placeholder="Porcentaje del Material"
            />
          </div>
        </div>
        <p>Outsole:</p>
        <div class="row">
          <div class="col-6">
            <q-select v-model="model3" :options="options3" label="Material" />
          </div>
          <div class="col-6">
            <input
              type="number"
              id="name"
              class="custom-input"
              placeholder="Porcentaje del Material"
            />
          </div>
        </div>
        <p>Sock Lining</p>
        <div class="row">
          <div class="col-6">
            <q-select v-model="model4" :options="options4" label="Material" />
          </div>
          <div class="col-6">
            <input
              type="number"
              id="name"
              class="custom-input"
              placeholder="Porcentaje del Material"
            />
          </div>
        </div>
        <p>Insole</p>
        <div class="row">
          <div class="col-6">
            <q-select v-model="model5" :options="options5" label="Material" />
          </div>
          <div class="col-6">
            <input
              type="number"
              id="name"
              class="custom-input"
              placeholder="Porcentaje del Material"
            />
          </div>
        </div>
        <q-form>
          <q-btn
            type="submit"
            color="primary"
            class="submit-btn"
            label="Enviar"
            @click="obtenerCadenas"
          />
        </q-form>

        <div class="form-group"></div>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  data() {
    return {
      selectedOption: "",
      answer: "",
      answer2: "",
      answer3: "",
      answer4: "",
      answer5: "",
      options: [
        "Action Leather",
        "BLENDED YARN",
        "COTTON",
        "EVA",
        "FELT",
        "Glass",
        "HEMP",
        "JUTE",
        "LAMINATED PVC",
        "LEATHER (Bovine)",
        "LEATHER (Goat)",
        "LEATHER (Pigskin)",
        "LEATHER (Sheep)",
        "NYLON",
        "POLYESTER",
        "POLYPROPYLENE",
        "PU",
        "PVC",
        "Raffia",
        "RUBBER",
        "SILK",
        "SYNTHETIC FIBER",
        "TPU",
        "WOOL",
      ],
      options2: [
        "BLENDED YARN",
        "BOA",
        "COTTON",
        "EVA",
        "FLEECE",
        "GORTEX",
        "HEMP",
        "JUTE",
        "LEATHER (Bovine)",
        "LEATHER (Goat)",
        "LEATHER (Pigskin)",
        "LEATHER (Sheep)",
        "No lining",
        "NYLON",
        "POLYESTER",
        "PU",
        "PVC",
        "Raffia",
        "SILK",
        "SYNTHETIC FIBER",
        "THINSULATE",
        "TRICO",
      ],
      options3: [
        "ABS",
        "COTTON",
        "EVA",
        "HEMP",
        "IRON",
        "JUTE",
        "LEATHER (Bovine)",
        "LEATHER (Goat)",
        "LEATHER (Pigskin)",
        "LEATHER (Sheep)",
        "PCU",
        "PLASTIC",
        "PU",
        "PVC",
        "PVR",
        "RUBBER",
        "SPU",
        "SYNTHETIC FIBER",
        "TEXTILE",
        "TPR",
        "TPU",
        "TVR",
      ],
      options4: [
        "FOAM",
        "GORTEX",
        "JUTE",
        "LAMINATED PVC",
        "LATEX",
        "LEATHER (Bovine)",
        "LEATHER (Goat)",
        "LEATHER (Pigskin)",
        "LEATHER (Sheep)",
        "PCU",
        "POLYPROPYLENE",
        "PU",
        "PVC",
        "RUBBER",
        "STRAW",
        "TEXTILE",
        "THINSULATE",
        "TRICO",
        "WOOD",
        "WOOL",
      ],
      options5: [
        "BOARD",
        "NONE",
        "Non-woven or woven artificial textile",
        "Non-woven or woven natural textile",
        "POLYPROPYLENE",
        "Synthetic & woven or non-woven textile",
        "Textiles",
      ],
      model1: "",
      model2: "",
      model3: "",
      model4: "",
      model5: "",
    };
  },
  methods: {
    obtenerCadenas() {
      const upperCategoryMap = {
        "Action Leather": "L",
        "COSTED LEATHER": "L",
        "BLENDED YARN": "T",
        COTTON: "T",
        EVA: "S",
        FELT: "T",
        Glass: "O",
        HEMP: "T",
        JUTE: "TL",
        "LAMINATED PVC": "S",
        "LEATHER (Bovine)": "L",
        "LEATHER (Goat)": "L",
        "LEATHER (Pigskin)": "L",
        "LEATHER (Sheep)": "L",
        NYLON: "T",
        POLYESTER: "T",
        POLYPROPYLENE: "S",
        PU: "S",
        PVC: "S",
        Raffia: "T",
        RUBBER: "R",
        SILK: "T",
        "SYNTHETIC FIBER": "T",
        TPU: "S",
        WOOL: "T",
      };
      let string = "";
      if (
        this.selectedOption == "option1" ||
        this.selectedOption == "option2" ||
        this.selectedOption == "optio3"
      ) {
        string += "S";
      } else {
        string += "N";
      }
      let upper = upperCategoryMap[this.model1];
      console.log(upper);
    },
  },
};
</script>
<style scoped>
.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  font-size: 16px;
  color: #333;
  margin-bottom: 8px;
  font-weight: bold;
}

.custom-input {
  width: 100%;
  padding: 10px 15px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid #ccc;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: border-color 0.3s ease;
}

.custom-input:focus {
  border-color: #a8edea;
  outline: none;
  box-shadow: 0 0 8px rgba(168, 237, 234, 0.5);
}

.custom-input::placeholder {
  color: #aaa;
  font-style: italic;
}
.bg-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* Asegura que el contenedor ocupe toda la altura de la pantalla */
  background: linear-gradient(135deg, #a8edea, #fed6e3);
}

.form-container {
  background-color: #ffffff;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.1);
  width: 80%;
  max-width: 600px;
  /* Elimina el valor de height para permitir que el contenedor se ajuste al contenido */
}
.submit-btn {
  width: 100%;
  padding: 10px 20px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: bold;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s ease, transform 0.3s ease;
  margin-top: 20px; /* Ajusta el valor según tu necesidad */
}

.submit-btn:hover {
  background-color: #0056b3; /* Ajusta el color según tu paleta */
  transform: translateY(-2px);
}

.submit-btn:active {
  background-color: #004494; /* Ajusta el color según tu paleta */
  transform: translateY(0);
}
</style>
