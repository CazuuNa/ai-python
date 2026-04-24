# Python asyncio 异步编程实战 - 模拟 AI 学习任务并发执行

import asyncio
import time
from typing import List


# ==================== 1. 基本异步函数 ====================
async def simulate_learning_task(task_name: str, seconds: float) -> str:
    """模拟一个学习任务（比如调用 LLM、读取文档等）"""
    print(f"🚀 开始任务: {task_name} （预计耗时 {seconds} 秒）")
    await asyncio.sleep(seconds)  # 模拟 IO 等待（网络、文件、API 调用）
    result = f"✅ 任务 [{task_name}] 完成！"
    print(result)
    return result


# ==================== 2. 同步 vs 异步对比 ====================
def sync_learning(tasks: List[str]):
    """同步方式执行（串行）"""
    print("\n=== 同步执行（串行） ===")
    start = time.time()

    for task in tasks:
        # 模拟同步耗时
        time.sleep(1.5)
        print(f"✅ 同步完成: {task}")

    end = time.time()
    print(f"同步总耗时: {end - start:.2f} 秒\n")


async def async_learning(tasks: List[str]):
    """异步方式执行（并发）"""
    print("=== 异步执行（并发） ===")
    start = time.time()

    # 创建任务列表
    task_coroutines = [simulate_learning_task(f"学习 {task}", 1.5) for task in tasks]

    # 并发执行所有任务
    results = await asyncio.gather(*task_coroutines)

    end = time.time()
    print(f"异步总耗时: {end - start:.2f} 秒")
    print(f"完成任务数量: {len(results)}")
    return results


# ==================== 3. 实际 AI 场景模拟 ====================
async def fetch_llm_response(prompt: str) -> str:
    """模拟调用 LLM API（异步网络请求）"""
    print(f"📡 正在调用 LLM 处理提示词: {prompt[:30]}...")
    await asyncio.sleep(2.0)  # 模拟网络延迟
    return f"LLM 回复: 你好！这是一个关于 '{prompt}' 的智能回答。"


async def process_multiple_prompts():
    """并发处理多个 Prompt（真实 AI 应用常见场景）"""
    prompts = [
        "解释什么是 RAG",
        "如何用 FastAPI 构建 AI 接口",
        "LangChain Agent 是什么",
        "Prompt Engineering 最佳实践",
    ]

    print("\n=== 并发处理多个 LLM Prompt ===")
    start = time.time()

    # 并发调用
    responses = await asyncio.gather(*[fetch_llm_response(p) for p in prompts])

    end = time.time()
    print(f"\n全部 Prompt 处理完成！总耗时: {end - start:.2f} 秒\n")

    for i, resp in enumerate(responses, 1):
        print(f"Prompt {i} 结果:\n{resp}\n")


# ==================== 主函数 ====================
async def main():
    print("=== Day 4 Python 异步编程实战 ===\n")

    tasks = ["Python 基础", "FastAPI", "异步编程", "Prompt Engineering"]

    # 1. 同步对比
    sync_learning(tasks)

    # 2. 异步执行
    await async_learning(tasks)

    # 3. AI 真实场景模拟
    await process_multiple_prompts()


# 运行异步程序
if __name__ == "__main__":
    asyncio.run(main())
