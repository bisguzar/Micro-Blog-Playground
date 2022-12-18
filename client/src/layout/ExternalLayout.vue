<template>
  <div>
    <v-app-bar app color="primary" class="mb-12" dark>
      <div class="d-flex align-center">
        <v-img
          src="@/assets/logo-black.svg"
          max-height="80"
          max-width="150"
        ></v-img>
      </div>

      <v-spacer></v-spacer>
    </v-app-bar>
    <router-view />
    <FooterC></FooterC>
  </div>
</template>

<script>
import FooterC from "../layout/Footer.vue";
export default {
  name: "exterenal-layout",
  data() {
    return {};
  },
    components: {
    FooterC,
  },
};
</script>

<style></style>
