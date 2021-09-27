<!--
 * @FileDescription: markdown editor
 * @Author: wenbin
 * @Date: 2021-09-14
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-25
 -->
<template>
  <div class="container mt-4 mb-4">
    <div class="mavonEditor">
        <mavon-editor ref=md v-model="text" :toolbars="toolbars" :editable="is_admin" :toolbarsFlag="is_admin"
                      :defaultOpen="is_admin?null:'preview'" :preview="!is_admin" :subfield="is_admin"
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
    file:{
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
    };
  },
  computed:{
    is_admin(){
      return this.$store.state.authority.is_admin;
    }
  },
  created() {
    this.get_file();
  },
  methods:{
    get_file(){
      if(this.type!=='' && this.file!=='' && this.$cookies.get("ajax-ready")){
        this.$axios.get(this.$cookies.get("backend-url")+"/file", {params:{
            "type":this.type,
            "file":this.file
        }}).then(
          (response)=>{
            if(response.data['data']!==undefined) {
              this.text = response.data['data'];
            }
          }
        );
      }
    },

    add_image(pos, $file){

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
