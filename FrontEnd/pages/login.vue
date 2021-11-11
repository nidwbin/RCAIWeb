<!--
 * @FileDescription: login page
 * @Author: wenbin
 * @Date: 2021-09-26
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-26
 -->
<template>
  <div>
    <Nav/>
    <PageHeader title_zh="登录" title_en="login"/>
    <LoginArea/>
    <Footer/>
  </div>
</template>

<script>
  import Nav from "../components/Nav";
  import PageHeader from "../components/PageHeader";
  import LoginArea from "../components/LoginArea";
  import Footer from "../components/Footer";

  export default {
    components:{
      Nav,
      PageHeader,
      LoginArea,
      Footer,
    },
  }

</script>
