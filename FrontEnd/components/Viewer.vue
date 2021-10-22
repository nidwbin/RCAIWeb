<!--
 * @FileDescription: markdown editor
 * @Author: wenbin
 * @Date: 2021-09-14
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
 -->
<template>
  <div class="container mt-4 mb-4">
<!--    <div class="row">-->
<!--      <div class="col-lg-10">-->
<!--        <div class="card text-center">-->
<!--          <h5 class="card-header">-->
<!--            编辑新闻标题-->
<!--          </h5>-->
<!--          <button type="button" class="btn btn-outline-primary btn-lg btn-block" @click="new_item">-->
<!--            +-->
<!--          </button>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div class="col-lg-2">-->
<!--        <div class="card text-center">-->
<!--          <h5 class="card-header">-->
<!--            删除编辑-->
<!--          </h5>-->
<!--          <button type="button" class="btn btn-outline-danger btn-lg btn-block" @click="new_item">-->
<!--            ×-->
<!--          </button>-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
    <div :class="admin?'showBorder':''">
      <div class="mavonEditor">
        <mavon-editor ref=md v-model="text" :toolbars="toolbars" :editable="admin" :toolbarsFlag="admin"
                      :defaultOpen="admin?null:'preview'" :preview="!admin" :subfield="admin"
                      :boxShadow="false" @imgAdd="add_image" @imgDel="del_image" @save="save"
                      previewBackground="white"
        />
      </div>
    </div>
<!--    <HeaderArea ref="header" :type="type" :btn_more="true" @reload_page="reload_page"/>-->
  </div>
</template>
<script>
    import Functions from "./Functions";
    // import HeaderArea from "./HeaderArea";

    export default {
        mixins: [Functions],
        // components: {HeaderArea},
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
                images_saved: {},
                image_base: this.$store.state.image_base + 'body/',
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
                this.get("/file/", {type: this.type, filetype: 'markdown', filename: this.filename},
                    (data) => {
                        switch (data['message']) {
                            case 'success': {
                                this.text = data['content'];
                                break;
                            }
                            case 'error': {
                                this.text = '哎呀！出错了╮(￣▽￣)╭';
                                break;
                            }
                            default: {
                                this.$toast.info(data['message'])
                            }
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
            add_image(pos, $file) {
                this.images[pos] = $file;
            },

            del_image(pos) {
                delete this.images[pos];
            },

            async process_image_saved(val) {
                for (let i in this.images_saved) {
                    let url = (this.image_base + this.images_saved[i]);
                    let reg_str = "/(!\\[\[^\\[\]*?\\]\(?=\\(\)\)\\(\\s*\(" + url.replace(/\//g, '\\/') + "\)\\s*\\)/g";
                    let reg = eval(reg_str);

                    if (!val.match(reg)) {
                        if (this.debug) {
                            console.log('delete unmatched image', i, this.images_saved[i]);
                        }
                        await this.delete("/file/", {
                            type: this.type,
                            filetype: 'image',
                            filename: this.images_saved[i],
                        }, data => {
                            switch (data['message']) {
                                case 'success': {
                                    delete this.images_saved[i];
                                    break;
                                }
                                case 'error': {
                                    this.$toast.error('删除失败');
                                    break;
                                }
                                default: {
                                    this.$toast.info(data['message'])
                                }
                            }
                        });
                    }
                }
            },

            process_markdown(val) {
                this.post("/file/", {
                    type: this.type, filetype: 'markdown', filename: this.filename, content: val,
                }, data => {
                    switch (data['message']) {
                        case 'success': {
                            this.$toast.success('保存成功');
                            break;
                        }
                        case 'error': {
                            this.$toast.error('保存失败');
                            break;
                        }
                        default: {
                            this.$toast.info(data['message'])
                        }
                    }
                });
            },

            async process_image_upload(val) {
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
                            data.append('filename', this.filename);
                            data.append('content', this.images[i]);
                            await this.post("/file/", data, data => {
                                switch (data['message']) {
                                    case 'success': {
                                        this.images_saved[i] = data['content'];
                                        this.$refs.md.$img2Url(i, this.image_base + data['content']);
                                        break;
                                    }
                                    case 'error': {
                                        this.$toast.error('图片上传失败');
                                        break;
                                    }
                                    default: {
                                        this.$toast.info(data['message'])
                                    }
                                }
                            });
                        }
                    } else {
                        this.del_image(i);
                    }
                }
                return this.$refs.md.d_value;
            },
            save(val, render) {
                if (this.debug) {
                    console.log('markdown val', val);
                    console.log('images', this.images);
                    console.log('images map', this.images_saved);
                }

                this.process_image_saved(val).then(() => {
                    this.process_image_upload(val).then((value) => {
                        this.process_markdown(value);
                    })
                });
            }
        },
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
