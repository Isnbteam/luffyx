// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
<<<<<<< HEAD

Vue.prototype.$axios = axios

=======
import store from './store/store'
Vue.prototype.$axios = axios
>>>>>>> 110e704269c11c0c94cf7e4e9a070569795ddd59
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})
