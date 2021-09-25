<!--
 * @FileDescription: list components
 * @Author: wenbin
 * @Date: 2021-09-13
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-13
 -->
<template>
  <div>
  <div class="container mt-2">
    <div>
      <div class="card mt-2 mb-2" v-for="item in items">
        <h4 class="card-header">{{ item.title }}</h4>
        <div class="card-body">
          <h6 class="card-subtitle mb-2 text-muted">
            <i class="fa fa-clock-o"></i>:{{ item.date }}
          </h6>
          <div class="ml-1 mr-1 mt-1 mb-1">
            <p class="card-text">{{ item.overview }}</p>
          </div>
          <div class="text-right">
            <button type="button" class="btn btn-outline-success" :id="'view-'+item.file"><i class="fa fa-reply"></i> 查看</button>
            <button type="button" class="btn btn-outline-warning" :id="'edit-'+item.file" :hidden="!is_admin"><i class="fa fa-pencil"></i> 编辑</button>
            <button type="button" class="btn btn-outline-danger" :id="'del-'+item.file" :hidden="!is_admin"><i class="fa fa-remove"></i> 删除</button>
          </div>
        </div>
      </div>
    </div>
  </div>
    <div class="container">
      <div class="row">
        <div class="col"></div>
          <ul class="pagination">
            <li :class="pages.active === pages.page_list[0] ? 'page-item disabled' : 'page-item'">
              <a class="page-link" href="#" @click="changePage(-1)"><i class="fa fa-chevron-left" ></i></a>
            </li>
            <li v-for="page in pages.page_list" :class="pages.active === page ? 'page-item active' : 'page-item'" >
              <a class="page-link" href="#" @click="changePage(page)">{{ page }}</a>
            </li>
            <li :class="pages.active === pages.page_list[pages.page_list.length-1] ? 'page-item disabled' : 'page-item'">
              <a class="page-link" href="#" @click="changePage(0)"><i class="fa fa-chevron-right"></i></a>
            </li>
          </ul>
        <div class="col"></div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name:"List",
    data(){
      return{
        items:[
          {title:"1",date:"2021/9/10",overview:"something",file:"1",},
          {title:"2",date:"2021/9/10",overview:"something",file:"2"},
          {title:"3",date:"2021/9/10",overview:"something",file:"3"},
        ],
        pages:{
          active:1,
          page_list:[1,2,3,4],
        },
      }
    },
    computed:{
      is_admin(){
        return this.$store.state.is_admin;
      },
      location(){
        return this.$store.state.location;
      }
    },
    methods:{
      changePage(page){
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
      a(){

      }
    }
  }
</script>
