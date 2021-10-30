<!--
 * @FileDescription: news page
 * @Author: liuyoude
 * @Date: 2021-10-02
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-15
 -->
<template>
  <div>
    <section class="paper-details">
      <div class="container">
        <div class="row">
          <div class="col-lg-8">
            <div class="paper-aera">
              <div class="card-text border-bottom mt-2 mb-4 pb-2" v-if="admin">
                <div class="ml-4 float-left"
                     style="font-size: 18px; font-family: 'Times New Roman';letter-spacing: .6px;line-height: 46px;">
                  0.&nbsp;&nbsp;{{ new_item.name }}<a :href="new_item.link">&nbsp;&nbsp;<span class="	fa fa-chain" style="color: gray"></span></a>
                </div>
                <div class="pt-1 pb-5">
                  <button type="button" class="btn btn-primary btn-sm float-right" @click="create('paper')">
                    <span class="fa fa-edit" style="color: white !important;"></span>&nbsp;&nbsp;新增
                  </button>
                </div>
              </div>
              <div class="card-header mb-2">
                <div class="h2"><span class="fa fa-graduation-cap"></span>&nbsp;&nbsp;论文专著</div>
              </div>
            </div>
            <div class="comment-one">
              <div class="card-text border-bottom mt-2 mb-2 pb-2" v-for="(item,index) in items">
                <div class="ml-4"
                     style="font-size: 18px; font-family: 'Times New Roman';letter-spacing: .6px;line-height: 46px;">
                  {{ index + 1 }}.&nbsp;&nbsp;{{ item.name }}&nbsp;&nbsp;<a :href="item.link"><span class="	fa fa-chain" style="color: #007bff"></span></a>
                </div>
                <div class="pt-0 pb-5" v-if="admin">
                  <button type="button" class="btn btn-danger btn-sm float-right" @click="remove(item,'paper')">
                    <span class="fa fa-trash-o"></span>&nbsp;&nbsp;删除
                  </button>
                  <span class="float-right">&nbsp;&nbsp;</span>
                  <button type="button" class="btn btn-warning btn-sm float-right" @click="view(item,false,'paper')">
                    <span class="fa fa-edit"></span>&nbsp;&nbsp;编辑
                  </button>
                </div>
              </div>
            </div><!-- /.comment-one -->
          </div><!-- /.col-lg-8 -->
          <div class="col-lg-4">
            <div class="card-header" style="background-color: white;">
              <div class="h2"><span class="fa fa-book" style="color: #ff5316"></span>&nbsp;&nbsp;出版物</div>
            </div>
            <div class="book-area" v-if="admin">
              <div class="book-single">
                <div class="name">
                  <h4>名称：</h4>
                  <p>{{ new_book.name }}</p>
                </div>
                <div class="info">
                  <h6>作者：</h6>
                  <p>{{ new_book.authors }}</p>
                </div>
                <div class="info">
                  <h6>出版时间：</h6>
                  <p>{{ new_book.pub_time }}</p>
                </div>
                <div class="info">
                  <h6>出版社：</h6>
                  <p>{{ new_book.press }}</p>
                </div>
                <div class="desc">
                  <h6>简介：</h6>
                  <p>{{ new_book.desc }}</p>
                </div>
                <div class="mt-4 mb-4" style="text-align: center">
                  <button type="button" class="btn btn-primary" @click="create('book')">
                    <span class="fa fa-edit"></span>&nbsp;&nbsp;新增
                  </button>
                </div>
                <div class="border-bottom"></div>
              </div>
              <!--              <div class="title">-->
              <!--                <h3><span class="fa fa-book"></span>出版物</h3>-->
              <!--              </div>-->
              <div class="book-single" v-for="book in books">
                <div class="name">
                  <h4>名称：</h4>
                  <p>{{ book.name }}</p>
                </div>
                <div class="info">
                  <h6>作者：</h6>
                  <p>{{ book.authors }}</p>
                </div>
                <div class="info">
                  <h6>出版时间：</h6>
                  <p>{{ book.pub_time }}</p>
                </div>
                <div class="info">
                  <h6>出版社：</h6>
                  <p>{{ book.press }}</p>
                </div>
                <div class="desc">
                  <h6>简介：</h6>
                  <p>{{ book.desc }}</p>
                </div>
                <div class="mt-4 mb-4" v-if="admin" style="text-align: center">
                  <button type="button" class="btn btn-warning" @click="view(book,false,'book')">
                    <span class="fa fa-edit"></span>&nbsp;&nbsp;编辑
                  </button>
                  <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
                  <button type="button" class="btn btn-danger" @click="remove(book,'book')">
                    <span class="fa fa-trash-o"></span>&nbsp;&nbsp;删除
                  </button>
                </div>
                <div class="border-bottom"></div>
              </div>
            </div>
          </div><!-- /.col-lg-4 -->
        </div><!-- /.row -->
      </div><!-- /.container -->
      <PagesList/>
    </section>

    <div v-if="modal">
      <div class="modal" v-on:click.self="modal=false">
        <div class="modal-dialog modal-dialog-centered">
          <div v-if="item_type === 'paper'">
            <div class="modal-content">
              <div class="modal-header">
                <h4 class="modal-title">编辑论文信息</h4>
                <button type="button" class="close" @click="modal=false">×</button>
              </div>
              <div class="modal-body">
                <div class="input-group mb-3">
                  <div class="input-group mb-3">
                  <div class="input-group-prepend">
                    <span class="input-group-text" id="basic-addon0_0">论文链接</span>
                  </div>
                  <input type="text" class="form-control" v-model="viewing_edit.link" aria-describedby="basic-addon0_0">
                </div>
                  <div class="input-group-prepend">
                    <span class="input-group-text" id="basic-addon0_1">论文名称</span>
                  </div>
                  <textarea class="form-control" v-model="viewing_edit.name"
                            aria-describedby="basic-addon0_1"
                            style="min-height: 200px !important; min-width: 500px !important; font-size: 22px; font-family: 'Times New Roman';"></textarea>
                </div>
              </div>
              <div class="modal-footer">
                <div v-if="create_flag">
                  <button type="button" class="btn btn-primary" @click="edit"><span class="fa fa-edit"></span>&nbsp;&nbsp;确定
                  </button>
                </div>
                <div v-else>
                  <button type="button" class="btn btn-warning" @click="edit"><span class="fa fa-edit"></span>&nbsp;&nbsp;修改
                  </button>
                  <button type="button" class="btn btn-danger" @click="remove(viewing_edit,item_type)">
                    <span class="fa fa-trash-o"></span>删除
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div v-else-if="item_type === 'book'">
            <div class="modal-content">
              <div class="modal-header">
                <h4 class="modal-title">编辑书籍信息</h4>
                <button type="button" class="close" @click="modal=false">×</button>
              </div>
              <div class="modal-body">
                <div class="input-group mb-3">
                  <div class="input-group-prepend">
                    <span class="input-group-text" id="basic-addon1_1">书籍名称</span>
                  </div>
                  <input type="text" class="form-control" v-model="viewing_edit.name" aria-describedby="basic-addon1_1">
                </div>
                <div class="input-group mb-3">
                  <div class="input-group-prepend">
                    <span class="input-group-text" id="basic-addon1_2">作者信息</span>
                  </div>
                  <input type="text" class="form-control" v-model="viewing_edit.authors"
                         aria-describedby="basic-addon1_2">
                </div>
                <div class="input-group mb-3">
                  <div class="input-group-prepend">
                    <span class="input-group-text" id="basic-addon1_3">出版时间</span>
                  </div>
                  <input type="date" class="form-control" v-model="viewing_edit.pub_time"
                         aria-describedby="basic-addon1_3">
                </div>
                <div class="input-group mb-3">
                  <div class="input-group-prepend">
                    <span class="input-group-text" id="basic-addon1_4">出版社</span>
                  </div>
                  <input type="text" class="form-control" v-model="viewing_edit.press"
                         aria-describedby="basic-addon1_4">
                </div>
                <div class="input-group mb-3">
                  <div class="input-group-prepend">
                    <span class="input-group-text" id="basic-addon1_5">简介</span>
                  </div>
                  <textarea class="form-control" v-model="viewing_edit.desc"
                            aria-describedby="basic-addon1_5"
                            style="min-height: 200px !important; min-width: 400px !important;"></textarea>
                </div>
              </div>
              <div class="modal-footer">
                <div v-if="create_flag">
                  <button type="button" class="btn btn-primary" @click="edit"><span class="fa fa-edit"></span>&nbsp;&nbsp;确定
                  </button>
                </div>
                <div v-else>
                  <button type="button" class="btn btn-warning" @click="edit"><span class="fa fa-edit"></span>&nbsp;&nbsp;修改
                  </button>
                  <button type="button" class="btn btn-danger" @click="remove(viewing_edit,item_type)">
                    <span class="fa fa-trash-o"></span>删除
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div v-else>
            <div class="modal-content">
              <div class="modal-header">
                <h4 class="modal-title">出错啦</h4>
                <button type="button" class="close" @click="modal=false">×</button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="modal-backdrop show" style=" z-index: 2000"></div>
    </div>
    <PagesList ref="page" :type="this.type" :per_page="this.per_page" @change_page="load_list"/>
    <div>
      <!--    <div v-else>-->
      <!--      <section class="paper-details">-->
      <!--        <div class="container">-->
      <!--          <div class="row">-->
      <!--            <div class="col-lg-8">-->
      <!--              <div class="paper-aera">-->
      <!--                <h3><span class="fa fa-graduation-cap"></span>论文专著</h3>-->
      <!--              </div>-->
      <!--              <div class="comment-one">-->
      <!--                <div class="comment-one__single" v-for="item in items_default">-->
      <!--                  <form>-->
      <!--                    <div class="comment-one__content">-->
      <!--                      <nuxt-link to="#">-->
      <!--                        <p>{{ item.index }}.<textarea name="paper_name" type="text"-->
      <!--                                                      :placeholder="item.paper"></textarea></p>-->
      <!--                      </nuxt-link>-->
      <!--                      <div class="but">-->
      <!--                        <span class="fa fa-send-o" id="add_1" @click="onSubmit(item)">&nbsp;新&nbsp;增</span>-->
      <!--                      </div>-->
      <!--                    </div>&lt;!&ndash; /.comment-one__content &ndash;&gt;-->
      <!--                  </form>-->
      <!--                </div>-->
      <!--                <div class="comment-one__single" v-for="item in items">-->
      <!--                  <form>-->
      <!--                    <div class="comment-one__content">-->
      <!--                      <nuxt-link to="#">-->
      <!--                        <p>{{ item.index }}.<textarea name="paper_name" type="text" :placeholder="item.paper"-->
      <!--                                                      v-model="item.paper"></textarea></p>-->
      <!--                      </nuxt-link>-->
      <!--                      <div class="but">-->
      <!--                        <span class="fa fa-send-o" id="add_2" @click="onSubmit(item)">&nbsp;提&nbsp;交</span>-->
      <!--                        <span class="fa fa-trash-o" id="del" @click="onSubmit(item)">&nbsp;删&nbsp;除</span>-->
      <!--                      </div>-->
      <!--                    </div>&lt;!&ndash; /.comment-one__content &ndash;&gt;-->
      <!--                  </form>-->
      <!--                </div>-->
      <!--              </div>&lt;!&ndash; /.comment-one &ndash;&gt;-->
      <!--            </div>&lt;!&ndash; /.col-lg-8 &ndash;&gt;-->
      <!--            <div class="col-lg-4">-->
      <!--              <div class="book-area">-->
      <!--                <div class="title">-->
      <!--                  <h3><span class="fa fa-book"></span>出版物</h3>-->
      <!--                </div>-->
      <!--                <div class="book-single" v-for="book in books_default">-->
      <!--                  <form>-->
      <!--                    <div class="name">-->
      <!--                      <h4>名称：</h4>-->
      <!--                      <p><input name="book_name" type="text" :placeholder="book.name"-->
      <!--                                style="font-size: 17px;font-weight: 600;"></p>-->
      <!--                    </div>-->
      <!--                    <div class="info">-->
      <!--                      <h6>作者：</h6>-->
      <!--                      <p><input name="book_authors" type="text" :placeholder="book.authors"></p>-->
      <!--                    </div>-->
      <!--                    <div class="info">-->
      <!--                      <h6>出版时间：</h6>-->
      <!--                      <p><input name="book_pub_time" type="text" :placeholder="book.pub_time"></p>-->
      <!--                    </div>-->
      <!--                    <div class="info">-->
      <!--                      <h6>出版社：</h6>-->
      <!--                      <p><input name="book_press" type="text" :placeholder="book.press"></p>-->
      <!--                    </div>-->
      <!--                    <div class="desc">-->
      <!--                      <h6>简介：</h6>-->
      <!--                      <p><textarea name="book_desc" type="text" :placeholder="book.desc"></textarea></p>-->
      <!--                    </div>-->
      <!--                    <div class="but">-->
      <!--                      <span class="fa fa-send-o" id="add_b_1" @click="onSubmit(item)">&nbsp;提&nbsp;交</span>-->
      <!--                    </div>-->
      <!--                  </form>-->
      <!--                </div>-->
      <!--                <div class="book-single" v-for="book in books">-->
      <!--                  <form>-->
      <!--                    <div class="name">-->
      <!--                      <h4>名称：</h4>-->
      <!--                      <p><input name="book_name" type="text" :placeholder="book.name" v-model="book.name"-->
      <!--                                style="font-size: 17px;font-weight: 600;"></p>-->
      <!--                    </div>-->
      <!--                    <div class="info">-->
      <!--                      <h6>作者：</h6>-->
      <!--                      <p><input name="book_authors" type="text" :placeholder="book.authors" v-model="book.authors"></p>-->
      <!--                    </div>-->
      <!--                    <div class="info">-->
      <!--                      <h6>出版时间：</h6>-->
      <!--                      <p><input name="book_pub_time" type="text" :placeholder="book.pub_time" v-model="book.pub_time">-->
      <!--                      </p>-->
      <!--                    </div>-->
      <!--                    <div class="info">-->
      <!--                      <h6>出版社：</h6>-->
      <!--                      <p><input name="book_press" type="text" :placeholder="book.press" v-model="book.press"></p>-->
      <!--                    </div>-->
      <!--                    <div class="desc">-->
      <!--                      <h6>简介：</h6>-->
      <!--                      <p><textarea name="book_desc" type="text" :placeholder="book.desc" v-model="book.desc"></textarea>-->
      <!--                      </p>-->
      <!--                    </div>-->
      <!--                  </form>-->
      <!--                  <div class="but">-->
      <!--                    <span class="fa fa-send-o" id="add_b_2" @click="onSubmit(item)">&nbsp;提&nbsp;交</span>-->
      <!--                    &lt;!&ndash;                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&ndash;&gt;-->
      <!--                    <span class="fa fa-trash-o" id="del_b" @click="onSubmit(item)">&nbsp;删&nbsp;除</span>-->
      <!--                  </div>-->
      <!--                </div>-->
      <!--              </div>-->
      <!--            </div>&lt;!&ndash; /.col-lg-4 &ndash;&gt;-->
      <!--          </div>&lt;!&ndash; /.row &ndash;&gt;-->
      <!--        </div>&lt;!&ndash; /.container &ndash;&gt;-->
      <!--        <PagesList/>-->
      <!--      </section>-->
      <!--    </div>-->
    </div>
  </div>
</template>

<script>
import Functions from "./Functions";
import PagesList from "@/components/PagesList";

export default {
  name: "NewsList",
  components: {PagesList},
  mixins: [Functions],
  data() {
    return {
      type: 'papers',
      per_page: 10,
      modal: false,
      viewing: null,
      viewing_edit: null,
      create_flag: false,
      item_type: 'paper', // paper or book
      items: [
        {
          name: "Wenjie Song, Jiqing Han, Hongwei Song. Contrastive Embedding Learning Method for Respiratory Sound Classification, ICASSP2021, Toronto, Canada",
          link: '#'
        },
        {
          index: "2",
          name: "Hongwei Song, Jiqing Han, Shiwen Deng, Zhihao Du. Capturing Temporal Dependencies through Future Prediction for CNN-Based Audio Classifiers, ICASSP2021, Toronto, Canada",
          link: '#'
        },
        {
          name: "Zhihao Du, Ming Lei, Jiqing Han, Shiliang Zhang. Self-supervised Adversarial Multi-task Learning for Vocoder-based Monaural Speech Enhancement, Interspeech2020, Shanghai, China",
          link: '#'
        },
        {
          name: "Zhihao Du, Jiqing Han, Xueliang Zhang. Double Adversarial Nework based Monaural Speech Enhancement for Robust Speech Recognition, Interspeech2020, Shanghai, China",
          link: '#'
        },
        {
          name: "Liwen Zhang, Jiqing Han, Ziqing Shi. ATReSN-Net: Capturing Attentive Temporal Relations in Semantic Neighborhood for Acoustic Scene Classification, Interspeech2020, Shanghai, China",
          link: '#'
        },
        {
          name: "Jiabin Xue, Tieran Zheng, Jiqing Han. Structured Sparse Attention for End-to-End Automatic Speech recognition, ICASSP2020, Barcelona, Spain",
          link: '#'
        },
        {
          name: "Zhihao Du, Ming Lei, Jiqing Han, Shiliang Zhang. PAN: Phoneme-Aware Network for Monaural Speech Enhancement, ICASSP2020, Barcelona, Spain",
          link: '#'
        },
        {
          name: "Chen Chen, Jiqing Han. TDMF: Task-Driven Multi-Level Framework for End-to-End Speaker Verification, ICASSP2020, Barcelona, Spain",
          link: '#'
        },
        {
          name: "Jiabin Xue, Tieran Zheng, Jiqing Han, Convolutional Grid Long Short-Term Memory Recurrent Neural Network for Automatic Speech Recognition. ICONIP2019, Sydney Autstralia",
          link: '#'
        },
      ],
      new_item: {id: 'new', name: "请输入论文引用", link: '#'},

      books: [
        {name: "语音信号处理", authors: "韩纪庆，张磊，郑铁然 编著", pub_time: "2004-09-01", press: "清华大学出版社", desc: ""},
        {
          name: "音频信息处理技术",
          authors: "韩纪庆，冯涛，郑贵滨，马翼平 编著",
          pub_time: "2007-01-01",
          press: "清华大学出版社",
          desc: "该书为普通高等教育“十一五”国家级规划教材"
        },
        {name: "语音信号处理（第2版）", authors: "韩纪庆，张磊，郑铁然 编著", pub_time: "2013-04-01", press: "清华大学出版社", desc: ""},
        {
          name: "声学事件检测理论与方法",
          authors: "韩纪庆，石自强 著",
          pub_time: "2016-08-15",
          press: "科学出版社",
          desc: "本书可作为高等院校计算机应用、信号与信息处理、通信与电子系统等专业及学科的研究生教材，也可供该领域的科研及工程技术人员参考。"
        },
      ],
      new_book: {id: 'new', name: "书籍名称", authors: "作者信息", pub_time: "XXXX-XX-XX", press: "出版社信息", desc: "书籍描述"},

    }
  },
  mounted() {
    this.load_list(1);
    this.load_book();
  },
  computed: {
    admin() {
      return this.$store.state.admin;
    }
  },

  methods: {
    create(item_type) {
      this.view(JSON.parse(JSON.stringify(item_type === 'paper' ? this.new_item : this.new_book)), true, item_type);
    },
    view(item, flag, item_type) {
      this.viewing = item;
      this.create_flag = flag;
      this.item_type = item_type;
      if (this.admin) {
        this.viewing_edit = JSON.parse(JSON.stringify(item));
        this.modal = true;
      } else {
        this.$toast.error('没有权限');
      }
    },
    edit() {
      let data = new FormData();
      data.append('type', this.type);
      data.append('id', this.viewing_edit.id);
      data.append('name', this.viewing_edit.name);
      if (this.item_type === 'paper') {
        data.append('filetype', 'item');
        data.append('link', this.viewing_edit.link);
      } else {
        data.append('filetype', 'book');
        data.append('authors', this.viewing_edit.authors);
        data.append('pub_time', this.viewing_edit.pub_time);
        data.append('press', this.viewing_edit.press);
        data.append('desc', this.viewing_edit.desc);
      }
      this.post('/list/', data, data => {
        switch (data['message']) {
          case 'success': {
            if (this.item_type === 'paper') {
              console.log('a');
              this.reload_list();
            } else {
              console.log('b');
              this.reload_book();
            }
            break;
          }
          case 'error': {
            this.$toast.error('修改失败');
            break;
          }
          default: {
            this.$toast.info(data['message']);
          }
        }
      })
      this.modal = false;
    },
    remove(item, item_type) {
      this.delete('/list/', {
        type: this.type,
        filetype: item_type === 'paper' ? 'item' : 'book',
        filename: item.id
      }, data => {
        switch (data['message']) {
          case 'success': {
            console.log('a');
            if (item_type === 'paper') {
              console.log('a');
              this.reload_list();
            } else {
              console.log('b');
              this.reload_book();
            }
            break;
          }
          case 'error': {
            this.$toast.error('删除失败');
            break;
          }
          default: {
            this.$toast.info(data['message']);
          }
        }
      });
      this.modal = false;
    },
    load_book() {
      this.get('/list/', {type: this.type, filetype: 'books'}, data => {
        switch (data['message']) {
          case 'success': {
            this.books = data['content'];
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
    load_list(page) {
      this.get('/list/', {type: this.type, filetype: 'lists', page: page, per_page: this.per_page}, data => {
        switch (data['message']) {
          case 'success': {
            this.items = data['content'];
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
    reload_list() {
      this.create_flag = false;
      this.$refs.page.reload();
    },
    reload_book() {
      this.create_flag = false;
      this.load_book();
    }
  }
}
</script>

<style scoped>
.modal {
  display: block;
  z-index: 2001;
}

a, a:link, a:visited, a:hover, a:active {
  text-decoration: none;
  color: inherit;
}
</style>

