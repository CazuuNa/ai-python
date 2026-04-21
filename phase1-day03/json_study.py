"""
json模块常用函数
json.dumps()  # 将Python对象转换为JSON字符串        dict/list等 =》 str   API请求体，日志，缓存
json.loads()  # 将JSON字符串转换为Python对象        str =》 dict/list等   解析API返回结果
json.dump()  # 将Python对象写入文件                 dict/list等 =》 文件  保存config，数据集，checkpoint
json.load()  # 从文件读取JSON对象转为Python对象      文件 =》 dict/list等  加载数据集、配置文件
"""

# json.dumps()
import json
from datetime import datetime

# AI中最常见结构
data = {
    "mode_name": "Qwen2-7B-Instruct",
    "version": "1.0.0",
    "hyperparameters": {
        "learning_rate": 2e-5,
        "batch_size": 8,
        "epochs": 3,
        "use_lora": True,
    },
    "metrics": {"accuracy": 0.945, "f1_score": 0.932},
    "created_at": datetime.now().isoformat(),  # 时间必须转字符串
    "tags": ["chinese", "llm", "finetune"],
    "status": "training",
}

# 基础用法
json_str = json.dumps(data)
print(json_str)  # 一行紧凑格式
# 推荐写法
json_str_pretty = json.dumps(
    data,
    ensure_ascii=False,  # 不转义中文
    indent=2,  # 缩进2格
    separators=(",", ":"),  # 自定义分隔符 去掉空格
)
print(json_str_pretty)

# json.dump()
# 保存训练配置
config = {
    "experiment_name": "exp_2026_04",
    "dataset": "alpaca-zh-clean.jsonl",
    "model_path": "/models/Qwen2-7B",
    "output_dir": "./checkpoints",
    "wandb": True,
}

with open("phase1-day03/config.json", "w", encoding="utf-8") as f:
    json.dump(
        config,
        f,
        ensure_ascii=False,
        indent=2,
    )
print("✅ 配置已保存为 config.json")


# json.loads()
# 模拟 OpenAI / Hugging Face API 返回的 JSON 字符串
api_response = """
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1745220000,
  "model": "gpt-4o",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "你好！我是 Grok，由 xAI 构建。"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 28,
    "total_tokens": 43
  }
}
"""

# 解析JSON字符串为Python对象
result = json.loads(api_response)

# 提取访问
print(result["choices"][0]["message"]["content"])
print(f"总 token 数: {result['usage']['total_tokens']}")

# json.load()
# 假设有一个 COCO 格式的数据集标注文件
with open("annotations/instances_train2017.json", "r", encoding="utf-8") as f:
    coco_data = json.load(f)

print(f"图片数量: {len(coco_data['images'])}")
print(f"类别数量: {len(coco_data['categories'])}")

# 遍历前 3 张图片
for img in coco_data["images"][:3]:
    print(f"文件名: {img['file_name']}, 高:{img['height']}, 宽:{img['width']}")

"""
写字符串 → dumps（API 请求、日志）
写文件 → dump（保存 config、checkpoint）
读字符串 → loads（解析 API 返回）
读文件 → load（加载数据集、标注）
ensure_ascii=False（中文不乱码）
encoding="utf-8"（读写文件）
indent=2（调试时可读性强）
"""
