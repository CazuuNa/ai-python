"""
并发模拟下载 写一个异步函数 download_file(url: str)，模拟下载 3 个不同文件，使用 asyncio.gather() 并发下载，最后打印总耗时。
异步任务队列 创建 5 个不同耗时的学习任务（耗时分别为 1s、2s、1.5s、3s、0.5s），并发执行并按完成顺序打印结果。
异常处理进阶 在 simulate_learning_task 中加入 try-except，捕获可能的异常并继续执行其他任务。的案例代码详细解释
"""

import asyncio
import time

loopStr = ["a", "b", "c", "d", "e"]


async def test():
    start_time = time.time()
    print("开始测试", start_time)
    # await asyncio.sleep(1)
    # end_time = time.time()
    # print("测试耗时", end_time, end_time - start_time)

    for i, item in enumerate(loopStr):
        time.sleep(1 + i)
        print(f"当前任务{item}完成")
    end_time = time.time()
    print(f"测试耗时 {end_time - start_time:.2f} 秒")


if __name__ == "__main__":
    asyncio.run(test())
