<template>
  <v-container fill-height fluid>
    <v-row class="align-center justify-center">
      <v-col cols="4">
        <v-card class="elevation-0" height="120%">
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="registerInfo.name"
              :counter="10"
              :rules="nameRules"
              label="Name"
              required
            ></v-text-field>

            <v-text-field
              v-model="registerInfo.surname"
              :rules="nameRules"
              label="Surname"
              required
            ></v-text-field>
            <v-text-field
              v-model="registerInfo.username"
              :rules="nameRules"
              label="Username"
              required
            ></v-text-field>
            <v-text-field
              v-model="registerInfo.email"
              :rules="emailRules"
              label="E-mail"
              required
            ></v-text-field>
            <v-text-field
              v-model="registerInfo.password"
              label="Password"
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
  </v-container>
</template>
<script>
export default {
  name: "register-component",
  data() {
    return {
      valid: true,
      loading: false,
      registerInfo: {
        name: "",
        surname: "",
        username: "",
        email: "",
        password: "",
        rPassword: "",
      },
      userList: [],

      nameRules: [
        (v) => !!v || "Name is required",
        (v) => (v && v.length <= 10) || "Name must be less than 10 characters",
      ],
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
      ],
    };
  },
  methods: {
    async postUser() {
      this.loading = true;

      const bodyFormData = {
        name: this.registerInfo.name,
        surname: this.registerInfo.surname,
        username: this.registerInfo.username,
        email: this.registerInfo.email,
        password: this.registerInfo.password,
      };
      this.axios({
        method: "post",
        baseURL: "http://127.0.0.1:8000/createUser",
        data: JSON.stringify(bodyFormData),
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      }).then(async (response) => {
        await new Promise((resolve) => setTimeout(resolve, 5000));
        if (response.status == 200) {
          this.$router.push("login");
        }
        this.loading = false;
      });
    },
  },
};
</script>
