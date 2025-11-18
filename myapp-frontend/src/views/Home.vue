<script setup lang="ts">
import { ref, onMounted } from "vue";
import { ElSelect, ElOption } from "element-plus";
import DataService from "../services/DataService.js";
import { useCounterStore } from "@/store/counter";
import { useUserStore } from "@/store/userStore";
import type { UserInfo } from "@/types/user";
import { useRoute } from "vue-router";
import { watch } from "vue";

const counter = useCounterStore();
const userStore = useUserStore();

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

// 点击事件处理（明确参数类型）
const handleGetUser = async (userId: number) => {
  try {
    await userStore.fetchUserInfo(userId);
  } catch (err) {
    // 处理错误
  }
};

// 按钮点击事件：调用 Store 中的 increment 方法
const handleIncrement = () => {
  counter.increment(); // 直接调用 actions 中的方法
};

// 可选：添加重置功能（需在 Store 中新增 reset 方法）
const handleReset = () => {
  counter.reset();
};

// 在<script setup>中，不需要定义setup()函数// 直接编写逻辑即可，变量会自动暴露给模板
// 初始化数据

// 定义数据类型（TypeScript 类型约束）
interface UserOption {
  id: number;
  name: string;
}

interface UserData {
  message: string;
  // 其他用户信息字段（根据实际接口返回补充）
  [key: string]: any; // 允许其他未知字段
}

// 初始化数据（指定类型，避免 any）
const message = ref<string>("");
const item = ref<UserData>({} as UserData); // 初始化为空对象并断言类型

// 选项数据（明确类型）
const options: UserOption[] = [
  { id: 1, name: "用户1" },
  { id: 2, name: "用户2" },
  { id: 3, name: "用户3" },
  { id: 4, name: "用户4" },
  { id: 5, name: "用户5" },
];

// 选中的值（类型为 number | ""，因为选项id是number，初始为空字符串）
const selectedId = ref<number | "">("");
const title = "FastAPI+Vue+Vite hello!!";
// 定义异步函数（参数指定类型）
const fetchData = async (id: number) => {
  try {
    const response = await DataService.getData(id);
    // 假设接口返回格式为 { data: { message: string, ... } }

    item.value = response.data;
    message.value = `用户${id}的信息已获取`;
  } catch (error) {
    console.error("获取数据失败：", error);
    message.value = "获取数据失败，请重试"; // 错误提示
  }
};

// 处理选择变化（兼容初始空值）
const handleSelectChange = () => {
  if (selectedId.value) {
    fetchData(selectedId.value); // 只有选中有效id时才请求
    handleGetUser(selectedId.value); // 只有选中有效id时才请求
  } else {
    // 清空选择时重置数据
    item.value = {} as UserData;
    message.value = "未选择用户";
  }
};

const route = useRoute();
// 判断是否有子路由内容需要渲染
const hasRouteContent = ref(false);

// 初始化时检查
const checkRouteContent = () => {
  // 根路由的层级是 0，若 matched 长度 > 1，说明有子路由匹配
  // 例如：访问 /math 时，matched 包含 [根路由, /math]，长度为 2 > 1 → 有内容
  // 访问 / 时，matched 仅包含 [根路由]，长度为 1 → 无内容
  hasRouteContent.value = route.matched.length > 1;
};

// 初始检查一次
checkRouteContent();

// 监听路由变化，动态更新状态
watch(
  () => route.path,
  () => {
    checkRouteContent();
  }
);
</script>

<template>
  <template v-if="hasRouteContent">
    <!-- 子路由组件将在这里渲染 -->
    <router-view />
  </template>
  <template v-else>
    <div class="hello">
      <h1>{{ title }}</h1>

      <div>
        <label>选择用户：</label>
        <!-- 使用 Element Plus 的 ElSelect 更美观，且兼容 TS -->
        <ElSelect
          v-model="selectedId"
          placeholder="请选择用户"
          @change="handleSelectChange"
        >
          <ElOption
            v-for="opt in options"
            :key="opt.id"
            :label="opt.name"
            :value="opt.id"
          />
        </ElSelect>
      </div>
      <h2>直接获取到的用户信息：</h2>
      <p v-if="Object.keys(item).length">{{ item }}</p>
      <p v-else-if="selectedId">暂无用户信息</p>
      <hr />
      <div class="user-detail">
        <h2>pinia获取到用户详情</h2>
        <div v-if="userStore.isLoading">加载中...</div>
        <div v-else-if="userStore.error" class="error">
          {{ userStore.error }}
        </div>
        <div v-else-if="userStore.userInfo">
          <p>
            ID: {{ userStore.userInfo.id }}，用户名:
            {{ userStore.userInfo.username }}，email:
            {{ userStore.userInfo.email }}，是否激活:
            {{ userStore.userInfo.is_active }}，创建时间:
            {{ userStore.userInfo.created_at }}
          </p>

          <!-- 其他字段 -->
        </div>
      </div>
    </div>
    <hr />
    <!-- 添加按钮，点击触发 increment 函数 -->
    <button @click="handleIncrement">点击加 1</button>

    <!-- 可选：添加一个重置按钮 -->
    <button @click="handleReset" style="margin-left: 10px">重置计数</button>
    <div>Current Count: {{ counter.count }}</div>
  </template>
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
