// src/store/userStore.ts
import { defineStore } from "pinia";
import axios from "axios"; // 导入全局 axios（用于 isAxiosError 静态方法）
import api from "@/utils/axios"; // 导入配置好的 Axios 实例（用于发请求）
import type { ChemicalElementInfo } from "@/types/chemicalelement"; // 类型导入用 import type

interface ChemicalElementState {
  chemicalElementInfo: ChemicalElementInfo | null;
  allElements: ChemicalElementInfo[]; // 全量元素数组
  isLoading: boolean;
  error: string | null;
}

export const useChemicalElementStore = defineStore("chemicalElement", {
  state: (): ChemicalElementState => ({
    chemicalElementInfo: null,
    allElements: [],
    isLoading: false,
    error: null,
  }),

  actions: {
    async fetchChemicalElementInfo(
      elecmentId: number
    ): Promise<ChemicalElementInfo> {
      try {
        this.isLoading = true;
        this.error = null;
        this.chemicalElementInfo = null;

        // 直接使用相对路径（基础路径已配置）
        const response = await api.get("/api/v1/chemical/element/info", {
          params: { element_id: elecmentId },
        });

        // 此时 response.data 是后端返回的用户数据，而非 HTML
        const chemicalElementData = response.data as ChemicalElementInfo;
        this.chemicalElementInfo = chemicalElementData;
        return chemicalElementData;
      } catch (err) {
        // 正确：用全局 axios 调用 isAxiosError
        if (axios.isAxiosError(err)) {
          // 这里改 api 为 axios
          this.error = err.response?.data?.detail || "获取用户信息失败";
        } else {
          this.error = "网络异常，请检查后端是否启动";
        }
        throw err;
      } finally {
        this.isLoading = false;
      }
    },

    async fetchAllChemicalElements(): Promise<ChemicalElementInfo[]> {
      try {
        this.isLoading = true;
        this.error = null;
        this.allElements = []; // 清空原有数据

        // 调用获取全量数据的API（无需筛选参数）
        // 注意：后端需要有对应的接口（如 /api/v1/chemical/elements）返回所有元素
        const response = await api.get("/api/v1/chemical/element/all");

        // 假设后端返回格式为 { data: [...] } 或直接返回数组
        const allData = response.data as ChemicalElementInfo[];
        this.allElements = allData; // 存储全量数据
        return allData;
      } catch (err) {
        if (axios.isAxiosError(err)) {
          this.error = err.response?.data?.detail || "获取全量元素数据失败";
        } else {
          this.error = "网络异常，请检查后端是否启动";
        }
        throw err;
      } finally {
        this.isLoading = false;
      }
    },

    resetUserInfo(): void {
      this.chemicalElementInfo = null;
      this.error = null;
    },
  },
});
