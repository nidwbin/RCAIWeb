<template>

</template>

<script>
export default {
  name: "Functions",
  methods: {
    ready() {
      let cnt = 10;
      while (!this.$cookies.get('ajax-ready') && cnt) {
        this.$axios.get('/csrf');
        cnt--;
      }
      return this.$cookies.get('ajax-ready');
    },

    get(url = null, data = null, func = undefined) {
      if (process.client && url !== null && data !== null && func !== undefined && this.ready()) {
        this.$axios.get(url, {params: data}).then(response => func(response.data)
        ).catch(() => {
          this.$toast.error('网络错误');
        });
      } else {
        if (this.debug) {
          console.log('get', url, data, func);
        }
        this.$toast.error('未知错误');
      }
    },

    post(url = null, data = null, func = undefined) {
      if (process.client && url !== null && data !== null && func !== undefined && this.ready()) {
        this.$axios.post(url, data).then(response => func(response.data)).catch(() => {
          this.$toast.error('网络错误');
        });
      } else {
        if (this.debug) {
          console.log('post', url, data, func);
        }
        this.$toast.error('未知错误');
      }
    },

    delete(url = null, data = null, func = undefined) {
      if (process.client && url !== null && data !== null && func !== undefined && this.ready()) {
        this.$axios.delete(url, {params: data}).then(response => func(response.data)).catch((error) => {
          this.$toast.error('网络错误');
        });
      } else {
        if (this.debug) {
          console.log('delete', url, data, func);
        }
        this.$toast.error('未知错误');
      }
    },
  }
}
</script>

<style scoped>

</style>
