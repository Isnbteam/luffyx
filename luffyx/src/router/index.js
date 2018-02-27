import Vue from 'vue'
import Router from 'vue-router'
import Course from '@/components/Course'
import CourseDetail from '@/components/CourseDetail'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/course',
      name: 'course',
      component: Course
    },
    {
      path: '/course-detail/:id/',
      name: 'courseDetail',
      component: CourseDetail
    },
  ],
  mode: 'history'
})
