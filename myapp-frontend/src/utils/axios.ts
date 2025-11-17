// src/utils/axios.ts
import axios from 'axios';

// 创建 Axios 实例，配置后端基础路径
const api = axios.create({
  baseURL: 'http://localhost:8000', // 后端 FastAPI 地址（必须正确）
  timeout: 5000, // 超时时间
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;