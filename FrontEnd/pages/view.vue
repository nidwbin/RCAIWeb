<!--
 * @FileDescription: news page
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-26
 -->
<template>
  <div>
    <Nav/>
    <Viewer :type="this.$route.query.type" :filename="this.$route.query.file"/>
    <Footer/>
  </div>
</template>

<script>
  import Nav from "../components/Nav";
  import PageHeader from "../components/PageHeader";
  import Viewer from "../components/Viewer";
  import Footer from "../components/Footer";

  export default {
    components:{
      Nav,
      PageHeader,
      Viewer,
      Footer,
    },
  }
</script>
