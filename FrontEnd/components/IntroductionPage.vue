<!--
 * @FileDescription: home page
 * @Author: liuyoude
 * @Date: 2021-09-29
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-01
 -->
<template>
  <section class="single-project-area pt-120">
    <div class="container">
      <div class="row">
        <div class="col-lg-7">
          <div class="single-project">
            <div class="single-project-thumb">
            </div>
            <div class="single-project-content-1">
              <h4 class="title">中心概况</h4>
              <p>哈工大听觉智能研究中心(Research Center of Auditory Intelligence, 简称：RCAI)致力于语音、音乐及声音的识别的识别、分析、增强等处理技术的研究最早成立于 20 世纪 80年代初，是国内较早开展此研究的单位之一。</p>
              <p>中心现有教授1名、副教授4名，博士生导师3人，科研秘书1名，拥有包括企业级服务器在内的一批现代化的仪器设备。研究室室注重交流与合作，与相关领域的知名学者保持密切的联系，与国家计算机信息内容安全组成重点实验室、IBM联合实验室、语言语音教育部 - 微软重点实验室的重要组成部分，并先后派出多名硕士、博士到微软亚洲研究院和IBM中国研究中心学习。</p>
              <p>研究室近年来已发表国内外学术期刊论文及国际学术会议论文100余篇其中被SCI、EI权威索引论文40多篇次，著书5部，获得国家发明专利多项，申报国家发明专利40多项；多次获得省、部级科技奖项。</p>
              <h3 class="title">研究方向</h3>
              <p>目前，中心紧密围绕着国家重大需求、战略目标和国际学术前沿，立足于语音处理的发展方向，坚持需求与发展并举、理论与实践并重，在“语音分析、识别与合成技术、基于语音的信息安全技术、音频信息检索技术、数字音频水印与信息伪装、说话人识别技术”等方面的研究显示了自己的优势与特色，形成了一批具有自主知识产权的专利技术、一批有技术创新和显著经济效益的标志性成果，努力把中心建设成为科学高效、功能完备、体系齐全、人才辈出的科研平台。</p>
              <h3 class="title">承担项目</h3>
              <p>中心近年来承担了30余项科研工作项目，包括国家重大研究计划、国家自然科学基金重点项目、国家973项目、国家自然科学基金项目、国家863重点项目、国家863重大项目子课题、国家242项目、国家信息安全中心项目、国家重点实验室项目、教育部跨世纪优秀人才基金项目、省部委重点项目等。</p>
            </div>
          </div>
        </div>
        <div class="col-lg-5">
            <div class="history-area pt-115">
              <div class="history-item">
                <h3 class="title">发展历史</h3>
                <div class="item d-block d-sm-flex align-items-center" v-for="item in items">
                  <div class="thumb">
    <!--                <img src="/assets/images/history-1.jpg" alt="">-->
                    <span>{{ item.year }}</span>
                  </div>
                  <div class="content">
                    <nuxt-link to="/single-project">Company was Founded</nuxt-link>
                    <p>there are many variations of passages of lorem Ipsum available but the majority have suffered alteration in some form injected which don't look of available but the majority have suffered even slightly believable.</p>
                  </div>
                </div>
              </div>
            </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
    export default {
        name: "ProjectSingle",
        data () {
            return{
                items: [
                    {year:1996},
                    {year:2001},
                    {year:2007},
                    {year:2020},
                ]

            }

        }
    }
</script>

<style scoped>

</style>
