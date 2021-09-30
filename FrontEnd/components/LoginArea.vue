<!--
 * @FileDescription: login area
 * @Author: wenbin
 * @Date: 2021-09-26
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
 -->
<template>
  <div class="container mt-2 mb-2">
    <div class="row">
      <div class="col-4"></div>
      <div class="card col">
        <div class="card-body">
          <form>
            <div class="form-group">
              <label for="username">用户名</label>
              <input type="text" class="form-control" id="username" v-model="username" placeholder="输入用户名">
            </div>
            <div class="form-group">
              <label for="password">密码</label>
              <input type="password" class="form-control" id="password" v-model="password" placeholder="输入密码">
            </div>
            <div class="row">
              <div class="col-4"></div>
              <div class="col-4" @click="login"><a href="#" :class="'btn '+button_class"><i
                class="fa fa-send"></i>登录</a></div>
              <div class="col-4"></div>
            </div>
          </form>
        </div>
      </div>
      <div class="col-4"></div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      button_class: 'btn-primary',
    }
  },
  methods: {
    login() {
      if (this.$store.state.debug) {
        console.log('before location', this.$cookies.get('location'));
      }
      if (this.username !== '' && this.password !== '' && this.$cookies.get("ajax-ready")) {
        this.$axios.post('/login/', {
          username: this.username,
          password: this.password,
        }).then(
          (response) => {
            if (response.data['message'] === 'success') {
              this.button_class = "btn-success";
              if (!this.$store.state.debug) {
                setTimeout(() => {
                  let location = this.$cookies.get('location');
                  this.$router.push(location === undefined ? '/' : location);
                }, 3000);
              }
            } else {
              this.button_class = "btn-danger";
            }
          }).catch(
          () => {
            this.button_class = "btn-danger";
          }
        )
      } else {
        this.button_class = "btn-danger";
      }
    }
  }
}
</script>
