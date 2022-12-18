<template>
  <v-app>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>
<style lang="scss">
@import "@/assets/scss/main.scss";
</style>
<script>
export default {
  name: "App",

  data: () => ({}),
};
</script>
