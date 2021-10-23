import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _3612ccbe = () => interopDefault(import('..\\pages\\contact-students.vue' /* webpackChunkName: "pages/contact-students" */))
const _3d3b7f4c = () => interopDefault(import('..\\pages\\contact-teachers.vue' /* webpackChunkName: "pages/contact-teachers" */))
const _3efd6233 = () => interopDefault(import('..\\pages\\direction.vue' /* webpackChunkName: "pages/direction" */))
const _c418bbca = () => interopDefault(import('..\\pages\\doctor.vue' /* webpackChunkName: "pages/doctor" */))
const _5fa1731d = () => interopDefault(import('..\\pages\\login.vue' /* webpackChunkName: "pages/login" */))
const _f4663c44 = () => interopDefault(import('..\\pages\\master.vue' /* webpackChunkName: "pages/master" */))
const _a7e86a62 = () => interopDefault(import('..\\pages\\news.vue' /* webpackChunkName: "pages/news" */))
const _27c54d63 = () => interopDefault(import('..\\pages\\papers.vue' /* webpackChunkName: "pages/papers" */))
const _023a1af6 = () => interopDefault(import('..\\pages\\projects.vue' /* webpackChunkName: "pages/projects" */))
const _50937416 = () => interopDefault(import('..\\pages\\teacher.vue' /* webpackChunkName: "pages/teacher" */))
const _bfa17cbe = () => interopDefault(import('..\\pages\\view.vue' /* webpackChunkName: "pages/view" */))
const _d40c5ff4 = () => interopDefault(import('..\\pages\\index.vue' /* webpackChunkName: "pages/index" */))

// TODO: remove in Nuxt 3
const emptyFn = () => {}
const originalPush = Router.prototype.push
Router.prototype.push = function push (location, onComplete = emptyFn, onAbort) {
  return originalPush.call(this, location, onComplete, onAbort)
}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: decodeURI('/'),
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/contact-students",
    component: _3612ccbe,
    name: "contact-students"
  }, {
    path: "/contact-teachers",
    component: _3d3b7f4c,
    name: "contact-teachers"
  }, {
    path: "/direction",
    component: _3efd6233,
    name: "direction"
  }, {
    path: "/doctor",
    component: _c418bbca,
    name: "doctor"
  }, {
    path: "/login",
    component: _5fa1731d,
    name: "login"
  }, {
    path: "/master",
    component: _f4663c44,
    name: "master"
  }, {
    path: "/news",
    component: _a7e86a62,
    name: "news"
  }, {
    path: "/papers",
    component: _27c54d63,
    name: "papers"
  }, {
    path: "/projects",
    component: _023a1af6,
    name: "projects"
  }, {
    path: "/teacher",
    component: _50937416,
    name: "teacher"
  }, {
    path: "/view",
    component: _bfa17cbe,
    name: "view"
  }, {
    path: "/",
    component: _d40c5ff4,
    name: "index"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
