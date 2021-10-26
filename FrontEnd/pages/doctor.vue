<!--
 * @FileDescription: doctors page
 * @Author: liuyoude
 * @Date: 2021-09-28
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-09-28
 -->
<template>
  <div>
    <Nav/>
    <PageHeader title_zh="中心博士生" title_en="Doctors"/>
    <TeamPage type="doctor"/>
    <Footer/>
  </div>
</template>

<script>

import Nav from "../components/Nav";
import Footer from "../components/Footer";
import PageHeader from "../components/PageHeader";
import TeamPage from "../components/TeamPage";

export default {
  components: {
    Nav,
    PageHeader,
    TeamPage,
    Footer,
  },
  head() {
    return {
      title: "Doctors of RCAI"
    }
  },
  mounted() {
    this.$cookies.set('location', this.$route.fullPath);
  },
}
</script>
