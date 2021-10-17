<!--
 * @FileDescription: news page list
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
 -->
<template>
  <div class="news-area news-posts-area pt-120">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-4 col-md-6 col-sm-9" v-for="item in items">
          <div class="news-item mt-30">
            <div class="news-thumb">
              <img :src="item.image" alt="news">
            </div>
            <div class="news-content text-center">
              <nuxt-link :to="{name:'view', query:{type:type,filename:item.filename}}">{{ item.title }}</nuxt-link>
              <div class="date">
                <span>{{ item.date }}</span>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-md-6 col-sm-9" v-if="admin">
          <div class="news-item mt-30">
            <div class="news-thumb">
              <nuxt-link :to="{name:'view', query:{type:type, filename:'new'}}">
                <img src="/static/images/add-button.png" alt="news">
              </nuxt-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "NewsList",
  computed: {
    admin() {
      return this.$store.state.admin;
    }
  },
  data() {
    return {
      type: 'news',
      items: [
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "1"},
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "2"},
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "3"},
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "3"},
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "3"},
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "3"},
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "3"},
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "3"},
        {title: "这是一条新闻", image: "/static/images/logo.png", date: "2021/9/10", filename: "3"},
      ],
    }
  },

}
</script>

<style scoped>

</style>
