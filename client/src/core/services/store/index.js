import Vue from "vue";
import Vuex from "vuex";

import auth from "./auth.module";
import createPersistedState from "vuex-persistedstate";

import SecureLS from "secure-ls";
const ls = new SecureLS({ isCompression: false });

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
  },
  plugins: [
    createPersistedState({
      paths: ["auth"],
      storage: {
        getItem: (key) => ls.get(key),
        setItem: (key, value) => ls.set(key, value),
        removeItem: (key) => ls.remove(key),
      },
    }),
  ],
});
