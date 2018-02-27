<template>
  <div>
    <ul>
      <li v-for="item in courseList" >
        <router-link :to="{'path':'/course-detail/'+item.id }">{{item.name}}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      courseList: [
      ]
    }
  },
  mounted: function () {
    this.initCourses()
  },
  methods: {
    initCourses:function () {
      var that = this
      this.$axios.request({
        url: 'http://127.0.0.1:8000/courses/',
        method: 'GET'
      }).then(function (response) {
        that.courseList = response.data.courseList
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
