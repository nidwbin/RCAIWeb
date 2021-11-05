<!--
 * @FileDescription: contact students page
 * @Author: liuyoude
 * @Date: 2021-10-03
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-03
 -->
<template>
  <div class="contact-area pt-115">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="card-header mb-5">
            <div class="h2"><span class="fa fa-address-book" style="color: #ff5316;"></span>&nbsp;&nbsp;加入我们</div>
          </div>
          <div class="contact-item">
            <div class="item d-block d-sm-flex align-items-top" v-for="item in items">
              <div class="thumb">
                <img :src="item.image" alt="">
                <!--                <span>1996</span>-->
              </div>
              <div class="content">
                <nuxt-link to="/single-project"><span class="	fa fa-caret-right"></span>{{ item.name }}</nuxt-link>
                <p>{{ item.require }}</p>
              </div>
            </div>
            <div class="about">
              <h3 class="mb-5">相关信息</h3>
              <div class="list-group">
                <div class="list-group-item text-center" v-for="item in info_items">
                  {{ item.desc }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HistoryPage",
  data() {
    return {
      items: [
        {name: "本科生", require: "招生要求", image: "/static/images/contact/recruitment-1.png"},
        {name: "硕士研究生", require: "招生要求", image: "/static/images/contact/recruitment-2.png"},
        {name: "博士研究生", require: "招生要求", image: "/static/images/contact/recruitment-3.png"},
      ],
      info_items: [
        {desc: "1.**********"},
        {desc: "2.**********"},
        {desc: "3.**********"},
        {desc: "联系我们：马心慧 xxxxxxxxx"},
      ]
    }
  }
}
</script>

<style scoped>

</style>
