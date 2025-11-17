// types/user.ts
export interface UserInfo {
  id: number;
  username: string;
  email: string;
  is_active: boolean;
  created_at: string; // 后端 datetime 通常返回字符串（如 "2025-11-17T12:34:56Z"）
}