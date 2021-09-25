<!--
 * @FileDescription: admin's nav
 * @Author: wenbin
 * @Date: 2021-09-13
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-13
 -->
<template>
  <header class="header-area">
    <div id="Nav" class="main-header">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="main-header-item d-flex justify-content-between align-items-center">
              <div class="main-header-menus  d-flex">
                <div class="header-btn">
                  <a @click="mobileToggle = !mobileToggle" href="#">{{ mse_header }}</a>
                </div>
                <div class="toggle-btn canvas_open">
                </div>
                <div class="header-menu d-none d-lg-block">
                  <ul>

                    <li><nuxt-link :to="url_home">{{ mse_home }}</nuxt-link></li>

                    <li><nuxt-link :to="url_news">{{ mse_news }}</nuxt-link></li>

                    <li>
                      <a href="#">{{ mse_team }}</a>
                      <ul class="sub-menu">
                        <li><nuxt-link :to="url_teacher">{{ mse_teacher }}</nuxt-link></li>
                        <li><nuxt-link :to="url_doctor">{{ mse_doctor }}</nuxt-link></li>
                        <li><nuxt-link :to="url_master">{{ mse_master }}</nuxt-link></li>
                      </ul>
                    </li>

                    <li><nuxt-link :to="url_direction">{{ mse_direction }}</nuxt-link></li>

                    <li>
                      <a href="#">{{ mse_projects }}</a>
                      <ul class="sub-menu">
                        <li><nuxt-link :to="url_all_projects">{{ mse_all_projects }}</nuxt-link></li>
                        <li><nuxt-link :to="url_single_project">{{ mse_single_project }}</nuxt-link></li>
                      </ul>
                    </li>

                    <li><nuxt-link :to="url_single_post">{{ mse_single_post }}</nuxt-link></li>

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


                  <li class="menu-item-has-children active"><span class="menu-expand"><i class="fa fa-angle-down"></i></span>
                    <a href="#">{{ mse_team }}</a>
                      <ul class="sub-menu">
                        <li><nuxt-link :to="url_teacher">{{ mse_teacher }}</nuxt-link></li>
                        <li><nuxt-link :to="url_doctor">{{ mse_doctor }}</nuxt-link></li>
                        <li><nuxt-link :to="url_master">{{ mse_master }}</nuxt-link></li>
                      </ul>
                  </li>

                  <li class="menu-item-has-children active"><nuxt-link :to="url_direction">{{ mse_direction }}</nuxt-link></li>

                  <li class="menu-item-has-children active"><span class="menu-expand"><i class="fa fa-angle-down"></i></span>
                    <a href="#">{{ mse_projects }}</a>
                      <ul class="sub-menu">
                        <li><nuxt-link :to="url_all_projects">{{ mse_all_projects }}</nuxt-link></li>
                        <li><nuxt-link :to="url_single_project">{{ mse_single_project }}</nuxt-link></li>
                      </ul>
                  </li>

                  <li class="menu-item-has-children active"><nuxt-link :to="url_single_post">{{ mse_single_post }}</nuxt-link></li>

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
                <span><a :href="'mailto:' + email"><i class="fa fa-envelope-o"></i> {{ email }} </a></span>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
    let AdminNavVars= {
          url_home:"/admin",
          url_news:"/admin/news",
          url_teacher:"/admin/team/teacher",
          url_doctor:"/admin/team/doctor",
          url_master:"/admin/team/master",
          url_direction:"/admin/direction",
          url_all_projects:"/admin/projects",
          url_single_project:"/admin/single-projects",
          url_single_post:"/admin/single-post",
          url_contact_students:"/admin/contact-students",
          url_contact_teacher:"/admin/contact-teacher",

          mse_header:"管理",
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
          mse_single_post:"学术成果",
          mse_contact:"加入我们",
          mse_contact_students:"结伴同行",
          mse_contact_teacher:"求贤若渴",

          email:"splab@hit.edu.cn",

          mobileToggle: false
    };

    export default {
      name: "AdminNav",
      data(){
        return AdminNavVars;
      },
    }
</script>

<style scoped>

</style>
