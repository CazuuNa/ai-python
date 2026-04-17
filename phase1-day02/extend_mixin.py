class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} 正在叫...")


class Dog(Animal):  # 继承 Animal
    def __init__(self, name, breed):
        super().__init__(name)  # 调用父类构造方法
        self.breed = breed  # 子类特有属性

    # 方法重写（Override）—— 多态核心
    def speak(self):
        print(f"{self.name}（{self.breed}）汪汪汪！")

    def fetch(self):
        print(f"{self.name} 正在捡球！")


dog = Dog("旺财", "金毛")
dog.speak()  # 调用子类重写的方法
dog.fetch()


class Flyable:
    def fly(self):
        print("正在飞行...")


class Swimmable:
    def swim(self):
        print("正在游泳...")


class Duck(Animal, Flyable, Swimmable):  # 多继承
    def speak(self):
        print("嘎嘎嘎！")


duck = Duck("唐老鸭")
duck.speak()
duck.fly()
duck.swim()
