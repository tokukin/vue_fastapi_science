<script setup lang="ts">
import Meun from "@/components/meun.vue";
import PageHeader from "@/components/PageHeader.vue";
import MeunRight from "@/components/MeunRight.vue";
</script>

<template>
  <el-container>
    <el-header>
      <!-- <Meun /> -->
      <MeunRight />
      <PageHeader />
      <hr />
    </el-header>
    <el-main>
      <router-view />
    </el-main>
  </el-container>
</template>

<style scoped>
.el-page-header {
  padding: 20px 0;
}
.el-header {
  width: 100%;
  height: 150px;
  padding: 15;
}
</style>
