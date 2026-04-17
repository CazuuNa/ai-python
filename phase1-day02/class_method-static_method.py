# classmethod：工厂模式、替代构造方法（如 from_json）
# staticmethod：工具函数（如日期校验、数学计算）


class Person:
    population = 0  # 类属性

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod  # 类方法：接收 cls 而非 self
    def get_population(cls):
        return cls.population

    @staticmethod  # 静态方法：不需要 self/cls
    def is_adult(age):
        return age >= 18


p1 = Person("A")
p2 = Person("B")
print(Person.get_population())  # 2
print(Person.is_adult(20))  # True
