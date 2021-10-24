<!--
 * @FileDescription: introduction page
 * @Author: liuyoude
 * @Date: 2021-10-02
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-02
 -->
<template>
  <section class="single-project-area pt-120">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="single-project" v-for="item in new_items" v-if="admin">
            <div class="single-project-thumb">
              <img :src="item.image" alt="project" style="max-height: 500px !important;">
              <div class="single-project-thumb-content d-flex">
                <ul>
                  <li>项目来源:</li>
                  <li>开始时间:</li>
                  <li>结束时间:</li>
                  <li>项目经费:</li>
                  <li>担任角色:</li>
                  <li>项目类别:</li>
                  <li>项目状态:</li>
                </ul>
                <ul class="pl-125">
                  <li>{{item.source }}</li>
                  <li>{{item.bg_time }}</li>
                  <li>{{item.ed_time }}</li>
                  <li>{{item.value }}</li>
                  <li>{{item.principal }}</li>
                  <li>{{item.class }}</li>
                  <li>{{item.state }}</li>
                </ul>
              </div>
            </div>
            <div class="single-project-content-1">
              <h3 class="title"><span class="	fa fa-clipboard"></span>{{ item.name }}</h3>
              <p>{{ item.desc }}</p>
            </div>
            <div class="mt-5" v-if="admin" style="text-align: center">
              <button type="button" class="btn btn-primary btn-lg" @click="view(item)">
                <span class="fa fa-edit"></span>&nbsp;&nbsp;&nbsp;&nbsp;新&nbsp;增
              </button>
            </div>
          </div>
          <div class="card-header mb-1">
            <div class="h2">科研项目</div>
          </div>
          <div class="single-project" v-for="item in items">
            <div class="single-project-thumb">
              <img :src="item.image" alt="project" >
              <div class="single-project-thumb-content d-flex">
                <ul>
                  <li>项目来源:</li>
                  <li>开始时间:</li>
                  <li>结束时间:</li>
                  <li>项目经费:</li>
                  <li>担任角色:</li>
                  <li>项目类别:</li>
                  <li>项目状态:</li>
                </ul>
                <ul class="pl-125">
                  <li>{{item.source }}</li>
                  <li>{{item.bg_time }}</li>
                  <li>{{item.ed_time }}</li>
                  <li>{{item.value }}</li>
                  <li>{{item.principal }}</li>
                  <li>{{item.class }}</li>
                  <li>{{item.state }}</li>
                </ul>
              </div>
            </div>
            <div class="single-project-content-1">
              <h3 class="title"><span class="	fa fa-clipboard"></span>{{ item.name }}</h3>
              <p>{{ item.desc }}</p>
            </div>
            <div class="mt-5" v-if="admin" style="text-align: center">
              <button type="button" class="btn btn-warning btn-lg" @click="view(item)">
                <span class="fa fa-edit"></span>&nbsp;&nbsp;&nbsp;&nbsp;编&nbsp;辑
              </button>
              <span>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              </span>
              <button type="button" class="btn btn-danger btn-lg" @click="remove(item)">
                <span class="fa fa-trash-o"></span>&nbsp;&nbsp;&nbsp;&nbsp;删&nbsp;除
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
    import Functions from "./Functions";

    export default {
        name: "ProjectSingle",
        mixins: [Functions],
        data() {
            return {
                items: [
                    {
                        image: "/static/images/project/project_1.jpg",
                        name: "复杂声学环境下声学事件检测与音频场景识别方法研究",
                        source: "国家重点研发项目子课题",
                        bg_time: "2017-10",
                        ed_time: "2021-09",
                        value: "153.5万",
                        principal: "负责",
                        class: "纵向项目",
                        state: "进行中",
                        desc: "Lorem ipsum is simply free text used by copytyping refreshing. Neque porro est qui dolorem ipsum quia\n" +
                            "                quaed inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Aelltes port lacus quis\n" +
                            "                enim var sed efficitur turpis gilla sed sit amet finibus eros. Lorem Ipsum is simply dummy text of the\n" +
                            "                printing and typesetting industry. Lorem Ipsum has been the ndustry standard dummy text ever since the\n" +
                            "                1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It\n" +
                            "                has survived not only five centuries. Lorem Ipsum is simply dummy text of the new design printng and\n" +
                            "                type setting Ipsum Take a look at our round up of the best shows coming soon to your telly box has been\n" +
                            "                the is industrys. When an unknown printer took a galley of type and scrambled it to make a type specimen\n" +
                            "                book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining\n" +
                            "                essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets\n" +
                            "                containing."
                    },
                    {
                        image: "/static/images/project/project_2.jpg",
                        name: "面向自然口语交互的情境化语义理解和多轮对话交互管理技术",
                        source: "国家自然科学基金重点项目",
                        bg_time: "2015-01-01",
                        ed_time: "2018-12-01",
                        value: "86万",
                        principal: "负责",
                        class: "纵向项目",
                        state: "进行中",
                        desc: "Lorem ipsum is simply free text used by copytyping refreshing. Neque porro est qui dolorem ipsum quia\n" +
                            "                quaed inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Aelltes port lacus quis\n" +
                            "                enim var sed efficitur turpis gilla sed sit amet finibus eros. Lorem Ipsum is simply dummy text of the\n" +
                            "                printing and typesetting industry. Lorem Ipsum has been the ndustry standard dummy text ever since the\n" +
                            "                1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It\n" +
                            "                has survived not only five centuries. Lorem Ipsum is simply dummy text of the new design printng and\n" +
                            "                type setting Ipsum Take a look at our round up of the best shows coming soon to your telly box has been\n" +
                            "                the is industrys. When an unknown printer took a galley of type and scrambled it to make a type specimen\n" +
                            "                book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining\n" +
                            "                essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets\n" +
                            "                containing."
                    },
                    {
                        image: "/static/images/project/project_3.jpg",
                        name: "复杂声学环境下声学事件检测与音频场景识别方法研究",
                        source: "国家自然科学基金重点项目",
                        bg_time: "2018-01",
                        ed_time: "2021-12",
                        value: "256万（直接）",
                        principal: "负责",
                        class: "纵向项目",
                        state: "进行中",
                        desc: "Lorem ipsum is simply free text used by copytyping refreshing. Neque porro est qui dolorem ipsum quia\n" +
                            "                quaed inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Aelltes port lacus quis\n" +
                            "                enim var sed efficitur turpis gilla sed sit amet finibus eros. Lorem Ipsum is simply dummy text of the\n" +
                            "                printing and typesetting industry. Lorem Ipsum has been the ndustry standard dummy text ever since the\n" +
                            "                1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It\n" +
                            "                has survived not only five centuries. Lorem Ipsum is simply dummy text of the new design printng and\n" +
                            "                type setting Ipsum Take a look at our round up of the best shows coming soon to your telly box has been\n" +
                            "                the is industrys. When an unknown printer took a galley of type and scrambled it to make a type specimen\n" +
                            "                book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining\n" +
                            "                essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets\n" +
                            "                containing."
                    },
                ],
                new_items: [
                    {
                        image: "/static/images/default/header.png",
                        name: "项目名称",
                        source: "xxxxxxxx",
                        bg_time: "xxxx-xx",
                        ed_time: "xxxx-xx",
                        value: "xxx",
                        principal: "xx",
                        class: "xxxx",
                        state: "xx",
                        desc: "项目具体内容的描述......"
                    },
                ]
            }
        },
        computed: {
            admin() {
                return this.$store.state.admin;
            }
        },

    }
</script>

<style scoped>

</style>
