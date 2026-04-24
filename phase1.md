# Phase 1：Python & 后端基础 详细学习内容（14天精确到天计划）

**适用人群**：有 HTML/CSS/JS/TS/React/Vue 基础的前端开发者  
**目标**：快速掌握 Python 后端开发（FastAPI），同时进阶 TypeScript，为后续 AI 应用全栈（LangChain Python + Vercel AI SDK）打下坚实基础。  
**学习原则**：  
- **每天 4-6 小时**：Python 主线 3-4h + TypeScript 辅助线 1-2h（并行学习，利用前端 TS 优势快速进阶）  
- **项目驱动**：每天写代码、Git 提交，逐步构建一个 Todo List CRUD API（Python） + TS 结构化验证工具  
- **工具准备**：Python 3.12+、VS Code + Cursor、FastAPI、Pydantic、Zod（TS）、Docker、PostgreSQL/SQLite  
- **资源优先**：2026 年最新免费/中文资源（FastAPI 官方中文文档、B站实战课、TS Handbook）  
- **考核标准**：Day 14 能独立部署一个 FastAPI CRUD 服务 + TS Zod 结构化输出示例到 GitHub  

---

## 一、两个学习线路说明

### **1. Python 学习线路（主线 · 14天）**  
**为什么重点学 Python？**  
- AI 应用后端（LangChain、LlamaIndex、RAG、Agent）生态以 Python 为主，2026 年 FastAPI 仍是高性能 AI API 首选框架（性能优于 Flask，支持异步、Pydantic 自动验证、自动 Swagger 文档）。  
- 前端转 AI 需补齐后端能力，FastAPI 上手快、与 TS 生态高度互补。  

**核心内容**：Python 语法 → OOP → 异步 → FastAPI 全栈后端（路由、依赖注入、数据库、Docker）。  

### **2. TypeScript 学习线路（辅助线 · 14天并行）**  
**为什么同时进阶 TypeScript？**  
- 你已有 TS 基础，本线路聚焦 **AI 应用专用进阶**：Zod（结构化输出，替代 Python Pydantic）、Generics、高级类型、Node.js/Next.js AI 后端准备（Vercel AI SDK v6  heavily 依赖 TS + Zod）。  
- 后续 Phase 3-5 会大量使用 Vercel AI SDK（TS 工具包），提前掌握可无缝衔接。  

**核心内容**：TS 高级类型 → Zod 实战 → TS + Node 轻量后端（为 AI SDK 铺路）。  

**学习建议**：Python 是每天主战场，TypeScript 每天 1-2h 穿插（早晚各 1h），利用已有的 TS 经验快速完成。

---

## 二、14天精确到天详细日程表（Python + TypeScript 并行）

**每日模板**：  
- **上午/主线（3h）**：Python 理论 + 编码  
- **下午/辅助线（1-2h）**：TypeScript 进阶 + 小练习  
- **晚上（1h）**：复盘 + Git 提交 + 记录问题  
- **资源链接**：全部 2026 年最新可访问（官方文档 + B站免费课）  

### **Day 1**  
**Python**：环境搭建 + 语法基础（变量、数据类型、控制流、函数）  
- 安装 Python 3.12 + pip + virtualenv  
- 完成 Python 官方教程前 3 章（https://docs.python.org/zh-cn/3/tutorial/）  
- 练习：10 道 LeetCode Easy（Python）  
**TypeScript**：复习高级类型基础（Type、Interface、Union/Intersection）  
- 资源：TypeScript Handbook（中文版）https://www.typescriptlang.org/zh/docs/handbook/  
- 练习：重构一个前端项目中的类型定义  
**输出**：GitHub 创建仓库 `ai-backend-phase1`，提交 `hello.py` 和 `types.ts`

### **Day 2**  
**Python**：OOP（类、继承、封装、魔术方法） + 模块/包  
- 资源：B站《Python 从入门到精通》（2026 更新版）第 4-5 章  
- 练习：编写一个 CLI 工具类（TodoItem 类）  
**TypeScript**：Generics + Utility Types（Partial、Pick、Omit）  
- 练习：实现一个泛型 Hook `useLocalStorage<T>`  
**输出**：提交 OOP 示例代码

### **Day 3**  
**Python**：文件操作、异常处理、列表/字典推导式  
- 练习：读写 JSON 文件实现简单配置管理  
**TypeScript**：Decorators（实验性） + 类型守卫  
- 资源：TS 进阶文档 + Zod 准备（提前看 Zod 官网 https://zod.dev）  
- 练习：用 decorator 实现简单日志  
**输出**：文件操作脚本 + TS decorator 示例

### **Day 4**  
**Python**：异步编程（asyncio、await、aiohttp 基础）  
- 资源：FastAPI 官方文档异步部分（https://fastapi.tiangolo.com/async/）  
- 练习：异步爬取 3 个网页标题  
**TypeScript**：Async/Await 进阶 + Promise 类型  
- 练习：用 TS 重写 Day 4 Python 异步任务  
**输出**：异步脚本对比 Python vs TS

### **Day 5**  
**Python**：FastAPI 入门（路由、请求体、响应模型、Pydantic）  
- 资源：**2026 推荐** FastAPI 官方教程（中文版）https://fastapi.tiangolo.com/tutorial/ + 掘金《2026版 FastAPI 框架快速搭建》  
- 练习：搭建第一个 `/hello` 接口 + Swagger 自动文档  
**TypeScript**：Zod 入门（schema 定义、parse、infer）  
- 资源：Zod 官方文档（https://zod.dev）  
- 练习：用 Zod 定义 User Schema（替代 Pydantic）  
**输出**：FastAPI hello world + Zod schema

### **Day 6**  
**Python**：FastAPI 进阶（Path/Query 参数、依赖注入、错误处理、CORS）  
- 资源：B站《FastAPI 从入门到实战》（2026 版）  
- 练习：实现带参数的 Todo API  
**TypeScript**：Zod 进阶（.extend、.refine、 discriminated unions）  
- 练习：构建复杂 AI Prompt Schema  
**输出**：带依赖注入的 FastAPI 接口

### **Day 7**  
**Python**：数据库集成（SQLAlchemy + SQLite/PostgreSQL + Pydantic 模型）  
- 资源：FastAPI 官方 SQLAlchemy 教程  
- 练习：Todo CRUD 数据库版  
**TypeScript**：Prisma / Drizzle ORM 对比（或直接用 Zod + in-memory）  
- 练习：用 Zod + TS 实现内存数据库 CRUD  
**输出**：数据库 CRUD（Python 主）

### **Day 8-9**  
**Python**：完整 CRUD 项目（Todo List with FastAPI + SQLAlchemy）  
- 资源：Udemy《FastAPI 2026 年完整課程》（免费试看部分）或官方示例  
- Day 8：实现所有 CRUD + 自动文档  
- Day 9：添加分页、搜索、认证基础（JWT 可选）  
**TypeScript**：用 Zod 验证所有请求体 + 构建 TS 版 Todo 类型系统  
- 练习：写一个 `validateRequest` 高阶函数  
**输出**：完整 Todo API（Day 9 提交主分支）

### **Day 10**  
**Python**：Docker 容器化（Dockerfile + docker-compose + PostgreSQL）  
- 资源：FastAPI 官方 Docker 部署教程  
- 练习：打包 Todo API 并本地运行  
**TypeScript**：TS 项目 Docker 化（Node.js + ts-node 或 Next.js）  
- 练习：为后续 Vercel AI SDK 准备 Dockerfile  
**输出**：Dockerized Python 服务

### **Day 11**  
**Python**：测试（Pytest + FastAPI TestClient） + 基础 CI/CD（GitHub Actions）  
- 练习：为 3 个接口写单元测试  
**TypeScript**：Jest + Zod 测试 + TS 类型测试  
- 练习：测试 Zod schema  
**输出**：测试覆盖 + GitHub Actions YAML

### **Day 12-13**  
**Python**：项目实战优化 + 性能调优（异步、缓存、限流）  
- 练习：为 Todo API 添加 Redis 缓存（可选）  
**TypeScript**：集成 Vercel AI SDK 预习（安装 `ai` + `@ai-sdk/openai` + Zod）  
- 资源：Vercel AI SDK 官方文档（2026 v6）https://ai-sdk.dev/docs  
- 练习：用 `generateObject` + Zod 实现结构化输出示例  
**输出**：优化后完整项目 + TS AI SDK 小 demo

### **Day 14**  
**Python + TypeScript**：周复盘 + 项目部署 + 总结  
- Python：部署 Todo API 到 Render / Railway（免费）  
- TypeScript：将 Zod 示例部署到 Vercel  
- 复盘：写一篇 Notion 笔记（遇到的问题、Pydantic vs Zod 对比、FastAPI 优势）  
- 考核：GitHub README 包含运行截图 + Swagger 链接  
**输出**：完整 Phase 1 项目仓库 + 复盘文档

---

## 三、推荐资源总览（2026 最新）

**Python 线路**：  
- 官方文档（首选）：https://fastapi.tiangolo.com/zh/  
- B站免费实战：搜索“FastAPI 从入门到实战 2026”  
- 掘金进阶：https://juejin.cn/post/7618916358924419113 （2026版快速搭建）  
- 进阶书籍：《FastAPI 开发实战》（2025/2026 版）  

**TypeScript 线路**：  
- TS 官方 Handbook：https://www.typescriptlang.org/zh/docs/handbook/  
- Zod 官方（AI 必备）：https://zod.dev  
- Vercel AI SDK 预习：https://ai-sdk.dev/docs（v6 已支持更多模型 + 结构化输出）  

**通用工具**：  
- Cursor / GitHub Copilot 辅助编码  
- Postman / Swagger 测试 API  
- GitHub 仓库模板：https://github.com/（搜索 fastapi-template + ts-zod）

---

## 四、XMind 思维导图结构（直接复制到 XMind）


