<!--
 * @FileDescription: init some settings
 * @Author: wenbin
 * @Date: 2021-09-14
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
 -->
<template>

</template>
<script>
export default {
  mounted() {
      this.init();
  },
  methods:{
    init(){
      if(process.client){
        this.$axios.get('/csrf');
      }
    },
  }
}
</script>
