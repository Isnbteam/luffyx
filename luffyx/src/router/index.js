import Vue from 'vue'
import Router from 'vue-router'

import Course from '@/components/Course'
import Index from '@/components/Index'
import Micro from '@/components/Micro'
import News from '@/components/News'
import NewsDetail from '@/components/NewsDetail'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/course',
      name: 'Course',
      component: Course,
    },
    {
      path: '/index',
      name: 'Index',
      component: Index
    },
    {
      path: '/micro',
      name: 'micro',
      component: Micro
    },
    {
      path: '/news',
      name: 'news',
      component: News
    },
    {
      path: '/newsDetail/:id/',
      name: 'newsDetail',
      component: NewsDetail
    },
  ],
  mode:'history'
})
