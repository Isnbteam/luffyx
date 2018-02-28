<template>
  <div class="hello">
    <h1>登录页面</h1>
    <div>
      <input type="text" v-model="username" placeholder="用户名">
      <input type="text" v-model="password" placeholder="密码">
      <a @click="doLogin">提交</a>
    </div>
  </div>
</template>

<script>

export default {

  name: 'login',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    doLogin () {
      var that = this
      this.$axios.request({
        url: 'http://127.0.0.1:8000/login/',
        method: 'POST',
        data: {
          username: this.username,
          password: this.password
        },
        responseType: 'json'
      }).then(function (response) {
        console.log(response.data)
        // 找到全局变量，把用户名和token赋值到其中。
        that.$store.commit('saveToken', response.data);
        // 重定向到index
        that.$router.push('/index')
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
