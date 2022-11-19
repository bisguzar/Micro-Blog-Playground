<template>
  <v-container fill-height fluid>
    <v-row class="align-center justify-center">
      <v-col cols="4">
        <v-card class="elevation-0" height="120%">
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="loginInfo.email"
              label="E-mail"
              required
            ></v-text-field>

            <v-text-field
              v-model="loginInfo.password"
              label="Password"
              required
            ></v-text-field>

            <v-btn
              :disabled="!valid"
              color="success"
              class="mr-4"
              @click="login"
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
  name: "login-component",
  data() {
    return {
      valid: true,
      loading: false,
      loginInfo: { email: "", password: "" },
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
    async login() {
      this.loading = true;
      const bodyFormData = {
        email: this.loginInfo.email,
        password: this.loginInfo.password,
      };
      console.log(bodyFormData);
      this.axios({
        method: "post",
        baseURL: "http://127.0.0.1:8000/login",
        data: JSON.stringify(bodyFormData),
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      })
        .then(async (response) => {
          this.loading = false;
          await new Promise((resolve) => setTimeout(resolve, 1000));
          if (response.status == 200) {
            localStorage.setItem("JWT", response.data.token);
            localStorage.setItem("isAuthenticated", true);
           this.$router.push("user");
          }
        })
        .catch(() => {
          this.loading = false;
        });
    },
  },
};
</script>
