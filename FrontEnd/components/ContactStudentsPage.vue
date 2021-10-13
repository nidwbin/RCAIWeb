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
                <p>{{ item.require }}</p>
              </div>
            </div>
            <div class="about">
              <h3>相关信息</h3>
              <div class="list">
                <ul>
                  <li>1.***************</li>
                  <li>2.**********************</li>
                  <li>3.***************</li>
                  <li>4.**********************</li>
                  <li>联系我们：***********</li>
                  <li>详情见主页：***********</li>
                </ul>
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
                    {name:"本科生", require:"招生要求", image:"/images/contact/recruitment-1.png"},
                    {name:"硕士研究生", require:"招生要求", image:"/images/contact/recruitment-2.png"},
                    {name:"博士研究生", require:"招生要求", image:"/images/contact/recruitment-3.png"},
                ]
            }
        }
    }
</script>

<style scoped>

</style>
