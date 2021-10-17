<!--
 * @FileDescription: hot news page
 * @Author: liuyoude
 * @Date: 2021-09-28
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-09-29
 -->
<template>
  <section class="client-area client-2-area client-about">
    <div class="client-full">
      <div class="container-fluid">
        <div class="row">
          <div class="col-lg-7">
            <div class="client-title">
              <h6 class="title">近期新闻</h6>
            </div>
          </div>
        </div>
        <div class="row client-active">
          <swiper :options="swiperOptions">
            <swiper-slide v-for="item in items" :key="item.file">
              <div class="client-item mt-30">
                <div class="shape">
                  <img src="/static/images/shape/shape-4.png" alt="shape">
                </div>
                <div class="user">
                  <div class="user-thumb">
                    <img :src="item.image" alt="new">
                    <i class="fa fa-quote-left"></i>
                  </div>
                  <h5 class="title">
                    <nuxt-link :to="{name:'view', query:{type:type, filename:item.filename}}">
                      {{ item.title }}
                    </nuxt-link>
                  </h5>
                  <span>{{ item.date }}</span>
                </div>
                <div class="text">
                  <p>{{ item.overview }}</p>
                </div>
              </div>
            </swiper-slide>
          </swiper>
        </div>
      </div>
    </div>
<!--    <div class="client-shape animated wow fadeInLeft" data-wow-duration="1500ms" data-wow-delay="0ms">-->
<!--      <img src="/static/images/shape/shape-7.png" alt="">-->
<!--    </div>-->
  </section>
</template>

<script>
import {Swiper, SwiperSlide, directive} from 'vue-awesome-swiper';
import 'swiper/css/swiper.css';

export default {
  name: "HotNewsPage",
  components: {
    Swiper,
    SwiperSlide
  },
  directives: {
    swiper: directive
  },
  data() {
    return {
      swiperOptions: {
        slidesPerView: 2,
        loop: true,
        speed: 1000,
        spaceBetween: 30,
        autoplay: {
          delay: 3000,
          disableOnInteraction: false
        },
        // Responsive breakpoints
        breakpoints: {
          1024: {
            slidesPerView: 2
          },
          768: {
            slidesPerView: 1
          },
          640: {
            slidesPerView: 1
          },
          320: {
            slidesPerView: 1
          }
        }
      },
      type: 'news',
      items: [
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "1", overview: "新闻概览"},
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "2", overview: "新闻概览"},
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "3", overview: "新闻概览"},
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "3", overview: "新闻概览"},
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "3", overview: "新闻概览"},
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "3", overview: "新闻概览"},
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "3", overview: "新闻概览"},
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "3", overview: "新闻概览"},
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "3", overview: "新闻概览"},
      ],
    }
  },
}
</script>

<style scoped>

</style>
