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
          <div class="news_new_area">
            <div class="new_add mb-4 border-bottom" v-show="admin">
              <img :src="btn_image" alt="" class="img_filter" @click="new_item" width="100%">
              <div class="footer">
                发布新闻
              </div>
            </div>
          </div>
          <div class="card-header mb-3">
            <div class="h2"><span class="	fa fa-newspaper-o" style="color: #ff5316;">&nbsp;&nbsp;</span>新闻</div>
          </div>
          <div v-for="item in lists" v-show="item.show || admin">
            <div class="comment-one__single">
              <div class="comment-one__image">
                <img :src="item.image===''?default_image:image_base+item.image" alt="">
              </div>
              <nuxt-link :to="{name:'view', query:{type:type, filename:item.filename}}">
                <div class="comment-one__content">
                  <h3>
                    {{ item.title }}
                    <span :class="item.show?'comment-one__date':'comment-one__date text-muted'">{{ item.date }}</span>
                  </h3>
                  <p style="line-height: 22px;">{{ item.overview }}</p>
                </div>
              </nuxt-link>
            </div>
            <div class="pb-5 pt-1" v-show="admin">
              <button type="button" class="btn btn-danger float-right" @click="remove(item)">
                <span class="fa fa-trash-o"></span>&nbsp;&nbsp;删除
              </button>
              <span class="float-right">&nbsp;</span>
              <button type="button" class="btn btn-warning float-right" @click="view(item)">
                <span class="fa fa-edit"></span>&nbsp;&nbsp;编辑
              </button>
              <span class="float-right">&nbsp;</span>
              <button type="button" class="btn btn-primary float-right display-1" @click="more(item)">
                <span class="fa fa-eye"></span>&nbsp;&nbsp;查看
              </button>
            </div>
            <div class="comment-one__footer">

            </div>
          </div>
        </div>
        <div class="col-lg-4">
          <div class="sidebar">
            <div class="new_add mb-4 text-center border-bottom" v-show="admin">
              <img :src="btn_image" alt="" @click="new_item" class="img_filter" width="100%">
              <div class="footer">
                发布新闻
              </div>
            </div>
            <div class="sidebar__single sidebar__search">
              <form action="#" class="sidebar__search-form">
                <input type="text" name="search" placeholder="开始搜索...">
                <button type="submit"><i class="fa fa-search"></i></button>
              </form>
            </div>
            <div class="sidebar__single sidebar__post">
              <h3 class="sidebar__title">近期新闻</h3>
              <div class="sidebar__post-wrap">
                <div class="sidebar__post__single" v-for="item in hots">
                  <div class="sidebar__post-image">
                    <div class="inner-block"><img :src="item.image===''?default_image:image_base+item.image" alt="">
                    </div>
                  </div>
                  <nuxt-link :to="{name:'view', query:{type:type, filename:item.filename}}">
                    <div class="sidebar__post-content">
                      <span>{{ item.date }}</span>
                      <h4 class="sidebar__post-title"><a href="/single-post">{{ item.title }}</a></h4>
                    </div>
                  </nuxt-link>
                </div>
              </div>
            </div>
<!--            <div class="sidebar__single sidebar__category">-->
<!--              <h3 class="sidebar__title">Categories</h3>&lt;!&ndash; /.sidebar__title &ndash;&gt;-->
<!--              <ul class="sidebar__category-list">-->
<!--                <li class="sidebar__category-list-item"><a href="#">Business</a></li>-->
<!--                <li class="sidebar__category-list-item"><a href="#">Introductions</a></li>-->
<!--                <li class="sidebar__category-list-item"><a href="#">One Page Template</a></li>-->
<!--                <li class="sidebar__category-list-item"><a href="#">Parallax Effects</a></li>-->
<!--                <li class="sidebar__category-list-item"><a href="#">New Technologies</a></li>-->
<!--                <li class="sidebar__category-list-item"><a href="#">Video Backgrounds</a></li>-->
<!--              </ul>&lt;!&ndash; /.sidebar__category-list &ndash;&gt;-->
<!--            </div>-->
<!--            <div class="sidebar__single sidebar__tags">-->
<!--              <h3 class="sidebar__title">Tags</h3>&lt;!&ndash; /.sidebar__title &ndash;&gt;-->
<!--              <ul class="sidebar__tags-list">-->
<!--                <li class="sidebar__tags-list-item"><a href="#">Construction,</a></li>-->
<!--                <li class="sidebar__tags-list-item"><a href="#">Build,</a></li>-->
<!--                <li class="sidebar__tags-list-item"><a href="#">Factory.</a></li>-->
<!--                <li class="sidebar__tags-list-item"><a href="#">Engineering.</a></li>-->
<!--                <li class="sidebar__tags-list-item"><a href="#">Repairing,</a></li>-->
<!--                <li class="sidebar__tags-list-item"><a href="#">Industry,</a></li>-->
<!--                <li class="sidebar__tags-list-item"><a href="#">Materials,</a></li>-->
<!--                <li class="sidebar__tags-list-item"><a href="#">Mechanical,</a></li>-->
<!--                <li class="sidebar__tags-list-item"><a href="#">Buildings,</a></li>-->
<!--              </ul>&lt;!&ndash; /.sidebar__category-list &ndash;&gt;-->
<!--            </div>-->
          </div>
        </div>
      </div>
    </div>
    <HeaderArea ref="header" :type="type" :btn_more="true"/>
    <PagesList ref="page" :type="type" :per_page="per_page" @change_page="load_list"/>
  </section>
</template>

<script>
import PagesList from "./PagesList";
import Functions from "./Functions";
import HeaderArea from "./HeaderArea";
import {bus} from "@/plugins/bus";

export default {
  name: "NewsPage",
  mixins: [Functions],
  components: {PagesList, HeaderArea},
  data() {
    return {
      type: 'news',
      lists: [],
      hots: [],
      per_page: 10,
      image_base: this.$store.state.image_base + 'header/',
      btn_image: '/static/images/default/add.png',
      default_image: '/static/images/default/image.jpg',
    }
  },
  mounted() {
    this.load_list(1);
    this.load_hots(5);
    this.listen_events();
  },
  computed: {
    admin() {
      return this.$store.state.admin;
    }
  },
  methods: {
    listen_events() {
      bus.$on('reload_list', () => {
        this.$refs.page.reload();
      });
      bus.$on('reload_hots', () => {
        this.load_hots(5);
      });
    },
    stop_listen() {
      bus.$off(['reload_list', 'reload_hots']);
    },
    more(item) {
      this.$router.push({name: 'view', query: {type: this.type, filename: item.filename}});
    },
    remove(item) {
      this.$refs.header.remove(item);
    },
    view(item) {
      this.$refs.header.view(item);
    },
    load_list(page) {
      this.get('/list/', {type: this.type, filetype: 'lists', admin: this.admin, page: page, per_page: this.per_page},
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
    load_hots(len) {
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
  },
  destroyed() {
    this.stop_listen();
  }
}
</script>

<style scoped>
.img_filter {
  filter: brightness(98%)
}
</style>
