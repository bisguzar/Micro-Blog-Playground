import Vue from "vue";
import Vuex from "vuex";

import moduleAuth from "./auth.module";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      key: "vuex",
    }),
  ],
  modules: {
    auth: moduleAuth,
  },
  strict: process.env.DEV,
});
