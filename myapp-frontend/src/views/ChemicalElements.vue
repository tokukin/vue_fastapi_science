<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import { ElSelect, ElOption } from "element-plus";

import { useChemicalElementStore } from "@/store/chemicalElementsStore";
import { off } from "process";
import { log } from "console";

// 批量设置所有 .ratio-item 的高度 = 宽度 × 1.2
const setAllRatioItems = () => {
  // 获取所有带 .ratio-item 类的元素
  const items = document.querySelectorAll<HTMLDivElement>(".grid-element");

  items.forEach((item) => {
    // 类型守卫：确保元素存在
    if (item) {
      const width = item.offsetWidth; // 获取元素宽度
      item.style.height = `${width * 1.2}px`; // 高度 = 宽度 × 1.2
    }
  });
};

// 初始化时设置
onMounted(() => {
  setAllRatioItems();
  // 监听窗口大小变化，实时更新（可选）
  window.addEventListener("resize", setAllRatioItems);
});

// 组件卸载时清理事件监听
onUnmounted(() => {
  window.removeEventListener("resize", setAllRatioItems);
});

const store = useChemicalElementStore();

// 组件挂载时自动加载全量数据
const loadAllElements = async () => {
  try {
    await store.fetchAllChemicalElements();
    console.log("全量元素加载完成");
    console.log(store.allElements);

    for (let elem of store.allElements) {
      console.log(elem.type);

      var elementDom = document.getElementById(`element-${elem.number}`);
      if (elementDom) {
        // 修改元素名称（找到 .element-name 类的子元素）
        // const newDivHtml = `${elem.symbol}`;
        const newDivHtml = `<div class="element-symbol">${elem.symbol}</div><div class="element-chineseName">${elem.chineseName}</div>`;
        elementDom.innerHTML += newDivHtml;
        elementDom.classList.add(elem.type);
      }
    }
    elementDom = document.getElementById(`element-57-71`);
    if (elementDom) {
      // 修改元素名称（找到 .element-name 类的子元素）
      // const newDivHtml = `${elem.symbol}`;
      const newDivHtml = `57-71<br />镧系`;
      elementDom.innerHTML += newDivHtml;
      elementDom.classList.add("nide-sample");
    }
    elementDom = document.getElementById(`element-89-103`);
    if (elementDom) {
      // 修改元素名称（找到 .element-name 类的子元素）
      // const newDivHtml = `${elem.symbol}`;
      const newDivHtml = `89-103<br />锕系`;
      elementDom.innerHTML += newDivHtml;
      elementDom.classList.add("nide-sample");
    }
    elementDom = document.getElementById(`element-57-71-1`);
    if (elementDom) {
      // 修改元素名称（找到 .element-name 类的子元素）
      // const newDivHtml = `${elem.symbol}`;
      const newDivHtml = `57-71<br />镧系`;
      elementDom.innerHTML += newDivHtml;
      elementDom.classList.add("nide-sample");
    }
    elementDom = document.getElementById(`element-89-103-1`);
    if (elementDom) {
      // 修改元素名称（找到 .element-name 类的子元素）
      // const newDivHtml = `${elem.symbol}`;
      const newDivHtml = `89-103<br />锕系`;
      elementDom.innerHTML += newDivHtml;
      elementDom.classList.add("nide-sample");
    }
    // 批量添加新内容
  } catch (err) {
    console.error("加载失败", err);
  }
};
loadAllElements();

const title = "元素周期表";

// 通过 id 获取元素容器
// const elementDom = document.getElementById(`element-${elementId}`);
// if (!elementDom) return;
// for(let elem of store.allElements){
//   if(elem.number === elementId){
//     // 修改元素名称（找到 .element-name 类的子元素）
//     const nameDom = elementDom.querySelector(".element-name");
//     if (nameDom) {
//       nameDom.textContent = `${elem.chineseName}（${elem.symbol}）`; // 示例：修改6号元素名称
//     }
//   }
// }
</script>

<template>
  <h1>{{ title }}</h1>

  <!-- <div class="element-detail">
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
    </div> -->

  <el-row :gutter="10" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-1"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4" :offset="8">
          <div class="grid-element element-type-sample nonmetal">
            nonmetal<br />非金属
          </div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element element-type-sample noblegas">
            noblegas<br />
            稀有气体
          </div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element element-type-sample alkalimetal">
            alkali-<br />metal<br />碱金属
          </div>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element element-type-sample alkalineearth">
            alkali-<br />neearth<br />碱土金属
          </div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element element-type-sample metalloid">
            metalloid<br />类金属
          </div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element element-type-sample metal">
            metal<br />金属
          </div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element element-type-sample transitionmetal">
            transi-<br />tionmetal<br />过渡金属
          </div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element element-type-sample lanthanide">
            lantha-<br />nide<br />镧系元素
          </div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element element-type-sample halogen">
            halogen<br />卤素
          </div>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element element-type-sample actinide">
            actinide<br />锕系元素
          </div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4" :offset="16">
          <div class="grid-element" id="element-2"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row :gutter="10" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-3"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-4"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="6">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-5"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-6"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-7"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-8"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-9"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-10"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row :gutter="10" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-11"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-12"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="6">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-13"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-14"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-15"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-16"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-17"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-18"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row :gutter="10" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-19"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-20"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-21"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-22"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-23"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-24"></div>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-25"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-26"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-27"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-28"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-29"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-30"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-31"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-32"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-33"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-34"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-35"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-36"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row :gutter="10" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-37"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-38"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-39"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-40"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-41"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-42"></div>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-43"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-44"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-45"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-46"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-47"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-48"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-49"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-50"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-51"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-52"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-53"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-54"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row :gutter="10" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-55"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-56"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-57-71"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-72"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-73"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-74"></div>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-75"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-76"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-77"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-78"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-79"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-80"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-81"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-82"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-83"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-84"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-85"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-86"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row :gutter="10" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-87"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-88"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-89-103"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-104"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-105"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-106"></div>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-107"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-108"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-109"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-110"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-111"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-112"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-113"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-114"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-115"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-116"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-117"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-118"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row :gutter="10" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4" :offset="4">
          <div class="grid-element" id="element-57-71-1"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-57"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-58"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-59"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-60"></div>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-61"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-62"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-63"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-64"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-65"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-66"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-67"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-68"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-69"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-70"></div>
        </el-col>

        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-71"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row :gutter="10" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4" :offset="4">
          <div class="grid-element" id="element-89-103-1"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-89"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-90"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-91"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-92"></div>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-93"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-94"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-95"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-96"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-97"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-98"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-99"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-100"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-101"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-102"></div>
        </el-col>

        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-103"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>

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

.grid-element {
  border-radius: 4px;
  /* min-height: 36px; */

  background-color: gray;

  display: flex;
  flex-direction: column; /* 垂直方向排列子元素 */
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  color: aliceblue;
  font-size: clamp(12px, 5vw, 24px);
  overflow: hidden;
}

.grid-element > div {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 8px 4px; /* 上下内边距8px，左右4px */
  display: flex;
  flex-direction: column; /* 垂直行排列（关键） */
  justify-content: center; /* 整体垂直居中 */
  align-items: center; /* 整体水平居中 */
  gap: 4px; /* 内部元素间距（可调整） */
}

.element-symbol {
  font-size: clamp(12px, 5vw, 24px);
  width: 100%;
  text-align: left; /* 确保文本水平居中 */
}
.element-chineseName {
  font-size: clamp(12px, 5vw, 24px);
  width: 100%;
  text-align: center; /* 确保文本水平居中 */
}

.period-row {
  margin-bottom: 20px;
}

.nonmetal {
  background-color: #4caf50;
}
.noblegas {
  background-color: #2196f3;
}
.alkalimetal {
  background-color: #ff9800;
}
.alkalineearth {
  background-color: #ffc107;
}
.metalloid {
  background-color: #795548;
}
.metal {
  background-color: #9c27b0;
}
.transitionmetal {
  background-color: #3f51b5;
}
.lanthanide {
  background-color: #26a69a;
}
.halogen {
  background-color: #8bc34a;
}
.actinide {
  background-color: #e91e63;
}
#element-57-71 {
  background-color: #26a69a;
}
#element-89-103 {
  background-color: #e91e63;
}

.element-type-sample {
  font-size: clamp(6px, 3vw, 16px);
}
.nide-sample {
  font-size: clamp(6px, 3vw, 16px);
}
</style>
