<template>
  <div class="container">
    <div v-if="admin">

    </div>
    <div v-else>

    </div>
  </div>
</template>

<script>
export default {
  name: "ViewerHeader",
  computed: {
    admin() {
      return this.$store.state.admin;
    }
  }
}
</script>

<style scoped>

</style>
