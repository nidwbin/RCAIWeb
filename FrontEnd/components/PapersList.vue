<!--
 * @FileDescription: news page list
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-25
 -->
<template>
  <section class="industri-services-area services-page">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-4 col-md-6 col-sm-9" v-for="item in items">
          <div class="services-item mt-30">
            <div class="services-thumb">
              <img :src="item.image" alt="news">
            </div>
            <div class="services-content">
              <h1 class="title">{{ item.title }}</h1>
              <p>{{ item.date }}</p>
              <p>{{ item.abstract }}</p>
              <nuxt-link :to="{name:'view', query:{type:type, filename:item.filename}}">查看</nuxt-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "PapersList",
  data() {
    return {
      type: 'paper',

      items: [
        {title: "这是一篇论文", image: "/images/logo.png", date: "2021/9/10", abstract: "something", filename: "1",},
        {title: "这是一篇论文", image: "/images/logo.png", date: "2021/9/10", abstract: "something", filename: "2"},
        {title: "这是一篇论文", image: "/images/logo.png", date: "2021/9/10", abstract: "something", filename: "3"},
        {title: "这是一篇论文", image: "/images/logo.png", date: "2021/9/10", abstract: "something", filename: "3"},
        {title: "这是一篇论文", image: "/images/logo.png", date: "2021/9/10", abstract: "something", filename: "3"},
        {title: "这是一篇论文", image: "/images/logo.png", date: "2021/9/10", abstract: "something", filename: "3"},
        {title: "这是一篇论文", image: "/images/logo.png", date: "2021/9/10", abstract: "something", filename: "3"},
        {title: "这是一篇论文", image: "/images/logo.png", date: "2021/9/10", abstract: "something", filename: "3"},
        {title: "这是一篇论文", image: "/images/logo.png", date: "2021/9/10", abstract: "something", filename: "3"},
      ],
    }
  },
}
</script>

<style scoped>

</style>
