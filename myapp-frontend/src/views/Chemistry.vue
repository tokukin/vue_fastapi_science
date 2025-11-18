<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();

// 接收路由路径参数，实现跳转
const handleSelect = (path: string) => {
  console.log("跳转路径：", path);
  router.push(path); // 跳转到传入的路由路径
};
</script>

<template>
  <div class="hello">
    <h1>Chemistry</h1>
    <div class="button-row">
      <!-- 点击时通过参数传递路由路径 -->
      <el-button
        type="primary"
        @click="handleSelect('/chemistry/periodic-table')"
      >
        跳转到化学元素周期表页面
      </el-button>

      <el-button type="success" @click="handleSelect('/chemistry/other')">
        其他化学页面
      </el-button>
      <!-- 其他按钮 -->
      <el-button type="info" disabled>Info</el-button>
      <el-button type="warning" disabled>Warning</el-button>
      <el-button type="danger" disabled>Danger</el-button>
    </div>
  </div>
</template>
