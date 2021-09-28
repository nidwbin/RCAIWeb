<!--
 * @FileDescription: pages button list
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
 -->
<template>
  <div class="container mb-40" :hidden="hidden">
      <div class="row">
        <div class="col" ></div>
          <ul class="pagination">
            <li :class="pages.active === pages.page_list[0] ? 'page-item disabled' : 'page-item'" >
              <a class="page-link" href="#" @click="change_page(-1)"><i class="fa fa-chevron-left" ></i></a>
            </li>
            <li v-for="page in pages.page_list" :class="pages.active === page ? 'page-item active' : 'page-item'">
              <a class="page-link" href="#" @click="change_page(page)" >{{ page }}</a>
            </li>
            <li :class="pages.active === pages.page_list[pages.page_list.length-1] ? 'page-item disabled' : 'page-item'">
              <a class="page-link" href="#" @click="change_page(0)"><i class="fa fa-chevron-right"></i></a>
            </li>
          </ul>
        <div class="col"></div>
      </div>
  </div>
</template>

<script>
export default {
  name: "PagesList",
  data(){
    return {
      pages:{
        active:1,
        page_list:[1,2,3,4],
      },
    }
  },
  computed:{
    hidden(){
      return this.pages.page_list.length === 1
    }
  },
  methods:{
      change_page(page){
        if(page!==this.pages.active){
          switch (page){
            case -1:{
              this.pages.active= this.pages.active-1;
              break;
            }
            case 0:{
              this.pages.active= this.pages.active+1;
              break;
            }
            default:{
              this.pages.active=page;
            }
          }
        }
      },
    }
}
</script>

<style scoped>

</style>
