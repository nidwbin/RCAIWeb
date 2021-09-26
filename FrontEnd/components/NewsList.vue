<!--
 * @FileDescription: news page list
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-25
 -->
<template>
    <section class="industri-services-area services-page">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-4 col-md-6 col-sm-9" v-for="item in items">
            <div class="services-item mt-30">
              <div class="services-thumb">
                <img :src="item.image" alt="news">
              </div>
              <div class="services-content">
                <h1 class="title">{{ item.title }}</h1>
                <p>{{ item.date }}</p>
                <p>{{ item.overview }}</p>
                <nuxt-link :to="url_view_new" @click="view(item.file)">查看</nuxt-link>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="container mt-4" :hidden="pages.hidden">
      <div class="row">
        <div class="col"></div>
          <ul class="pagination">
            <li :class="pages.active === pages.page_list[0] ? 'page-item disabled' : 'page-item'">
              <a class="page-link" href="#" @click="change_page(-1)"><i class="fa fa-chevron-left" ></i></a>
            </li>
            <li v-for="page in pages.page_list" :class="pages.active === page ? 'page-item active' : 'page-item'" >
              <a class="page-link" href="#" @click="change_page(page)">{{ page }}</a>
            </li>
            <li :class="pages.active === pages.page_list[pages.page_list.length-1] ? 'page-item disabled' : 'page-item'">
              <a class="page-link" href="#" @click="change_page(0)"><i class="fa fa-chevron-right"></i></a>
            </li>
          </ul>
        <div class="col"></div>
      </div>
    </div>
    </section>
</template>

<script>
  export default {
    name:"NewsList",
    data(){
      return{
        url_view_new:"/view",

        items:[
          {title:"这是一条新闻",image:"/images/logo.png",date:"2021/9/10",overview:"something",file:"1",},
          {title:"这是一条新闻",image:"/images/logo.png",date:"2021/9/10",overview:"something",file:"2"},
          {title:"这是一条新闻",image:"/images/logo.png",date:"2021/9/10",overview:"something",file:"3"},
        ],
        pages:{
          active:1,
          hidden:false,
          page_list:[1,2,3,4],
        },
      }
    },
    computed:{
      is_admin(){
        return this.$store.state.authority.is_admin;
      },
      location(){
        return this.$store.state.com_sync.location;
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
      view(file){
        this.$store.commit("set_message","news-"+file);
      },
    }
  }
</script>

<style scoped>

</style>
