<!--
 * @FileDescription: home page
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-09-28
 -->
<template>
  <div>
    <Nav />
    <Slider />
    <HotNewsPage />
    <FunfactsThreeArea />
    <Footer />
  </div>

</template>

<script>
  import Nav from "../components/Nav";
  import Footer from "../components/Footer";
  import Slider from "../components/Slider";
  import FunfactsThreeArea from "../components/FunfactsArea";
  import HotNewsPage from "../components/HotNewsPage";
  export default {
    components: {
      Nav,
      Footer,

      FunfactsThreeArea,
      Slider,
      HotNewsPage,
    },
    head(){
      return {
        title: "听觉智能研究中心"
      }
    },
  }


</script>
