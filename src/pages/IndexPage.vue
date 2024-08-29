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
          v-model="proveedor"
        />
        <label for="name">Descripcion</label>
        <input
          type="text"
          id="name"
          class="custom-input"
          placeholder="Ingrese Descripcion del Producto"
          v-model="descripcion"
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
              <q-radio v-model="answer" val="S" label="Sí"></q-radio>
              <q-radio v-model="answer" val="N" label="No"></q-radio>
            </q-field>
            <q-field label="Cover Ankle?" stack-label>
              <q-radio v-model="answer2" val="S" label="Sí"></q-radio>
              <q-radio v-model="answer2" val="N" label="No"></q-radio>
            </q-field>
            <q-field label="Wedge?" stack-label>
              <q-radio v-model="answer3" val="S" label="Sí"></q-radio>
              <q-radio v-model="answer3" val="N" label="No"></q-radio>
            </q-field>
            <q-field label="Upper straps fixed with studs?" stack-label>
              <q-radio v-model="answer4" val="S" label="Sí"></q-radio>
              <q-radio v-model="answer4" val="N" label="No"></q-radio>
            </q-field>
            <q-field label="Shoe cover?" stack-label>
              <q-radio v-model="answer10" val="S" label="Sí"></q-radio>
              <q-radio v-model="answer10" val="N" label="No"></q-radio>
            </q-field>
          </div>

          <div class="col-6">
            <q-field label="Metal Toe Cap?" stack-label>
              <q-radio v-model="answer5" val="S" label="Sí"></q-radio>
              <q-radio v-model="answer5" val="N" label="No"></q-radio>
            </q-field>
            <q-field label="Knee cover?" stack-label>
              <q-radio v-model="answer6" val="S" label="Sí"></q-radio>
              <q-radio v-model="answer6" val="N" label="No"></q-radio>
            </q-field>
            <q-field label="surround the toe and instep?" stack-label>
              <q-radio v-model="answer9" val="S" label="Sí"></q-radio>
              <q-radio v-model="answer9" val="N" label="No"></q-radio>
            </q-field>
            <q-field label="Sports shoes?" stack-label>
              <q-radio v-model="answer7" val="S" label="Sí"></q-radio>
              <q-radio v-model="answer7" val="N" label="No"></q-radio>
            </q-field>
            <div v-if="answer7 == 'S'">
              <q-field label="Snowboarding shoe?" stack-label>
                <q-radio v-model="answer8" val="S" label="Sí"></q-radio>
                <q-radio v-model="answer8" val="N" label="No"></q-radio>
              </q-field>
            </div>
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
            @click="enviarDatos()"
          />
        </q-form>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  data() {
    return {
      proveedor: "prueba",
      descripcion: "prueba",
      selectedOption: "",
      answer: "",
      answer2: "",
      answer3: "",
      answer4: "",
      answer5: "",
      answer6: "",
      answer7: "",
      answer8: "N",
      answer9: "",
      answer10: "",
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
    upper(material) {
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
        RUBBER: "O",
        SILK: "T",
        "SYNTHETIC FIBER": "T",
        TPU: "S",
        WOOL: "T",
      };
      return upperCategoryMap[material] || "UNKNOWN";
    },
    lining(material) {
      const materialCategoryMap = {
        "BLENDED YARN": "T",
        BOA: "T",
        COTTON: "T",
        EVA: "S",
        FLEECE: "T",
        GORTEX: "T",
        HEMP: "T",
        JUTE: "T",
        "LEATHER (Bovine)": "L",
        "LEATHER (Goat)": "L",
        "LEATHER (Pigskin)": "L",
        "LEATHER (Sheep)": "L",
        "No lining": "No Lining",
        NYLON: "T",
        POLYESTER: "T",
        PU: "S",
        PVC: "S",
        Raffia: "T",
        SILK: "T",
        "SYNTHETIC FIBER": "T",
        THINSULATE: "T",
        TRICO: "T",
      };

      return materialCategoryMap[material] || "UNKNOWN";
    },
    outsole(material) {
      const materialCategoryMap = {
        ABS: "S",
        COTTON: "T",
        EVA: "S",
        HEMP: "T",
        IRON: "METAL",
        JUTE: "T",
        "LEATHER (Bovine)": "L",
        "LEATHER (Goat)": "L",
        "LEATHER (Pigskin)": "L",
        "LEATHER (Sheep)": "L",
        PCU: "S",
        PLASTIC: "S",
        PU: "S",
        PVC: "S",
        PVR: "S",
        RUBBER: "RUBBER",
        SPU: "S",
        "SYNTHETIC FIBER": "T",
        TEXTILE: "T",
        TPR: "S",
        TPU: "S",
        TVR: "S",
      };

      return materialCategoryMap[material] || "UNKNOWN";
    },
    sockLinning(material) {
      const materialCategoryMap = {
        FOAM: "S",
        GORTEX: "T",
        JUTE: "T",
        "LAMINATED PVC": "S",
        LATEX: "S",
        "LEATHER (Bovine)": "L",
        "LEATHER (Goat)": "L",
        "LEATHER (Pigskin)": "L",
        "LEATHER (Sheep)": "L",
        PCU: "S",
        POLYPROPYLENE: "S",
        PU: "S",
        PVC: "S",
        RUBBER: "RUBBER",
        STRAW: "T",
        TEXTILE: "T",
        THINSULATE: "T",
        TRICO: "T",
        WOOD: "OTHER",
        WOOL: "T",
      };

      return materialCategoryMap[material] || "UNKNOWN";
    },
    insole(material) {
      const materialCategoryMap = {
        BOARD: "OTHER",
        NONE: "OTHER",
        "Non-woven or woven artificial textile": "OTHER",
        "Non-woven or woven natural textile": "OTHER",
        POLYPROPYLENE: "SYNTHETIC",
        "Synthetic & woven or non-woven textile": "OTHER",
        Textiles: "Elastodiene",
      };
      return materialCategoryMap[material] || "UNKNOWN";
    },
    obtenerCadenas() {
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
      string += this.answer;
      string += this.answer2;
      string += this.answer3;
      string += this.answer4;
      string += this.answer5;
      string += this.answer6;
      string += this.answer7;
      string += this.answer8;
      string += this.answer9;
      string += this.answer10;
      string += this.upper(this.model1);
      string += this.outsole(this.model3);
      return string;
    },
    async getPartida() {
      let string = this.obtenerCadenas();
      try {
        const response = await this.$axios.get("/api/partida", {
          params: {
            cadena: string,
          },
        });
        let datos = response.data;
        ///let datosNumber = JSON.parse(datos);
        //console.log(datosNumber.partida);
        //numeroPartida = datos.partida;
        return datos;
      } catch (error) {
        console.error("Error fetching data");
      }
    },
    async enviarDatos() {
      try {
        let partidaS = await this.getPartida();
        let partidaN = Number(partidaS.partida);
        console.log(this.descripcion);
        console.log(this.proveedor);
        let postData = {
          numeroArticulo: 11000,
          proveedor: this.proveedor,
          partida: partidaN,
          descripcion: this.descripcion,
          upper: this.model1,
          forro: this.model5,
          suela: this.model3, // no aparece
          origen: "GT",
          informacionAdicional: "Es grande", //no aparece
        };
        console.log(postData);
        const response = await this.$axios.post("/api/articulo", postData);
        console.log("Datos enviados con éxito:", response.data);
      } catch (error) {
        console.error("Error al enviar datos:", error);
      }
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
  height: 300vh;
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
