<template>
  <div class="container">
    <div v-if="admin">

    </div>
    <div v-else>

    </div>
  </div>
</template>

<script>
import Functions from "./Functions";

export default {
  name: "ViewerHeader",
  mixins: [Functions],
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
  computed: {
    admin() {
      return this.$store.state.admin;
    }
  }
}
</script>

<style scoped>

</style>
