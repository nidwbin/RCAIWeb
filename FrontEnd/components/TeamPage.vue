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
            <div class="leadership-thumb" style="filter: brightness(98%); cursor: pointer">
              <img :src=" item.image " alt="doctors" @click="view(item)">
            </div>
            <div class="leadership-content text-center">
              <h4>{{ item.name }}</h4>
              <span>{{ item.class }}</span>
              <p style="min-height: 115px!important;">{{ item.abstract }}</p>
            </div>
            <div class="mt-2" v-if="admin" style="text-align: center">
              <button type="button" class="btn btn-primary" @click="view(item)">
                <span class="fa fa-edit"></span>&nbsp;&nbsp;新增
              </button>
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
              <p style="min-height: 102px;">{{ item.abstract }}</p>
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
    <div v-if="modal">
      <div class="modal" v-on:click.self="modal=false">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">编辑成员信息</h4>
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
                  <span class="input-group-text" id="basic-addon1">姓名</span>
                </div>
                <input type="text" class="form-control" v-model="viewing_edit.name" aria-describedby="basic-addon1">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon2">年级</span>
                </div>
                <select class="form-control" id="sel1">
                  <option>{{viewing_edit.class }}</option>
                  <option v-for="class_item in classes" v-if="class_item !== viewing_edit.class">
                    {{ class_item }}
                  </option>
                </select>
                <!--                <input type="text" class="form-control" v-model="viewing_edit.class" aria-describedby="basic-addon2">-->
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon3">简介</span>
                </div>
                <textarea class="form-control" v-model="viewing_edit.abstract"
                          aria-describedby="basic-addon3"></textarea>
              </div>
            </div>
            <div class="modal-footer">
              <div v-if="viewing_edit.image === default_image">
                <button type="button" class="btn btn-primary" @click="edit"><span class="fa fa-edit"></span>&nbsp;&nbsp;确定</button>
              </div>
              <div v-else>
                <button type="button" class="btn btn-warning" @click="edit"><span class="fa fa-edit"></span>&nbsp;&nbsp;修改</button>
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
        name: "TeamPage",
        mixins: [Functions],
        data() {
            return {
                type: "student",
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
                        class: "博一",
                        email: "#",
                        link: "#",
                        abstract: "描述",
                    },
                ],
                classes: [
                    '博一', '博二', '博三', '博四', '博五'
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
                data.append('class', this.viewing_edit.class);
                data.append('abstract', this.viewing_edit.abstract);
                data.append('image', this.upload_image);
                this.post('/list/', data, data => {
                    switch (data['message']) {
                        case 'success': {
                            this.viewing.name = this.viewing_edit.name;
                            this.viewing.class = this.viewing_edit.class;
                            this.viewing.abstract = this.viewing_edit.abstract;
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
            gotolink(link) {
                window.location.href = link;
                // window.open(link, "_blank");
            }
        }

    }
</script>

<style scoped>
  .modal {
    z-index: 2001;
    display: block;
  }
</style>
