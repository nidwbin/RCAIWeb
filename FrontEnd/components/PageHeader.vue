<!--
 * @FileDescription: header page
 * @Author: wenbin, liuyoude
 * @Date: 2021-09-28
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-09-28
 -->
<template>
  <div class="page-title-area bg_cover pt-200">
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
      <img src="/static/images/page-shadow.png" alt="">
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
.page-title-area {
  /* TODO change header background */
  /*background-image: url(/static/images/background/header-bg1.jpg);*/
  /*background-position-y: -220px;*/

  background-image: url(/static/images/background/header-bg2.jpg);
  background-position-y: -300px;

  /*background-image: url(/static/images/background/header-bg3.jpg);*/
  /*background-position-y: -400px;*/

  /*background-image: url(/static/images/background/header-bg4.jpg);*/
  /*background-position-y: -100px;*/

}
</style>
