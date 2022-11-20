<template>
  <div>
    <v-app-bar app color="primary" class="mb-12" dark>
      <div class="d-flex align-center">
        <v-toolbar-title>Micro-Blog</v-toolbar-title>
      </div>

      <v-spacer></v-spacer>
    </v-app-bar>
    <router-view />
  </div>
</template>

<script>

export default {
  name: "exterenal-layout",
  data() {
    return {};
  },
};
</script>

<style></style>
