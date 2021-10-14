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
                <img src="/images/add-button.png" alt="">
              </div>
              <nuxt-link :to="{name:'view', query:{type:type, filename:'new'}}">
                <div class="comment-one__content">
                  <h3>
                    新建条目
                    <span class="comment-one__date">****/**/**</span>
                  </h3>
                  <p>点击开始新建条目</p>
                </div><!-- /.comment-one__content -->
              </nuxt-link>
            </div><!-- /.comment-one__single -->
          </div><!-- /.comment-one -->
            <div class="comment-one__single" v-for="item in lists">
              <div class="comment-one__image">
                <img :src="item.image" alt="">
              </div><!-- /.comment-one__image -->
              <nuxt-link :to="{name:'view', query:{type:type, filename:item.filename}}">
                <div class="comment-one__content">
                  <h3>
                    {{ item.title }}
                    <span class="comment-one__date">{{ item.date }}</span>
                  </h3>
                  <p>{{ item.overview }}</p>
                </div><!-- /.comment-one__content -->
              </nuxt-link>
              <!--              <div class="blog-btn">-->
              <!--                <a href="#" class="main-btn text-center">Reply</a>-->
              <!--              </div>-->
              <!-- /.thm-btn comment-one__btn -->
            </div><!-- /.comment-one__single -->
          </div><!-- /.comment-one -->

        </div><!-- /.col-lg-8 -->
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
                    <div class="inner-block"><img :src="item.image" alt=""></div>
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
    <PagesList :type="type" @change_page="change_page"/>
  </section>
</template>

<script>
import PagesList from "./PagesList";
import Functions from "./Functions";

export default {
  name: "NewsList",
  mixins: [Functions],
  components: {PagesList},
  data() {
    return {
      type: 'news',
      lists: [],
      hots: [],
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
      this.get('/list/', {type: this.type, filetype: 'lists', filename: this.admin, content: page},
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
      this.get('/list/', {type: this.type, filetype: 'hots', filename: this.admin, content: len},
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
    }
  }
}
</script>

<style scoped>

</style>
