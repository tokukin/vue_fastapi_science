// src/store/userStore.ts
import { defineStore } from 'pinia';
import axios from 'axios'; // 导入全局 axios（用于 isAxiosError 静态方法）
import api from '@/utils/axios'; // 导入配置好的 Axios 实例（用于发请求）
import type { UserInfo } from '@/types/user'; // 类型导入用 import type

interface UserState {
  userInfo: UserInfo | null;
  isLoading: boolean;
  error: string | null;
}

export const useUserStore = defineStore('user', {
  state: (): UserState => ({
    userInfo: null,
    isLoading: false,
    error: null,
  }),

  actions: {
    async fetchUserInfo(userId: number): Promise<UserInfo> {
      try {
        this.isLoading = true;
        this.error = null;
        this.userInfo = null;

        // 直接使用相对路径（基础路径已配置）
        const response = await api.get('/api/v1/users/info', {
          params: { user_id: userId },
        });

        // 此时 response.data 是后端返回的用户数据，而非 HTML
        const userData = response.data as UserInfo;
        this.userInfo = userData;
        return userData;
      } catch (err) {
        // 正确：用全局 axios 调用 isAxiosError
        if (axios.isAxiosError(err)) {  // 这里改 api 为 axios
          this.error = err.response?.data?.detail || '获取用户信息失败';
        } else {
          this.error = '网络异常，请检查后端是否启动';
        }
        throw err;
      } finally {
        this.isLoading = false;
      }
    },

    resetUserInfo(): void {
      this.userInfo = null;
      this.error = null;
    },
  },
});