<!--
 * @FileDescription: team page
 * @Author: liuyoude,wenbin
 * @Date: 2021-09-28
 * @LastEditors: liuyoude,wenbin
 * @LastEditTime: 2021-09-28
 -->
<template>
  <section class="leadership-area about-leadership team-leadership">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-4 col-md-6 col-sm-9" v-if="admin">
          <div class="leadership-item mt-30">
            <div class="leadership-thumb" style="filter: brightness(98%); cursor: pointer">
              <img :src=" btn_image " alt="doctors" @click="create">
            </div>
            <div class="leadership-content text-center">
              <h4>{{ new_item.name }}</h4>
              <span>{{ new_item.class }}</span>
              <p style="min-height: 102px!important;">{{ new_item.abstract }}</p>
            </div>
            <div class="mt-2" style="text-align: center">
              <button type="button" class="btn btn-primary" @click="create">
                <span class="fa fa-edit"></span>&nbsp;&nbsp;新增
              </button>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-md-6 col-sm-9" v-for="item in items">
          <div class="leadership-item mt-30">
            <div class="leadership-thumb">
              <img :src=" item.image===''?default_image:image_base+item.image" alt="doctors">
              <div class="social">
                <a href="#"><i class="fa fa-plus"></i></a>
                <ul>
                  <li><a :href="'mailto:'+item.email"><i class="fa fa-at"></i></a></li>
                  <li><a href="#"><i @click="goto_link(item.link)" class="fa fa-vcard-o"></i></a></li>
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
              <button type="button" class="btn btn-warning" @click="view(item,false)">
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
                  <span class="input-group-text" id="basic-addon2">邮件</span>
                </div>
                <input type="email" class="form-control" v-model="viewing_edit.email" aria-describedby="basic-addon2">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon3">主页</span>
                </div>
                <input type="text" class="form-control" v-model="viewing_edit.link" aria-describedby="basic-addon3">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon4">年级</span>
                </div>
                <select class="form-control" id="sel1">
                  <option>{{ viewing_edit.class }}</option>
                  <option v-for="class_item in classes" v-if="class_item !== viewing_edit.class">
                    {{ class_item }}
                  </option>
                </select>
                <!--                <input type="text" class="form-control" v-model="viewing_edit.class" aria-describedby="basic-addon2">-->
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon5">简介</span>
                </div>
                <textarea class="form-control" v-model="viewing_edit.abstract"
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
  name: "TeamPage",
  components: {PagesList},
  mixins: [Functions],
  props: {
    type: {
      type: String,
      default: '',
    }
  },
  mounted() {
    this.load_list(1);
  },
  data() {
    return {
      modal: false,
      viewing: null,
      viewing_edit: null,
      local: false,
      create_flag: false,
      upload_image: null,
      image_base: this.$store.state.image_base + 'people/',
      btn_image: '/static/images/default/add.png',
      default_image: '/static/images/default/image.jpg',
      items: [],
      new_item: {
        id: 'new',
        name: "姓名",
        image: '',
        class: this.type === "doctor" ? "博一" : "研一",
        email: "example@exa.com",
        link: "#",
        abstract: "描述",
      },
      classes: this.type === "doctor" ? ['博一', '博二', '博三', '博四', '博五'] : ['研一', '研二', '研三'],
    }
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
      this.view(JSON.parse(JSON.stringify(this.new_item)), true);
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
      data.append('email', this.viewing_edit.email);
      data.append('link', this.viewing_edit.link);
      data.append('class', this.viewing_edit.class);
      data.append('abstract', this.viewing_edit.abstract);
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
      // window.open(link, "_blank");
    },
    load_list(page) {
      this.get('/list/', {type: this.type, filetype: 'lists', page: page, per_page: this.per_page}, data => {
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
      this.$refs.page.reload();
    },
  }

}
</script>

<style scoped>
.modal {
  display: block;
  z-index: 2001;
}
</style>
