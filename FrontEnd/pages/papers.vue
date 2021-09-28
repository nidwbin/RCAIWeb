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
    <PageHeader title="论文"/>
    <PapersList/>
    <PagesList/>
    <Footer/>
  </div>
</template>

<script>
  import Nav from "../components/Nav";
  import PageHeader from "../components/PageHeader";
  import PapersList from "../components/PapersList";
  import PagesList from "../components/PagesList";
  import Footer from "../components/Footer";

  export default {
    components:{
      Nav,
      PageHeader,
      PapersList,
      PagesList,
      Footer,
    }
  }
</script>
