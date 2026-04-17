# 基础定义
def greet(name: str, age: int = 18) -> str:
    """
    欢迎函数(类型提示 + 文档字符串)
    """
    return f"你好，{name}！你今年{age}岁。"


print(greet("小明"))  # 使用默认值
print(greet("小红", 20))


# 参数类型详解
def order_pizza(size, *toppings, **extras):
    """*args(可变位置参数) + **kwargs(可变关键字参数)"""
    print(f"你点的{size} pizza有以下配料：{toppings}")
    for k, v in extras.items():
        print(f"额外要求{k}：{v}")


order_pizza("大", "香肠", "蘑菇", "培根", 备注="不要加奶酪", 送达时间="10:00")

# lambda 匿名函数（常用排序，map,filter等）
# lambda + 高阶函数
students = [("张三", 90), ("李四", 85), ("王五", 95)]

# 按成绩排序
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)

# 递归函数
# 递归 -斐波那契数列（带缓存优化）
from functools import lru_cache


@lru_cache(maxsize=128)  # 缓存最大大小  记忆化装饰器
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print([fibonacci(i) for i in range(15)])

# 作用域  global / nonlocal
# 全局变量：在函数外部定义的变量，可以在函数内部访问
# 本地变量：在函数内部定义的变量，只能在函数内部访问
# 非本地变量：在嵌套函数中定义的变量，可以在嵌套函数中访问
x = 10  # 全局变量


def outer():
    x = 20  # 本地变量 局部变量

    def inner():
        nonlocal x  # 修改外层函数的 x
        x = 30
        print(x)

    inner()
    print(x)


outer()
print("global x:", x)
