<!--
 * @FileDescription: team page
 * @Author: liuyoude
 * @Date: 2021-09-28
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-09-28
 -->
<template>
  <section class="leadership-area about-leadership team-leadership">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-4 col-md-6 col-sm-9" v-for="item in new_items" v-if="admin">
          <div class="leadership-item mt-30">
            <div class="leadership-thumb">
              <img :src=" item.image " alt="doctors">
            </div>
            <div class="leadership-content text-center">
              <h4>{{ item.name }}</h4>
              <span>{{ item.class }}</span>
              <p>{{ item.abstract }}</p>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-md-6 col-sm-9" v-for="item in items">
          <div class="leadership-item mt-30">
            <div class="leadership-thumb">
              <img :src=" item.image " alt="doctors">
              <div class="social">
                <a href="#"><i class="fa fa-plus"></i></a>
                <ul>
                  <li><a :href="'mailto:'+item.email"><i class="fa fa-at"></i></a></li>
                  <li><a href="#"><i @click="gotolink(item.link)" class="fa fa-vcard-o"></i></a></li>
                  <!--                  <li><a href="#"><i class="fa fa-instagram"></i></a></li>-->
                </ul>
              </div>
            </div>
            <div class="leadership-content text-center">
              <h4>{{ item.name }}</h4>
              <span>{{ item.class }}</span>
              <p>{{ item.abstract }}</p>
            </div>
            <div class="mt-2" v-if="admin" style="text-align: center">
              <button type="button" class="btn btn-warning" @click="view(item)">
                <span class="fa fa-edit"></span>&nbsp;&nbsp;编辑
              </button>
              <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
              <button type="button" class="btn btn-danger" @click="remove(item)">
                <span class="fa fa-trash-o"></span>&nbsp;&nbsp;删除
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
    export default {
        name: "TeamPage",
        data() {
            return {
                type: "student",
                items: [
                    {
                        name: "David",
                        image: "/static/images/team-1.png",
                        class: "博一",
                        email: "12345@qq.com",
                        link: "https://www.baidu.com/",
                        abstract: "There are many of lorem ipsum available but the have in some form, by injected humour."
                    },
                    {
                        name: "David",
                        image: "/static/images/team-1.png",
                        class: "博一",
                        email: "12345@qq.com",
                        link: "https://www.baidu.com/",
                        abstract: "There are many of lorem ipsum available but the have in some form, by injected humour."
                    },
                    {
                        name: "David",
                        image: "/static/images/team-1.png",
                        class: "博一",
                        email: "12345@qq.com",
                        link: "https://www.baidu.com/",
                        abstract: "There are many of lorem ipsum available but the have in some form, by injected humour."
                    },
                    {
                        name: "David",
                        image: "/static/images/team-1.png",
                        class: "博一",
                        email: "12345@qq.com",
                        link: "https://www.baidu.com/",
                        abstract: "There are many of lorem ipsum available but the have in some form, by injected humour."
                    },
                    {
                        name: "David",
                        image: "/static/images/team-1.png",
                        class: "博一",
                        email: "12345@qq.com",
                        link: "https://www.baidu.com/",
                        abstract: "There are many of lorem ipsum available but the have in some form, by injected humour."
                    },
                    {
                        name: "David",
                        image: "/static/images/team-1.png",
                        class: "博一",
                        email: "12345@qq.com",
                        link: "https://www.baidu.com/",
                        abstract: "There are many of lorem ipsum available but the have in some form, by injected humour."
                    },
                ],

                new_items: [
                    {
                        name: "姓名",
                        image: "/static/images/default/header.png",
                        class: "年级",
                        email: "#",
                        link: "#",
                        abstract: "描述"
                    },
                ],
                pages: {
                    active: 1,
                    hidden: true,
                    page_list: [1, 2, 3, 4],
                },

            }
        },
        computed: {
            admin() {
                return this.$store.state.admin;
            }
        },

        methods: {
            gotolink(link) {
                window.location.href = link;
                // window.open(link, "_blank");
            }
        }

    }
</script>

<style scoped>

</style>
