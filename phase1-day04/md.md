# Phase 1 Day 4：Python 异步编程（asyncio） + TypeScript Async/Await 进阶

**日期**：第 4 天  
**目标**：  
- Python：掌握 `asyncio`、`await`、`async def`，理解异步编程思想，能编写并发任务（为后续 FastAPI 异步 API 打基础）。  
- TypeScript：深入 Async/Await、Promise 类型处理，并与 Python 异步进行对比。  
- 总时长建议：4-6 小时（Python 主线 3-4h + TypeScript 1-2h）

**为什么今天学异步？**  
FastAPI 是异步框架，后续 Phase 3 调用 LLM API、Phase 4 做 RAG 时，大量操作（网络请求、文件读写、数据库查询）都需要异步处理。早掌握，早受益。

---

## 一、Python 部分（主线 · 推荐 3-4 小时）

### 1. 核心知识点

- `async def` 定义异步函数
- `await` 等待异步操作完成
- `asyncio.run()` 运行异步程序
- `asyncio.gather()` 并发执行多个任务（最常用）
- `asyncio.sleep()` 模拟耗时操作
- 异步 vs 同步性能对比

### 2. 完整案例代码（保存为 `day4_async_python.py`）
