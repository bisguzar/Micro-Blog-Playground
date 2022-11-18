<template>
  <v-app>
    <v-app-bar app color="primary" class="mb-12" dark>
      <div class="d-flex align-center">

        <v-toolbar-title>Micro-Blog</v-toolbar-title>
      </div>

      <v-spacer></v-spacer>

      <router-link to="/"><div class="white--text mx-2 ">Home</div></router-link>
      |
      <router-link to="/test"><div class="white--text mx-2">
                      User
                    </div></router-link>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>
