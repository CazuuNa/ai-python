# Phase 1 Day 1：Python 基础语法 + TypeScript 高级类型复习

**日期**：第 1 天  
**目标**：  
- Python：快速搭建开发环境，掌握变量、数据类型、控制流、函数基础，能写简单脚本。  
- TypeScript：复习高级类型（Type、Interface、Union、Intersection），为后续 Zod + Vercel AI SDK 结构化输出做准备。  
- 总时长：4-6 小时（Python 3-4h + TypeScript 1-2h）  

**学习原则**：  
- 手敲代码，不要复制粘贴  
- 每写一段代码就运行测试  
- 用 Cursor / GitHub Copilot 辅助理解，但必须自己理解逻辑  
- 所有代码提交到 GitHub 仓库 `frontend-to-ai-phase1`

---

## 一、Python 部分（主线 · 推荐 3-4 小时）

### 1. 环境搭建（30-40 分钟）
1. 下载安装 **Python 3.12 或更高版本**（2026 年推荐 3.12+）
   - 官网：https://www.python.org/downloads/
   - 安装时勾选 **Add python.exe to PATH**
2. 验证安装：
   ```bash
   python --version
   # 或 python3 --version
   pip --version