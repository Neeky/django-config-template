<template>
  <el-container>
    <el-header>Header</el-header>
    <el-container>
      <el-aside width="200px">Aside</el-aside>
      <el-container>
        <el-main>
          <el-row :gutter="20">
            <el-col :span="24">
              <div class="grid-content bg-purple">
                <h2>django-config-template</h2>

                <ul>
                  <li v-for="name in names">{{name}}</li>
                </ul>

                <button @click="loadNames">加载后台数据</button>
              </div>
            </el-col>
          </el-row>
        </el-main>
        <el-footer>Footer</el-footer>
      </el-container>
    </el-container>
  </el-container>
</template>

<style scoped>
.el-main li {
  list-style: none;
}

.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
  vertical-align: middle;
}

.el-aside {
  background-color: #d3dce6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 16px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>


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