# Phase 1 Day 3：Python 文件操作、异常处理、列表/字典推导式 + TypeScript Decorators 与类型守卫

**日期**：第 3 天  
**目标**：  
- Python：掌握文件读写、JSON 处理、异常处理机制，以及高效的列表/字典推导式，能处理实际配置文件和数据。  
- TypeScript：学习装饰器（Decorators）和类型守卫，为后续 FastAPI 风格的 TS 项目和 AI SDK 做准备。  
- 总时长建议：4-6 小时（Python 主线 3-4h + TypeScript 辅助 1-2h）

---

## 一、Python 部分（主线 · 推荐 3-4 小时）

### 1. 核心知识点

#### （1）文件操作（读、写、追加、上下文管理器）
- `open()` 函数：`r`, `w`, `a`, `r+` 等模式
- `with` 语句（推荐写法，自动关闭文件）
- 文本文件 vs 二进制文件

#### （2）JSON 处理（AI 开发中最常用）
- `json` 模块：`dump`、`dumps`、`load`、`loads`

#### （3）异常处理
- `try-except-else-finally`
- 常见异常：`FileNotFoundError`、`JSONDecodeError`、`ValueError` 等
- 自定义异常（可选进阶）

#### （4）列表推导式 & 字典推导式（Pythonic 写法）