# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 02分支控制.py
# @Time     : 2024/8/6 下午7:54


"""
1、单分支
2、双分支
3、多分支
"""

"""
单分支是通过
    if 条件表达式 :
        代码块(可以有多条语句)    
"""

# if 4 > 2:
#     print('111')
#     if 4 < 3:
#         print('222')
#
# print('333')

# 案例：输入一个学员年龄 判断是否大于十八岁
# age = int(input('输入你的年龄：'))
# print(type(age))
# if age > 18:
#     print('大于十八岁')


"""
双分支代码 基本语法
if 条件表达式:
    执行语句1
else:
    执行语句2
"""

# age = int(input('请输入你的年龄：'))
# if age >= 18:
#     print('大于等于十八岁')
# else:
#     print('小于十八岁')

# 逻辑运算符 and or not
# num1 = int(input('输入数字1：'))
# num2 = int(input("输入数字2："))
# sum = num1 + num2
# if sum % 3 == 0 and sum % 5 == 0:
#     print('符合条件')
# else:
#     print('不符合条件')

# 判断是否为闰年
# year = 1660
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('是闰年')
# else:
#     print("不是闰年")


"""
多分支代码 基本语法
if 条件表达式:
    执行语句1
elif 条件表达式2:
    执行语句2
...
else:
    执行语句n+1
"""

age = int(input('输入成绩：'))
if 0 <= age <= 100:
    if age == 100:
        print('奖励一台BMW')
    elif 80 < age <= 99:
        print('奖励一台ipone')
    elif 60 <= age <= 80:
        print('奖励一个ipad')
    else:
        print('什么都没有')
else:
    print('输入成绩不正确')
