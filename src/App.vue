<template>
  <div>
    <ul>
      <li v-for="name in names">{{name}}</li>
    </ul>
    <button @click="loadNames">加载数据</button>
  </div>
</template>

<script>
const axios = require("axios");

module.exports = {
  data: function() {
    return {
      names: ["hello", "world"]
    };
  },
  methods: {
    loadNames() {
      _this = this;
      axios
        .get("/exsample/apis/persons")
        .then(function(response) {
          let persons = response.data.data;
          _this.names = persons;

          console.log(persons);
        })
        .catch(function(error) {
          console.log(error);
        })
        .then(function() {});
    }
  }
};
</script>