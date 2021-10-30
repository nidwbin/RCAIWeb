import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _395e99d0 = () => interopDefault(import('..\\pages\\contact-students.vue' /* webpackChunkName: "pages/contact-students" */))
const _40874c5e = () => interopDefault(import('..\\pages\\contact-teachers.vue' /* webpackChunkName: "pages/contact-teachers" */))
const _5b42f09c = () => interopDefault(import('..\\pages\\direction.vue' /* webpackChunkName: "pages/direction" */))
const _447c575c = () => interopDefault(import('..\\pages\\doctor.vue' /* webpackChunkName: "pages/doctor" */))
const _fa8ec3f4 = () => interopDefault(import('..\\pages\\login.vue' /* webpackChunkName: "pages/login" */))
const _74c9d7d6 = () => interopDefault(import('..\\pages\\master.vue' /* webpackChunkName: "pages/master" */))
const _735f1ec6 = () => interopDefault(import('..\\pages\\news.vue' /* webpackChunkName: "pages/news" */))
const _67937f9a = () => interopDefault(import('..\\pages\\papers.vue' /* webpackChunkName: "pages/papers" */))
const _f176c926 = () => interopDefault(import('..\\pages\\projects.vue' /* webpackChunkName: "pages/projects" */))
const _0a8b88bf = () => interopDefault(import('..\\pages\\teacher.vue' /* webpackChunkName: "pages/teacher" */))
const _67829598 = () => interopDefault(import('..\\pages\\view.vue' /* webpackChunkName: "pages/view" */))
const _8dde0a22 = () => interopDefault(import('..\\pages\\index.vue' /* webpackChunkName: "pages/index" */))

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
    component: _395e99d0,
    name: "contact-students"
  }, {
    path: "/contact-teachers",
    component: _40874c5e,
    name: "contact-teachers"
  }, {
    path: "/direction",
    component: _5b42f09c,
    name: "direction"
  }, {
    path: "/doctor",
    component: _447c575c,
    name: "doctor"
  }, {
    path: "/login",
    component: _fa8ec3f4,
    name: "login"
  }, {
    path: "/master",
    component: _74c9d7d6,
    name: "master"
  }, {
    path: "/news",
    component: _735f1ec6,
    name: "news"
  }, {
    path: "/papers",
    component: _67937f9a,
    name: "papers"
  }, {
    path: "/projects",
    component: _f176c926,
    name: "projects"
  }, {
    path: "/teacher",
    component: _0a8b88bf,
    name: "teacher"
  }, {
    path: "/view",
    component: _67829598,
    name: "view"
  }, {
    path: "/",
    component: _8dde0a22,
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
