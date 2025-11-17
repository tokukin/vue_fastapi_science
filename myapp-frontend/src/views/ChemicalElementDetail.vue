<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { ElSelect, ElOption } from "element-plus";

import { useChemicalElementStore } from "@/store/chemicalElementsStore";
import type { ChemicalElementInfo } from "@/types/chemicalelement";
import { log } from "node:console";

const chemicalElementStore = useChemicalElementStore();

// 组件挂载时获取用户信息
/*
onMounted(async () => {
  try {
    const userData: UserInfo = await userStore.fetchUserInfo(2);
    console.log('用户数据:', userData);
  } catch (err) {
    console.error('获取失败:', err);
  }
});*/
const route = useRoute();
onMounted(async () => {
  try {
    const elementId = Number(route.params.elementId);
    const elementData: ChemicalElementInfo =
      await chemicalElementStore.fetchChemicalElementInfo(elementId);
    console.log("元素数据:", elementData);
  } catch (err) {
    console.error("获取失败:", err);
  }
});

// 点击事件处理（明确参数类型）

const handleGetElement = async (elementId: number) => {
  try {
    await chemicalElementStore.fetchChemicalElementInfo(elementId);
  } catch (err) {
    // 处理错误
  }
};

const title = "chemical element";

// 在组件挂载时调用 fetchData 函数
//onMounted(fetchData);
</script>

<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <hr />
    <h2>元素序号：{{ route.params.elementId }}</h2>

    <div class="element-detail">
      <h2>pinia获取到元素详情</h2>
      <div v-if="chemicalElementStore.isLoading">加载中...</div>
      <div v-else-if="chemicalElementStore.error" class="error">
        {{ chemicalElementStore.error }}
      </div>
      <div v-else-if="chemicalElementStore.chemicalElementInfo">
        <p>
          元素编号:
          {{ chemicalElementStore.chemicalElementInfo.number }}，元素符号:
          {{ chemicalElementStore.chemicalElementInfo.symbol }}，元素名称:
          {{ chemicalElementStore.chemicalElementInfo.chineseName }}，原子质量:
          {{ chemicalElementStore.chemicalElementInfo.weight }}，元素周期:
          {{ chemicalElementStore.chemicalElementInfo.period }}，元素组:
          {{ chemicalElementStore.chemicalElementInfo.group }}，元素类型:
          {{ chemicalElementStore.chemicalElementInfo.type }}
        </p>

        <!-- 其他字段 -->
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
