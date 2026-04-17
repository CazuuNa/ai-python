# 控制流
# 条件语句  if-elif-else
# 多分支判断  if-elif-elif-else
score = 80
if score >= 90:
    grade = "A"
    print(grade)
elif score >= 80:
    grade = "B"
    print(grade)
elif score >= 70:
    grade = "C"
    print(grade)
elif score >= 60:
    grade = "D"
    print(grade)
else:
    grade = "E"
    print(grade)

# 循环语句  for-while
# for循环
for i in range(10):  # 从0开始，到10-1结束
    print(i, end=" ")

"""
for fruit in ["apple","orange","banana"]:
    print(fruit)

带索引
for i,fruit in enumerate(["apple","orange","banana"],start=1):
    print(i,fruit)
"""

# while循环 + break/continue
count = 0
while count < 10:
    count += 1
    if count == 3:
        continue  # 跳过本次循环
    if count == 7:
        break  # 直接跳出循环
    print(count)
i = 0
while i < 10:
    print(i, end=" ")
    i += 1

# 随机数字
import random

secret = random.randint(1, 100)

tries = 0

print("请猜一个1到100之间的数字")

while True:
    guess = int(input("请输入你猜的数字："))
    tries += 1

    if guess < secret:
        print("太小了！")
    elif guess > secret:
        print("太大了！")
    else:
        print(f"恭喜你！用了 {tries} 次猜对了！")
        break
