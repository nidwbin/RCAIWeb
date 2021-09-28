<!--
 * @FileDescription: default for all pages
 * @Author: liuyoude
 * @Date: 2021-09-10
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-09-27
 -->

<template>
  <div>
    <nuxt />
  </div>
</template>


<script>

  export default {
    components: {
    },
    head(){
      return {
        title: "RCAI - Research Center of Auditory Intelligence"
      }
    },
    mounted(){
      this.$nextTick(() => {
        this.$nuxt.$loading.start()
        setTimeout(() => this.$nuxt.$loading.finish(), 500)
      })
    }
  }
</script>

<style>
</style>
