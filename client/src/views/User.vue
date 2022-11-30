<template>
  <div class="test">
    <v-row class="align-center justify-center">
      <v-col cols="8">
        <v-card class="mt-12">
          <v-data-table
            :headers="headers"
            :items="userList"
            :items-per-page="5"
            class="elevation-1"
          ></v-data-table>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  data: () => ({
    headers: [
      {
        text: "Name",
        align: "start",
        sortable: false,
        value: "name",
      },
      { text: "Surname", value: "surname" },
    ],
    userList: [],
  }),

  mounted() {
    this.getUserList();
  },
  methods: {
    getUserList() {
      let data = {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("id_token"),
        },
      };
      this.axios.get("http://127.0.0.1:8000/users", data).then((response) => {
        this.userList = response.data;
      });
    },
  },
};
</script>
