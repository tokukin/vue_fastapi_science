// src/router/index.ts
import { createRouter, createWebHistory } from "vue-router";
// 关键：使用 import type 导入 RouteRecordRaw 类型
import type { RouteRecordRaw } from "vue-router";

// 导入页面组件（按需导入）
import Home from "../views/Home.vue";

// 定义路由规则
const routes: RouteRecordRaw[] = [
  {
    path: "/", // 路由路径
    // name: "Home", // 路由名称（可选）
    component: () => import("../views/Home.vue"),
    meta: { title: "首页", breadcrumb: "首页" },
  },
  {
    path: "/math",
    name: "Math",
    component: () => import("../views/Math.vue"),
    meta: {
      title: "数学",
      breadcrumb: "数学",
      parentBreadcrumb: { path: "/", name: "首页" },
    },
  },
  {
    path: "/physics",
    name: "Physics",
    component: () => import("../views/Physics.vue"),
    meta: {
      title: "物理",
      breadcrumb: "物理",
      parentBreadcrumb: { path: "/", name: "首页" },
    },
  },
  {
    path: "/chemistry",
    name: "Chemistry",
    component: () => import("../views/Chemistry.vue"),
    meta: {
      title: "化学",
      breadcrumb: "化学",
      parentBreadcrumb: { path: "/", name: "首页" },
    },
    children: [],
  },
  {
    path: "/chemistry/periodic-table",
    name: "periodic-table",
    component: () => import("../views/ChemicalElements.vue"),
    meta: {
      title: "元素周期表",
      breadcrumb: "元素周期表",
      parentBreadcrumb: [
        { path: "/", name: "首页" }, // 第一层父级
        { path: "/chemistry", name: "化学" },
      ],
    },
  },
  ///chemistry/other
  {
    path: "/chemistry/other",
    name: "ChemicalElements",
    component: () => import("../views/che_test.vue"),
    meta: {
      title: "元素周期表",
      breadcrumb: "元素周期表_test",
      parentBreadcrumb: [
        { path: "/", name: "首页" }, // 第一层父级
        { path: "/chemistry", name: "化学" },
      ],
    },
  },

  {
    path: "/chemistry/element/:elementId",
    name: "ChemicalElementDetail",
    component: () => import("../views/ChemicalElementDetail.vue"),
    meta: { title: "元素详情", breadcrumb: "元素详情" },
  },

  {
    // 404 路由（放在最后）
    path: "/:pathMatch(.*)*", // 匹配所有未定义的路由
    name: "NotFound",
    component: () => import("../views/NotFound.vue"), // 懒加载 404 页面
    meta: {
      title: "404 未找到",
      breadcrumb: "404 未找到",
      parentBreadcrumb: { path: "/", name: "首页" },
    },
  },
];

// 创建路由实例
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL), // HTML5 历史模式（无 #）
  // history: createWebHashHistory(), // 哈希模式（带 #）
  routes, // 注入路由规则
});

export default router;

// 接上面的 router/index.ts
router.beforeEach((to, from, next) => {
  // 如果路由配置了 meta.title，则设置标题
  if (to.meta.title) {
    document.title = to.meta.title as string; // 类型断言为字符串
  } else {
    // 默认标题（可选）
    document.title = "元素周期表";
  }
  next(); // 必须调用 next() 继续导航
});
