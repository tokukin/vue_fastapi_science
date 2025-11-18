import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
// 导入路由配置
import router from "./router";

import { createPinia } from "pinia";
const pinia = createPinia();

// 导入 Element Plus 组件
import ElementPlus from "element-plus";
// 导入 Element Plus 样式（关键）
import "element-plus/dist/index.css";

import * as ElementPlusIconsVue from "@element-plus/icons-vue";

const app = createApp(App);
app.use(ElementPlus); // 全局注册组件
// // 全局注册 Element Plus 图标组件
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component);
}
//使用路由;
app.use(router);
app.use(pinia);
app.mount("#app");
