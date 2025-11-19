<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import { ElSelect, ElOption } from "element-plus";

import { useChemicalElementStore } from "@/store/chemicalElementsStore";
import { off } from "process";
import { log } from "console";

const store = useChemicalElementStore();

// 组件挂载时自动加载全量数据
const loadAllElements = async () => {
  try {
    await store.fetchAllChemicalElements();
    console.log("全量元素加载完成");
    //console.log(store.allElements);
    console.log(windowSize.value.clientWidth);
    // 获取所有 .element-type-sample 元素
    const elementSamples = document.querySelectorAll<HTMLDivElement>(
      ".element-type-sample"
    );

    elementSamples.forEach((elementSample) => {
      elementSample.classList.remove("element-type-sample-large");
      elementSample.classList.remove("element-type-sample-mid");
      elementSample.classList.remove("element-type-sample-small");
      //elementSample.classList.add("element-type-sample-large");
    });

    if (windowSize.value.clientWidth > 1970) {
      elementSamples.forEach((elementSample) => {
        elementSample.classList.add("element-type-sample-large");
      });
      for (let elem of store.allElements) {
        //console.log(elem.type);

        var elementDom = document.getElementById(`element-${elem.number}`);
        if (elementDom) {
          // 修改元素名称（找到 .element-name 类的子元素）
          // const newDivHtml = `${elem.symbol}`;
          const newDivHtml = `<div class="element-info-up"><div class="element-number">${elem.number}</div><div class="element-symbol">${elem.symbol}</div></div><div class="element-info-mid"><div class="element-chineseName">${elem.chineseName}</div></div>`;
          elementDom.innerHTML += newDivHtml;
          elementDom.classList.add(elem.type);
        }
      }
      var elementDoms =
        document.querySelectorAll<HTMLDivElement>(".lanthanide-sample");
      elementDoms.forEach((elementDom) => {
        const newDivHtml = `57-71<br />镧系`;
        elementDom.innerHTML += newDivHtml;
        elementDom.classList.add("nide-sample");
      });
      var elementDoms =
        document.querySelectorAll<HTMLDivElement>(".actinide-sample");
      elementDoms.forEach((elementDom) => {
        const newDivHtml = `89-103<br />锕系`;
        elementDom.innerHTML += newDivHtml;
        elementDom.classList.add("nide-sample");
      });
    } else if (windowSize.value.clientWidth > 1300) {
      elementSamples.forEach((elementSample) => {
        elementSample.classList.add("element-type-sample-mid");
      });
      for (let elem of store.allElements) {
        //console.log(elem.type);

        var elementDom = document.getElementById(`element-${elem.number}`);
        if (elementDom) {
          // 修改元素名称（找到 .element-name 类的子元素）
          // const newDivHtml = `${elem.symbol}`;
          const newDivHtml = `<div class="element-info-up"><div class="element-number-mid">${elem.number}</div></div><div class="element-info-mid"><div class="element-symbol-mid">${elem.symbol}</div></div>`;
          elementDom.innerHTML += newDivHtml;
          elementDom.classList.add(elem.type);
        }
      }
      var elementDoms =
        document.querySelectorAll<HTMLDivElement>(".lanthanide-sample");
      elementDoms.forEach((elementDom) => {
        const newDivHtml = `57-71<br />镧系`;
        elementDom.innerHTML += newDivHtml;
        elementDom.classList.add("nide-sample-mid");
      });
      var elementDoms =
        document.querySelectorAll<HTMLDivElement>(".actinide-sample");
      elementDoms.forEach((elementDom) => {
        const newDivHtml = `89-103<br />锕系`;
        elementDom.innerHTML += newDivHtml;
        elementDom.classList.add("nide-sample-mid");
      });
    } else {
      elementSamples.forEach((elementSample) => {
        elementSample.classList.add("element-type-sample-small");
      });
      for (let elem of store.allElements) {
        //console.log(elem.type);

        var elementDom = document.getElementById(`element-${elem.number}`);
        if (elementDom) {
          // 修改元素名称（找到 .element-name 类的子元素）
          // const newDivHtml = `${elem.symbol}`;
          const newDivHtml = `<div class="element-symbol-small">${elem.symbol}</div>`;
          elementDom.innerHTML += newDivHtml;
          elementDom.classList.add(elem.type);
        }
      }
      var elementDoms =
        document.querySelectorAll<HTMLDivElement>(".lanthanide-sample");
      elementDoms.forEach((elementDom) => {
        const newDivHtml = `57-71<br />镧系`;
        elementDom.innerHTML += newDivHtml;
        elementDom.classList.add("nide-sample-small");
      });
      var elementDoms =
        document.querySelectorAll<HTMLDivElement>(".actinide-sample");
      elementDoms.forEach((elementDom) => {
        const newDivHtml = `89-103<br />锕系`;
        elementDom.innerHTML += newDivHtml;
        elementDom.classList.add("nide-sample-small");
      });
    }

    // 批量添加新内容
  } catch (err) {
    console.error("加载失败", err);
  }
};

const title = "元素周期表";

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
  const items = document.querySelectorAll<HTMLDivElement>(".grid-element");

  items.forEach((item) => {
    // 类型守卫：确保元素存在
    if (item) {
      const width = item.offsetWidth; // 获取元素宽度
      item.style.height = `${width * 1.2}px`; // 高度 = 宽度 × 1.2
    }
  });
  clearGridElements();
  loadAllElements();
};

const clearGridElements = () => {
  // 获取所有 .grid-element 元素
  const gridElements =
    document.querySelectorAll<HTMLDivElement>(".grid-element");

  gridElements.forEach((el) => {
    if (el.id) {
      // 1. 清除所有子内容（包括文本和嵌套元素）
      el.innerHTML = "";

      // 2. 仅保留 grid-element 类，移除其他所有类
      // 先获取当前所有类名
      const classes = el.classList;
      // 过滤出需要保留的类（仅 grid-element）
      const classesToKeep = Array.from(classes).filter(
        (cls) => cls === "grid-element"
      );
      // 移除所有类，再重新添加需要保留的类
      el.className = classesToKeep.join(" ");
    }
  });
};
const openElementDetail = (elementId: string) => {
  // 带参数的路由路径：/element-detail?id=1
  const routePath = `/element-detail?id=${elementId}`;
  const fullUrl = window.location.origin + routePath;
  window.open(fullUrl, "_blank", "width=800,height=600");
};

// 初始化时设置
onMounted(() => {
  setAllRatioItems();
  // 监听窗口大小变化，实时更新（可选）
  window.addEventListener("resize", setAllRatioItems);
  // 获取所有 .grid-element 元素
  const gridElements =
    document.querySelectorAll<HTMLDivElement>(".grid-element");

  gridElements.forEach((el) => {
    el.addEventListener("click", () => {
      // 从 id 中提取元素序号（如 element-1 → 1）
      const elementId = el.id.split("-").slice(-1)[0];
      if (!elementId) {
        return;
      }
      // 弹窗显示元素信息
      //alert(`你点击了元素：${elementId}`);
      const windowWidth = window.innerWidth; // 窗口宽度
      const windowHeight = window.innerHeight; // 窗口高度
      // 计算窗口居中位置（基于当前窗口大小）
      const left = (window.screen.width - windowWidth) / 2;
      const top = (window.screen.height - windowHeight) / 2;
      // 窗口参数：width/height=尺寸，left/top=位置，toolbar=no=隐藏工具栏
      //const windowFeatures = `width=${windowWidth},height=${windowHeight},left=${left},top=${top},toolbar=no,menubar=no,scrollbars=yes,resizable=yes`;
      const windowFeatures = `width=${windowWidth},height=${windowHeight},left=${left},top=${top}`;
      //const routePath = `/chemistry/element-detail?id=${elementId}`;
      const routePath = `/chemistry/element-detail/${elementId}`;
      const fullUrl = window.location.origin + routePath;
      const newWindow = window.open(fullUrl, "_blank");
      // const newWindow = window.open(fullUrl, "_blank", windowFeatures);
      // const newWindow = window.open("", "_blank", windowFeatures);
      if (!newWindow) {
        alert("浏览器阻止了弹出窗口，请允许弹出权限");
        return;
      }

      // 若需添加点击态样式（如背景色变化），可临时添加类名并延迟移除
      el.classList.add("clicked");
      setTimeout(() => {
        el.classList.remove("clicked");
      }, 200);
    });
  });
});

// 组件卸载时清理事件监听
onUnmounted(() => {
  window.removeEventListener("resize", setAllRatioItems);
});

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

  <el-row :gutter="5" class="period-row">
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
  <el-row :gutter="5" class="period-row">
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
  <el-row :gutter="5" class="period-row">
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
  <el-row :gutter="5" class="period-row">
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
  <el-row :gutter="5" class="period-row">
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
  <el-row :gutter="5" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-55"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-56"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element lanthanide-sample"></div>
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
  <el-row :gutter="5" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-87"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-88"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element actinide-sample"></div>
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
  <el-row :gutter="5" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4" :offset="4">
          <div class="grid-element lanthanide-sample"></div>
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
  <el-row :gutter="5" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4" :offset="4">
          <div class="grid-element actinide-sample"></div>
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
/* 给选择框添加一点样式 */

.grid-element {
  border-radius: 4px;
  display: flex;
  flex-direction: column;
  color: aliceblue;
}

/* 动态效果 */
.grid-element:active,
.grid-element:focus,
.grid-element:hover {
  transform: scale(1.05); /* 点击/悬浮时轻微放大 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 添加阴影增强立体感 */
  cursor: pointer;
}

/* 若需点击时背景色变化，可单独定义 */
.grid-element.clicked {
}

/* .element-info-up 内部：水平行排列 */
::v-deep .element-info-up {
  display: flex;
  flex-direction: row;
  width: 100%; /* 确保容器宽度 */
  height: 30px;
  padding-top: 2%;
}
::v-deep .element-info-up .element-number {
  display: inline-block;
  width: 40%;
  text-align: left;
  overflow: hidden;
  text-overflow: ellipsis; /* 防止内容过长 */
  padding-left: 2%;

  text-align: center;
}
::v-deep .element-info-up .element-number-mid {
  display: inline-block;
  width: 100%;
  overflow: hidden;
  text-overflow: ellipsis; /* 防止内容过长 */
  padding-left: 2%;

  text-align: center;
}
::v-deep .element-info-up .element-symbol {
  display: inline-block;
  width: 45%;
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-right: 2%;
}
::v-deep .element-symbol-small {
  justify-content: center;
  text-align: center;
  height: 100%;
  width: 100%;
}
::v-deep .element-info-mid .element-symbol-mid {
  display: inline-block;
  width: 100%;
  text-align: center;
  font-size: clamp(12px, 3vw, 20px);
}
::v-deep .element-info-mid {
  height: 50px;
  display: flex;
  flex-direction: column; /* 垂直排列子元素 */
  justify-content: center; /* 垂直方向居中（主轴居中） */
  align-items: center; /* 水平方向居中（交叉轴居中） */
}
::v-deep .element-info-mid .element-chineseName {
  font-size: clamp(12px, 3vw, 23px);
}

.period-row {
  margin-bottom: 5px;
}

::v-deep .element-type-sample {
  font-size: clamp(6px, 3vw, 16px);
  justify-content: center;
  align-items: center;
  text-overflow: ellipsis;
}
::v-deep .element-type-sample-large {
  font-size: clamp(6px, 3vw, 16px);
  justify-content: center;
  align-items: center;
  text-overflow: ellipsis;
}
::v-deep .element-type-sample-mid {
  font-size: clamp(6px, 3vw, 10px);
  justify-content: center;
  align-items: center;
  text-overflow: ellipsis;
}
::v-deep .element-type-sample-small {
  font-size: clamp(6px, 3vw, 8px);
  justify-content: center;
  align-items: center;
  text-overflow: ellipsis;
}

::v-deep .nide-sample {
  font-size: clamp(6px, 3vw, 16px);
  justify-content: center;
  align-items: center;
}
::v-deep .nide-sample-mid {
  font-size: clamp(6px, 3vw, 10px);
  justify-content: center;
  align-items: center;
}
::v-deep .nide-sample-small {
  font-size: clamp(6px, 3vw, 8px);
  justify-content: center;
  align-items: center;
}
</style>
