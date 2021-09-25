<!--
 * @FileDescription: admin's news page
 * @Author: wenbin
 * @Date: 2021-09-13
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-13
 -->
<template>
  <div>
    <CheckAdmin />
    <AdminNav />
    <AddButton />
    <List />
  </div>
</template>

<script>
    import CheckAdmin from "@/components/admin/CheckAdmin";
    import AdminNav from "@/components/admin/AdminNav";
    import AddButton from "@/components/admin/AddButton";
    import List from "@/components/admin/List";
    export default {
      components: {
        CheckAdmin,
        AdminNav,
        AddButton,
        List
      },
      mounted() {
        this.$store.commit("change_location",this.$route.path);
      }
    }
</script>
