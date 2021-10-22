<template>
  <div v-if="modal">
    <div class="modal" v-on:click.self="modal=false">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title">修改标题头</h4>
            <button type="button" class="close" @click="modal=false">×</button>
          </div>
          <div class="modal-body">
            <div class="card mb-1">
              <img :src="(local?'':image_base)+viewing_edit.image" class="card-img-top" alt="">
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
                <span class="input-group-text" id="basic-addon1">日期</span>
              </div>
              <input type="date" class="form-control" v-model="viewing_edit.date" aria-describedby="basic-addon1">
            </div>
            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text" id="basic-addon2">标题</span>
              </div>
              <input type="text" class="form-control" v-model="viewing_edit.title" aria-describedby="basic-addon2">
            </div>
            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text" id="basic-addon3">概述</span>
              </div>
              <textarea class="form-control" v-model="viewing_edit.overview"
                        aria-describedby="basic-addon3"></textarea>
            </div>
          </div>
          <div class="modal-footer">
            <div class="custom-control custom-switch">
              <input type="checkbox" class="custom-control-input" id="switch" v-model="viewing_edit.show">
              <label class="custom-control-label" for="switch">展示</label>
            </div>
            <button type="button" class="btn btn-success" @click="more" v-if="btn_more"><i
              class="fa fa-fighter-jet"></i>查看
            </button>
            <button type="button" class="btn btn-warning" @click="edit"><i class="fa fa-send"></i>修改</button>
            <button type="button" class="btn btn-danger" @click="remove"><i class="fa fa-remove"></i>删除</button>
          </div>
        </div>
      </div>
    </div>
    <div class="modal-backdrop show" style="z-index: 2000"></div>
  </div>
</template>

<script>
import Functions from "./Functions";

export default {
  name: "HeaderArea",
  mixins: [Functions],
  props: {
    type: {
      type: String,
      default: '',
    },
    btn_more: {
      type: Boolean,
      default: false,
    }
  },
  data() {
    return {
      modal: false,
      local: false,
      viewing: null,
      viewing_edit: null,
      upload_image: null,
      image_base: this.$store.state.image_base + 'header/',
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
        this.$router.push({name: 'view', query: {type: this.type, filename: this.viewing.filename}});
      }
    },
    more() {
      this.$router.push({name: 'view', query: {type: this.type, filename: this.viewing.filename}});
    },
    remove() {
      this.delete('/list/', {type: this.type, filetype: 'item', filename: this.viewing_edit.filename}, data => {
        switch (data['message']) {
          case 'success': {
            this.$emit('reload_page');
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
    edit() {
      let data = new FormData();
      data.append('type', this.type);
      data.append('filetype', 'item');
      data.append('filename', this.viewing_edit.filename);
      data.append('date', this.viewing_edit.date);
      data.append('show', this.viewing_edit.show);
      data.append('title', this.viewing_edit.title);
      data.append('overview', this.viewing_edit.overview);
      data.append('image', this.upload_image);
      this.post('/list/', data, data => {
        switch (data['message']) {
          case 'success': {
            this.viewing.filename = this.viewing_edit.filename;
            this.viewing.date = this.viewing_edit.date;
            this.viewing.show = this.viewing_edit.show;
            this.viewing.title = this.viewing_edit.title;
            this.viewing.overview = this.viewing_edit.overview;
            this.local = false;
            this.viewing.image = data['content'];
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
  }
}
</script>

<style scoped>
.modal {
  z-index: 2001;
  display: block;
}
</style>
