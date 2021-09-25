<template>
<div class="container mt-2" :hidden="!is_admin">
  <div class="card">
    <h3 class="card-header text-muted">
      <div class="btn btn-light btn-lg btn-block"><i class="fa fa-terminal">: 新建条目</i>
      </div>
    </h3>
  </div>
</div>
</template>

<script>
export default {
  computed:{
    is_admin(){
      return this.$store.state.is_admin;
    }
  },
}
</script>
