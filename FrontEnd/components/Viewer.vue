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
  props: {
    type: {
      type: String,
      default: '',
    },
    filename: {
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
      images: {},
      images_save: {}
    };
  },
  computed: {
    admin() {
      return this.$store.state.admin;
    }
  },
  created() {
    if (process.client) {
      this.get_file();
      if (this.admin) {
        setInterval(() => {
          this.save(this.$refs.md.d_value, this.$refs.md.d_render);
        }, 5 * 60 * 1000);
      }
    }
  },
  methods: {
    get_file() {
      if (this.type !== '' && this.filename !== '' && this.$cookies.get('ajax-ready')) {
        this.$axios.get("/file", {
          params: {
            type: this.type,
            filename: this.filename
          }
        }).then(
          (response) => {
            if (response.data['message'] === 'success') {
              this.text = response.data['content'];
            }
          }
        );
      }
    },

    add_image(pos, $file) {
      this.images[pos] = $file;
    },

    del_image(pos) {
      delete this.images[pos];
    },

    save(val, render) {
      for(let i in this.images_save){
        let reg_str = "/(!\\[\[^\\[\]*?\\]\(?=\\(\)\)\\(\\s*\(" + i[0] + "\)\\s*\\)/g";
        let reg = eval(reg_str);
        if(!val.match(reg)){
          delete this.images_save[i[0]];
        }
      }

      let cnt = 10;
      while (!this.$cookies.get('ajax-ready') && cnt) {
        this.$axios.get('/csrf');
        cnt--;
      }

      if (this.$cookies.get('ajax-ready')) {
        this.$axios.post('/file/', {
          type: 'markdown',
          filename: this.filename,
          content: val,
        }).then(
          (response) => {
            if (response.data['message'] === 'success') {
              this.$toast.success('保存成功');
            } else {
              this.$toast.error('保存失败');
            }
          }
        ).catch(() => {
          this.$toast.error('网络错误');
        });
        this.$axios.post('/file/',{
          type:'map',
          filename: this.filename,
          content: this.images_save,
        }).then(
          (response) => {
            if (response.data['message'] === 'success') {
              this.$toast.success('保存成功');
            } else {
              this.$toast.error('保存失败');
            }
          }
        ).catch(() => {
          this.$toast.error('网络错误');
        });
      }

      for (let i in this.images) {
        let reg_str = "/(!\\[\[^\\[\]*?\\]\(?=\\(\)\)\\(\\s*\(" + i[0] + "\)\\s*\\)/g";
        let reg = eval(reg_str);
        if (val.match(reg)) {
          if (this.$cookies.get('ajax-ready') && !(i[0] in this.images_save)) {
            let data = new FormData();
            data.append('type', 'image');
            data.append('filename', i[0]);
            data.append('content', i[1]);
            this.$axios.post('/file/', data).then(
              (response) => {
                if (response.data['message']) {
                  this.images_save[i[0]] = response.data['content'];
                } else {
                  this.$toast.error('图片上传失败');
                }
              }
            ).then(() => {
              this.$toast.error('网络错误');
            })
          }
        } else {
          this.del_image(i[0]);
        }
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
