<template>
  <v-container fluid class="profile-section">
    <v-card max-width="800px" class="mx-auto bg" elevation="2">
      <v-img
        class=""
        height="200px"
        src="https://images.unsplash.com/photo-1454117096348-e4abbeba002c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"
        gradient="150deg, rgb(185 224 255 / 58%) 0%, rgb(243 220 246 / 52%) 35%, rgb(223 255 242 / 74%) 74%"
      >
      </v-img>
      <v-row justify="center">
        <v-col
          align-self="start"
          class="d-flex justify-center align-center pa-0"
          cols="12"
        >
          <v-avatar
            class="profile avatar-center-heigth avatar-shadow"
            color="grey"
            size="164"
          >
            <v-btn  class="upload-btn" x-large icon>
              <v-icon> mdi-camera </v-icon>
            </v-btn>

            <v-img
              src="https://firebasestorage.googleapis.com/v0/b/ardabozlak-aa91c.appspot.com/o/pic%2Fi01_1651534925173.jpeg?alt=media&token=74141753-9687-44ce-b657-50e764a4610c"
            ></v-img>
          </v-avatar>
        </v-col>
      </v-row>
      <v-list-item color="#0000" class="profile-text-name ma-4 pt-16">
        <v-list-item-content>
          <v-list-item-title class="text-h6"> {{this.currentUser.username}} </v-list-item-title>
          <v-list-item-subtitle>Student</v-list-item-subtitle>
        </v-list-item-content>

      </v-list-item>


      <v-spacer></v-spacer>
      <v-text-field
        class="pa-6"
        v-model="this.currentUser.email"
        prepend-icon="mdi-gmail"
        label="Mail"
        disabled
      ></v-text-field>
      <v-spacer></v-spacer>

      <v-row>
        <v-col cols="6" class="text-end">
          <v-list-item-content class="sutitles">
            <v-list-item-title class="text-h6"> 2 </v-list-item-title>
            <v-list-item-subtitle class="text-caption"
              >Posts</v-list-item-subtitle
            >
          </v-list-item-content>
        </v-col>
        <v-col cols="6" class="text-start">
          <v-list-item-content class="sutitles">
            <v-list-item-title class="text-h6"> 10 </v-list-item-title>
            <v-list-item-subtitle class="text-caption"
              >Likes</v-list-item-subtitle
            >
          </v-list-item-content>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import { mapGetters, mapState } from "vuex";

export default {
  pageTitle: "My Profile",

  data() {
    return {

    };
  },

  computed: {
    ...mapState({
      errors: (state) => state.auth.errors,
    }),
    ...mapGetters(["currentUser"]),
  },
};
</script>
