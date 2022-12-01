<template>
  <v-container>
    <v-row class="align-center justify-center">
      <v-col sm="8" class="text-left">
        <h1>{{postDetail.title}}</h1>
        <p>
            {{postDetail.content}}
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "post-component",
  data() {
    return {
      postDetail: {},
      post_id: this.$route.params.postID,
    };
  },
  mounted() {
      this.getPost();
    },
    methods: {
        getPost() {
            this.axios.get("blog_posts/" + this.post_id).then((response) => {
                this.postDetail = response.data.data;
      });
    },
  },
};
</script>

<style></style>
