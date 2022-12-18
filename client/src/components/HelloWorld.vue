<template>
  <v-container class="home">
    <v-row class="text-center">
      <v-col md="4" lg="6"  class="mb-4">
        <h1 class="display-2 text-left font-weight-bold my-6">
          Publish, grow, and learn, <br />all in one place.
        </h1>
        <h2 class="text-left home__typer-container">
          <vue-typer
            :type-delay="50"
            text="If you have a story to tell, knowledge to share, or a perspective to offer —
welcome home. Sign up for free so your writing can thrive in a network
supported by millions of readers"
          ></vue-typer>
        </h2>
      </v-col>
      <v-col  md="4" lg="6"  class="mb-4 home__image-container">
        <v-img max-width="650" class="home__image" src="../assets/homepage_m.png" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { VueTyper } from "vue-typer";

export default {
  name: "HelloWorld",
  components: {
    // ES6; property shorthand + Vue should automatically dasherize the key for us
    VueTyper,
  },
  data: () => ({}),
};
</script>
