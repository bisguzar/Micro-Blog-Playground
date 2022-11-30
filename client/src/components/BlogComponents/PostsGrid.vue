!
<template>
  <div>
    <v-row class="mt-4 mx-2">
      <v-col sm="4" md="3" xs="8">
        <v-text-field
          label="Search..."
          id="search-post"
          v-model="keyword"
          append-icon="mdi-magnify"
        ></v-text-field>
      </v-col>
      <v-spacer></v-spacer>
      <v-col sm="1" md="3" xs="2" class="text-right mr-7"
        ><v-btn color="primary" @click="$router.push('New_Post')"
          >New Post</v-btn
        ></v-col
      >
    </v-row>

    <v-row class="mt-5">
      <v-col
        v-for="(item, index) in filteredList"
        :key="index"
        sm="4"
        md="3"
        xs="12"
      >
        <v-card class="mx-auto" max-width="420" max-height="340">
          <v-img
            src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
            height="200px"
          ></v-img>
          <v-card-title>
            {{ item.title }}
          </v-card-title>
          <v-card-subtitle
            class="d-inline-block text-truncate"
            style="max-width: 400px"
          >
            {{ item.content }}
          </v-card-subtitle>
          <v-card-actions>
            <v-btn color="orange lighten-2" text> Explore </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "post-grid-components",
  data() {
    return {
      token: localStorage.getItem("id_token"),
      postList: [],
      keyword: "",
    };
  },
  mounted() {
    this.posts();
  },
  methods: {
    posts() {
      this.axios
        .get("blog_posts")
        .then((response) => {
          this.postList = response.data;
        });
    },
  },
  computed: {
    filteredList() {
      return this.postList.filter((post) => {
        return this.keyword
          .toLowerCase()
          .split(" ")
          .every((v) => post.title.toLowerCase().includes(v));
      });
    },
  },
};
</script>
