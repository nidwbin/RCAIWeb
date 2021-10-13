<!--
 * @FileDescription: papers page
 * @Author: wenbin, liuyoude
 * @Date: 2021-09-25
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-02
 -->
<template>
  <div>
    <Nav/>
    <PageHeader title_zh="学术成果" title_en="Academic Achievements"/>
    <PapersPage />
    <Footer/>
  </div>
</template>

<script>
  import Nav from "../components/Nav";
  import PageHeader from "../components/PageHeader";
  import PapersPage from "../components/PapersPage";
  import Footer from "../components/Footer";

  export default {
    components:{
      Nav,
      PageHeader,
      PapersPage,
      Footer,
    },
    mounted() {
      this.$cookies.set('location',this.$route.fullPath);
    }
  }
</script>
