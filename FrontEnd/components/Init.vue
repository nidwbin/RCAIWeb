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
      this.init();
    }
  },
  methods:{
    init(){
      let csrf="error";
      this.$cookies.set("csrftoken",csrf);
      this.$axios.get('/csrf').then(
        (response)=>{
          csrf=response.data["csrf"];
          this.$cookies.set("csrftoken",csrf);
        });
    },
  }
}
</script>
