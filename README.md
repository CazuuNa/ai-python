
## 一、需要掌握的核心技能知识

### 1. 编程基础（前端已有 JS/TS 优势）
- Python（语法、OOP、异步、Pydantic）
- FastAPI（高性能后端 API 框架）
- TypeScript 进阶（Zod 结构化输出）

### 2. AI 核心概念与理论（应用层为主，非训练模型）
- LLM 原理：Token、Embedding、上下文窗口、Prompt Engineering（角色、Few-shot、CoT、ReAct）
- RAG（检索增强生成）：向量数据库 + 知识注入
- Agent & Tools：LangChain/LangGraph、Function Calling、MCP 协议
- Memory 管理：短时/长时记忆、对话历史
- 多模态：文本+图像+语音基础处理

### 3. 技术栈与框架
- **前端 AI**：Next.js + Vercel AI SDK（流式 UI、useChat）、Transformers.js / TensorFlow.js（浏览器端 AI）
- **后端 AI**：LangChain.js / LangChain Python、LlamaIndex、Hugging Face
- **向量数据库**：Chroma（本地）、Pinecone/Qdrant（云）
- **部署与工程化**：Docker、Vercel/AWS、Streamlit/Gradio 快速原型、MLOps 基础（监控、CI/CD）

### 4. 软技能与工程思维
- AI 架构设计（前端 → API → LLM → 向量 DB）
- 成本/性能优化（Token 预算、Prompt 缓存、模型路由）
- 安全与合规（数据脱敏、工具权限控制）
- 项目实战能力（至少 4 个完整 AI 应用）

## 二、学习资源总览（持续更新）
- **Python**：Python 官方教程 + freeCodeCamp Python（Bilibili）
- **AI 基础**：Fast.ai《面向程序员的深度学习》、Google 生成式 AI 学习路径
- **Prompt**：Learn Prompting（中文版）
- **LangChain**：官方文档 + LangGraph 教程
- **Vercel AI SDK**：sdk.vercel.ai/docs
- **项目**：Ollama 本地测试、火山引擎/DeepSeek API（免费）
- **社区**：掘金 AI 专栏、GitHub（LangChain 示例、Dify/Coze）

## 三、90天精确到天日程表（每周日复盘 + 周末小项目）

### **Phase 1: Python & 后端基础（Day 1-14）** —— 打牢编程底座
- **Day 1**：Python 环境 + 语法基础（变量、数据类型、控制流）—— 完成 Python 教程前 3 章，练习 10 道 LeetCode Easy
- **Day 2**：函数、OOP（类、继承、封装）—— 写一个简单 CLI 工具
- **Day 3**：模块、包、文件操作、异常处理
- **Day 4**：异步编程（asyncio）、列表推导式、高级特性
- **Day 5**：Pydantic + FastAPI 入门（路由、请求体）
- **Day 6**：FastAPI 进阶（依赖注入、响应模型、错误处理）
- **Day 7**：数据库集成（SQLAlchemy + SQLite/PostgreSQL）
- **Day 8-9**：完整 CRUD API 项目（Todo List with FastAPI）
- **Day 10**：Docker 容器化 Python 服务
- **Day 11**：测试（Pytest）+ CI/CD 基础（GitHub Actions）
- **Day 12-13**：项目实战——构建一个简单的 REST API 服务
- **Day 14**：周复盘 + 优化代码，GitHub 提交

### **Phase 2: AI 基础概念 & Prompt Engineering（Day 15-28）**
- **Day 15**：LLM 概念（Token、Embedding、Transformer 入门）
- **Day 16**：Prompt Engineering 基础（角色设定、Few-shot）
- **Day 17**：Chain of Thought (CoT)、ReAct 提示技巧
- **Day 18**：本地 LLM 测试（Ollama 安装 + DeepSeek-R1 运行）
- **Day 19**：API 调用实践（OpenAI / DeepSeek SDK）
- **Day 20**：流式输出（SSE/WebSocket）实现
- **Day 21-22**：Memory 管理（历史对话拼接 + 摘要）
- **Day 23**：工具调用（Function Calling）基础
- **Day 24-25**：小项目——AI 聊天机器人（Node.js/Express 或 FastAPI + SSE）
- **Day 26-27**：Prompt 优化 + 结构化输出（Zod / Pydantic）
- **Day 28**：周复盘 + 对比不同 Prompt 效果

### **Phase 3: LLM API & 基础 AI 应用（Day 29-42）**
- **Day 29**：Hugging Face 模型仓库使用
- **Day 30**：浏览器端 AI（Transformers.js / TensorFlow.js 入门）
- **Day 31**：Vercel AI SDK 集成（Next.js + useChat）
- **Day 32-33**：流式 UI + 实时 Markdown 渲染项目
- **Day 34**：多模态入门（图像/语音简单处理）
- **Day 35-37**：完整项目——AI 编程助手（Prompt + Memory + Tools）
- **Day 38-39**：Agent 基础（ReAct 循环）
- **Day 40**：MCP 协议入门（工具发现与调用）
- **Day 41**：成本控制与 Token 优化
- **Day 42**：周复盘 + 部署第一个 AI 聊天 App 到 Vercel

### **Phase 4: LangChain / RAG / Agent 进阶（Day 43-56）**
- **Day 43-44**：LangChain 核心（Chains、Agents、Memory）
- **Day 45-46**：向量数据库（Chroma 本地 + Pinecone 云）
- **Day 47-49**：RAG 完整实现（文档加载 → 嵌入 → 检索 → 生成）
- **Day 50-52**：LangGraph 构建复杂 Agent 工作流
- **Day 53-54**：LlamaIndex 知识库项目
- **Day 55**：多 Agent 协同 + 人类介入
- **Day 56**：周复盘 + RAG 智能客服项目（含 PDF/网页知识库）

### **Phase 5: 全栈 AI 集成（Day 57-70）**
- **Day 57-59**：Next.js + FastAPI 全栈架构（前后端分离）
- **Day 60-62**：Vercel AI SDK + LangChain.js 结合
- **Day 63-65**：Agentic UI（动态生成界面、思考过程可视化）
- **Day 66-67**：多模态交互（图像上传 + 分析）
- **Day 68-69**：完整项目——AI Agent 平台（拖拽式工作流原型）
- **Day 70**：周复盘 + 性能优化

### **Phase 6: 部署、MLOps & 工程化（Day 71-77）**
- **Day 71**：Docker + Triton / vLLM 模型服务化
- **Day 72**：云部署（Vercel + AWS / 阿里云）
- **Day 73**：监控（LangSmith / Prometheus + Grafana）
- **Day 74**：CI/CD + 模型版本管理
- **Day 75**：安全（数据脱敏、工具权限）
- **Day 76**：成本与 scaling 优化
- **Day 77**：周复盘 + 部署所有项目

### **Phase 7: 高级主题 & Capstone 项目（Day 78-90）**
- **Day 78-80**：Fine-tuning 基础（LoRA 概念 + Llama-Factory 体验）
- **Day 81-83**：Capstone 项目 1 —— 企业级 RAG 文档助手（完整上线）
- **Day 84-86**：Capstone 项目 2 —— 多 Agent 智能工作流平台
- **Day 87-88**：Capstone 项目 3 —— 浏览器端 + 云端混合 AI 应用
- **Day 89**：简历项目整理 + 面试题准备（Prompt、RAG、Agent 常见问题）
- **Day 90**：总复盘 + 未来学习路径（MCP 生态、AI IDE、垂直领域深耕） + 分享到 GitHub / 掘金

**结语**：90 天后，你已具备前端 + AI 应用开发完整能力。持续迭代项目，关注 Dify/Coze/Cursor 等产品动态。保持好奇心，深耕 1-2 个垂直领域（如 AIGC 工具、智能客服）。
