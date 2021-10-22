<!--
 * @FileDescription: login area
 * @Author: wenbin
 * @Date: 2021-09-26
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
 -->
<template>
  <div>
    <div class="container mt-2 mb-2">
      <div class="row">
        <div class="col-lg-3 col-md-2"></div>
        <div class="card col">
          <div class="card-body">
            <form>
              <div class="custom-control custom-switch">
                <input type="checkbox" class="custom-control-input" id="switch" v-model="change_mode">
                <label class="custom-control-label" for="switch">高级模式</label>
              </div>
              <div class="form-group">
                <label for="username">用户名</label>
                <input type="text" class="form-control" id="username" v-model="username" placeholder="输入用户名">
              </div>
              <div class="form-group">
                <label for="password">密码</label>
                <input type="password" class="form-control" id="password" v-model="password" placeholder="输入密码"
                       @keydown.enter="login">
              </div>
              <div class="form-group" v-if="change_mode">
                <label for="username_">被修改者</label>
                <input type="text" class="form-control" id="username_" v-model="username_" placeholder="输入用户名">
              </div>
              <div class="form-group" v-if="change_mode">
                <label for="password_">被修改者密码</label>
                <input type="password" class="form-control" id="password_" v-model="password_" placeholder="输入密码">
              </div>
              <div class="form-group" v-if="change_mode">
                <label for="password__">确认密码</label>
                <input type="password" class="form-control" id="password__" v-model="password__" placeholder="输入密码"
                       @keydown.enter="change">
              </div>
              <div class="row">
                <div class="col-1"></div>
                <div class="col text-center" @click="login($event)">
                  <a ref="login" href="#" :class="'btn '+btn_login">
                    <i class="fa fa-send"></i>登录
                  </a>
                </div>
                <div class="col text-center" @click="change($event)" v-if="change_mode">
                  <a ref="change" href="#" :class="'btn '+btn_change">
                    <i class="fa fa-pencil"></i>修改
                  </a>
                </div>
                <div class="col text-center" @click="remove" v-if="change_mode">
                  <a href="#" class="btn btn-danger"><i class="fa fa-send"></i>删除
                  </a>
                </div>
                <div class="col-1"></div>
              </div>
            </form>
          </div>
        </div>
        <div class="col-lg-3 col-md-2"></div>
      </div>
    </div>
  </div>
</template>
<script>
import Functions from "./Functions";

export default {
  mixins: [Functions],
  data() {
    return {
      username: '',
      password: '',
      username_: '',
      password_: '',
      password__: '',
      btn_login: 'btn-primary',
      btn_change: 'btn-warning',
      change_mode: false,
    }
  },
  methods: {
    response(data, message, btn) {
      switch (data['message']) {
        case 'success': {
          btn = 'btn-success';
          if (!this.$store.state.debug) {
            setTimeout(() => {
              let location = this.$cookies.get('location');
              this.$router.push(location === undefined ? '/' : location);
            }, 1000);
          }
          break;
        }
        case 'error': {
          this.$toast.error(message);
          btn = 'btn-danger';
          break;
        }
        default: {
          this.$toast.info(data['message']);
        }
      }
    },
    login() {
      if (this.$store.state.debug) {
        console.log('before location', this.$cookies.get('location'));
      }
      if (this.username !== '' && this.password !== '') {
        this.post('/login/', {username: this.username, password: this.password}, data => {
          this.response(data, '登录失败', this.btn_login)
        })
      } else {
        this.btn_login = 'btn-danger';
      }
    },
    change(e) {
      if (this.username !== '' && this.password !== ''
        && this.username_ !== '' && this.password_ !== ''
        && this.password_ === this.password__) {
        this.post('/admin/', {
          username: this.username,
          password: this.password,
          username_: this.username_,
          password_: this.password_
        }, data => {
          this.response(data, '修改失败', this.btn_change);
        })
      } else {
        this.btn_change = 'btn-danger';
      }
    },
    remove() {
      if (this.username !== '' && this.password !== '' && this.username_ !== '' && this.password_ !== '') {
        this.delete('/admin/', {
          username: this.username,
          password: this.password,
          username_: this.username_,
          password_: this.password_
        }, data => {
          this.response(data, '删除失败', this.btn_change);
        })
      }
    }
  }
}
</script>
<style scoped>
.modal {
  display: block;
}
</style>
