<!--
 * @FileDescription: contact students page
 * @Author: liuyoude
 * @Date: 2021-10-03
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-03
 -->
<template>
  <section class="teacher-area pt-30 testimonials-client">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="teacher-item mt-30" style="min-height: 360px !important;" v-show="admin">
            <div class="shape">
              <img src="/static/images/shape/shape-4.png" alt="shape">
            </div>
            <div class="user">
              <div class="user-thumb">
                <img :src="default_image" alt="client">
                <i class="fa fa-quote-left"></i>
              </div>
              <h5 class="title">{{ new_item.name }}</h5>
              <span>{{ new_item.prof }}</span>
              <div class="contact">
                <p>电话：<span>{{ new_item.tel }}</span></p>
                <p>邮箱：<span>{{ new_item.email }}</span></p>
                <p>地址：<span>{{ new_item.adress }}</span></p>
                <p>主页：<span>{{ new_item.link }}</span></p>
              </div>

            </div>
            <div class="text">
              <p>{{ new_item.desc }}</p>
            </div>
            <div class="mt-4" style="text-align: center">
              <button type="button" class="btn btn-primary" @click="create">
                <span class="fa fa-edit"></span>&nbsp;&nbsp;新增
              </button>
            </div>
          </div>
          <div class="card-header">
            <div class="h2"><span class="fa fa-user-secret" style="color: #ff5316;">&nbsp;&nbsp;</span>中心教师</div>
          </div>
          <div class="teacher-item mt-30" v-for="item in items">
            <div class="shape">
              <img src="/static/images/shape/shape-4.png" alt="shape">
            </div>
            <div class="user">
              <div class="user-thumb">
                <img :src="item.image===''?default_image:image_base+item.image" alt="client">
                <i class="fa fa-quote-left"></i>
              </div>
              <h5 class="title">{{ item.name }}</h5>
              <span>{{ item.prof }}</span>
              <div class="contact">
                <p>电话：<span><a :href="'tel:'+item.tel">{{ item.tel }}</a></span></p>
                <p>邮箱：<span><a :href="'mailto:'+ item.email">{{ item.email }}</a></span></p>
                <p>地址：<span style="line-break: anywhere!important;">{{ item.adress }}</span></p>
                <p>主页：<span style="color: #007bff !important; cursor: pointer;"><a
                  @click="goto_link(item.link)">{{ item.link }}</a></span></p>
              </div>

            </div>
            <div class="text" style="min-height: 300px;">
              <p>{{ item.desc }}</p>
            </div>
            <div class="mt-2" v-show="admin" style="text-align: center">
              <button type="button" class="btn btn-warning" @click="view(item,false)">
                <span class="fa fa-edit"></span>&nbsp;&nbsp;编辑
              </button>
              <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
              <button type="button" class="btn btn-danger" @click="remove(item)">
                <span class="fa fa-trash-o"></span>&nbsp;&nbsp;删除
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-show="modal">
      <div class="modal" v-on:click.self="modal=false">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">编辑教师信息</h4>
              <button type="button" class="close" @click="modal=false">×</button>
            </div>
            <div class="modal-body">
              <div class="card mb-1">
                <div>
                  <img :src="viewing_edit.image===''?default_image:(local?'':image_base)+viewing_edit.image"
                       class="card-img-top" alt="" style="max-height: 500px;">
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
                  <span class="input-group-text" id="basic-addon2">职称</span>
                </div>
                <input type="text" class="form-control" v-model="viewing_edit.prof" aria-describedby="basic-addon2">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon3">电话</span>
                </div>
                <input type="tel" class="form-control" v-model="viewing_edit.tel" aria-describedby="basic-addon3">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon4">邮箱</span>
                </div>
                <input type="email" class="form-control" v-model="viewing_edit.email" aria-describedby="basic-addon4">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon5">地址</span>
                </div>
                <input type="text" class="form-control" v-model="viewing_edit.adress" aria-describedby="basic-addon5">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon6">主页</span>
                </div>
                <input type="email" class="form-control" v-model="viewing_edit.link" aria-describedby="basic-addon6">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon7">简介</span>
                </div>
                <textarea class="form-control" v-model="viewing_edit.desc"
                          aria-describedby="basic-addon5"></textarea>
              </div>
            </div>
            <div class="modal-footer">
              <div v-if="create_flag">
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
      <div class="modal-backdrop show" style=" z-index: 2000"></div>
    </div>
    <PagesList ref="page" :type="this.type" :per_page="per_page" @change_page="load_list"/>
  </section>
</template>

<script>

import Functions from "./Functions";
import PagesList from "@/components/PagesList";

export default {
  name: "TeacherPage",
  components: {PagesList},
  mixins: [Functions],

  data() {
    return {
      type: 'teachers',
      modal: false,
      viewing: {
        id: 'new',
        name: "姓名",
        prof: "职称",
        desc: "简介",
        image: "",
        tel: "xxxx-xxxxxxxx",
        email: "xxx@hit.edu.cn",
        adress: "哈尔滨工业大学xxx信箱",
        link: "http://homepage.hit.edu.cn/xxx"
      },
      viewing_edit: {
        id: 'new',
        name: "姓名",
        prof: "职称",
        desc: "简介",
        image: "",
        tel: "xxxx-xxxxxxxx",
        email: "xxx@hit.edu.cn",
        adress: "哈尔滨工业大学xxx信箱",
        link: "http://homepage.hit.edu.cn/xxx"
      },
      local: false,
      create_flag: false,
      upload_image: null,
      image_base: this.$store.state.image_base + 'people/',
      btn_image: '/static/images/default/add.png',
      default_image: '/static/images/default/image.jpg',
      items: [
        // {
        //   name: "韩纪庆",
        //   prof: "教授，博士生导师",
        //   desc: "简介",
        //   image: "/static/images/teacher/JQH.png",
        //   tel: "0451-86417981",
        //   email: "jqhan@hit.edu.cn",
        //   adress: "哈尔滨工业大学321信箱",
        //   link: "http://homepage.hit.edu.cn/hanjiqing"
        // },
        // {
        //   name: "韩纪庆",
        //   prof: "教授，博士生导师",
        //   desc: "简介",
        //   image: "/static/images/teacher/JQH.png",
        //   tel: "0451-86417981",
        //   email: "jqhan@hit.edu.cn",
        //   adress: "哈尔滨工业大学321信箱",
        //   link: "http://homepage.hit.edu.cn/hanjiqing"
        // },
        // {
        //   name: "韩纪庆",
        //   prof: "教授，博士生导师",
        //   desc: "简介",
        //   image: "/static/images/teacher/JQH.png",
        //   tel: "0451-86417981",
        //   email: "jqhan@hit.edu.cn",
        //   adress: "哈尔滨工业大学321信箱",
        //   link: "http://homepage.hit.edu.cn/hanjiqing"
        // },
        // {
        //   name: "韩纪庆",
        //   prof: "教授，博士生导师",
        //   desc: "简介",
        //   image: "/static/images/teacher/JQH.png",
        //   tel: "0451-86417981",
        //   email: "jqhan@hit.edu.cn",
        //   adress: "哈尔滨工业大学321信箱",
        //   link: "http://homepage.hit.edu.cn/hanjiqing"
        // },
      ],
      new_item: {
        id: 'new',
        name: "姓名",
        prof: "职称",
        desc: "简介",
        image: "",
        tel: "xxxx-xxxxxxxx",
        email: "xxx@hit.edu.cn",
        adress: "哈尔滨工业大学xxx信箱",
        link: "http://homepage.hit.edu.cn/xxx"
      },
      edit_new_item: {
        id: 'new',
        name: "",
        prof: "",
        desc: "",
        image: "",
        tel: "",
        email: "",
        adress: "",
        link: ""
      },
    }
  },
  mounted() {
    this.load_list();
  },
  computed: {
    per_page() {
      return this.$store.state.admin ? 5 : 6;
    },
    admin() {
      return this.$store.state.admin;
    }
  },
  methods: {
    change_image(e) {
      let file = e.target.files[0];
      this.upload_image = file;
      this.local = true;
      this.viewing_edit.image = file ? window.URL.createObjectURL(file) : this.viewing_edit.image;
    },
    create() {
      this.view(JSON.parse(JSON.stringify(this.edit_new_item)), true);
    },
    view(item, flag) {
      this.viewing = item;
      this.create_flag = flag;
      if (this.admin) {
        this.viewing_edit = JSON.parse(JSON.stringify(item));
        this.modal = true;
      } else {
        this.$toast.error('没有权限');
      }
    },
    edit() {
      let data = new FormData();
      data.append('type', this.type);
      data.append('filetype', 'item');
      data.append('id', this.viewing_edit.id);
      data.append('name', this.viewing_edit.name);
      data.append('prof', this.viewing_edit.prof);
      data.append('link', this.viewing_edit.link);
      data.append('tel', this.viewing_edit.tel);
      data.append('email', this.viewing_edit.email);
      data.append('adress', this.viewing_edit.adress);
      data.append('desc', this.viewing_edit.desc);
      data.append('image', this.viewing_edit.image);
      data.append('image_file', this.upload_image);
      this.post('/list/', data, data => {
        switch (data['message']) {
          case 'success': {
            this.reload_list();
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
      this.delete('/list/', {type: this.type, filetype: 'item', filename: item.id}, data => {
        switch (data['message']) {
          case 'success': {
            this.reload_list();
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
    goto_link(link) {
      window.location.href = link;
    },
    load_list() {
      this.get('/list/', {type: this.type, filetype: 'lists'}, data => {
        switch (data['message']) {
          case 'success': {
            this.items = data['content'];
            break;
          }
          case 'error': {
            break;
          }
          default: {
            this.$toast.info(data['message']);
          }
        }
      })
    },
    reload_list() {
      this.create_flag = false;
      this.local = false;
      this.load_list();
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
  top: 10%;
  bottom: 10%;
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
