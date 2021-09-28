<!--
 * @FileDescription: news page
 * @Author: wenbin, liuyoude
 * @Date: 2021-09-25
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-09-28
 -->
<template>
  <div>
    <Init/>
    <Nav/>
    <PageHeader title_zh="新闻" title_en="News"/>
    <NewsList/>
    <PagesList/>
    <Footer/>
  </div>
</template>

<script>
  import Init from "../components/Init";
  import Nav from "../components/Nav";
  import PageHeader from "../components/PageHeader";
  import NewsList from "../components/NewsList";
  import PagesList from "../components/PagesList";
  import Footer from "../components/Footer";

  export default {
    components:{
      Init,
      Nav,
      PageHeader,
      NewsList,
      PagesList,
      Footer,
    }
  }
</script>
