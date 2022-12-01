<template>
  <v-container>
    <v-row>
      <v-col>
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-row>
            <v-col sm="6" xs="12">
              <v-text-field
                v-model="postDetail.title"
                :rules="required"
                label="Title"
                required
              ></v-text-field>
            </v-col>
            <v-col sm="6" xs="12">
              <v-select
                v-model="postDetail.category"
                :items="categoryItems"
                item-text="category_name"
                item-value="category_id"
                :rules="[(v) => !!v || 'Item is required']"
                label="Item"
                required
              ></v-select>
            </v-col>
          </v-row>

          <v-textarea
            v-model="postDetail.content"
            :rules="required"
            label="Content"
            required
          ></v-textarea>
          <v-row class="text-right">
            <v-col>
              <v-btn
                :disabled="!valid"
                color="success"
                class="mr-4"
                @click="newBlogPost"
              >
                POST IT
              </v-btn>

              <v-btn color="error" class="mr-4" @click="reset"> clear </v-btn>
            </v-col>
          </v-row>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import { mapGetters } from "vuex";
import axios from "axios"
export default {
  name: "new-post",
  data: () => ({
    valid: true,
    required: [(v) => !!v || "This field is required"],
    categoryItems: [],
    postDetail: { title: "", content: "", category: null },
    id_token: "Bearer " + localStorage.getItem("id_token"),
  }),
  mounted() {
    this.getPostCategories();
  },
  methods: {
    newBlogPost() {
      const bodyFormData = {
        user_id: this.currentUser.uid,
        title: this.postDetail.title,
        content: this.postDetail.content,
        category_id: this.postDetail.category,
      };
      axios({
        method: "post",
        baseURL: "http://127.0.0.1:8000/blog_posts/add",
        data: JSON.stringify(bodyFormData),
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      }).then(() => { })
        .catch((err) => {
        console.log(err);
      })
    },
    getPostCategories() {
      let data = {
        headers: {
          Authorization: this.id_token,
        },
      };
      this.axios
        .get("http://127.0.0.1:8000/blog_posts/categories", data)
        .then((response) => {
          this.categoryItems = response.data;
        });
    },

    validate() {
      this.$refs.form.validate();
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
  },
  computed: {
    ...mapGetters(["currentUser"]),
  },
};
</script>
