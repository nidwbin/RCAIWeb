<template>
  <div>
    <div class="page-title-area bg_cover pt-120" style="background-image: url(/static/images/banner-bg-1.jpg);">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="page-title-item text-center" @click="view">
              <nav aria-label="breadcrumb">
                <ol class="breadcrumb">
                  <li class="breadcrumb-item active" aria-current="page">{{ viewing.date }}</li>
                </ol>
              </nav>
              <h3 class="title">{{ viewing.title }}</h3>
              <p class="mt-40" style="color: whitesmoke!important;">{{ viewing.overview }}</p>
              <button type="button" class="btn btn-primary btn-lg mt-40 card-text" v-show="admin">
                <span class="fa fa-edit"></span>&nbsp;&nbsp;&nbsp;&nbsp;编&nbsp;辑&nbsp;标&nbsp;题
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="page-shadow" @click="view">
        <img src="/static/images/page-shadow.png" alt="">
      </div>
    </div>
    <HeaderArea ref="header" :type="type" :btn_more="false" @deleted="back" @saved="saved"/>
  </div>
</template>

<script>
import Functions from "./Functions";
import HeaderArea from "./HeaderArea"
import {bus} from "@/plugins/bus";

export default {
  name: "ViewerHeader",
  components: {HeaderArea},
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
      viewing: {},
    }
  },
  mounted() {
    this.get('/list/', {type: this.type, filetype: 'item', filename: this.filename}, data => {
      switch (data['message']) {
        case 'success': {
          this.viewing = data['content'];
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
    this.listen_events();
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
    listen_events() {
      bus.$on('delete', () => {
        this.view();
      });
      bus.$on('finish', () => {
        this.viewing.show=true;
        this.$refs.header.view(this.viewing, false);
        this.$refs.header.edit();
        this.back();
      });
    },
    stop_listen() {
      bus.$off(['delete', 'send']);
    },
    saved() {
      bus.$emit('save');
    },
    view() {
      this.$refs.header.view(this.viewing);
    },
    back() {
      this.$router.back();
    }
  },
  destroyed() {
    this.stop_listen();
  },
}
</script>

<style scoped>
.modal {
  display: block;
}
</style>
