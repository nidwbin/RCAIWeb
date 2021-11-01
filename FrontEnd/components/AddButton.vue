<template>
<div class="container mt-2" v-show="admin">
  <div class="card">
    <h3 class="card-header text-muted">
      <div class="btn btn-light btn-lg btn-block" @click="">
        <i class="fa fa-terminal">: 新建条目</i>
      </div>
    </h3>
  </div>
</div>
</template>

<script>
export default {
  computed:{
    admin(){
      return this.$store.state.admin;
    }
  },
  methods:{
    add_new(){
      window.location.replace(this.$store.state.backend.domain+":"+this.$store.state.backend.port+"/admin/editor");
    },
  },
}
</script>
