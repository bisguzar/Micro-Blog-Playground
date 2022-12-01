import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "@/core/services/store";
import ApiService from "@/core/services/api.service";

import { VERIFY_AUTH } from "@/core/services/store/auth.module";

import vuetify from "./plugins/vuetify";
import axios from "axios";
import VueAxios from "vue-axios";

Vue.config.productionTip = false;

Vue.use(VueAxios, axios);

ApiService.init("http://127.0.0.1:8000/");
// GOOD
router.beforeEach((to, from, next) => {
  // Ensure we checked auth before each page load.
  if (to.name == "404") {
    next();
  } else {
    // Ensure we checked auth before each page load.
    Promise.all([store.dispatch(VERIFY_AUTH)]).then(next);
  }

  // reset config to initial state

  // Scroll page to top on every route change
  setTimeout(() => {
    window.scrollTo(0, 0);
  }, 100);
});

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
