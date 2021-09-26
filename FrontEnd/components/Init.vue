<!--
 * @FileDescription: init some settings
 * @Author: wenbin
 * @Date: 2021-09-14
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-25
 -->
<template>

</template>
<script>
export default {
  mounted() {
    this.init_ajax();
  },
  methods:{
    back_url(){
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
          url="http://" + this.$store.state.backend.domain + ":" + this.$store.state.backend.port;
        }
      }
      url += "/backend";
      return url;
    },
    async init_ajax(){
      let csrf;
      this.$axios.get(this.back_url()).then(
        (data)=>{
          csrf=data["status"];

          this.$axios.onRequest((config)=> {
            config.xsrfCookieName = 'csrftoken';
            config.xsrfHeaderName = 'X-CSRFToken';
            config.headers.common['Content-Type'] = 'application/json';
            config.headers.common['X-CSRFToken'] = this.$cookies.get("csrf");
          });

          this.$cookies.set("csrf",csrf);
          this.$cookies.set("ajax-ready",true);
        }).catch(
        (error)=>{
          console.log(error);
          this.$cookies.set("ajax-ready",false);
        }).finally(()=>{
          this.key_chain();
        });
    },
    key_chain() {
      let debug=true;
      if (!debug && this.$cookies.get("ajax-ready")) {
          this.$axios.get(this.back_url(),{
                "message": "key",
            }).then(
              (data) => {
                this.$cookies.set("key",data["key"]);
                if(data["key"]!=="visitor"){
                  this.$store.commit("set_admin",true);
                }else{
                  this.$store.commit("set_admin",false);
                }
              }
          ).catch(
            (error)=>{
              console.log(error);
              this.$cookies.set("key","visitor");
            }
          )
      }else{
        this.$store.commit("set_admin",true);
        this.$cookies.set("key","visitor");
      }
  }
}
}
</script>
