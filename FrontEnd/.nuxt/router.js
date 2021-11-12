import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _126ad14e = () => interopDefault(import('..\\pages\\contact-students.vue' /* webpackChunkName: "pages/contact-students" */))
const _199383dc = () => interopDefault(import('..\\pages\\contact-teachers.vue' /* webpackChunkName: "pages/contact-teachers" */))
const _057ae37b = () => interopDefault(import('..\\pages\\direction.vue' /* webpackChunkName: "pages/direction" */))
const _1a5ee5d3 = () => interopDefault(import('..\\pages\\doctor.vue' /* webpackChunkName: "pages/doctor" */))
const _5b62d865 = () => interopDefault(import('..\\pages\\login.vue' /* webpackChunkName: "pages/login" */))
const _02382596 = () => interopDefault(import('..\\pages\\master.vue' /* webpackChunkName: "pages/master" */))
const _c936c6f2 = () => interopDefault(import('..\\pages\\news.vue' /* webpackChunkName: "pages/news" */))
const _b79eddca = () => interopDefault(import('..\\pages\\papers.vue' /* webpackChunkName: "pages/papers" */))
const _10e350ae = () => interopDefault(import('..\\pages\\projects.vue' /* webpackChunkName: "pages/projects" */))
const _6190a75e = () => interopDefault(import('..\\pages\\teacher.vue' /* webpackChunkName: "pages/teacher" */))
const _e0efd94e = () => interopDefault(import('..\\pages\\view.vue' /* webpackChunkName: "pages/view" */))
const _dc899564 = () => interopDefault(import('..\\pages\\index.vue' /* webpackChunkName: "pages/index" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/contact-students",
    component: _126ad14e,
    name: "contact-students"
  }, {
    path: "/contact-teachers",
    component: _199383dc,
    name: "contact-teachers"
  }, {
    path: "/direction",
    component: _057ae37b,
    name: "direction"
  }, {
    path: "/doctor",
    component: _1a5ee5d3,
    name: "doctor"
  }, {
    path: "/login",
    component: _5b62d865,
    name: "login"
  }, {
    path: "/master",
    component: _02382596,
    name: "master"
  }, {
    path: "/news",
    component: _c936c6f2,
    name: "news"
  }, {
    path: "/papers",
    component: _b79eddca,
    name: "papers"
  }, {
    path: "/projects",
    component: _10e350ae,
    name: "projects"
  }, {
    path: "/teacher",
    component: _6190a75e,
    name: "teacher"
  }, {
    path: "/view",
    component: _e0efd94e,
    name: "view"
  }, {
    path: "/",
    component: _dc899564,
    name: "index"
  }],

  fallback: false
}

export function createRouter (ssrContext, config) {
  const base = (config._app && config._app.basePath) || routerOptions.base
  const router = new Router({ ...routerOptions, base  })

  // TODO: remove in Nuxt 3
  const originalPush = router.push
  router.push = function push (location, onComplete = emptyFn, onAbort) {
    return originalPush.call(this, location, onComplete, onAbort)
  }

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    return resolve(to, current, append)
  }

  return router
}
