# 文件操作 + 异常处理 + 推导式

# 文件读写基础
# 打开/关闭文件（with语句）
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
    lines = f.readlines()  # 读取所有行（带\n）
    line = f.readline()  # 读取一行

# 常用模式
"r"  # 读取模式（默认）
"w"  # 写入模式（覆盖文件）
"a"  # 追加模式（不覆盖文件）
"r+"  # 读写模式
"w+"  # 写入模式（覆盖文件）
"a+"  # 追加模式（不覆盖文件）


# 文件读写 + 异常处理 + 列表推导式
def process_file_demo():
    try:
        # 写入文件
        with open("example.txt", "w", encoding="utf-8") as f:
            f.write("张三,85\n李四,92\n王五,78\n赵六,95\n")
        print("文件写入成功！")
        # 读取并处理文件
        with open("example.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            # 使用列表推导式 + 异常处理解析数据
            students = []
            for line in lines:
                try:
                    name, score_str = line.strip().split(",")
                    score = int(score_str)
                    students.append((name, score))
                except ValueError:
                    print(f"无效数据：{line.strip()}")
                    continue

        # 使用推导式进行数据分析
        names = [name for name, score in students]
        high_scores = [name for name, score in students if score >= 90]
        avg_score = (
            sum(score for _, score in students) / len(students) if students else 0
        )

        print(f"所有学生姓名：{names}")
        print(f"成绩大于等于90分的学生姓名：{high_scores}")
        print(f"平均成绩：{avg_score:.2f}")
    except FileNotFoundError:
        print("文件不存在！")
    except PermissionError:
        print("没有权限访问文件！")
    except Exception as e:
        print(f"发生未知错误：{e}")


# 异常处理（exception handling）
"""
常见文件相关异常
FileNotFoundError: 文件或路径目录不存在
PermissionError: 没有权限访问文件或目录
IsADirectoryError: 尝试将目录作为文件打开
UnicodeDecodeError: 解码错误，通常是因为编码不匹配
ValueError: 值错误，例如将字符串转换为整数时出错
"""
# 多异常处理 +else +finally


def safe_read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            print("文件读取成功！", content)
    except FileNotFoundError:
        print(f"文件 {filename} 不存在！")
    except UnicodeDecodeError:
        print(f"文件 {filename} 编码错误！，尝试使用gb18030编码读取")
        try:
            with open(filename, "r", encoding="gb18030") as f:
                content = f.read()
                print("文件读取成功！", content)
                return content
        except Exception as e:
            print(f"使用gb18030编码读取文件 {filename} 时发生错误：{e}")
            return None
    except PermissionError:
        print(f"没有权限访问文件 {filename}！")
    except Exception as e:  # 捕获所有其他异常
        print(f"读取文件时发生错误: {type(e).__name__}: {e}")
        return None
    else:
        # try 没有异常时执行
        print("else:文件处理完成")
        return content
    finally:
        # 无论是否有异常，都执行
        print("finally:文件处理完成")


# 推导式（Comprehensions）
"""
常用推导式类型
列表推导式：[expression for item in iterable if condition]
scores = [int(line.split(',')[1]) for line in lines if ',' in line]
字典推导式：{key:value for item in iterable if condition}
student_dict = {name: score for name, score in students if score >= 80}
集合推导式：{expression for item in iterable if condition}(去重)
unique_scores = {score for _, score in students}
元组推导式：(expression for item in iterable if condition)
tuples = [(name, score) for name, score in students if score >= 90]
生成器表达导式（节省内存，适合大文件）：(expression for item in iterable if condition)
total = sum(int(line.split(',')[1]) for line in open('students.txt', encoding='utf-8') 
            if ',' in line)
"""

# 进阶eg:处理大型日志文件


def analyze_log_file(log_path):
    try:
        with open(log_path, "r", encoding="utf-8") as f:
            # 使用生成器表达式 + 异常处理过滤有效日志
            errors = [
                line.strip()  # 移除首尾空格
                for line in f
                if "ERROR" in line or "CRITICAL" in line
            ]

            # 字典推导式统计错误类型
            error_types = {}
            for line in errors:
                try:
                    # 假设日志格式 [2026-04-20 15:30] ERROR: 用户登录失败
                    parts = line.split("ERROR:")
                    if len(parts) > 1:
                        msg = parts[1].strip()
                        error_types[msg] = error_types.get(msg, 0) + 1
                except:
                    continue
            return error_types
    except FileNotFoundError:
        print(f"文件 {log_path} 不存在！")
        return {}
    except Exception as e:
        print(f"分析日志文件 {log_path} 时发生错误：{e}")
        return {}


# JSON 文件操作
# 内置json模块处理JSON数据，始终使用with + encoding="utf-8"打开文件

import json

# 写入json
data = {
    "students": [
        {"name": "张三", "score": 85, "subjects": ["数学", "英语"]},
        {"name": "李四", "score": 92, "subjects": ["语文", "物理"]},
    ],
    "class": "高三(1)班",
}

with open("phase1-day03/students.json", "w", encoding="utf-8") as f:
    json.dump(
        data, f, ensure_ascii=False, indent=2
    )  # indent 美化，ensure_ascii=False 支持中文

# 读取json
try:
    with open("phase1-day03/students.json", "r", encoding="utf-8") as f:
        data = json.load(f)  # 直接转为python对象（dict/list）
    # 使用推导式处理数据
    high_score_students = [
        s["name"] for s in data.get("students", []) if s.get("score", 0) >= 90
    ]
    print("高分学生:", high_score_students)
    print("班级:", data.get("class"))
except FileNotFoundError:
    print("文件 students.json 不存在！")
except json.JSONDecodeError as e:
    print(f"JSON 格式错误: {e}")
except Exception as e:
    print(f"读取失败: {e}")

# JSONL
# 写入 JSONL 大文件处理
with open("logs.jsonl", "w", encoding="utf-8") as f:
    for i in range(100):
        log = {"id": i, "level": "ERROR" if i % 5 == 0 else "INFO", "msg": f"事件 {i}"}
        f.write(json.dumps(log, ensure_ascii=False) + "\n")


# 读取 JSONL（推荐用于大文件）
def read_jsonl(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            # 生成器表达式 + 异常处理
            for line_num, line in enumerate(f, 1):
                try:
                    if line.strip():  # 跳过空行
                        yield json.loads(line)
                except json.JSONDecodeError:
                    print(f"第 {line_num} 行 JSON 格式错误，跳过")
                    continue
    except Exception as e:
        print(f"文件读取错误: {e}")
        yield from []


# 使用示例
error_logs = [log for log in read_jsonl("logs.jsonl") if log.get("level") == "ERROR"]
print(f"错误日志数量: {len(error_logs)}")

# 二进制文件操作
# 二进制模式使用 'rb' 'wb' 'ab' 数据类型为bytes

# 写入二进制
data = b"Hello Python! \x00\x01\x02" + bytes(range(256))  # 包含二进制数据

with open("binary_data.bin", "wb") as f:
    f.write(data)

# 读取二进制
try:
    with open("binary_data.bin", "rb") as f:
        content = f.read()  # 返回 bytes
        content_part = f.read(10)  # 读取前10字节（但这里已读完）

    print(f"总字节数: {len(content)}")
    print("前20字节:", content[:20])

    # 转换为十六进制查看
    print("Hex:", content[:16].hex())

except Exception as e:
    print(f"二进制文件操作失败: {e}")


# 分块读取 大二进制文件（图片/视频）
def copy_file_in_chunks(src, dst, chunk_size=4096):
    try:
        with open(src, "rb") as fsrc, open(dst, "wb") as fdst:
            while True:
                chunk = fsrc.read(chunk_size)
                if not chunk:  # 读取到末尾返回 b''
                    break
                fdst.write(chunk)
        print(f"文件复制完成: {src} -> {dst}")
    except FileNotFoundError:
        print("源文件不存在")
    except PermissionError:
        print("权限不足")
