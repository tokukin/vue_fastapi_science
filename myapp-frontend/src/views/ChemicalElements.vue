<script setup lang="ts">
import { ref, onMounted } from "vue";
import { ElSelect, ElOption } from "element-plus";

import { useChemicalElementStore } from "@/store/chemicalElementsStore";

const store = useChemicalElementStore();

// 组件挂载时自动加载全量数据
const loadAllElements = async () => {
  try {
    await store.fetchAllChemicalElements();
    console.log("全量元素加载完成");
    console.log(store);
  } catch (err) {
    console.error("加载失败", err);
  }
};
loadAllElements();

const title = "chemical element";
</script>

<template>
  <div class="hello">
    <h1>{{ title }}</h1>

    <div class="element-detail">
      <h2>pinia获取到元素详情</h2>
      <div>
        <div v-if="store.isLoading">加载中...</div>
        <div v-if="store.error">{{ store.error }}</div>

        <ul v-if="store.allElements.length">
          <li v-for="elem in store.allElements" :key="elem.number">
            {{ elem.number }} - {{ elem.chineseName }} ({{ elem.symbol }})
          </li>
        </ul>
      </div>
    </div>
  </div>
  <hr />
  <!-- 添加按钮，点击触发 increment 函数 -->
</template>
<style scoped>
.read-the-docs {
  color: #888;
}
/* 给选择框添加一点样式 */
.el-select {
  margin-left: 8px;
  width: 200px;
}
</style>
