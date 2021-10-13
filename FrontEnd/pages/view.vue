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
    <ViewerHeader :type="this.$route.query.type" :filename="this.$route.query.filename"/>
    <Viewer :type="this.$route.query.type" :filename="this.$route.query.filename"/>
    <Footer/>
  </div>
</template>

<script>
import Nav from "../components/Nav";
import ViewerHeader from "../components/ViewerHeader";
import Viewer from "../components/Viewer";
import Footer from "../components/Footer";

export default {
  components: {
    Nav,
    ViewerHeader,
    Viewer,
    Footer,
  },
  mounted() {
    this.$cookies.set('location', this.$route.fullPath);
  }
}
</script>
