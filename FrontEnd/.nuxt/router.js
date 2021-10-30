import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

<<<<<<< HEAD
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
=======
const _4112f673 = () => interopDefault(import('../pages/contact-students.vue' /* webpackChunkName: "pages/contact-students" */))
const _3d7e9d2c = () => interopDefault(import('../pages/contact-teachers.vue' /* webpackChunkName: "pages/contact-teachers" */))
const _6abfeda1 = () => interopDefault(import('../pages/direction.vue' /* webpackChunkName: "pages/direction" */))
const _4fe47d6d = () => interopDefault(import('../pages/doctor.vue' /* webpackChunkName: "pages/doctor" */))
const _655ee58b = () => interopDefault(import('../pages/login.vue' /* webpackChunkName: "pages/login" */))
const _37bdbd30 = () => interopDefault(import('../pages/master.vue' /* webpackChunkName: "pages/master" */))
const _86815abe = () => interopDefault(import('../pages/news.vue' /* webpackChunkName: "pages/news" */))
const _4c93ae96 = () => interopDefault(import('../pages/papers.vue' /* webpackChunkName: "pages/papers" */))
const _093d2c70 = () => interopDefault(import('../pages/projects.vue' /* webpackChunkName: "pages/projects" */))
const _4683f9f8 = () => interopDefault(import('../pages/teacher.vue' /* webpackChunkName: "pages/teacher" */))
const _9e3a6d1a = () => interopDefault(import('../pages/view.vue' /* webpackChunkName: "pages/view" */))
const _c8917b18 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))
>>>>>>> dev

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
<<<<<<< HEAD
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
=======
    component: _4112f673,
    name: "contact-students"
  }, {
    path: "/contact-teachers",
    component: _3d7e9d2c,
    name: "contact-teachers"
  }, {
    path: "/direction",
    component: _6abfeda1,
    name: "direction"
  }, {
    path: "/doctor",
    component: _4fe47d6d,
    name: "doctor"
  }, {
    path: "/login",
    component: _655ee58b,
    name: "login"
  }, {
    path: "/master",
    component: _37bdbd30,
    name: "master"
  }, {
    path: "/news",
    component: _86815abe,
    name: "news"
  }, {
    path: "/papers",
    component: _4c93ae96,
    name: "papers"
  }, {
    path: "/projects",
    component: _093d2c70,
    name: "projects"
  }, {
    path: "/teacher",
    component: _4683f9f8,
    name: "teacher"
  }, {
    path: "/view",
    component: _9e3a6d1a,
    name: "view"
  }, {
    path: "/",
    component: _c8917b18,
>>>>>>> dev
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
