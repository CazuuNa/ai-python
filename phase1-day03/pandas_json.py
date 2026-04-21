# pd.read_json() 读取 JSON 文件 => DataFrame  加载数据集，API返回，配置文件
import json
from pathlib import Path

import pandas as pd

# 一个实验记录json
data = {
    "experiments": [
        {
            "exp_id": "exp001",
            "model": "Qwen2-7B",
            "lr": 2e-5,
            "batch_size": 8,
            "metrics": {"accuracy": 0.912, "f1": 0.905, "loss": 0.234},
            "status": "completed",
        },
        {
            "exp_id": "exp002",
            "model": "Llama-3-8B",
            "lr": 1e-5,
            "batch_size": 16,
            "metrics": {"accuracy": 0.935, "f1": 0.928, "loss": 0.187},
            "status": "completed",
        },
    ]
}

# 先保存为文件（演示用）
Path("phase1-day03/experiments.json").write_text(
    json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
)

# 读取方式一：直接读取嵌套列表（推荐先 normalize）
df = pd.read_json(
    "phase1-day03/experiments.json", orient="records"
)  # 如果是列表直接在根
# 但上面例子是 {"experiments": [...] }，所以需要这样读：
with open("phase1-day03/experiments.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

df = pd.json_normalize(raw["experiments"])  # 后面会详细讲
print(df)

# pd.to_json() DataFrame => JSON 文件/字符串  保存处理后的数据集、导出给前端/模型

# 创建一个 DataFrame（模拟模型评估结果）
df = pd.DataFrame(
    {
        "model": ["Qwen2-7B", "Llama-3-8B", "Gemma-2-9B"],
        "accuracy": [0.912, 0.935, 0.898],
        "f1_score": [0.905, 0.928, 0.887],
        "inference_time_ms": [45.2, 62.1, 38.7],
        "parameters_billions": [7.0, 8.0, 9.0],
    }
)

# 最常用：保存为 records 格式（每行一个对象）
df.to_json(
    "model_results_records.json",
    orient="records",  # AI 中最常用
    force_ascii=False,
    indent=2,
)

# 其他常用 orient 参数（AI 场景推荐）
df.to_json("model_results_split.json", orient="split")  # 适合大文件传输
df.to_json("model_results_table.json", orient="table")  # 带 schema，推荐给前端
df.to_json("model_results_values.json", orient="values")  # 纯数组，适合数值计算

print("已保存多种 JSON 格式")


# pd.json_normalize() 从 JSON 嵌套结构中提取数据  处理 API 返回的嵌套结构、COCO 标注、日志

# 模拟 OpenAI Chat Completion + 工具调用返回的嵌套 JSON
nested_data = [
    {
        "id": "chat_001",
        "model": "gpt-4o",
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "推荐使用 json_normalize 处理嵌套数据。",
                    "tool_calls": [
                        {"name": "search_web", "args": {"query": "pandas json"}}
                    ],
                },
                "finish_reason": "tool_calls",
            }
        ],
        "usage": {"prompt_tokens": 28, "completion_tokens": 12, "total_tokens": 40},
        "timestamp": "2026-04-21T15:30:00Z",
    }
]

# 直接展开
df_flat = pd.json_normalize(
    nested_data,
    record_path="choices",  # 展开列表字段
    meta=["id", "model", "timestamp", "usage"],  # 保留上层字段
    meta_prefix="meta_",  # 加前缀避免冲突
    record_prefix="choice_",
)

print(df_flat.columns)
# 输出示例列：id, model, choice_message.role, choice_message.content, choice_message.tool_calls, usage.total_tokens ...

# pd.read_json(...,lines=True) 读取 JSON 行数据  处理日志文件、多条 JSON 数据

"""
小中型数据：直接用 pd.read_json(lines=True) 或 json_normalize
超大 JSONL（GB 级别）：推荐使用 jsonlines 库 + 分批处理，或 Dask / Polars
始终指定：encoding="utf-8"、force_ascii=False
嵌套字段多时：先用 json_normalize(max_level=...) 限制层级
保存给模型训练：优先使用 orient="records", lines=True（jsonl）

读取普通 JSON → pd.read_json() + json_normalize()
读取对话/日志数据集 → pd.read_json(..., lines=True)
展开嵌套 → pd.json_normalize()（必会技能）
保存训练数据 → df.to_json(..., orient="records", lines=True)
后续分析 → DataFrame 的所有强大功能（groupby、merge、plot 等）
"""
