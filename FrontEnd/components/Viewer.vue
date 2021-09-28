<!--
 * @FileDescription: markdown editor
 * @Author: wenbin
 * @Date: 2021-09-14
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
 -->
<template>
  <div class="container mt-4 mb-4">
    <div class="mavonEditor">
        <mavon-editor ref=md v-model="text" :toolbars="toolbars" :editable="admin" :toolbarsFlag="admin"
                      :defaultOpen="admin?null:'preview'" :preview="!admin" :subfield="admin"
                      :boxShadow="false" @imgAdd="add_image" @imgDel="del_image" @save="save"
                      />
    </div>
  </div>
</template>
<script>
export default {
  props:{
    type:{
      type: String,
      default: '',
    },
    filename:{
      type: String,
      default: '',
    }
  },
  data() {
    return {
      toolbars: {
              bold: true, // 粗体
              italic: true, // 斜体
              header: true, // 标题
              underline: true, // 下划线
              strikethrough: true, // 中划线
              mark: true, // 标记
              superscript: true, // 上角标
              subscript: true, // 下角标
              quote: true, // 引用
              ol: true, // 有序列表
              ul: true, // 无序列表
              link: true, // 链接
              imagelink: true, // 图片链接
              code: true, // code
              table: true, // 表格
              fullscreen: true, // 全屏编辑
              readmodel: true, // 沉浸式阅读
              htmlcode: true, // 展示html源码
              help: true, // 帮助
              /* 1.3.5 */
              undo: true, // 上一步
              redo: true, // 下一步
              trash: true, // 清空
              save: true, // 保存（触发events中的save事件）
              /* 1.4.2 */
              navigation: true, // 导航目录
              /* 2.1.8 */
              alignleft: true, // 左对齐
              aligncenter: true, // 居中
              alignright: true, // 右对齐
              /* 2.2.1 */
              subfield: true, // 单双栏模式
              preview: true, // 预览
      },
      text: '哎呀！出错了╮(￣▽￣)╭',
      images:{},
    };
  },
  computed:{
    admin(){
      return this.$store.state.admin;
    }
  },
  created() {
    this.get_file();
  },
  methods:{
    get_file(){
      if(this.type!=='' && this.filename!=='' && this.$cookies.get('ajax-ready')){
        this.$axios.get("/file", {params:{
            type:this.type,
            filename:this.filename
        }}).then(
          (response)=>{
            if(response.data['message']==='success') {
              this.text = response.data['content'];
            }
          }
        );
      }
    },

    add_image(pos, $file){
      this.$toast.success('hello');
      if(this.$cookies.get('ajax-ready')){
        this.$axios.post("/file/", {
          type:'image',
          filename:pos,
          content:$file,
        },{
          headers: { 'Content-Type': 'multipart/form-data' },
        }).then(
          (respose)=>{
            if(respose.data['message']==='success') {
              this.images[pos] = respose.data['content'];
            }
          }
        )
      }else{
        this.$router.go(0);
      }
    },

    del_image(pos){
        if(this.$cookies.get('ajax-ready')){
          this.$axios.delete('/file/',{
            data:{
              type:'image',
              filename:pos,
              content:this.images[pos],
            }
          }).then(
            (respose)=>{
              if(respose.data['message']==='success') {
                delete this.images[pos];
              }
            }
          )
        }else{
          this.$router.go(0);
        }
    },

    save(val, render){
      // md内容，html内容
      for (let i in this.images){
        this.$ref.md.$img2Url(i[0],i[1]);
      }
      if(this.$cookies.get('ajax-ready')){
        this.$axios.post('/file/',{
          type:'markdown',
          filename:this.filename,
          content:val,
        }).then(
          (response) => {
            if(response.data['message']==='success'){

            }
          }
        )
      }
    }

  }
};
</script>

<style scoped>
.mavonEditor {
  width: 100%;
  height: 100%;
}
</style>
