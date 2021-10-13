<!--
 * @FileDescription: news page
 * @Author: wenbin, liuyoude
 * @Date: 2021-09-25
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-01
 -->
<template>
  <div>
    <Nav/>
    <PageHeader title_zh="新闻" title_en="News"/>
    <NewsPage />
    <Footer/>
  </div>
</template>

<script>
  import Nav from "../components/Nav";
  import PageHeader from "../components/PageHeader";
  import Footer from "../components/Footer";
  import NewsPage from "../components/NewsPage";

  export default {
    components:{
      Nav,
      PageHeader,
      NewsPage,
      Footer,
    },
  mounted() {
    this.$cookies.set('location',this.$route.fullPath);
  },
  }
</script>
