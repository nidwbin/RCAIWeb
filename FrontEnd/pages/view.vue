<!--
 * @FileDescription: news page
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-25
 -->
<template>
  <div>
    <Init/>
    <Nav/>
    <Viewer/>
    <Footer/>
  </div>
</template>

<script>
  import Init from "../components/Init";
  import Nav from "../components/Nav";
  import PageHeader from "../components/PageHeader";
  import Viewer from "../components/Viewer";
  import Footer from "../components/Footer";

  export default {
    components:{
      Init,
      Nav,
      PageHeader,
      Viewer,
      Footer,
    },
    mounted() {

    },
    computed:{
      message(){
        return this.$store.state.com_sync.message;
      }
    },
    methods:{

    }
  }
</script>
