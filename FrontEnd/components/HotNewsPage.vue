<!--
 * @FileDescription: hot news page
 * @Author: liuyoude
 * @Date: 2021-09-28
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-09-29
 -->
<template>
  <section class="client-area client-2-area client-about">
    <div class="col">
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
            <!--            <swiper-slide v-for="item in hots" :key="item.filename">-->
            <!--              <div class="client-item mt-30">-->
            <!--                <div class="shape">-->
            <!--                  <img src="/static/images/shape/shape-4.png" alt="shape">-->
            <!--                </div>-->
            <!--                <div class="float-left" style="max-width: 20%;">-->
            <!--                  <img :src="item.image===''?default_image:image_base+item.image" alt="new" style="max-height: 110px;">-->
            <!--                </div>-->
            <!--                <div class="float-left ml-4" style="max-height: 20%;">-->
            <!--                  <h4 class="title">-->
            <!--                    <nuxt-link :to="{name:'view', query:{type:type, filename:item.filename}}">-->
            <!--                      {{ item.title }}-->
            <!--                    </nuxt-link>-->
            <!--                  </h4>-->
            <!--                  <span style="color: #ff5316; font-size: 14px;">{{ item.date }}</span>-->
            <!--                  <div class="text">-->
            <!--                    <p>{{ item.overview }}sadadasdadadadasdadsadasdasdasdsadasdasdsadsa</p>-->
            <!--                  </div>-->
            <!--                </div>-->
            <!--              </div>-->
            <!--            </swiper-slide>-->
            <swiper-slide v-for="item in hots" :key="item.filename">
              <div class="client-item mt-30">
                <div class="shape">
                  <img src="/static/images/shape/shape-4.png" alt="shape">
                </div>
                <div class="user">
                  <nuxt-link :to="{name:'view', query:{type:type, filename:item.filename}}">
                    <div class="user-thumb">
                      <img :src="item.image===''?default_image:image_base+item.image" alt="new">
                      <i class="fa fa-quote-left"></i>
                    </div>
                    <h5 class="title">
                      {{ item.title }}
                    </h5>
                    <span>{{ item.date }}</span>
                    <div class="text">
                      <p>{{ item.overview }}</p>
                    </div>
                  </nuxt-link>
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
import Functions from "./Functions";
import 'swiper/css/swiper.css';

export default {
  name: "HotNewsPage",
  mixins: [Functions],
  components: {
    Swiper,
    SwiperSlide
  },
  directives: {
    swiper: directive
  },
  mounted() {
    this.load_data(5);
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
      hots: [],
      default_image: '/static/images/default/image.jpg',
      image_base: this.$store.state.image_base + 'header/',
    }
  },
  methods: {
    load_data(len) {
      this.get('/list/', {type: this.type, filetype: 'hots', len: len},
        data => {
          switch (data['message']) {
            case 'success': {
              let hots = data['content'];
              this.hots = hots.length === 1 ? [JSON.parse(JSON.stringify(hots[0])), JSON.parse(JSON.stringify(hots[0]))] : hots;
              break;
            }
            case 'error': {
              break;
            }
            default: {
              this.$toast.info(data['message']);
            }
          }
        })
    }
  },
}
</script>

<style scoped>
a, a:link, a:visited, a:hover, a:active {
  text-decoration: none;
  color: inherit;
}
</style>
