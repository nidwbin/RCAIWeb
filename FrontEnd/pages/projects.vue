<!--
 * @FileDescription: papers page
 * @Author: liuyoude
 * @Date: 2021-10-02
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-02
 -->
<template>
  <div>
    <Nav/>
    <PageHeader title_zh="科研项目" title_en="Scientific Research Project"/>
    <ProjectsPage />
    <PagesList/>
    <Footer/>
  </div>
</template>

<script>
  import Nav from "../components/Nav";
  import PageHeader from "../components/PageHeader";
  import ProjectsPage from "../components/ProjectsPage";
  import PagesList from "../components/PagesList";
  import Footer from "../components/Footer";

  export default {
    components:{
      Nav,
      PageHeader,
      ProjectsPage,
      PagesList,
      Footer,
    },
    mounted() {
      this.$cookies.set('location',this.$route.fullPath);
    }
  }
</script>
