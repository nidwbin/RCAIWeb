<!--
 * @FileDescription: nav
 * @Author: liuyoude, wenbin
 * @Date: 2021-09-10
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-09-27
 -->
<template>
  <section class="banner-slide">

    <VueSlickCarousel v-bind="settings">
      <div class="banner-area slide-bg1 bg_cover d-flex align-items-center">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-10">
            <div class="banner-content text-center">
              <span data-animation="fadeInDown" data-delay="1s">{{ SliderVars.lab_name_en }}</span>
              <h3 data-animation="fadeInDown" data-delay=".1s" class="title">{{ SliderVars.lab_name_zh }}</h3>
<!--              <a data-animation="fadeInUp" data-delay="1s" class="main-btn" href="#">Discover more</a>-->
            </div>
          </div>
        </div>
      </div>
    </div>
      <div class="banner-area slide-bg2 bg_cover d-flex align-items-center">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-10">
            <div class="banner-content text-center">
              <span data-animation="fadeInDown" data-delay="1s">{{ SliderVars.lab_name_en }}</span>
              <h3 data-animation="fadeInDown" data-delay=".1s" class="title">{{ SliderVars.lab_name_zh }}</h3>
<!--              <a data-animation="fadeInUp" data-delay="1s" class="main-btn" href="#">Discover more</a>-->
            </div>
          </div>
        </div>
      </div>
    </div>

    </VueSlickCarousel>
  </section>
</template>

<script>
  import VueSlickCarousel from 'vue-slick-carousel'
  import 'vue-slick-carousel/dist/vue-slick-carousel.css'
    let SliderVars = {
        lab_name_zh:"听觉智能研究中心",
        lab_name_en:"Research Center of Auditory Intelligence",
    };
    export default {
      name: "Banner",
      components: { VueSlickCarousel },
      data() {
        return {
            SliderVars,
          settings: {
            arrows: false,
            autoplay: true
          },
        }
      },
    }
</script>

<style scoped>

</style>
