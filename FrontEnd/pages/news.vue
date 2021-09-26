<!--
 * @FileDescription: news page
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-25
 -->
<template>
  <div>
    <Init/>
    <Nav/>
    <PageHeader title="新闻"/>
    <NewsList/>
    <Footer/>
  </div>
</template>

<script>
  import Init from "../components/Init";
  import Nav from "../components/Nav";
  import PageHeader from "../components/PageHeader";
  import NewsList from "../components/NewsList";
  import Footer from "../components/Footer";

  export default {
    components:{
      Init,
      Nav,
      PageHeader,
      NewsList,
      Footer,
    }
  }
</script>
