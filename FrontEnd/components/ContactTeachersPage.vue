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
          <div class="contact-item">
            <div class="item d-block d-sm-flex align-items-top" v-for="item in items">
              <div class="thumb">
                <img :src="item.image" alt="">
<!--                <span>1996</span>-->
              </div>
              <div class="content">
                <nuxt-link to="/single-project"><span class="	fa fa-caret-right"></span>{{ item.name }}</nuxt-link>
                <p>年龄要求：{{ item.require }}</p>
                <p>相关待遇：{{ item.treatment }}</p>
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
        data () {
            return {
                items: [
                    {treatment:"年薪30万，10万科研启动经费",name:"师资博士后/项目博士后", require:"30周岁以下", image:"/static/images/contact/teacher-2.png"},
                    {treatment:"年薪28万，20万科研启动经费，20万安家费",name:"青年拔尖/准聘副教授", require:"32周岁以下", image:"/static/images/contact/teacher-1.png"},
                    {treatment:"年薪35万，100万科研启动经费，60万安家费",name:"青年拔尖/准聘教授", require:"35周岁以下", image:"/static/images/contact/teacher-3.png"},
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
