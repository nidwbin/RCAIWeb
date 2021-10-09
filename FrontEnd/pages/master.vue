<!--
 * @FileDescription: doctors page
 * @Author: liuyoude
 * @Date: 2021-09-28
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-09-28
 -->
<template>
  <div>
    <Nav />
    <PageHeader title_zh="中心研究生" title_en="Masters" />
    <TeamPage />
    <PagesList />
    <Footer />
  </div>
</template>

<script>

  import Nav from "../components/Nav";
  import Footer from "../components/Footer";
  import PageHeader from "../components/PageHeader";
  import TeamPage from "../components/TeamPage";
  import PagesList from "../components/PagesList";
  export default {
    components: {
      Nav,
      PageHeader,
      TeamPage,
      PagesList,
      Footer,
    },
    head(){
      return {
        title: "Masters of RCAI"
      }
    },
  mounted() {
    this.$cookies.set('location', this.$route.fullPath);
  },
  }
</script>
