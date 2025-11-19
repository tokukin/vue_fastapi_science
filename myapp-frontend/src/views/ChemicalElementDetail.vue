<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
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

// 响应式变量存储窗口大小
const windowSize = ref({
  width: 0,
  height: 0,
  // 可选：添加不含滚动条的尺寸
  clientWidth: 0,
  clientHeight: 0,
});

// 更新窗口大小的函数
const updateWindowSize = () => {
  windowSize.value.width = window.innerWidth;
  windowSize.value.height = window.innerHeight;
  windowSize.value.clientWidth = document.documentElement.clientWidth;
  windowSize.value.clientHeight = document.documentElement.clientHeight;
};
// 批量设置所有 .ratio-item 的高度 = 宽度 × 1.2
const setAllRatioItems = () => {
  updateWindowSize();

  // 获取所有带 .ratio-item 类的元素
  const elementDetail = document.getElementById("element-detail-large");
  if (elementDetail) {
    const width = elementDetail.offsetWidth; // 获取元素宽度
    elementDetail.style.height = `${width * 1.2}px`; // 高度 = 宽度 × 1.2
  }
};

onMounted(async () => {
  try {
    const elementId = Number(route.params.elementId);
    const elementData: ChemicalElementInfo =
      await chemicalElementStore.fetchChemicalElementInfo(elementId);
    console.log("元素数据:", elementData);
    const elementDetail = document.getElementById("element-detail-large");
    if (elementDetail) {
      const newDivHtml = `<div class="element-detail-info-header">
      <div class="element-detail-number">${elementData.number}</div>
      <div class="element-detail-symbol">${elementData.symbol}</div>
      </div>
      <div class="element-detail-info-body">
      <div class="element-detail-chineseName">${elementData.chineseName}</div>
      <div class="element-detail-englishName">${elementData.englishName}</div>
      <div class="element-detail-electronConfig">${elementData.electronConfig}</div>
      <div class="element-detail-type">${elementData.type}</div>
 
      </div>
      <div class="element-detail-info-foot">
      
      <div class="element-detail-weight">${elementData.weight}</div>
      
      
      </div>`;
      elementDetail.innerHTML += newDivHtml;
      elementDetail.classList.add(elementData.type);
    }
  } catch (err) {
    console.error("获取失败:", err);
  }
});

onMounted(() => {
  setAllRatioItems();
  window.addEventListener("resize", setAllRatioItems);
});
onUnmounted(() => {
  window.removeEventListener("resize", setAllRatioItems);
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
  </div>

  <el-row :gutter="10">
    <el-col :xs="8" :sm="8" :md="8" :lg="8" :xl="8" :offset="8">
      <div class="element-detail-large" id="element-detail-large"></div>
    </el-col>
  </el-row>
</template>
<style scoped>
#element-detail-large {
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  color: aliceblue;
}
::v-deep .element-detail-info-header {
  display: flex;
  flex-direction: row;
  justify-content: center; /* 垂直方向居中（主轴居中） */
  align-items: center; /* 水平方向居中（交叉轴居中） */
  width: 100%; /* 确保容器宽度 */
  height: 20%;
  /* padding-top: 5%; */
}
::v-deep .element-detail-info-body {
  display: flex;
  flex-direction: column;
  justify-content: center; /* 垂直方向居中（主轴居中） */
  align-items: center; /* 水平方向居中（交叉轴居中） */
  width: 100%; /* 确保容器宽度 */

  height: 60%;
}
::v-deep .element-detail-info-foot {
  display: flex;
  flex-direction: row;
  justify-content: center; /* 垂直方向居中（主轴居中） */
  align-items: center; /* 水平方向居中（交叉轴居中） */
  width: 100%; /* 确保容器宽度 */
  height: 20%;
  /* padding-top: 5%; */
}
::v-deep .element-detail-info-header .element-detail-number {
  font-size: 24px;
  font-weight: bold;
  width: 50%;
  text-align: left;
  padding-left: 5%;
  font-size: clamp(5px, 3vw, 50px);
}
::v-deep .element-detail-info-header .element-detail-symbol {
  font-size: 24px;
  font-weight: bold;
  width: 50%;
  text-align: right;
  padding-right: 5%;
  font-size: clamp(5px, 3vw, 50px);
}
::v-deep .element-detail-info-body .element-detail-chineseName {
  font-weight: bold;
  text-align: center;
  font-size: clamp(20px, 3vw, 200px);
}
::v-deep .element-detail-info-body .element-detail-englishName {
  font-weight: bold;
  text-align: center;
  font-size: clamp(10px, 3vw, 50px);
}
::v-deep .element-detail-info-body .element-detail-electronConfig {
  font-weight: bold;
  text-align: center;
  font-size: clamp(8px, 3vw, 45px);
}
::v-deep .element-detail-info-body .element-detail-type {
  font-weight: bold;
  text-align: center;
  font-size: clamp(8px, 3vw, 40px);
}
::v-deep .element-detail-info-body .element-detail-group {
  font-weight: bold;
  text-align: center;
  font-size: clamp(8px, 3vw, 35px);
}
::v-deep .element-detail-info-body .element-detail-period {
  font-weight: bold;
  text-align: center;
  font-size: clamp(8px, 3vw, 35px);
}
::v-deep .element-detail-info-foot .element-detail-weight {
  font-weight: bold;
  text-align: center;
  font-size: clamp(5px, 3vw, 45px);
}
</style>
