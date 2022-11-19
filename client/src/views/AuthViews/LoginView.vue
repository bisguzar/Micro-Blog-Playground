<template>
  <div class="login-view">
    <Login></Login>
  </div>
</template>
<script>
import Login from "@/components/AuthComponents/Login.vue";
export default {
    name: "login-view",
    components: {
    Login
  }
};
</script>