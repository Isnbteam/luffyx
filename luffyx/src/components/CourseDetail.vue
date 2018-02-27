<template>
  <div>
    <div>专题课程</div>
    <h1>{{name}}</h1>
    <span>{{course_slogan}}</span>
    <div>
      <ul>
        <li><span v-on:click="qh(1)">课程概述</span></li>
        <li><span v-on:click="qh(2)">课程章节</span></li>
        <li><span v-on:click="qh(3)">用户评价</span></li>
        <li><span v-on:click="qh(4)">常见问题</span></li>
      </ul>
      <div v-show="a[0]">
        <h2>课程概述</h2>
        <p>{{video_brief_link}}</p>
        <span class="gs">学习时间：{{hours}}</span>
        <span class="gs">难度：{{level}}</span>
        <span class="gs">学习人数：0人</span>
        <div>
          <ul id="price">
            <li>399</li>
            <li>499</li>
            <li>599</li>
            <li>799</li>
          </ul>
          <btn>开课时通知我</btn>
        </div>
        <h2>为什么学这门课程</h2>
        <p>{{why_study}}</p>
        <h2>我将学到哪些内容？</h2>
        <p>{{what_to_study_brief}}</p>
        <h2>此项目如何有助于我的职业生涯？</h2>
        <p>{{career_improvement}}</p>
        <h2>课程先修要求</h2>
        <p>{{prerequisite}}</p>
        <h2>讲师简介</h2>
        <div v-for="item in teachers">
          <h3>{{item.name}}、{{item.title}}</h3>
          <img src="\static\img\peiqi@3x_1517450115.4163337.png">
          <span>{{item.signature}}</span>
          <span>{{item.brief}}</span>

        </div>
      </div>
      <div v-show="a[1]">课程章节</div>
      <div v-show="a[2]">用户评价</div>
      <div v-show="a[3]">常见问题</div>
    </div>
  </div>

</template>

<script>
  export default {
    data () {
      return {
        name: '',
        hours: '',
        level: '',
        course_slogan: '',
        video_brief_link: '',
        why_study: '',
        what_to_study_brief: '',
        career_improvement: '',
        prerequisite: '',
        teachers: [],
        a: [1, 0, 0, 0]
      }
    },
    mounted: function () {
      this.initCourseDetail()
    },
    methods: {
      qh: function (t) {
        if (t == 2) {
          this.a = [0, 1, 0, 0]
        } else if (t == 3) {
          this.a = [0, 0, 1, 0]


        } else if (t == 4) {
          this.a = [0, 0, 0, 1]

        } else if (t == 1) {
          this.a = [1, 0, 0, 0]
        }
      },
      initCourseDetail (){
        var nid = this.$route.params.id
        var that = this
        var url = 'http://127.0.0.1:8000/courses/' + nid + '.json'
        this.$axios.request({
          url: url,
          method: 'GET',
          responseType: 'json'
        }).then(function (response) {
          console.log(response)
          that.name = response.data.name
          that.hours = response.data.courses.hours
          that.course_slogan = response.data.courses.course_slogan
          that.why_study = response.data.courses.why_study
          that.what_to_study_brief = response.data.courses.what_to_study_brief
          that.career_improvement = response.data.courses.career_improvement
          that.prerequisite = response.data.courses.prerequisite
          that.video_brief_link = response.data.courses.video_brief_link
          that.teachers = response.data.courses.teachers
          that.level = response.data.level
        })
      }
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  ul li {
    list-style: none;
    display: inline-block;
    border: 1px solid #b7b4ed;
    height: 40px;
    line-height: 40px;
    width: 120px;
    margin-left: 40px;

    text-align: center;
  }

  #price li {
    list-style: none;
    display: inline-block;
    border: 1px solid #b7b4ed;
    height: 80px;
    line-height: 80px;
    width: 150px;
    margin-left: 30px;
    text-align: center;
  }

  .gs {
    margin-left: 15px;
  }
</style>
