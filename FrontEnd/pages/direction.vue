<!--
 * @FileDescription: research page
 * @Author: liuyoude
 * @Date: 2021-10-01
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-01
 -->
<template>
  <div>
    <Nav/>
    <PageHeader title_zh="研究方向" title_en="Research Direction"/>
    <ResearchPage />
    <Footer/>
  </div>
</template>

<script>
  import Nav from "../components/Nav";
  import PageHeader from "../components/PageHeader";
  import ResearchPage from "../components/ResearchPage";
  import Footer from "../components/Footer";

  export default {
    components:{
      Nav,
      PageHeader,
      ResearchPage,
      Footer,
    },
  mounted() {
    this.$cookies.set('location',this.$route.fullPath);
  },
  }
</script>
