<!--
 * @FileDescription: contact students page
 * @Author: liuyoude
 * @Date: 2021-10-03
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-03
 -->
<template>
  <section class="teacher-area pt-90 testimonials-client">
    <div class="container">
      <div class="row">
        <div class="col-lg-12" v-for="item in items">
          <div class="teacher-item mt-30">
            <div class="shape">
              <img src="/static/images/shape/shape-4.png" alt="shape">
            </div>
            <div class="user">
              <div class="user-thumb">
                <img :src="item.image" alt="client">
                <i class="fa fa-quote-left"></i>
              </div>
              <h5 class="title">{{ item.name }}</h5>
              <span>{{ item.prof }}</span>
              <div class="contact">
                <p>电话：<span>0451-86417981</span></p>
                <p>邮箱：<span>jqhan@hit.edu.cn</span></p>
                <p>地址：<span>哈尔滨工业大学321信箱</span></p>
                <p>主页：<span>http://homepage.hit.edu.cn/hanjiqing</span></p>
              </div>

            </div>
            <div class="text">
              <p>{{ item.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
    export default {
        name: "TestimonialPage",
        data () {
            return {
                items:[
                    {name:"韩纪庆",prof:"教授，博士生导师",desc:"简介",image:"/static/images/teacher/JQH.png"},
                    {name:"韩纪庆",prof:"教授，博士生导师",desc:"简介",image:"/static/images/teacher/JQH.png"},
                    {name:"韩纪庆",prof:"教授，博士生导师",desc:"简介",image:"/static/images/teacher/JQH.png"},
                    {name:"韩纪庆",prof:"教授，博士生导师",desc:"简介",image:"/static/images/teacher/JQH.png"},
                ]
            }
        }
    }
</script>

<style scoped>

</style>
