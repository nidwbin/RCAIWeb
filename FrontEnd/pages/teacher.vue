<!--
 * @FileDescription: contact students page
 * @Author: liuyoude
 * @Date: 2021-10-03
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-03
 -->
<template>
  <div>
    <Nav/>
    <PageHeader title_zh="中心教师" title_en="Teachers"/>
    <TeachersPage />
    <Footer/>
  </div>
</template>

<script>
  import Nav from "../components/Nav";
  import PageHeader from "../components/PageHeader";
  import TeachersPage from "../components/TeachersPage";
  import Footer from "../components/Footer";

  export default {
    components:{
      Nav,
      PageHeader,
      TeachersPage,
      Footer,
    },
  mounted() {
    this.$cookies.set('location',this.$route.fullPath);
  },
  }
</script>
