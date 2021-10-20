<!--
 * @FileDescription: pages button list
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
 -->
<template>
  <div class="container mt-4 mb-4" v-if="!hidden">
    <div class="row">
      <div class="col"></div>
      <ul class="pagination">
        <li :class="pages.active === pages.page_list[0] ? 'page-item disabled' : 'page-item'">
          <a class="page-link" href="#" @click="$change_page(-1)"><i class="fa fa-chevron-left"></i></a>
        </li>
        <li v-for="page in pages.page_list" :class="pages.active === page ? 'page-item active' : 'page-item'">
          <a class="page-link" href="#" @click="$change_page(page)">{{ page }}</a>
        </li>
        <li :class="pages.active === pages.page_list[pages.page_list.length-1] ? 'page-item disabled' : 'page-item'">
          <a class="page-link" href="#" @click="$change_page(0)"><i class="fa fa-chevron-right"></i></a>
        </li>
      </ul>
      <div class="col"></div>
    </div>
  </div>
</template>

<script>
import Functions from "./Functions";

export default {
  name: "PagesList",
  mixins: [Functions],
  props: {
    type: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      pages: {
        active: 1,
        page_list: [1],
      },
    }
  },
  computed: {
    admin() {
      return this.$store.state.admin;
    },
    hidden() {
      return this.pages.page_list.length === 1
    }
  },
  mounted() {
    this.get('/list/', {type: this.type, filetype: 'pages', admin: this.admin, per_page: 10},
      data => {
        switch (data['message']) {
          case 'success': {
            let array = [];
            for (let i = 1; i <= data['content']; ++i) {
              array.push(i);
            }
            this.pages.page_list = array;
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
  methods: {
    $change_page(page) {
      if (page !== this.pages.active) {
        switch (page) {
          case -1: {
            this.pages.active = this.pages.active - 1;
            break;
          }
          case 0: {
            this.pages.active = this.pages.active + 1;
            break;
          }
          default: {
            this.pages.active = page;
          }
        }
        this.$emit('change_page', this.pages.active);
      }
    },
  }
}
</script>

<style scoped>

</style>
