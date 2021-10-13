<!--
 * @FileDescription: news page
 * @Author: liuyoude
 * @Date: 2021-10-02
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-02
 -->
<template>
  <section class="paper-details">
    <div class="container">
      <div class="row">
        <div class="col-lg-8">
          <div class="paper-aera">
            <h3><span class="fa fa-graduation-cap"></span>论文专著</h3>
          </div>
          <div class="comment-one">
            <div class="comment-one__single" v-for="item in items">
              <nuxt-link :to="{name:'view', query:{type:type, filename:item.filename}}">
                <div class="comment-one__content">
                    <p>{{ item.index }}.{{ item.paper }}</p>
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
          <div class="book-area">
            <div class="title">
              <h3><span class="fa fa-book"></span>出版物</h3>
            </div>
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
            </div>
          </div>
        </div><!-- /.col-lg-4 -->
      </div><!-- /.row -->
    </div><!-- /.container -->
    <PagesList/>
  </section>
</template>

<script>
    import PagesList from "./PagesList";
    export default {
        name: "NewsList",
      components: {PagesList},
      data() {
            return {
                type: 'news',

                items: [
                    {index:"1",paper: "Wenjie Song, Jiqing Han, Hongwei Song. Contrastive Embedding Learning Method for Respiratory Sound Classification, ICASSP2021, Toronto, Canada"},
                    {index:"2",paper: "Hongwei Song, Jiqing Han, Shiwen Deng, Zhihao Du. Capturing Temporal Dependencies through Future Prediction for CNN-Based Audio Classifiers, ICASSP2021, Toronto, Canada"},
                    {index:"3",paper: "Zhihao Du, Ming Lei, Jiqing Han, Shiliang Zhang. Self-supervised Adversarial Multi-task Learning for Vocoder-based Monaural Speech Enhancement, Interspeech2020, Shanghai, China"},
                    {index:"4",paper: "Zhihao Du, Jiqing Han, Xueliang Zhang. Double Adversarial Nework based Monaural Speech Enhancement for Robust Speech Recognition, Interspeech2020, Shanghai, China"},
                    {index:"5",paper: "Liwen Zhang, Jiqing Han, Ziqing Shi. ATReSN-Net: Capturing Attentive Temporal Relations in Semantic Neighborhood for Acoustic Scene Classification, Interspeech2020, Shanghai, China"},
                    {index:"6",paper: "Jiabin Xue, Tieran Zheng, Jiqing Han. Structured Sparse Attention for End-to-End Automatic Speech recognition, ICASSP2020, Barcelona, Spain"},
                    {index:"7",paper: "Zhihao Du, Ming Lei, Jiqing Han, Shiliang Zhang. PAN: Phoneme-Aware Network for Monaural Speech Enhancement, ICASSP2020, Barcelona, Spain"},
                    {index:"8",paper: "Chen Chen, Jiqing Han. TDMF: Task-Driven Multi-Level Framework for End-to-End Speaker Verification, ICASSP2020, Barcelona, Spain"},
                    {index:"9",paper: "Jiabin Xue, Tieran Zheng, Jiqing Han, Convolutional Grid Long Short-Term Memory Recurrent Neural Network for Automatic Speech Recognition. ICONIP2019, Sydney Autstralia"},
                ],

                books: [
                    {name:"语音信号处理", authors: "韩纪庆，张磊，郑铁然 编著", pub_time:"2004-09-01", press:"清华大学出版社", desc:""},
                    {name:"音频信息处理技术", authors: "韩纪庆，冯涛，郑贵滨，马翼平 编著", pub_time:"2007-01-01", press:"清华大学出版社", desc:"该书为普通高等教育“十一五”国家级规划教材"},
                    {name:"语音信号处理（第2版）", authors:"韩纪庆，张磊，郑铁然 编著", pub_time:"2013-04-01", press:"清华大学出版社", desc:""},
                    {name:"声学事件检测理论与方法", authors: "韩纪庆，石自强 著", pub_time:"2016-08-15", press:"科学出版社", desc:"本书可作为高等院校计算机应用、信号与信息处理、通信与电子系统等专业及学科的研究生教材，也可供该领域的科研及工程技术人员参考。"},
                ]
            }
        }
    }
</script>

<style scoped>

</style>

