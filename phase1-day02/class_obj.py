# OOP (面向对象编程)
"""
核心 class，允许数据（属性）和行为（方法）封装在一起
OOP四大特性
封装：将数据和方法绑定在一起，隐藏实现细节
继承：基于已有的类创建新类，重用代码
多态：不同对象可以以相同的方式响应相同的消息
抽象：定义一个类，不实现具体的方法，只定义方法的签名
"""

"""
魔术方法
__init__：初始化方法，创建对象时调用 （必须有，不能省略，不是构造函数）
__new__：创建并返回一个新的实例对象，然后__init__方法对对象进行初始化
__del__：对象销毁时调用, 用于清理资源.释放资源（关闭文件、断开网络连接、释放数据库游标等）
"""


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # 创建实例
        return cls._instance

    def __init__(self, value):
        self.value = value  # 注意：单例模式下 __init__ 可能会被多次调用


s1 = Singleton(10)
s2 = Singleton(20)
print(s1 is s2)  # True（同一个对象）


class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, "w")

    def __del__(self):
        if hasattr(self, "file"):
            self.file.close()
            print("文件已关闭")


"""
字符串相关魔术方法
__str__(self)：将对象转换为字符串,print(obj) 或 str(obj) 时调用，面向用户的友好字符串。
__repr__(self)：返回对象的官方表示，用于创建对象的代码。
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"点坐标：({self.x}, {self.y})"  # 友好输出

    def __repr__(self):
        return f"Point({self.x}, {self.y})"  # 可用于 eval 重建对象


p = Point(3, 4)
print(p)  # 点坐标：(3, 4)
print(repr(p))  # Point(3, 4)

"""
运算符重载（让对象支持 + - == 等运算符）
__add__(self, other) -> obj1 + obj2：定义对象之间的加法运算
__eq__(self, other) → obj1 == obj2：定义对象之间的相等运算
__ne__(self, other) → obj1 != obj2：定义对象之间的不相等运算  还有lt gt
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6) （需要配合 __repr__ 才能好看输出）
print(v1 == Vector(1, 2))  # True

"""
容器行为
__len__(self)：返回对象的长度，用于 len(obj) 或 for 循环。
__getitem__(self, key)：返回对象的指定索引的元素，用于 obj[key]。
__iter__(self)：返回一个迭代器，用于 for 循环。
__contains__(self, item) → bool：检查对象是否包含指定元素，用于 item in obj。
__setitem__(self, key, value)：设置对象的指定索引的元素，用于 obj[key] = value。
__delitem__(self, key)：删除对象的指定索引的元素，用于 del obj[key]。
__add__(self, other) → new_obj：定义对象之间的加法运算，用于 new_obj = self + other。
__mul__(self, other) → new_obj：定义对象之间的乘法运算，用于 new_obj = self * other。
"""
