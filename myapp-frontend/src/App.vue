<script setup lang="ts">
import Meun from "@/components/Meun.vue";
import PageHeader from "@/components/PageHeader.vue";
import MeunRight from "@/components/MeunRight.vue";
import { useRoute } from "vue-router"; // 引入useRoute
const route = useRoute();

console.log(route.path);
</script>

<template>
  <el-container>
    <el-header v-if="!route.meta.hideHeader">
      <!-- 根据路由元信息判断是否渲染 -->
      <MeunRight />
      <PageHeader />
      <!-- <Meun /> -->

      <!-- <hr /> -->
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
