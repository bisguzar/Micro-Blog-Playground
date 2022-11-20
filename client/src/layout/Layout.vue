<template>
  <div>
    <v-app-bar app color="primary" class="mb-12" dark>
      <div class="d-flex align-center">
        <v-toolbar-title>Micro-Blog</v-toolbar-title>
      </div>

      <v-spacer></v-spacer>

      <router-link to="/"><div class="white--text mx-2">Home</div></router-link>

      <router-link to="/user"
        ><div class="white--text mx-2">User</div></router-link
      >
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn icon color="white" dark v-bind="attrs" v-on="on">
            <v-icon>mdi-account</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item v-for="(item, index) in menuItems" :key="index"
            ><router-link :to="item.route" class="text-decoration-none">
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </router-link>
          </v-list-item>
          <v-list-item>
            <v-list-item-title
              class="text-primary"
              style="cursor: pointer"
              @click="purgeAuth()"
              ><div class="primary--text cursor-pointer">
                Logout
              </div></v-list-item-title
            >
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    <router-view />
  </div>
</template>

<script>
import { LOGOUT } from "@/core/services/store/auth.module";

export default {
  data() {
    return {
      menuItems: [
        { title: "Profile", route: "/user" },
      ],
    };
  },
  methods: {
    logout() {
    this.$store.dispatch(LOGOUT);
    },
    purgeAuth() {
      this.logout()   
      localStorage.setItem("isAuthenticated", false);
      localStorage.setItem("JWT", null);
      this.$router.push("login");
    },
    chekAuth(x) {
      if (!x) {
        console.log("imhere");
        this.$router.push("login");
      }
    },
  },


};
</script>

<style></style>
