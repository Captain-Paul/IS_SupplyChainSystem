import Vue from 'vue'
import VueRouter from 'vue-router'
import ShowOrder from '../pages/ShowOrder'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'ShowOrder',
    component: ShowOrder
  },
]

const router = new VueRouter({
  routes
})

export default router
