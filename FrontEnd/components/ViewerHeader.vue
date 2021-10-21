<template>
  <div>
    <div class="page-title-area bg_cover pt-120" style="background-image: url(/static/images/banner-bg-1.jpg);">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="page-title-item text-center">
              <nav aria-label="breadcrumb">
                <ol class="breadcrumb">
                  <li class="breadcrumb-item active" aria-current="page">{{ viewing.date }}</li>
                </ol>
              </nav>
              <h3 class="title">{{ viewing.title }}</h3>
              <p class="mt-40">{{ viewing.overview }}</p>
            </div>
          </div>
        </div>
      </div>
      <div class="page-shadow" @click="view">
        <img src="/static/images/page-shadow.png" alt="">
      </div>
    </div>
    <HeaderArea ref="header" :type="type" :btn_more="false" @reload_page="reload_page"/>
  </div>
</template>

<script>
import Functions from "./Functions";
import HeaderArea from "./HeaderArea"

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
      viewing: {
        title: '开始新建',
        date: 'XXXX-XX-XX',
        overview: '点击开始新建条目',
      },
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
    view() {
      this.$refs.header.view(this.viewing);
    },
    reload_page() {
      this.$router.back();
    }
  },
}
</script>

<style scoped>
.modal {
  display: block;
}
</style>
