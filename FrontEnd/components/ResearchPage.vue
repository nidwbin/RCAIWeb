<!--
 * @FileDescription: history page
 * @Author: liuyoude
 * @Date: 2021-10-01
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-01
 -->
<template>
  <div class="direction-area pt-115">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="direction-item">
            <div class="item d-block d-sm-flex align-items-center" v-for="item in items">
              <div class="thumb">
                <img :src="item.image" alt="">
<!--                <span>{{ item.year }}</span>-->
              </div>
              <div class="content">
                <nuxt-link to="/single-project"><span class="	fa fa-fire"></span>{{ item.name }}</nuxt-link>
                <p>there are many variations of passages of lorem Ipsum available but the majority have suffered alteration in some form injected which don't look of available but the majority have suffered even slightly believable. Lorem Ipsum is simply dummy text of the printing and typesetting industry. </p>
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
            return{
                items: [
                    {name:"基于机器学习的识别方法", image:"./images/direction/direction_1.jpg"},
                    {name:"语音特征选择方法", image:"./images/direction/direction_2.jpg"},
                    {name:"说话人识别", image:"./images/direction/direction_3.jpg"},
                    {name:"语音中的副语言信息识别", image:"./images/direction/direction_4.gif"},
                    {name:"关键词检出", image:"./images/direction/direction_1.jpg"},
                    {name:"VOIP电话语音分析", image:"./images/direction/direction_2.jpg"},
                    {name:"机器的听觉智能", image:"./images/direction/direction_3.jpg"},
                    {name:"声学事件检测", image:"./images/direction/direction_4.gif"},
                ]

            }

        }
    }
</script>

<style scoped>

</style>
