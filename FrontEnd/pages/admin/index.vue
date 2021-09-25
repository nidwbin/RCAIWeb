<template>
  <div>
    <CheckAdmin />
    <AdminNav />
    <Slider />
    <ServiceArea />
    <SolutionArea />
    <VideoArea />
    <BuildingArea />
    <BrandArea />
    <ClientArea />
    <FunFactArea />
    <ProjectArea />
    <FaqBrandArea />
    <FaqArea />
    <FutureArea />
    <BlogArea />
    <Footer />
  </div>
</template>

<script>
  import CheckAdmin from "../../components/admin/CheckAdmin";
  import AdminNav from "../../components/admin/AdminNav";
  import Slider from "../../components/Slider";
  import ServiceArea from "../../components/ServiceArea";
  import SolutionArea from "../../components/SolutionArea";
  import VideoArea from "../../components/VideoArea";
  import BuildingArea from "../../components/BuildingArea";
  import BrandArea from "../../components/BrandArea";
  import ClientArea from "../../components/ClientArea";
  import FunFactArea from "../../components/FunFactArea";
  import ProjectArea from "../../components/ProjectArea";
  import FaqBrandArea from "../../components/FaqBrandArea";
  import FaqArea from "../../components/FaqArea";
  import FutureArea from "../../components/FutureArea";
  import BlogArea from "../../components/BlogArea";
  import Footer from "../../components/Footer";
  export default {
    components: {
      CheckAdmin,
      AdminNav,
      Footer,
      BlogArea,
      FutureArea,
      FaqArea,
      FaqBrandArea,
      ProjectArea,
      FunFactArea,
      ClientArea,
      BrandArea,
      BuildingArea,
      VideoArea,
      SolutionArea,
      ServiceArea,
      Slider
    },
    head(){
      return {
        title: "视听觉研究中心管理界面"
      }
    }
  }
</script>
