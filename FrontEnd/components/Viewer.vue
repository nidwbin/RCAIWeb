<!--
 * @FileDescription: markdown editor
 * @Author: wenbin
 * @Date: 2021-09-14
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
 -->
<template>
  <div class="container mt-4 mb-4">
    <div :class="admin?'showBorder':''">
      <div class="mavonEditor">
        <mavon-editor ref=md v-model="text" :toolbars="toolbars" :editable="admin" :toolbarsFlag="admin"
                      :defaultOpen="admin?null:'preview'" :preview="!admin" :subfield="admin"
                      :boxShadow="false" @imgAdd="add_image" @imgDel="del_image" @save="save"
                      previewBackground="white"
        />
      </div>
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
      text: '',
      images: {},
      images_saved: {}
    };
  },
  computed: {
    admin() {
      return this.$store.state.admin;
    },
    debug() {
      return this.$store.state.admin;
    }
  },
  created() {
    if (process.client) {
      this.get_file({type: this.type, filetype: 'markdown', filename: this.filename},
        (data) => {
          if (data['message'] === 'success') {
            this.text = data['content'];
          } else {
            this.text = '哎呀！出错了╮(￣▽￣)╭';
          }
        });
      if (this.admin) {
        setInterval(() => {
          this.save(this.$refs.md.d_value, this.$refs.md.d_render);
        }, 5 * 60 * 1000);
      }
    }
  },
  methods: {
    get_ready() {
      let cnt = 10;
      while (!this.$cookies.get('ajax-ready') && cnt) {
        this.$axios.get('/csrf');
        cnt--;
      }
      return this.$cookies.get('ajax-ready');
    },

    get_file(data = null, func = undefined) {
      if (process.client && data !== null && func !== undefined && this.get_ready()) {
        this.$axios.get("/file/", {params: data}).then(response => func(response.data)
        ).catch(() => {
          this.toast.error('网络错误');
        });
      } else {
        if (this.debug) {
          console.log('get file', data, func);
        }
        this.$toast.error('未知错误');
      }
    },

    post_file(data = null, func = undefined) {
      if (process.client && data !== null && func !== undefined && this.get_ready()) {
        this.$axios.post('/file/', data).then(response => func(response.data)).catch((error) => {
          this.$toast.error('网络错误');
        });
      } else {
        if (this.debug) {
          console.log('post file', data, func);
        }
        this.toast.error('未知错误');
      }
    },
    delete_file(data = null, func = undefined) {
      if (process.client && data !== null && func !== undefined && this.get_ready()) {
        this.$axios.delete('/file/', {params: data}).then(response => func(response.data)).catch((error) => {
          this.$toast.error('网络错误');
        });
      } else {
        if (this.debug) {
          console.log('delete file', data, func);
        }
        this.toast.error('未知错误');
      }
    },

    add_image(pos, $file) {
      this.images[pos] = $file;
    },

    del_image(pos) {
      delete this.images[pos];
    },

    save(val, render) {
      if (this.debug) {
        console.log('markdown val', val);
        console.log('images', this.images);
        console.log('images map', this.images_saved);
      }
      for (let i in this.images_saved) {
        let reg_str = "/(!\\[\[^\\[\]*?\\]\(?=\\(\)\)\\(\\s*\(" + this.images_saved[i].replace(/\//g, '\\/') + "\)\\s*\\)/g";
        let reg = eval(reg_str);

        if (!val.match(reg)) {
          if (this.debug) {
            console.log('delete unmatched image', i, this.images_saved[i]);
          }
          this.delete_file({type: this.type, filetype: 'image', filename: this.images_saved[i],}, data => {
            if (data['message']) {
              delete this.images_saved[i];
            } else {
              this.$toast.error('删除失败');
            }
          });
        }
      }

      this.post_file({
        type: this.type, filetype: 'markdown', filename: this.filename, content: val,
      }, data => {
        if (data['message'] === 'success') {
          this.$toast.success('保存成功');
        } else {
          this.$toast.error('保存失败');
        }
      });

      for (let i in this.images) {
        let reg_str = "/(!\\[\[^\\[\]*?\\]\(?=\\(\)\)\\(\\s*\(" + i + "\)\\s*\\)/g";
        let reg = eval(reg_str);
        if (val.match(reg)) {
          if (!(i in this.images_saved)) {
            if (this.debug) {
              console.log('images uploading', i);
            }
            let data = new FormData();
            data.append('type', this.type);
            data.append('filetype', 'image');
            data.append('filename', i);
            data.append('content', this.images[i]);
            this.post_file(data, data => {
              if (data['message'] === 'success') {
                this.images_saved[i] = data['content'];
                // this.$refs.md.$img2Url(i, data['content']);
              } else {
                this.$toast.error('图片上传失败');
              }
            });
          }
        } else {
          this.del_image(i);
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

.showBorder {
  border: 1px solid #f2f6fc;
}


</style>
