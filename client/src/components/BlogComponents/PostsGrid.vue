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
          <v-img :src="item.img_base64" height="200px"></v-img>
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
            <v-btn
              color="orange lighten-2"
              text
              @click="toPostDetail(item._id.$oid)"
            >
              Explore
            </v-btn>
            <v-spacer></v-spacer>
            <v-chip outlined class="mx-2" @click="votePost(1, item._id.$oid)">
              <v-avatar left>
                <v-icon icon color="success" small>mdi-thumb-up</v-icon>
              </v-avatar>
              {{ item.like }}
            </v-chip>
            <v-chip outlined class="mx-2" @click="votePost(2, item._id.$oid)">
              <v-avatar left>
                <v-icon color="error" small>mdi-thumb-down</v-icon>
              </v-avatar>
              {{ item.dislike }}
            </v-chip>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

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
    votePost(_vote_value, _post_id) {
      const bodyFormData = {
        vote_value: _vote_value,
        post_id: _post_id,
        author_id: this.currentUser.uid.$oid,
      };
      this.axios({
        method: "post",
        url: "rate",
        data: JSON.stringify(bodyFormData),
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      }).then((response) => {
        if (response.data == "Success") {
          let elementPost = this.postList.findIndex(
            (obj) => obj._id.$oid == _post_id
          );
          if (_vote_value == 1) {
            this.postList[elementPost].like += 1;
            this.postList[elementPost].dislike -= 1;
          }
          else if (_vote_value == 2) {
            this.postList[elementPost].dislike += 1;
            this.postList[elementPost].like -= 1;
            
          }
        }
      });
    },
    toPostDetail(_post_id) {
      this.$router.push({
        name: "Post",
        params: { postID: _post_id },
      });
    },
    posts() {
      this.axios.get("blog_posts").then((response) => {
        this.postList = response.data;
      });
    },
    deletePost(_id) {
      const bodyFormData = {
        id: _id,
      };
      this.axios({
        method: "delete",
        url: "blog_posts/" + _id,
        data: JSON.stringify(bodyFormData),
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      }).then(() => {
        this.posts();
      });
    },
  },
  computed: {
    ...mapGetters(["currentUser"]),
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
