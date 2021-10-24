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
              <img class="add" :src="item.image" alt="project" @click="view(item)">
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
              <img :src="item.image" alt="project">
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
    <div v-if="modal">
      <div class="modal" v-on:click.self="modal=false">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">编辑项目信息</h4>
              <button type="button" class="close" @click="modal=false">×</button>
            </div>
            <div class="modal-body">
              <div class="card mb-1">
                <div v-if="viewing_edit.image === default_image">
                  <img :src="(local?'':image_base)+default_edit_image" class="card-img-top" alt=""
                       style="max-height: 400px;">
                </div>
                <div v-else>
                  <img :src="(local?'':image_base)+viewing_edit.image" class="card-img-top" alt=""
                       style="max-height: 500px;">
                </div>
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="image1">图片</span>
                </div>
                <div class="custom-file">
                  <input type="file" id="image2" aria-describedby="image1" @change="change_image($event)">
                  <label class="custom-file-label" for="image2">选择图片</label>
                </div>
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon1">项目名称</span>
                </div>
                <input type="text" class="form-control" v-model="viewing_edit.name" aria-describedby="basic-addon1">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon2">项目来源</span>
                </div>
                <input type="text" class="form-control" v-model="viewing_edit.source" aria-describedby="basic-addon2">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon3">开始时间</span>
                </div>
                <input type="time" class="form-control" v-model="viewing_edit.bg_time" aria-describedby="basic-addon3">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon4">结束时间</span>
                </div>
                <input type="time" class="form-control" v-model="viewing_edit.ed_time" aria-describedby="basic-addon4">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon5">项目经费</span>
                </div>
                <input type="text" class="form-control" v-model="viewing_edit.value" aria-describedby="basic-addon5">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon6">担任角色</span>
                </div>
                <input type="text" class="form-control" v-model="viewing_edit.principal"
                       aria-describedby="basic-addon6">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon7">项目类别</span>
                </div>
                <input type="text" class="form-control" v-model="viewing_edit.class" aria-describedby="basic-addon7">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon8">项目状态</span>
                </div>
                <input type="text" class="form-control" v-model="viewing_edit.state" aria-describedby="basic-addon8">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon9">项目简介</span>
                </div>
                <textarea class="form-control" v-model="viewing_edit.desc"
                          aria-describedby="basic-addon9" style="min-height: 150px !important;"></textarea>
              </div>
            </div>
            <div class="modal-footer">
              <div v-if="viewing_edit.image === default_image">
                <button type="button" class="btn btn-primary" @click="edit"><span class="fa fa-edit"></span>&nbsp;&nbsp;确定
                </button>
              </div>
              <div v-else>
                <button type="button" class="btn btn-warning" @click="edit"><span class="fa fa-edit"></span>&nbsp;&nbsp;修改
                </button>
                <button type="button" class="btn btn-danger" @click="remove(viewing_edit)">
                  <span class="fa fa-trash-o"></span>删除
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="modal-backdrop show" style="z-index: 2000"></div>
    </div>
  </section>
</template>

<script>
    import Functions from "./Functions";
    import {bus} from "@/plugins/bus";

    export default {
        name: "ProjectSingle",
        mixins: [Functions],
        data() {
            return {
                type: 'project',
                modal: false,
                viewing: null,
                viewing_edit: null,
                local: true,
                upload_image: null,
                image_base: this.$store.state.image_base,
                default_edit_image: "/static/images/default/image.jpg",
                default_image: '/static/images/default/header.png',
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
            change_image(e) {
                let file = e.target.files[0];
                this.upload_image = file;
                this.local = true;
                this.viewing_edit.image = window.URL.createObjectURL(file);
            },
            view(item) {
                this.viewing = item;
                if (this.admin) {
                    this.viewing_edit = JSON.parse(JSON.stringify(item));
                    this.modal = true;
                } else {
                    this.$toast.info('没有权限');
                }
            },
            edit() {
                let data = new FormData();
                data.append('type', this.type);
                data.append('filetype', 'item');
                data.append('name', this.viewing_edit.name);
                data.append('source', this.viewing_edit.source);
                data.append('bg_time', this.viewing_edit.bg_time);
                data.append('ed_time', this.viewing_edit.ed_time);
                data.append('value', this.viewing_edit.value);
                data.append('principal', this.viewing_edit.principal);
                data.append('class', this.viewing_edit.class);
                data.append('state', this.viewing_edit.state);
                data.append('desc', this.viewing_edit.desc);
                data.append('image', this.upload_image);
                this.post('/list/', data, data => {
                    switch (data['message']) {
                        case 'success': {
                            this.viewing.name = this.viewing_edit.name;
                            this.viewing.source = this.viewing_edit.source;
                            this.viewing.bg_time = this.viewing_edit.bg_time;
                            this.viewing.ed_time = this.viewing_edit.ed_time;
                            this.viewing.value = this.viewing_edit.value;
                            this.viewing.principal = this.viewing_edit.principal;
                            this.viewing.class = this.viewing_edit.class;
                            this.viewing.state = this.viewing_edit.state;
                            this.viewing.deac = this.viewing_edit.deac;
                            this.local = true;
                            this.viewing.image = data['content'];
                            bus.$emit('reload_hots');
                            break;
                        }
                        case 'error': {
                            this.$toast.error('修改失败');
                            break;
                        }
                        default: {
                            this.$toast.info(data['message']);
                        }
                    }
                })
                this.modal = false;
            },
            remove(item) {
                this.delete('/list/', {type: this.type, filetype: 'item', filename: item.filename}, data => {
                    switch (data['message']) {
                        case 'success': {
                            bus.$emit('reload_list');
                            bus.$emit('reload_hots');
                            break;
                        }
                        case 'error': {
                            this.$toast.error('删除失败');
                            break;
                        }
                        default: {
                            this.$toast.info(data['message']);
                        }
                    }
                });
                this.modal = false;
            },
        }

    }
</script>

<style scoped>
  .modal {
    z-index: 2001;
    display: block;
  }

  .modal-dialog {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
  }

  .modal-content {
    /*overflow-y: scroll; */
    position: absolute;
    top: 0;
    bottom: 0;
    width: 100%;
  }

  .modal-body {
    overflow-y: scroll;
    position: absolute;
    top: 68px;
    bottom: 70px;
    width: 100%;
  }

  .modal-footer {
    position: absolute;
    width: 100%;
    bottom: 0;
  }
</style>
