<template>
<<<<<<< HEAD
   <h1>课程表</h1>
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
}
=======
  <div>
    <h3>课程</h3>
    <h4>项目实战 你的同行都在学</h4>
    <span>更全面的实战案例、更细致的讲解和课后辅导，让你的职业生涯能更轻松的完成进阶</span>
    <ul>
      <li  class="aa" v-for="item in courseList">
        <router-link :to="{'path':'/course-detail/'+item.id }">
          <img src="\static\img\default.png">
          <div>{{item.name}}</div>
          <div>{{item.brief}}</div>
          <div>难度：{{item.level}}</div>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: 'course',
    data () {
      return {
        courseList: []
      }
    },
    mounted: function () {
      this.initCourses()
    },
    methods: {
      initCourses: function () {
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
>>>>>>> 110e704269c11c0c94cf7e4e9a070569795ddd59
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.aa{
  display: inline;
}
</style>
