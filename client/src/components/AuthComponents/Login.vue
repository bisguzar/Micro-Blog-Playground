<template>
  <v-container fill-height fluid>
    <v-row class="align-center justify-center">
      <v-col cols="4">
        <v-card class="elevation-0" height="120%">
          <v-card-title primary-title> Please Login </v-card-title>
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="loginInfo.email"
              label="E-mail"
              :rules="emailRules"
              required
            ></v-text-field>

            <v-text-field
              v-model="loginInfo.password"
              label="Password"
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
               :type="showPassword ? 'text' : 'password'"
                @click:append="showPassword = !showPassword"
              :rules="nonEmpty"
              required
            ></v-text-field>

            <v-btn
              :disabled="!valid"
              color="success"
              class="mr-4"
              @click="login"
              :loading="loading"
            >
              Login
            </v-btn>
            
            <v-btn
              color="success"
              class="mr-4"
              @click="$router.push('register')"
              :loading="loading"
            >
              Sign Up
            </v-btn>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import { LOGIN, LOGOUT } from "@/core/services/store/auth.module";
import { mapGetters, mapState } from "vuex";

export default {
  name: "login-component",
  data() {
    return {
      valid: true,
      loading: false,
       showPassword: false,
      loginInfo: { email: "", password: "" },
      nonEmpty: [(v) => !!v || "E-mail is required"],
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
    goHome() {
      this.$router.push("home");
    },
    async login() {
      this.loading = true;
      const email = this.loginInfo.email;
      const password = this.loginInfo.password;
      this.$store.dispatch(LOGOUT);
      this.$store
        .dispatch(LOGIN, { email, password })
        .then((response) => {
          this.loadingSignIn1 = false;
          console.log(response);
          if (response.status != 500) {
            this.goHome();
          }
        })
        .catch(() => {
          this.loading = false;
        });
    },
  },
  created() {
    this.$store.dispatch(LOGOUT);
  },
  computed: {
    ...mapState({
      errors: (state) => state.auth.errors,
    }),
    ...mapGetters(["currentUser"]),
  },
};
</script>
