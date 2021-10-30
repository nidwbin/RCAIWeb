<!--
 * @FileDescription: contact students page
 * @Author: liuyoude
 * @Date: 2021-10-03
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-03
 -->
<template>
  <div>
    <Nav/>
    <PageHeader title_zh="招聘" title_en="Join Us"/>
    <ContactTeachersPage />
    <Map />
    <Footer/>
  </div>
</template>

<script>
  import Nav from "../components/Nav";
  import PageHeader from "../components/PageHeader";
  import ContactTeachersPage from "../components/ContactTeachersPage";
  import Map from "../components/Map";
  import Footer from "../components/Footer";

  export default {
    components:{
      Nav,
      PageHeader,
      ContactTeachersPage,
      Map,
      Footer,
    },
  mounted() {
    this.$cookies.set('location',this.$route.fullPath);
  },
  }
</script>
