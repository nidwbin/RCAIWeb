<!--
 * @FileDescription: check admin
 * @Author: wenbin
 * @Date: 2021-09-13
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-13
 -->

<template>
  <Init/>
</template>

<script>
import Init from "~/components/admin/Init";
    export default {
        name:"CheckAdmin",
        components:{
          Init,
        },
        mounted() {
            this.$store.commit("change_admin",this.check_admin());
        },
      methods:{
            check_admin(){
              let ans=true;
              console.log("Need Check Admin!");
              return ans;
            }
        }
    }
</script>
