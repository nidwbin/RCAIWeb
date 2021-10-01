<!--
 * @FileDescription: news page
 * @Author: liuyoude
 * @Date: 2021-09-29
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-01
 -->
<template>
  <section class="blog-details">
    <div class="container">
      <div class="row">
        <div class="col-lg-8">
          <div class="comment-one">
            <div class="comment-one__single" v-for="item in items">
<!--              <div class="comment-one__image">-->
<!--                <img src="/assets/images/comment-1-1.jpg" alt="">-->
<!--              </div>&lt;!&ndash; /.comment-one__image &ndash;&gt;-->
              <nuxt-link :to="{name:'view', query:{type:type, filename:item.filename}}">
                <div class="comment-one__content">
                    <h3>
                      {{ item.title }}
                      <span class="comment-one__date">{{ item.date }}</span>
                    </h3>
                    <p>Lorem ipsum is simply free text used by copytyping refreshing. Neque porro est qui dolorem ipsum quia quaed inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.</p>
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
                <input type="text" name="search" placeholder="Search here...">
                <button type="submit"><i class="fa fa-search"></i></button>
              </form>
            </div><!-- /.sidebar__single -->
            <div class="sidebar__single sidebar__post">
              <h3 class="sidebar__title">近期新闻</h3><!-- /.sidebar__title -->
              <div class="sidebar__post-wrap">
                <div class="sidebar__post__single" v-for="item in items">
<!--                  <div class="sidebar__post-image">-->
<!--                    <div class="inner-block"><img src="/assets/images/post-1.png" alt="Awesome Image"></div>-->
<!--                    &lt;!&ndash; /.inner-block &ndash;&gt;-->
<!--                  </div>&lt;!&ndash; /.sidebar__post-image &ndash;&gt;-->
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
  </section>
</template>

<script>
    export default {
        name: "NewsList",
        data() {
            return {
                type: 'news',

                items: [
                    {title: "这是一条新闻", image: "/images/logo.png", date: "2021/9/10", filename: "1",},
                    {title: "这是一条新闻", image: "/images/logo.png", date: "2021/9/10", filename: "2"},
                    {title: "这是一条新闻", image: "/images/logo.png", date: "2021/9/10", filename: "3"},
                    {title: "这是一条新闻", image: "/images/logo.png", date: "2021/9/10", filename: "3"},
                    {title: "这是一条新闻", image: "/images/logo.png", date: "2021/9/10", filename: "3"},
                    {title: "这是一条新闻", image: "/images/logo.png", date: "2021/9/10", filename: "3"},
                    {title: "这是一条新闻", image: "/images/logo.png", date: "2021/9/10", filename: "3"},
                    {title: "这是一条新闻", image: "/images/logo.png", date: "2021/9/10", filename: "3"},
                    {title: "这是一条新闻", image: "/images/logo.png", date: "2021/9/10", filename: "3"},
                ],
            }
        }
    }
</script>

<style scoped>

</style>
