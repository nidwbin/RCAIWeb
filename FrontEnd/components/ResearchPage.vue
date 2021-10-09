<!--
 * @FileDescription: history page
 * @Author: liuyoude
 * @Date: 2021-10-01
 * @LastEditors: liuyoude
 * @LastEditTime: 2021-10-09
 -->
<template>
  <div v-if="!admin">
    <div class="direction-area pt-115">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="direction-item">
            <div class="item d-block d-sm-flex align-items-center" v-for="item in items">
              <div class="thumb">
                <img :src="item.image" alt="">
<!--                <span>{{ item.year }}</span>-->
              </div>
              <div class="content">
                <nuxt-link to="#"><span class="	fa fa-fire"></span>{{ item.name }}</nuxt-link>
                <p>{{ item.desc }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </div>
  <div v-else>
    <div class="direction-area pt-115">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="direction-item">
            <div class="item d-block d-sm-flex align-items-center">
                <div class="thumb">
                  <img src="images/direction/direction_1.jpg" alt="">
                  <input type="file" @change="changeImg(item)" style="margin-top: 4px;">
                </div>
                <form>
                  <div class="content">
                  <nuxt-link to="#">
                    <span class="	fa fa-fire"></span>
                    <div class="name_input">
                      <input name="direction_name" type="text" placeholder="方向名称">
                    </div>
                  </nuxt-link>
                  <div class="desc_input">
                    <p>
                      <textarea name="direction_desc" placeholder="方向相关描述"></textarea>
                    </p>
                  </div>
                  <div class="but">
                    <span class="fa fa-send-o" @click="onSubmit(item)">&nbsp;提&nbsp;交</span>
                  </div>
                </div>
                </form>

            </div>

            <div class="item d-block d-sm-flex align-items-center" v-for="item in items">
                <div class="thumb">
                  <img :src="item.image" alt="" id="image_id">
                  <input type="file" @change="changeImg(item)" id="img_file" style="margin-top: 4px;">
                </div>
                <form>
                  <div class="content">
                  <nuxt-link to="#">
                    <span class="	fa fa-fire"></span>
                    <div class="name_input">
                      <input name="direction_name" type="text" :placeholder="item.name" v-model="item.name">
                    </div>
                  </nuxt-link>
                  <div class="desc_input">
                    <p>
                      <textarea name="direction_desc" :placeholder="item.desc" v-model="item.desc"></textarea>
                    </p>
                  </div>
                  <div class="but">
                    <span class="fa fa-send-o" @click="onSubmit(item)">&nbsp;提&nbsp;交</span>
                  </div>
                </div>
                </form>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
    export default {
        name: "HistoryPage",

        data () {
            return{
                items: [
                    {desc:"方向相关描述", name:"基于机器学习的识别方法", image:"./images/direction/direction_1.jpg"},
                    {desc:"方向相关描述", name:"语音特征选择方法", image:"./images/direction/direction_2.jpg"},
                    {desc:"方向相关描述", name:"说话人识别", image:"./images/direction/direction_3.jpg"},
                    {desc:"方向相关描述", name:"语音中的副语言信息识别", image:"./images/direction/direction_4.gif"},
                    {desc:"方向相关描述", name:"关键词检出", image:"./images/direction/direction_1.jpg"},
                    {desc:"方向相关描述", name:"VOIP电话语音分析", image:"./images/direction/direction_2.jpg"},
                    {desc:"方向相关描述", name:"机器的听觉智能", image:"./images/direction/direction_3.jpg"},
                    {desc:"方向相关描述", name:"声学事件检测", image:"./images/direction/direction_4.gif"},
                ]

            }

        },

        computed: {
          admin() {
            return this.$store.state.admin;
          }
        },

        methods: {
            onSubmit(item) {
                let formData = new FormData();
                for (var key in item) {
                    formData.append(key, this.item[key]);
                }
                axios({
                    method: "post",
                    url: "xxxxxxx",
                    headers: {
                        "Content-Type": "multipart/form-data"
                    },
                    withCredentials: true,
                    data: formData
                }).then((res) => {
                    console.log(res);
                });
            },

            changeImg(item) {
                var file =  document.getElementById('img_file').files[0];
                console.log(file);
                var re = new FileReader();
                re.readAsDataURL(file);
                console.log(re);
                // item.image = re.target.result;
                $('#img_id').attr("src", re.result);
            }
        }
    }
</script>

<style scoped>

</style>
