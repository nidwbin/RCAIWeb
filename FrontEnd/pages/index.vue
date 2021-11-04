<!--
 * @FileDescription: home page
 * @Author: wenbin, liuyoude
 * @Date: 2021-09-25
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-01
 -->
<template>
  <div>
    <Nav/>
    <Slider/>
    <HotNewsPage/>
    <IntroductionPage/>
    <StaticDataArea/>
    <Footer/>
  </div>

</template>

<script>
import Nav from "../components/Nav";
import Footer from "../components/Footer";
import Slider from "../components/Slider";
import IntroductionPage from "../components/IntroductionPage";
import StaticDataArea from "../components/StaticDataArea"
import HotNewsPage from "../components/HotNewsPage";

export default {
  components: {
    Nav,
    Footer,
    IntroductionPage,
    StaticDataArea,
    Slider,
    HotNewsPage,
  },
  mounted() {
    this.$cookies.set('location', this.$route.fullPath);
  },
  head() {
    return {
      title: "听觉智能研究中心"
    }
  },
}
</script>
