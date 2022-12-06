import Vue from "vue";
import Vuex from "vuex";

import moduleAuth from "./auth.module";
import createPersistedState from "vuex-persistedstate";

import SecureLS from "secure-ls";
const ls = new SecureLS({
  encodingType: "aes",
  isCompression: false,
});
Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      key: "vuex",
      storage: {
        getItem: (key) => ls.get(key),
        setItem: (key, value) => ls.set(key, value),
        removeItem: (key) => ls.remove(key),
      },
    }),
  ],
  modules: {
    auth: moduleAuth,
  },
  strict: process.env.DEV,
});