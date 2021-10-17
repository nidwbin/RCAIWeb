<template>
  <div class="page-title-area bg_cover pt-120" style="background-image: url(/static/images/banner-bg-1.jpg);">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="page-title-item text-center">
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page">{{ date }}</li>
              </ol>
            </nav>
            <h3 class="title">{{ title }}</h3>
            <p class="mt-40">{{ overview }}</p>
          </div>
        </div>
      </div>
    </div>
    <div v-if="modal">
      <div class="modal" v-on:click.self="modal=false">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">修改标题头</h4>
              <button type="button" class="close" v-on:click="modal=false">×</button>
            </div>
            <div class="modal-body">
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon1">日期</span>
                </div>
                <input type="date" class="form-control" v-model="date" aria-describedby="basic-addon1">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon2">标题</span>
                </div>
                <input type="text" class="form-control" v-model="title" aria-describedby="basic-addon2">
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon3">概述</span>
                </div>
                <textarea class="form-control" v-model="overview" aria-describedby="basic-addon3"></textarea>
              </div>
            </div>
            <div class="modal-footer">
              <div class="custom-control custom-switch">
                <input type="checkbox" class="custom-control-input" id="switch" v-model="show">
                <label class="custom-control-label" for="switch">展示</label>
              </div>
              <button type="button" class="btn btn-warning" @click="edit"><i class="fa fa-send"></i>修改</button>
              <button type="button" class="btn btn-danger" @click="remove"><i class="fa fa-remove"></i>删除</button>
            </div>
          </div>
        </div>
      </div>
      <div class="modal-backdrop show"></div>
    </div>
    <div class="page-shadow" @click="show_modal">
      <img src="/static/images/page-shadow.png" alt="">
    </div>
  </div>
</template>

<script>
import Functions from "./Functions";

export default {
  name: "ViewerHeader",
  mixins: [Functions],
  props: {
    type: {
      type: String,
      default: '',
    },
    filename: {
      type: String,
      default: '',
    }
  },
  data() {
    return {
      modal: false,
      title: '开始新建',
      date: 'XXXX-XX-XX',
      show: false,
      overview: '点击开始新建条目',
    }
  },
  mounted() {
    this.get('/list/', {type: this.type, filetype: 'item', filename: this.filetype, content: ''}, data => {
      switch (data['message']) {
        case 'success': {
          this.title = data['content']['title'];
          this.date = data['content']['date'];
          this.show = date['content']['show'];
          this.overview = date['content']['overview'];
          break;
        }
        case 'error': {
          break;
        }
        default: {
          this.$toast.info(data['message']);
        }
      }
    });
  },
  computed: {
    admin() {
      return this.$store.state.admin;
    },
    debug() {
      return this.$store.state.debug;
    }
  },
  methods: {
    show_modal() {
      if (this.admin) {
        this.modal = true;
      }
    },
    debug_show() {
      if (this.debug) {
        console.log(this.date);
        console.log(this.title);
        console.log(this.show);
        console.log(this.overview);
      }
    },
    edit() {
      this.debug_show();
      this.modal = false;
    },
    remove() {
      this.debug_show();
      this.modal = false;
    }
  },
}
</script>

<style scoped>
.modal {
  display: block;
}
</style>
