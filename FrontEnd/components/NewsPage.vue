<!--
 * @FileDescription: news page
 * @Author: liuyoude
 * @Date: 2021-09-29
 * @LastEditors: liuyoude,wenbin
 * @LastEditTime: 2021-10-13
 -->
<template>
  <section class="blog-details">
    <div class="container">
      <div class="row">
        <div class="col-lg-8">
          <div class="comment-one">
            <div class="comment-one__single" v-if="admin">
              <div class="comment-one__image">
              </div>
              <div class="comment-one__content" @click="new_item">
                <h3>
                  新建条目
                  <span class="comment-one__date">XXXX-XX-XX</span>
                </h3>
                <p>点击开始新建条目</p>
              </div><!-- /.comment-one__content -->
            </div><!-- /.comment-one__single -->
          </div><!-- /.comment-one -->
          <div class="comment-one__single" v-for="item in lists" v-if="item.show || admin">
            <div class="comment-one__image">
              <img :src="image_base+item.image" alt="">
            </div><!-- /.comment-one__image -->
            <div class="comment-one__content" @click="view(item)">
              <h3>
                {{ item.title }}
                <span :class="item.show?'comment-one__date':'comment-one__date text-muted'">{{ item.date }}</span>
              </h3>
              <p>{{ item.overview }}</p>
            </div><!-- /.comment-one__content -->
            <!--              <div class="blog-btn">-->
            <!--                <a href="#" class="main-btn text-center">Reply</a>-->
            <!--              </div>-->
            <!-- /.thm-btn comment-one__btn -->
          </div><!-- /.comment-one__single -->
        </div><!-- /.comment-one -->
        <div class="col-lg-4">
          <div class="sidebar">
            <div class="sidebar__single sidebar__search">
              <form action="#" class="sidebar__search-form">
                <input type="text" name="search" placeholder="开始搜索...">
                <button type="submit"><i class="fa fa-search"></i></button>
              </form>
            </div><!-- /.sidebar__single -->
            <div class="sidebar__single sidebar__post">
              <h3 class="sidebar__title">近期新闻</h3><!-- /.sidebar__title -->
              <div class="sidebar__post-wrap">
                <div class="sidebar__post__single" v-for="item in hots">
                  <div class="sidebar__post-image">
                    <div class="inner-block"><img :src="image_base+item.image" alt=""></div>
                    <!-- /.inner-block -->
                  </div><!-- /.sidebar__post-image -->
                  <nuxt-link :to="{name:'view', query:{type:type, filename:item.filename}}">
                    <div class="sidebar__post-content">
                      <span>{{ item.date }}</span>
                      <h4 class="sidebar__post-title"><a href="/single-post">{{ item.title }}</a></h4>
                      <!-- /.sidebar__post-title -->
                    </div><!-- /.sidebar__post-content -->
                  </nuxt-link>
                </div><!-- /.sidebar__post__single -->
              </div><!-- /.sidebar__post-wrap -->
            </div><!-- /.sidebar__single -->
            <div class="sidebar__single sidebar__category">
              <h3 class="sidebar__title">Categories</h3><!-- /.sidebar__title -->
              <ul class="sidebar__category-list">
                <li class="sidebar__category-list-item"><a href="#">Business</a></li>
                <li class="sidebar__category-list-item"><a href="#">Introductions</a></li>
                <li class="sidebar__category-list-item"><a href="#">One Page Template</a></li>
                <li class="sidebar__category-list-item"><a href="#">Parallax Effects</a></li>
                <li class="sidebar__category-list-item"><a href="#">New Technologies</a></li>
                <li class="sidebar__category-list-item"><a href="#">Video Backgrounds</a></li>
              </ul><!-- /.sidebar__category-list -->
            </div><!-- /.sidebar__single -->
            <div class="sidebar__single sidebar__tags">
              <h3 class="sidebar__title">Tags</h3><!-- /.sidebar__title -->
              <ul class="sidebar__tags-list">
                <li class="sidebar__tags-list-item"><a href="#">Construction,</a></li>
                <li class="sidebar__tags-list-item"><a href="#">Build,</a></li>
                <li class="sidebar__tags-list-item"><a href="#">Factory.</a></li>
                <li class="sidebar__tags-list-item"><a href="#">Engineering.</a></li>
                <li class="sidebar__tags-list-item"><a href="#">Repairing,</a></li>
                <li class="sidebar__tags-list-item"><a href="#">Industry,</a></li>
                <li class="sidebar__tags-list-item"><a href="#">Materials,</a></li>
                <li class="sidebar__tags-list-item"><a href="#">Mechanical,</a></li>
                <li class="sidebar__tags-list-item"><a href="#">Buildings,</a></li>
              </ul><!-- /.sidebar__category-list -->
            </div><!-- /.sidebar__single -->
          </div><!-- /.sidebar -->
        </div><!-- /.col-lg-4 -->
      </div><!-- /.row -->
    </div><!-- /.container -->
<<<<<<< HEAD
    <div v-if="modal">
      <div class="modal" v-on:click.self="modal=false">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">编辑</h4>
              <button type="button" class="close" @click="modal=false">×</button>
            </div>
            <div class="modal-body">
<!--              <div class="input-group mb-3" style="height: 100px;">-->
<!--                <div class="input-group-prepend">-->
<!--                  <span class="input-group-text" id="basic-addon0">封面图片</span>-->
<!--                </div>-->
<!--                <div class="custom-file">-->
<!--                  <input type="file" class="custom-file-input" id="inputGroupFile01" aria-describedby="inputGroupFileAddon01">-->
<!--                  <label class="custom-file-label" for="inputGroupFile01">-->
<!--                      <div class="card" style="width: 100%; margin-top:30px;">-->
<!--                        <img :src="viewing_edit.image" class="card-img">-->
<!--                      </div>-->
<!--                  </label>-->
<!--                </div>-->
<!--              </div>-->
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
                <textarea class="form-control" v-model="viewing_edit.overview" aria-describedby="basic-addon3"></textarea>
              </div>
            </div>
            <div class="modal-footer">
              <div class="custom-control custom-switch">
                <input type="checkbox" class="custom-control-input" id="switch" v-model="viewing_edit.show">
                <label class="custom-control-label" for="switch">展示</label>
              </div>
              <button type="button" class="btn btn-success" @click="more"><i class="fa fa-fighter-jet"></i>查看</button>
              <button type="button" class="btn btn-warning" @click="edit"><i class="fa fa-send"></i>修改</button>
              <button type="button" class="btn btn-danger" @click="remove"><i class="fa fa-remove"></i>删除</button>
            </div>
          </div>
        </div>
      </div>
      <div class="modal-backdrop show"></div>
    </div>
    <PagesList :type="type" @change_page="change_page"/>
=======
    <HeaderArea ref="header" :type="type" :btn_more="true" @reload_page="reload_page"/>
    <PagesList ref="page" :type="type" @change_page="change_page"/>
>>>>>>> dev
  </section>
</template>

<script>
import PagesList from "./PagesList";
import Functions from "./Functions";
import HeaderArea from "./HeaderArea";

export default {
  name: "NewsList",
  mixins: [Functions],
  components: {PagesList, HeaderArea},
  data() {
    return {
      type: 'news',
      lists: [],
      hots: [],
      image_base: this.$store.state.image_base + 'header/'
    }
  },
  mounted() {
    this.change_page(1);
    this.hot_list(5);
  },
  computed: {
    admin() {
      return this.$store.state.admin;
    }
  },
  methods: {
    change_page(page) {
      this.get('/list/', {type: this.type, filetype: 'lists', admin: this.admin, page: page},
        data => {
          switch (data['message']) {
            case 'success': {
              this.lists = data['content'];
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
    hot_list(len) {
      this.get('/list/', {type: this.type, filetype: 'hots', len: len},
        data => {
          switch (data['message']) {
            case 'success': {
              this.hots = data['content'];
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
    new_item() {
      this.post('/list/', {type: this.type, filetype: 'item', filename: 'new'}, data => {
        switch (data['message']) {
          case 'success': {
            this.$router.push({name: 'view', query: {type: this.type, filename: data['content']}});
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
    view(item) {
      this.$refs.header.view(item);
    },
    reload_page() {
      this.$refs.page.$change_page(-2);
    }
  }
}
</script>

<style scoped>

</style>
