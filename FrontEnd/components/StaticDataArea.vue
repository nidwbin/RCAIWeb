<template>
  <section class="fun-facts-area fun-facts-3-area" v-observe-visibility="onVisibilityChange">
    <div class="container">
      <div class="fun-facts-bg">
        <div class="row">
          <div class="col-lg-3 col-md-6">
            <div class="fun-facts-item text-center mt-30 animated wow fadeInUp" data-wow-duration="1500ms" data-wow-delay="0ms">
              <h3 class="title odometer"><countTo :startVal='0' :endVal='startCounter ? 100 : 0' :duration='3000'></countTo>余篇</h3>
              <span>累计发表论文数量</span>
            </div>
          </div>
          <div class="col-lg-3 col-md-6">
            <div class="fun-facts-item text-center mt-30 animated wow fadeInUp" data-wow-duration="1500ms" data-wow-delay="200ms">
              <h3 class="title odometer"><countTo :startVal='0' :endVal='startCounter ? 40 : 0' :duration='2000'></countTo>余篇</h3>
              <span>SCI/EI权威索引论文</span>
            </div>
          </div>
          <div class="col-lg-3 col-md-6">
            <div class="fun-facts-item text-center mt-30 animated wow fadeInUp" data-wow-duration="1500ms" data-wow-delay="300ms">
              <h3 class="title odometer"><countTo :startVal='0' :endVal='startCounter ? 5 : 0' :duration='500'></countTo>部</h3>
              <span>书籍著作</span>
            </div>
          </div>
          <div class="col-lg-3 col-md-6">
            <div class="fun-facts-item item text-center mt-30 animated wow fadeInUp" data-wow-duration="1500ms" data-wow-delay="400ms">
              <h3 class="title odometer"><countTo :startVal='0' :endVal='startCounter ? 30 : 0' :duration='2000'></countTo>多项</h3>
              <span>科研工作项目</span>
            </div>
          </div>
        </div>
        <div class="shape">
          <img src="/static/images/shape/shape-5.png" alt="shape">
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  import countTo from 'vue-count-to';
  import { ObserveVisibility } from 'vue-observe-visibility'
  export default {
    name: "FunfactsThreeArea",
    components: { countTo },
    directives: {
      ObserveVisibility
    },
    data() {
      return{
        startCounter: false
      }
    },
    methods: {
      onVisibilityChange (isVisible) {
        if (isVisible){
          this.startCounter = true;
        }
      },
    }
  }
</script>

<style scoped>

</style>
