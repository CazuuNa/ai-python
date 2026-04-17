class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # 双下划线 = 私有属性（名字改写）

    # 使用 property 实现“只读”或“受控访问”
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("余额不能为负数！")
        self.__balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"存款 {amount} 元，当前余额：{self.balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("余额不足！")
        else:
            self.__balance -= amount
            print(f"取款 {amount} 元，当前余额：{self.balance}")


# 使用
account = BankAccount("小明", 1000)
account.deposit(500)
print(account.balance)  # 1500
# account.__balance         # 直接访问会报错（封装成功）
