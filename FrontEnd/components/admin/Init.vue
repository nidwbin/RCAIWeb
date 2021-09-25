<!--
 * @FileDescription: init some settings
 * @Author: wenbin
 * @Date: 2021-09-14
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-14
 -->
<template>

</template>
<script>
export default {
  mounted() {
    this.initAjax();
  },
  methods:{
    async initAjax(){
      let csrftoken;
      this.$axios.get(this.$store.state.domain+":"+this.$store.state.port+"/admin"
      ).then(
        (data)=>{
          csrftoken=data["status"]===200?"yes":null;
          this.$cookies.set("csrftoken",csrftoken);
          this.$axios.onRequest((config)=>{
          config.headers.common['Content-Type'] = 'application/json';
          config.xsrfCookieName = 'csrftoken';
          config.xsrfHeaderName = 'X-CSRFToken';
          config.headers.common['X-CSRFToken'] = csrftoken;
      });
        }
      ).catch((error)=>{
        console.log(error);
        window.location.replace(this.$store.state.domain+":"+this.$store.state.port);
      });
    }
  }
}
</script>
