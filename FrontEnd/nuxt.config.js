
export default {
  mode: 'universal',
  /*
  ** Headers of the page
  */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'shortcut icon', sizes:'180x180', type: 'image/png', href: '/assets/images/logo/facvicon.png' },
      { rel: "stylesheet", href: "https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&display=swap" },
      { rel: "stylesheet", href: "/css/bootstrap.min.css" },
      { rel: "stylesheet", href: "/css/animate.min.css" },
      { rel: "stylesheet", href: "/css/font-awesome.min.css" },
      { rel: "stylesheet", href: "/plugins/glightbox/glightbox.min.css" },
      { rel: "stylesheet", href: "/css/flaticon.css" },
      { rel: "stylesheet", href: "/css/default.css" },
      { rel: "stylesheet", href: "/css/style.css" }
    ],

    script: [
      { src: "/plugins/glightbox/glightbox.min.js", body: true },
      { src: "/plugins/accordion/accordion.min.js", body: true }
    ]
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#ff5316', height: '4px' },
  /*
  ** Global CSS
  */
  css: [
  ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    {src: '@/plugins/owl.js', ssr: false},
    {src: '@/plugins/vue-mavon-editor.js', ssr: false },
    {src: '@/plugins/interceptor.js'},
  ],
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    'cookie-universal-nuxt',
    '@nuxtjs/axios',
    '@nuxtjs/toast',
  ],
  /*
  ** Build configuration
  */
  toast: {// toast模块的配置
    position: 'top-right',
    duration: 3000,
  },

  build: {
    /*
    ** You can extend webpack config here
    */
    extend (config, ctx) {
    }
  }
}
