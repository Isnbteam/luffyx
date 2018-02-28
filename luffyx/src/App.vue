<template>
  <div id="app">
    <img src="./assets/logo.png">

    <div class="hander">
      <router-link to="/index">首页</router-link>
      <router-link to="/Micro">路飞学位课</router-link>
      <router-link to="/course">课程</router-link>
      <router-link to="/news">深科技</router-link>
      <div class="login">
        <div v-if="this.$store.state.username">
          <a>{{ this.$store.state.username }}</a>
          <a @click="logout">注销</a>
        </div>
        <router-link v-else to="/login">登录</router-link>
      </div>

    </div>
    <router-view/>
    <h1>结束</h1>
  </div>
</template>

<script>
  export default {
    name: 'App',
    methods: {
      logout(){
        this.$store.state.username = ''
        this.$store.state.token = ''
      }
    }

  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;

  }

  body {
    margin: 0;
  }

  .hander {
    background: #fff;
    height: 80px;
    line-height: 80px;
    width: 100%;



  }

  .login {
    float: right;

  }
</style>





<!--<template>-->
  <!--<div id="app">-->
    <!--<img src="./assets/logo.png">-->
    <!--<router-view/>-->
  <!--</div>-->
<!--</template>-->

<!--<script>-->
<!--export default {-->
  <!--name: 'App'-->
<!--}-->
<!--</script>-->

<!--<style>-->
<!--#app {-->
  <!--font-family: 'Avenir', Helvetica, Arial, sans-serif;-->
      <!-- -webkit-font-smoothing: antialiased;-->
      <!-- -moz-osx-font-smoothing: grayscale;-->
  <!--text-align: center;-->
  <!--color: #2c3e50;-->
  <!--margin-top: 60px;-->
<!--}-->

  <!--body {-->
    <!--margin: 0;-->
  <!--}-->

  <!--.hander {-->
    <!--background: #fff;-->
    <!--height: 80px;-->
    <!--line-height: 80px;-->
    <!--width: 100%;-->



  <!--}-->

  <!--.login {-->
    <!--float: right;-->
  <!--}-->
<!--</style>-->
