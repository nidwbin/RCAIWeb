<!--
 * @FileDescription: login page
 * @Author: wenbin
 * @Date: 2021-09-26
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-26
 -->
<template>
  <div>
    <Init/>
    <Nav/>
    <PageHeader title="登录"/>
    <LoginArea/>
    <Footer/>
  </div>
</template>

<script>
  import Init from "../components/Init";
  import Nav from "../components/Nav";
  import PageHeader from "../components/PageHeader";
  import LoginArea from "../components/LoginArea";
  import Footer from "../components/Footer";

  export default {
    components:{
      Init,
      Nav,
      PageHeader,
      LoginArea,
      Footer,
    },
  }

</script>
