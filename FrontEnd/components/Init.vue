<!--
 * @FileDescription: init some settings
 * @Author: wenbin
 * @Date: 2021-09-14
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-26
 -->
<template>

</template>
<script>
export default {
  mounted() {
    if(process.client){
      console.log('client');
    }
    if(process.server){
      console.log('server');
    }
    this.init();
  },
  computed:{
    key(){
      return this.$store.state.authority.key;
    }
  },
  methods:{
    get_back_url(){
      let url;
      switch (this.$store.state.backend.port){
        case "80":{
          url="http://"+this.$store.state.backend.domain;
          break;
        }
        case "443":{
          url="https://"+this.$store.state.backend.domain;
          break;
        }
        default:{
          url="http://"+ this.$store.state.backend.domain + ":" + this.$store.state.backend.port;
        }
      }
      url += "/backend";
      this.$cookies.set("backend-url", url);
      return url;
    },
    init(){
      let csrf="error";
      this.$cookies.set("csrftoken",csrf);
      this.$axios.get(this.get_back_url()+'/csrf').then(
        (response)=>{
          csrf=response.data["csrf"];
          this.$cookies.set("csrftoken",csrf);
        });
    },
  }
}
</script>
