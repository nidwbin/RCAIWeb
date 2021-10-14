<template>
  <div class="page-title-area bg_cover pt-120" style="background-image: url(/images/banner-bg-1.jpg);">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="page-title-item text-center">
            <nav aria-label="breadcrumb">
              <input :placeholder="date" v-if="admin">
              <ol class="breadcrumb" v-else>
                <li class="breadcrumb-item active" aria-current="page">{{ date }}</li>
              </ol>
            </nav>
            <h3 class="title">{{ title }}</h3>
            <p class="mt-40">{{ overview }}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="page-shadow">
      <img src="/images/page-shadow.png" alt="">
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
      title: '开始新建',
      date: '****/**/**',
      overview: '点击开始新建条目',
    }
  },
  mounted() {
    this.get('/list/', {type: this.type, filetype: 'item', filename: this.filetype, content: ''}, data => {
      switch (data['message']) {
        case 'success': {
          this.title = data['content']['title'];
          this.date = data['content']['date'];
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
    }
  }
}
</script>

<style scoped>

</style>
