// Day 4: TypeScript Async/Await 进阶 + Promise

// 模拟耗时操作
function delay(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// 模拟学习任务（类似 Python 的 simulate_learning_task）
async function simulateLearningTask(taskName: string, seconds: number): Promise<string> {
    console.log(`🚀 开始任务: ${taskName} （预计耗时 ${seconds} 秒）`);
    await delay(seconds * 1000);
    const result = `✅ 任务 [${taskName}] 完成！`;
    console.log(result);
    return result;
}

// 并发处理多个任务（对应 asyncio.gather）
async function runConcurrentTasks() {
    const tasks = ["React 优化", "TypeScript 泛型", "FastAPI 集成", "Prompt 工程"];
    
    console.log("\n=== TypeScript 异步并发执行 ===");
    const start = Date.now();
    
    // Promise.all 并发执行
    const results = await Promise.all(
        tasks.map(task => simulateLearningTask(task, 1.5))
    );
    
    const end = Date.now();
    console.log(`\n所有任务完成！总耗时: ${(end - start) / 1000} 秒`);
    console.log("结果:", results);
}

// 模拟调用 LLM（真实 AI SDK 场景）
async function callLLM(prompt: string): Promise<string> {
    console.log(`📡 正在调用 LLM: ${prompt}`);
    await delay(2000);
    return `LLM 回复: "${prompt}" 的智能回答已生成。`;
}

async function processMultiplePrompts() {
    const prompts = [
        "什么是 RAG？",
        "LangChain 如何工作？",
        "如何优化 Token 消耗？"
    ];
    
    console.log("\n=== 并发处理多个 Prompt ===");
    const start = Date.now();
    
    const responses = await Promise.all(
        prompts.map(p => callLLM(p))
    );
    
    const end = Date.now();
    console.log(`\nPrompt 处理完成！总耗时: ${(end - start) / 1000} 秒`);
    
    responses.forEach((resp, i) => {
        console.log(`Prompt ${i + 1}:\n${resp}\n`);
    });
}

// 执行
async function main() {
    console.log("=== Day 4 TypeScript Async/Await 实战 ===\n");
    await runConcurrentTasks();
    await processMultiplePrompts();
}

main().catch(console.error);