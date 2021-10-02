<!--
 * @FileDescription: papers page
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-25
 -->
<template>
  <div>
    <Nav/>
    <PageHeader title_zh="学术成果" title_en="Academic Achievements"/>
    <PapersPage />
<!--    <PapersList/>-->
    <PagesList/>
    <Footer/>
  </div>
</template>

<script>
  import Nav from "../components/Nav";
  import PageHeader from "../components/PageHeader";
  import PapersPage from "../components/PapersPage";
  import PapersList from "../components/PapersList";
  import PagesList from "../components/PagesList";
  import Footer from "../components/Footer";

  export default {
    components:{
      Nav,
      PageHeader,
      PapersPage,
      PapersList,
      PagesList,
      Footer,
    },
    mounted() {
      this.$cookies.set('location',this.$route.fullPath);
    }
  }
</script>
