# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 05while循环.py
# @Time     : 2024/8/7 下午8:01


"""
while 语句-基本语法

while 判断条件:
    循环操作语句...

"""

# i = 0
# while i < 10:
#     print(i)
#     i += 1

"""
while 搭配 else 使用
语法格式：
while 判断条件：
    循环执行语句...
else:
    其他语句
    
触发：在while...else 判断条件为false时，会执行else语句，即：在遍历的过程中，没有被打断
"""
# i = 0
# while i < 5:
#     # if i==3:
#     #     break
#     print(i)
#     i += 1
# else:
#     print('成功循环while')


# 课后练习
# 1、打印1-100之间能被3整除的数字

# for写法
# for i in range(1, 101, 1):
#     if i % 3 == 0:
#         print(i)

# while写法
# i = 1
# maxi=100
# while i <= maxi:
#     if i % 3 == 0:
#         print(i)
#     i += 1
# else:
#     print("while循环")

# 2、打印40-200之间所有的偶数
# i = 40
# while i <= 200:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# 3、不断输入姓名，直到输入exit为止
# name = ''
# while name != 'exit':
#     name = str(input('输入你的名字：'))

# 4、统计1-100之间所有是9的倍数的整数，统计个数以及总和
# num = 0
# max_num = 100
# count = 0
# sum = 0
# while num <= max_num:
#     num += 1
#     if num % 9 == 0:
#         print(num)
#         sum += num
#         count += 1
# else:
#     print("个数：",count, "总和：",sum)
#     print(f"个数：{count} 总和：{sum}")


# 5、完成一个表达式的输出，输入一个数 得到这个数的各种加法结果
num = int(input('请输入一个整数：'))
i = 0
while i <= num:
    print(f"{i}+{num - i}={num}")
    i += 1
else:
    print('输出完毕')
