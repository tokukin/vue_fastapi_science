<script setup lang="ts">
import { off } from "node:process";
import { useRouter } from "vue-router";

const router = useRouter();

// 接收路由路径参数，实现跳转
const handleSelect = (path: string) => {
  console.log("跳转路径：", path);
  router.push(path); // 跳转到传入的路由路径
};
</script>

<template>
  <el-row>
    <el-col :span="20" :offset="2">
      <div class="hello">
        <h1>化学</h1>
        <p>
          <el-tag type="primary">定义</el-tag>
          化学是研究物质的组成、结构、性质、转化及应用的一门基础学科，其特征是从分子层次认识物质，通过化学变化创造物质。
        </p>
        <p>
          <el-tag type="success">特征</el-tag>
          化学变化的特征是有新物质生成，常表现为改变颜色、放出气体、生成沉淀等。化学变化不但生成新物质，而且伴随着能量的变化，这种能量变化常表现为放热、吸热、发光等。
        </p>
      </div>
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
    </el-col>
  </el-row>
</template>
