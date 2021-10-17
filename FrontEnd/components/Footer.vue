<!--
 * @FileDescription: nav
 * @Author: liuyoude, wenbin
 * @Date: 2021-09-10
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-27
 -->
<template>
    <div>
      <footer class="footer-area">
        <div class="container">
          <div class="footer-main">
            <div class="row">
              <div class="col-lg-3 col-md-6">
                <div class="footer-widget mt-30">
                  <div class="footer-title pb-30">
                    <h4 class="title">{{ mse_address }}</h4>
                  </div>
                  <div class="footer-about-content">
                    <p>{{ address }}</p>
                    <div class="email">
                      <a :href="'mailto:'+email">{{ email }}</a>
                    </div>
                    <div class="call">
                      <a :href="'tel:'+phone">{{ phone }}</a>
                    </div>
                    <div class="social">
                      <ul>
                        <li><a href="#"><i class="fa fa-facebook-f"></i></a></li>
                        <li><a href="#"><i class="fa fa-twitter"></i></a></li>
                        <li><a href="#"><i class="fa fa-instagram"></i></a></li>
                        <li><a href="#"><i class="fa fa-pinterest-p"></i></a></li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-6 col-sm-6">
                <div class="footer-widget mt-30 ml-30">
                  <div class="footer-title pb-20">
                    <h4 class="title">{{ mse_research }}</h4>
                  </div>
                  <div class="footer-about-list d-flex">
                    <ul class="mr-70">
                      <li><nuxt-link :to="url_direction"><i class="fa fa-angle-right"></i> {{ mse_direction }}</nuxt-link></li>
                      <li><nuxt-link :to="url_single_post"><i class="fa fa-angle-right"></i> {{ mse_single_post }}</nuxt-link></li>
                      <li><nuxt-link :to="url_all_projects"><i class="fa fa-angle-right"></i> {{ mse_all_projects }}</nuxt-link></li>
                      <li><nuxt-link :to="url_single_project"><i class="fa fa-angle-right"></i> {{ mse_single_project }}</nuxt-link></li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-6 col-sm-6">
                <div class="footer-widget mt-30 ml-30">
                  <div class="footer-title pb-20">
                    <h4 class="title">{{ mse_team }}</h4>
                  </div>
                  <div class="footer-about-list d-flex">
                    <ul class="mr-70">
                      <li><nuxt-link :to="url_teacher"><i class="fa fa-angle-right"></i> {{ mse_teacher }}</nuxt-link></li>
                      <li><nuxt-link :to="url_doctor"><i class="fa fa-angle-right"></i>{{ mse_doctor }}</nuxt-link></li>
                      <li><nuxt-link :to="url_master"><i class="fa fa-angle-right"></i>{{ mse_master }}</nuxt-link></li>
                    </ul>
                  </div>
                </div>
                <div class="footer-widget mt-30 ml-30">
                  <div class="footer-title pb-20">
                    <h4 class="title">{{ mse_contact}}</h4>
                  </div>
                  <div class="footer-about-list d-flex">
                    <ul class="mr-70">
                      <li><nuxt-link :to="url_contact_students"><i class="fa fa-angle-right"></i> {{ mse_contact_students }}</nuxt-link></li>
                      <li><nuxt-link :to="url_contact_teacher"><i class="fa fa-angle-right"></i> {{ mse_contact_teacher }}</nuxt-link></li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-6 col-sm-7">
                <div class="footer-widget footer-news mt-30">
                  <div class="footer-title pb-40">
                    <nuxt-link :to="url_news"><h4 class="title"> {{ mse_news }}</h4></nuxt-link>
                  </div>
                  <div class="footer-news-content">
                    <div class="news-item d-flex align-items-center">
                      <div class="news-item-thumb">
                        <img src="/static/images_/footer-news-1.jpg" alt="">
                      </div>
                      <div class="news-item-content">
                        <span>06 April, 2020</span>
                        <a href="#">We are designing industry materials of innovation</a>
                      </div>
                    </div>
                    <div class="news-item d-flex align-items-center mt-20">
                      <div class="news-item-thumb">
                        <img src="/static/images_/footer-news-2.jpg" alt="">
                      </div>
                      <div class="news-item-content">
                        <span>06 April, 2020</span>
                        <a href="#">We are designing industry materials of innovation</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="footer-copyright text-center">
            <p>© Copyright 2020</p>
          </div>
        </div>
        <div class="footer-shape-1">
          <img src="/static/images/shape/shape-5.png" alt="">
        </div>
        <div class="footer-shape-2 animated wow fadeInLeft" data-wow-duration="1500ms" data-wow-delay="0ms">
          <img src="/static/images/shape/shape-6.png" alt="">
        </div>
      </footer>

      <div class="go-top-area">
        <div class="go-top-wrap">
          <div class="go-top-btn-wrap">
            <div @click="scrollTop" :class="`go-top go-top-btn ${scrollBtn ? 'active' : ''}`">
              <i class="fa fa-angle-double-up"></i>
              <i class="fa fa-angle-double-up"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
      name: "Footer",
      data(){
        return {
              url_home:"/",
              url_news:"/news",
              url_teacher:"/team/teacher",
              url_doctor:"/team/doctor",
              url_master:"/team/master",
              url_direction:"/direction",
              url_all_projects:"/projects",
              url_single_project:"/single-projects",
              url_single_post:"/single-post",
              url_contact_students:"/contact-students",
              url_contact_teacher:"/contact-teacher",

              mse_news:"最近新闻",

              mse_research:"科研",
              mse_direction:"研究方向",
              mse_single_post:"学术成果",
              mse_all_projects:"项目总览",
              mse_single_project:"项目演示",

              mse_team:"研究团队",
              mse_teacher:"中心教师",
              mse_doctor:"中心博士",
              mse_master:"中心研究生",

              mse_address:"联系我们",

              mse_contact:"加入我们",
              mse_contact_students:"结伴同行",
              mse_contact_teacher:"求贤若渴",

              email:"splab@hit.edu.cn",
              phone:"0451-86417981",
              address:"黑龙江省哈尔滨市哈尔滨工业大学综合楼6层",

              mobileToggle: false,
              scrollBtn: false,
        }
      },
      mounted() {
        window.addEventListener('scroll', this.handleScroll);
      },

      methods: {

        handleScroll () {

          if (window.scrollY > 70) {
            this.scrollBtn = true
          }
          else if (window.scrollY < 70) {
            this.scrollBtn = false
          }
        },

        scrollTop () {
          window.scrollTo(0, 0);
        }


      }
    }
</script>

<style scoped>

</style>
