<!--
 * @FileDescription: home page
 * @Author: wenbin, liuyoude
 * @Date: 2021-09-25
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-01
 -->
<template>
  <div>
<<<<<<< Updated upstream
    <Nav />
    <Slider />
    <HotNewsPage />
    <IntroductionPage />
    <FunfactsThreeArea />
    <Footer />
=======
    <Nav/>
    <Slider/>
    <HotNewsPage/>
    <IntroductionPage/>
    <HistoryPage/>
    <FunfactsThreeArea/>
    <Footer/>
>>>>>>> Stashed changes
  </div>

</template>

<script>
<<<<<<< Updated upstream
  import Nav from "../components/Nav";
  import Footer from "../components/Footer";
  import Slider from "../components/Slider";
  import IntroductionPage from "../components/IntroductionPage";
  import FunfactsThreeArea from "../components/FunfactsArea";
  import HotNewsPage from "../components/HotNewsPage";
  export default {
    components: {
      Nav,
      Footer,
      IntroductionPage,
      FunfactsThreeArea,
      Slider,
      HotNewsPage,
    },
    mounted() {
      this.$cookies.set('location', this.$route.fullPath);
    },
    head(){
      return {
        title: "听觉智能研究中心"
      }
    },
  }
=======
import Nav from "../components/Nav";
import Footer from "../components/Footer";
import Slider from "../components/Slider";
import IntroductionPage from "../components/IntroductionPage";
import HistoryPage from "../components/HistoryPage";
import FunfactsThreeArea from "../components/FunfactsArea";
import HotNewsPage from "../components/HotNewsPage";

export default {
  components: {
    Nav,
    Footer,
    Slider,
    HotNewsPage,
    HistoryPage,

    IntroductionPage,
    FunfactsThreeArea,

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
>>>>>>> Stashed changes
</script>
