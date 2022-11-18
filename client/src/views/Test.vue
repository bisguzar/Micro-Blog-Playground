<template>
  <div class="test">
    <v-row class="align-center justify-center">
      <v-col cols="8">
        <v-card class="elevation-0">
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="name"
              :counter="10"
              :rules="nameRules"
              label="Name"
              required
            ></v-text-field>

            <v-text-field
              v-model="surname"
              :rules="nameRules"
              label="Surname"
              required
            ></v-text-field>

            <v-btn
              :disabled="!valid"
              color="success"
              class="mr-4"
              @click="postUser"
              :loading="loading"
            >
              Submit
            </v-btn>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
    <v-row class="align-center justify-center">
      <v-col cols="8">
        <v-data-table
          :headers="headers"
          :items="userList"
          :items-per-page="5"
          class="elevation-1"
        ></v-data-table>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    valid: true,
    name: "",
    surname: "",
    userList: [],
    loading: false,
    headers: [
      {
        text: "Name",
        align: "start",
        sortable: false,
        value: "name",
      },
      { text: "Surname", value: "surname" },
    ],
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => (v && v.length <= 10) || "Name must be less than 10 characters",
    ],
    checkbox: false,
  }),
  mounted() {
    this.getUserList();
  },
  methods: {
    async postUser() {
      this.loading = true;
      const bodyFormData = {
        name: this.name,
        surname: this.surname,
      };
      axios({
        method: "post",
        baseURL: "http://127.0.0.1:8000/createUser",
        data: JSON.stringify(bodyFormData),
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      }).then(async () => {
        this.userList.push(bodyFormData);
        await new Promise((resolve) => setTimeout(resolve, 5000));

        this.getUserList();
        this.loading = false;
      });
    },
    getUserList() {
      this.axios.get("http://127.0.0.1:8000/getUserList").then((response) => {
        this.userList = response.data;
        console.log(response.data);
      });
    },
  },
};
</script>
