<!--
 * @FileDescription: papers page
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-25
 -->
<template>
  <div>
    <Init/>
    <Nav/>
    <PageHeader title="论文"/>
    <PapersList/>
    <Footer/>
  </div>
</template>

<script>
  import Init from "../components/Init";
  import Nav from "../components/Nav";
  import PageHeader from "../components/PageHeader";
  import PapersList from "../components/PapersList";
  import Footer from "../components/Footer";

  export default {
    components:{
      Init,
      Nav,
      PageHeader,
      PapersList,
      Footer,
    }
  }
</script>
