<!--
 * @FileDescription: news page
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-25
 -->
<template>
  <div>
    <Nav/>
    <PageHeader title="新闻"/>
    <NewsList/>
    <PagesList/>
    <Footer/>
  </div>
</template>

<script>
  import Nav from "../components/Nav";
  import PageHeader from "../components/PageHeader";
  import NewsList from "../components/NewsList";
  import PagesList from "../components/PagesList";
  import Footer from "../components/Footer";

  export default {
    components:{
      Nav,
      PageHeader,
      NewsList,
      PagesList,
      Footer,
    }
  }
</script>
