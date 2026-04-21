class SafeFile:
    """自定义文件上下文管理器，支持自动关闭和异常记录"""

    def __init__(self, filename, mode="r", encoding="utf-8"):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode, encoding=self.encoding)
            print(f"文件打开成功: {self.filename}")
            return self.file
        except Exception as e:
            print(f"文件打开失败: {self.filename} - {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"文件关闭成功: {self.filename}")
        if exc_type is not None:
            print(f"发生异常: {exc_type.__name__}: {exc_val}")
            # 返回 True 可以抑制异常（不推荐，除非必要）
            return False  # 默认 False，继续抛出异常


# 使用自定义上下文管理器
try:
    with SafeFile("phase1-day03/test.txt", "w", encoding="utf-8") as f:
        f.write("使用自定义上下文管理器写入内容\n")
        # 故意制造异常测试
        # 1 / 0
except Exception as e:
    print(f"外部捕获到异常: {e}")
