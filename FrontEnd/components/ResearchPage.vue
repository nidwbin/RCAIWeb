<!--
 * @FileDescription: history page
 * @Author: liuyoude
 * @Date: 2021-10-01
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-09
 -->
<template>
  <div>
    <div class="direction-area pt-115">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="direction-item">
              <div class="item d-block d-sm-flex align-items-center" v-if="admin">
                <div class="thumb">
                  <img :src="btn_image" style="filter: brightness(98%); cursor: pointer" alt="direction"
                       @click="create">
                  <!--                <span>{{ item.year }}</span>-->
                </div>
                <div class="content">
                  <nuxt-link to="#"><span class="	fa fa-fire"></span>{{ new_item.name }}</nuxt-link>
                  <p>{{ new_item.desc }}</p>
                </div>
              </div>
              <div class="pt-2 pb-2">
                <button type="button" class="btn btn-primary btn-lg float-right" @click="create">
                  <span class="fa fa-edit"></span>&nbsp;&nbsp;新增
                </button>
              </div>
              <div class="item_footer"></div>
              <div class="card-header mt-5 mb-5">
                <div class="h2"><span class="	fa fa-codepen" style="color: #ff5316"></span>&nbsp;&nbsp;研究方向</div>
              </div>
              <div v-for="item in items">
                <div class="item d-block d-sm-flex align-items-center">
                  <div class="thumb">
                    <img :src="item.image===''?default_image:image_base+item.image" alt="">
                    <!--                <span>{{ item.year }}</span>-->
                  </div>
                  <div class="content">
                    <nuxt-link to="#"><span class="	fa fa-fire"></span>{{ item.name }}</nuxt-link>
                    <p>{{ item.desc }}</p>
                  </div>
                </div>
                <div class=" pt-2 pb-2" v-if="admin">
                  <button type="button" class="btn btn-danger btn-lg float-right" @click="remove(item)">
                    <span class="fa fa-trash-o"></span>&nbsp;&nbsp;删除
                  </button>
                  <span class="float-right">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
                  <button type="button" class="btn btn-warning btn-lg float-right" @click="view(item,false)">
                    <span class="fa fa-edit"></span>&nbsp;&nbsp;编辑
                  </button>
                </div>
                <div class="item_footer"></div>
              </div>
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
              <h4 class="modal-title">编辑研究方向</h4>
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
                  <span class="input-group-text" id="basic-addon1">方向名称</span>
                </div>
                <input type="text" class="form-control" v-model="viewing_edit.name" aria-describedby="basic-addon1">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon2">方向描述</span>
                </div>
                <textarea class="form-control" v-model="viewing_edit.desc"
                          aria-describedby="basic-addon2"></textarea>
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
    <div>
      <!--  <div v-else>-->
      <!--    <div class="direction-area pt-115">-->
      <!--    <div class="container">-->
      <!--      <div class="row">-->
      <!--        <div class="col-lg-12">-->
      <!--          <div class="direction-item">-->
      <!--            <div class="item d-block d-sm-flex align-items-center" v-for="item in items_default">-->
      <!--                <div class="thumb">-->
      <!--                  <img id="img_item" :src="item.image" alt="">-->
      <!--                  <input id="img_file" type="file" @change="changeImg(item)" style="margin-top: 4px;">-->
      <!--                </div>-->
      <!--                <form>-->
      <!--                  <div class="content">-->
      <!--                  <nuxt-link to="#">-->
      <!--                    <span class="	fa fa-fire"></span>-->
      <!--                    <div class="name_input">-->
      <!--                      <input name="direction_name" type="text" :placeholder="item.name">-->
      <!--                    </div>-->
      <!--                  </nuxt-link>-->
      <!--                  <div class="desc_input">-->
      <!--                    <p>-->
      <!--                      <textarea name="direction_desc" :placeholder="item.desc"></textarea>-->
      <!--                    </p>-->
      <!--                  </div>-->
      <!--                  <div class="but">-->
      <!--                    <span class="fa fa-send-o" id="add_1" @click="onSubmit(item)">&nbsp;提&nbsp;交</span>-->
      <!--                  </div>-->
      <!--                </div>-->
      <!--                </form>-->

      <!--            </div>-->

      <!--            <div class="item d-block d-sm-flex align-items-center" v-for="item in items">-->

      <!--                <div class="thumb">-->
      <!--                  <img :src="item.image" alt="" id="image_id">-->
      <!--                  <input type="file" @change="changeImg(item)" style="margin-top: 4px;">-->
      <!--                </div>-->
      <!--                <form>-->
      <!--                  <div class="content">-->
      <!--                  <nuxt-link to="#">-->
      <!--                    <span class="	fa fa-fire"></span>-->
      <!--                    <div class="name_input">-->
      <!--                      <input name="direction_name" type="text" :placeholder="item.name" v-model="item.name">-->
      <!--                    </div>-->
      <!--                  </nuxt-link>-->
      <!--                  <div class="desc_input">-->
      <!--                    <p>-->
      <!--                      <textarea name="direction_desc" :placeholder="item.desc" v-model="item.desc"></textarea>-->
      <!--                    </p>-->
      <!--                  </div>-->
      <!--                  <div class="but">-->
      <!--                    <span class="fa fa-send-o" id="add_2" @click="onSubmit(item)">&nbsp;提&nbsp;交</span>-->
      <!--                    <span class="fa fa-trash-o" id="del" @click="onSubmit(item)">&nbsp;删&nbsp;除</span>-->
      <!--                  </div>-->
      <!--                </div>-->
      <!--                </form>-->

      <!--            </div>-->
      <!--          </div>-->
      <!--        </div>-->
      <!--      </div>-->
      <!--    </div>-->
      <!--  </div>-->
      <!--  </div>-->
    </div>
  </div>
</template>

<script>
import Functions from "./Functions";
import PagesList from "@/components/PagesList";

export default {
  name: "ResearchPage",
  components: {PagesList},
  mixins: [Functions],
  data() {
    return {
      modal: false,
      viewing: null,
      viewing_edit: null,
      local: false,
      create_flag: false,
      upload_image: null,
      type: 'directions',
      per_page: 5,
      image_base: this.$store.state.image_base + 'fields/',
      btn_image: '/static/images/default/add.png',
      default_image: '/static/images/default/image.jpg',

      items: [],
      new_item: {id: 'new', desc: "方向相关描述", name: "方向名称", image: ""},
    }
  },
  mounted() {
    this.load_list(1);
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
