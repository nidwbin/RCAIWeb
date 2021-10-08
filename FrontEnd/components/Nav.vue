<!--
 * @FileDescription: nav
 * @Author: liuyoude, wenbin
 * @Date: 2021-09-10
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-02
 -->
<template>
  <header class="header-area">
    <div class="header-top">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="header-top-items d-flex justify-content-between align-items-center">
              <div class="logo">
                <a href="/"><img src="/assets/images/logo/logo.png" alt="" height="100px"></a>
              </div>
              <div class="header-top-info d-none d-md-block">
                <ul>
                  <li>
                    <i class="flaticon-email"></i>
                    <span>邮箱</span>
                    <a :href="'mailto:'+email">{{ email }}</a>
                  </li>
                  <li>
                    <i class="flaticon-calling"></i>
                    <span>电话</span>
                    <a href="'tel:'+phone">{{phone}}</a>
                  </li>
                  <li>
                    <i class="flaticon-address"></i>
                    <span>地址</span>
                    <a href="#">{{adress}}</a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div id="Nav" class="main-header">
       <div class="header-btn" @click="logout" v-if="admin">
           <a href="#">{{ mse_header }}</a>
       </div>
      <div class="container">

        <div class="row">

          <div class="col-lg-12">

            <div class="main-header-item">
            <div class="main-header-menus d-flex justify-content-between align-items-center">
                <div class="toggle-btn ml-30 canvas_open">
                  <i @click="mobileToggle = !mobileToggle" class="fa fa-bars"></i>
                </div>
                <div class="header-menu d-none d-lg-block">
                  <ul>
                    <li><nuxt-link :to="url_home">{{ mse_home }}</nuxt-link></li>

                    <li><nuxt-link :to="url_news">{{ mse_news }}</nuxt-link></li>

                    <li><nuxt-link :to="url_direction">{{ mse_direction }}</nuxt-link></li>

                    <li><nuxt-link :to="url_papers">{{ mse_papers }}</nuxt-link></li>

                    <li>
                      <a href="#">{{ mse_team }}</a>
                      <ul class="sub-menu">
                        <li><nuxt-link :to="url_teacher">{{ mse_teacher }}</nuxt-link></li>
                        <li><nuxt-link :to="url_doctor">{{ mse_doctor }}</nuxt-link></li>
                        <li><nuxt-link :to="url_master">{{ mse_master }}</nuxt-link></li>
                      </ul>
                    </li>

                    <li>
                      <a href="#">{{ mse_projects }}</a>
                      <ul class="sub-menu">
                        <li><nuxt-link :to="url_all_projects">{{ mse_all_projects }}</nuxt-link></li>
                        <li><nuxt-link :to="url_single_project">{{ mse_single_project }}</nuxt-link></li>
                      </ul>
                    </li>

                    <li>
                      <a href="#">{{ mse_contact }}</a>
                      <ul class="sub-menu">
                        <li><nuxt-link :to="url_contact_students">{{ mse_contact_students }}</nuxt-link></li>
                        <li><nuxt-link :to="url_contact_teacher">{{ mse_contact_teacher }}</nuxt-link></li>
                      </ul>
                    </li>
                  </ul>
                </div>
              </div>
            </div>

           <div :class="`offcanvas_menu_wrapper ${mobileToggle ? 'active' : ''}`">
              <div class="canvas_close">
                <a @click="mobileToggle = !mobileToggle" href="javascript:void(0)"><i class="fa fa-times"></i></a>
              </div>
              <div class="header-social">
                <ul class="text-center">
                  <li><a href="#"><i class="fa fa-facebook-f"></i></a></li>
                  <li><a href="#"><i class="fa fa-twitter"></i></a></li>
                  <li><a href="#"><i class="fa fa-skype"></i></a></li>
                  <li><a href="#"><i class="fa fa-pinterest-p"></i></a></li>
                </ul>
              </div>
              <div id="menu" class="text-left ">
                <ul class="offcanvas_main_menu">

                  <li class="menu-item-has-children active"><nuxt-link :to="url_home">{{ mse_home }}</nuxt-link></li>

                  <li class="menu-item-has-children active"><nuxt-link :to="url_news">{{ mse_news }}</nuxt-link></li>

                  <li class="menu-item-has-children active"><nuxt-link :to="url_direction">{{ mse_direction }}</nuxt-link></li>

                  <li class="menu-item-has-children active"><nuxt-link :to="url_papers">{{ mse_papers }}</nuxt-link></li>

                  <li class="menu-item-has-children active"><span class="menu-expand"><i class="fa fa-angle-down"></i></span>
                    <a href="#">{{ mse_team }}</a>
                      <ul class="sub-menu">
                        <li><nuxt-link :to="url_teacher">{{ mse_teacher }}</nuxt-link></li>
                        <li><nuxt-link :to="url_doctor">{{ mse_doctor }}</nuxt-link></li>
                        <li><nuxt-link :to="url_master">{{ mse_master }}</nuxt-link></li>
                      </ul>
                  </li>

                  <li class="menu-item-has-children active"><span class="menu-expand"><i class="fa fa-angle-down"></i></span>
                    <a href="#">{{ mse_projects }}</a>
                      <ul class="sub-menu">
                        <li><nuxt-link :to="url_all_projects">{{ mse_all_projects }}</nuxt-link></li>
                        <li><nuxt-link :to="url_single_project">{{ mse_single_project }}</nuxt-link></li>
                      </ul>
                  </li>

                  <li class="menu-item-has-children active"><span class="menu-expand"><i class="fa fa-angle-down"></i></span>
                    <a href="#">{{ mse_contact }}</a>
                      <ul class="sub-menu">
                        <li><nuxt-link :to="url_contact_students">{{ mse_contact_students }}</nuxt-link></li>
                        <li><nuxt-link :to="url_contact_teacher">{{ mse_contact_teacher }}</nuxt-link></li>
                      </ul>
                  </li>
                </ul>
              </div>
              <div class="offcanvas_footer">
                <span><a :href="'mailto:'+email"><i class="fa fa-envelope-o"></i> {{ email }}</a></span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
    let NavVars= {
          url_home:"/",
          url_news:"/news",
          url_teacher:"/teacher",
          url_doctor:"/doctor",
          url_master:"/master",
          url_direction:"/direction",
          url_all_projects:"/projects",
          url_single_project:"/single-projects",
          url_papers:"/papers",
          url_contact_students:"/contact-students",
          url_contact_teacher:"/contact-teacher",

          mse_header:"登出",
          mse_home:"首页",
          mse_news:"新闻",
          mse_team:"研究团队",
          mse_teacher:"中心教师",
          mse_doctor:"中心博士",
          mse_master:"中心研究生",
          mse_direction:"研究方向",
          mse_projects:"科研项目",
          mse_all_projects:"项目总览",
          mse_single_project:"项目演示",
          mse_papers:"学术成果",
          mse_contact:"加入我们",
          mse_contact_students:"结伴同行",
          mse_contact_teacher:"求贤若渴",

          email:"splab@hit.edu.cn",
          phone:"0451-86417981",
          adress:"黑龙江省哈尔滨市哈尔滨工业大学综合楼6层",

          mobileToggle: false
    };

    export default {
      name: "Nav",
      data(){
        return NavVars;
      },
        computed:{
          admin(){
              return this.$store.state.admin;
          }
        },

      methods: {
          // set_btn_display() {
          //     if (this.$cookies.isKey("isInLogin")){
          //       if(this.$cookies.get("isInLogin") == true){
          //           this.$("header-btn").css("display", "block");
          //       }
          //     }
          // },
          logout(){
              if(this.$cookies.get('ajax-ready')){
                  this.$axios.delete('/login/');
              }
          }
      }
    }


</script>

<style scoped>

</style>
