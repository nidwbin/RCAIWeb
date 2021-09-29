<template>
  <div class="history-area pt-115">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="history-item">
            <div class="item d-block d-sm-flex align-items-center" v-for="item in items">
              <div class="thumb">
<!--                <img src="/assets/images/history-1.jpg" alt="">-->
                <span>{{ item.year }}</span>
              </div>
              <div class="content">
                <nuxt-link to="/single-project">Company was Founded</nuxt-link>
                <p>there are many variations of passages of lorem Ipsum available but the majority have suffered alteration in some form injected which don't look of available but the majority have suffered even slightly believable. Lorem Ipsum is simply dummy text of the printing and typesetting industry. </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "HistoryPage",

        data () {
            return{
                items: [
                    {year:1996},
                    {year:2001},
                    {year:2007},
                    {year:2020},
                ]

            }

        }
    }
</script>

<style scoped>

</style>
