<!--
 * @FileDescription: header page
 * @Author: wenbin, liuyoude
 * @Date: 2021-09-28
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-09-28
 -->
<template>
  <div class="page-title-area bg_cover pt-120" style="background-image: url(/images/banner-bg-1.jpg);">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="page-title-item text-center">
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb">
<!--                <li class="breadcrumb-item"><nuxt-link to="/">首页</nuxt-link></li>-->
                <li class="breadcrumb-item active" aria-current="page">{{ title_en }}</li>
              </ol>
            </nav>
            <h3 class="title">{{ title_zh }}</h3>
          </div>
        </div>
      </div>
    </div>
    <div class="page-shadow">
      <img src="/images/page-shadow.png" alt="">
    </div>
  </div>
</template>

<script>
  export default {
    name: "PageHeader",
    props: {
      title_zh: {
        type: String
      },
      title_en: {
          type: String
      }
    },


  }
</script>

<style scoped>

</style>
