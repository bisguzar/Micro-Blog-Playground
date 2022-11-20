import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "@/core/services/store";
// import { VERIFY_AUTH } from "@/core/services/store/auth.module";

import vuetify from "./plugins/vuetify";
import axios from "axios";
import VueAxios from "vue-axios";

Vue.config.productionTip = false;

Vue.use(VueAxios, axios);

// GOOD
router.beforeEach((to, from, next) => {
  if (
    to.meta.requiresAuth === true &&
    store.state.auth.isAuthenticated === false
  ) {
    router.push("login");
  } else {
    next();
  }
});

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
