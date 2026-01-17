// types.ts
export interface User {
  id: number;
  name: string;
  email: string;
}

export interface Post {
  id: number;
  title: string;
  content: string;
  userId: number;
}

export interface Error {
  code: number;
  message: string;
}

export interface ApiResponse<T> {
  data: T;
  error: Error | null;
}

export enum ApiEndpoints {
  USERS = '/users',
  POSTS = '/posts',
}

export type ApiResponseCallback<T> = (response: ApiResponse<T>) => void; 

export interface NavigationProps {
  navigation: any;
  route: any;
}