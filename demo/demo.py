# 基础数据类型
# 数值类型（int, float, complex）
# eg1 数值类型与运算
a = 10        # 整数, 无限精度
b = 3.14      # 浮点数
c = 1+2j      # 复数 
print(type(a),type(b),type(c))  # <class 'int'> <class 'float'> <class 'complex'>
print(a)      # 10
print(b)      # 3.14
print(c)      # (1+2j)
print(a+b)    # 13.14  int + float = float
print(a*b)    # 31.4   int * float = float
print(a/b)    # 3.14 真除法
print(a//b)    # 3   整除（地板除法，只取商的整數部分）
print(a%b)    # 1.14   取数（取商的余數）
print(a ** b)                    # 指数运算(次方) int ** float → float
print(type(a ** b))              # <class 'float'>
print(a ** c)                    # int ** complex → complex
print(type(a ** c))              # <class 'complex'>

'''
混合运算规则
1. 整数和浮点数的混合运算结果为浮点数
2. 整数和复数的混合运算结果为复数
3. 浮点数和复数的混合运算结果为复数
4. 复数的混合运算结果为复数
'''

# 比较运算
print(a == b)  # False  等于
print(a != b)  # True   不等于
print(a > b)   # True   大于
print(a < b)   # False  小于
print(a >= b)  # True   大于等于
print(a <= b)  # False  小于等于

# 赋值运算
x = 10
x += 5  # x = 10 + 5 = 15
x*=2  # x = 15 * 2 = 30
print(x)  # 30

# 逻辑运算
# 用来组合条件判断，常在if语句中使用
# and 且
# or 或
# not 非
# age = 20
# has_id = True
# print(age >= 18 and has_id)   # True
# print(not (age < 18))         # True

# 位运算
# 位运算符（&, |, ^, ~, <<, >>）
# & 位元 and 与操作
# | 位元 or 或操作
# ^ 位元 xor 异或操作
# ~ 位元 not 非操作
# << 位元 left 左移操作
# >> 位元 right 右移操作
# 位元操作符在二进制数上进行操作，将结果转换为十进制数

# 用来对二进制位进行操作
# 例如，将一个整数的第3位设置为1，可以使用 | 运算符
print(10 | 5)  # 15  1011 0101
print(10 & 5)  # 0   0000 0000
print(10 ^ 5)  # 15  1111 1111
print(~10)    # -11  1010 1101
print(10 << 2)  # 40  10100000
print(10 >> 2)  # 2   00001010
print(10 << 2)  # 40  101000000000

# 身份运算
# is 检查两个对象是否是同一个对象
# is not 检查两个对象是否不是同一个对象
arr1 = [1,2,3]
arr2 = [1,2,3]
print(arr1 is arr2)      # False （內容一樣，但不是同一個物件）
print(arr1 == arr2)      # True  （內容相等）
print(a is b)  # False
print(a is not b)  # True
print(a is c)  # False
print(a is not c)  # True

# 成员运算
# in 检查一个元素是否在另一个对象中
# not in 检查一个元素是否不在另一个对象中
# fruits = ["apple", "banana", "orange"]
# print("apple" in fruits)     # True
# print("grape" not in fruits) # True

# 内置函数 （不需要导入 built-in 模块的函数）
'''
-- 函数 --     -- 功能 --            -- 示例 --           -- 结果 --
abs(x)        取绝对值               abs(-10)               10
round(x,n)    四舍五入               round(3.14,2)          3.14
pow(x,y)      指数运算 == x**y       pow(2,3)               8
max(x,y,z)    取最大值               max(1,2,3)             3
min(x,y,z)    取最小值               min(1,2,3)             1
sum(x,y,z)    求和                   sum(1,2,3)             6
'''
'''
math模组(需要引入 import math)
pi            圆周率                 math.pi            3.1415926535897932384626433832795
e             自然对数的底数          math.e             2.71828182845904523536028747135266
sqrt(x)       取平方根               math.sqrt(9)            3.0
pow(x,y)      指数运算 == x**y       math.pow(2,3)           8.0
fabs(x)       取绝对值               math.fabs(-10)           10.0
exp(x)        e的x次方              math.exp(2)             7.38905609893065
log(x)        取自然对数             math.log(9)             2.0
log10(x)      取10的对数             math.log10(100)         2.0
sin(x)        取正弦值               math.sin(0)             0.0
cos(x)        取余弦值               math.cos(0)             1.0
tan(x)        取正切值               math.tan(0)             0.0
asin(x)       取反正弦值             math.asin(0)             0.0
acos(x)       取反余弦值             math.acos(0)             0.0
atan(x)       取正切值             math.atan(0)             0.0
degrees(x)    将弧度转换为角度     math.degrees(0)          0.0
radians(x)    将角度转换为弧度     math.radians(0)          0.0
sqrt(x)       取平方根               math.sqrt(9)            3.0
ceil(x)       取上取整值             math.ceil(3.14)         4.0
floor(x)      取下取整值             math.floor(3.14)        3.0
factorial(x)  取阶乘               math.factorial(5)        120
gcd(x,y)      取最大公约数             math.gcd(12,16)        4.0
lcm(x,y)      取最小公倍数             math.lcm(12,16)        48.0
'''
'''
cmath模组(需要引入 import cmath 处理复数时使用 cmath 模组)
sqrt(-1) 可以开复数平方根             cmath.sqrt(-1)        1.0j
phase(z)  取复数z的相位（弧度） cmath.phase(1+1j)    0.7853981633974483
polar(z)  取复数z的极坐标（模，相位） cmath.polar(1+1j)    (1.4142135623730951, 0.7853981633974483)
rect(r,phi)  取复数z的直角坐标（模，相位） cmath.rect(1.4142135623730951, 0.7853981633974483) 142135623730951j
'''

# 字符串 str
# eg2
name = '张三'
age = 20
info = f"姓名：{name}，年龄：{age}" 
print(info)
# 姓名：张三，年龄：20

# 常用方法
s = "  Hello World"
print(s.strip())                            # Hello World
print(s.upper())                            # HELLO WORLD
print(s.lower())                            # hello world
print(s.title())                            # Hello World
print("World" in s)                         # True（成员判断）
print(s.replace("Hello","Hi"))              # Hi World
print("-".join(["a","b","c","d","e"]))      # a-b-c-d-e
print(s.split())                            # ['Hello', 'World']

# 布尔值 bool
# eg3
is_adult = age >= 18 # True
has_ticket = True
if is_adult and has_ticket:
    print("可以进入")
else:
    print("不能进入")

'''
真值判断规则
False,0,0.0,"",None,{},[],() 均为false
其他都是True
'''
# 序列类型 列表 list 元组 tuple
# eg4 列表可变[]  元组不可变()
fruits = ["苹果", "香蕉", "橙子"]      # list
colors = ("红", "绿", "蓝")           # tuple

fruits.append("葡萄")
print(fruits)
# ['苹果', '香蕉', '橙子', '葡萄']
# colors.append("紫色")  # 报错，元组不可变


# 切片操作
# 切片语法：[起始索引:结束索引:步长]
'''
start  # 切片起始索引（包含）
end  # 切片结束索引（不包含）
step  # 切片步长（默认1）
lst = [10,20,30,40,50,60,70,80,90,100]
lst[start:end] 从start开始，到end-1结束 lst[2:6]  # [30, 40, 50, 60]
lst[:end] 从0开始，到end-1结束 lst[:6]  # [10, 20, 30, 40, 50, 60]
lst[start:] 从start开始，到列表末尾 lst[2:]  # [30, 40, 50, 60, 70, 80, 90, 100, 80, 90, 100]
lst[:] 浅复制
lst[::step] 从0开始，每次跳过step个元素 lst[::2]  # [10, 30, 60, 90, 100]
lst[::-step] 从列表末尾开始，每次跳过step个元素 
lst[::-1]  # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10] 反转
lst[::-2]  # [100, 80, 60, 40, 20]
在py中 -1表示最后一个元素
-2表示倒数第二个元素
-3表示倒数第三个元素
...
lst[-3::]  # [80, 90, 100]

'''

'''
其他通用操作
len()  # 取序列长度
max()  # 取最大值
min()  # 取最小值
sum()  # 求和
count()  # 统计元素出现次数
index()  # 查找元素索引
insert()  # 插入元素
remove()  # 删除元素
sort()  # 排序
reverse()  # 反转序列
for # 遍历序列

'''
