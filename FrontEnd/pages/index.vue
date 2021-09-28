<!--
 * @FileDescription: home page
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-25
 -->
<template>
  <div>
    <Nav/>
    <SliderTwo/>
    <NanoArea/>
    <AboutArea/>
    <EmailArea/>
    <ServicesTwoArea/>
    <VideoArea/>
    <MissionArea/>
    <ProjectThreeArea/>
    <ClientThreeArea/>
    <FunfactsThreeArea/>
    <ExperienceArea/>
    <NewsList/>
    <BrandThreeArea/>
    <Footer/>
  </div>

</template>

<script>
import Nav from "../components/Nav";
import NewsList from "../components/NewsList";
import Footer from "../components/Footer";


import SliderTwo from "../components/Slider";
import NanoArea from "../components/NanoArea";
import AboutArea from "../components/AboutArea";
import EmailArea from "../components/EmailArea";
import ServicesTwoArea from "../components/ServicesArea";
import VideoArea from "../components/VideoArea";
import MissionArea from "../components/MissionArea";
import ProjectThreeArea from "../components/ProjectArea";
import ClientThreeArea from "../components/ClientArea";
import FunfactsThreeArea from "../components/FunfactsArea";
import ExperienceArea from "../components/ExperienceArea";
import BrandThreeArea from "../components/BrandArea";

export default {
  components: {
    Nav,
    NewsList,
    Footer,

    BrandThreeArea,
    ExperienceArea,
    FunfactsThreeArea,
    ClientThreeArea,
    ProjectThreeArea,
    MissionArea,
    VideoArea,
    ServicesTwoArea,
    EmailArea,
    AboutArea,
    NanoArea,
    SliderTwo,
  },
  mounted() {
    this.$cookies.set('location',this.$route.fullPath);
  },
  head() {
    return {
      title: "听觉智能研究中心"
    }
  },
}


</script>
