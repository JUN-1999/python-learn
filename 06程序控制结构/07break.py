# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 07break.py
# @Time     : 2024/8/7 下午10:49


"""
break的使用

注意事项：
1、用在for或while循环所嵌套的代码
2、它会终结最近的外层循环，如果循环有可选else子句，也会跳过该子句

random.randint(a,b)
生成 a<=n<=b 的一个数，相当于 randrange(a,b+1)
"""

#
# import random
#
# count = 0
# while True:
#     num = random.randint(1, 100)
#     count += 1
#     if num == 97:
#         print(count)
#         break


# 1-100之和，当第一次和大于20的时候，循环的控制的值是多少

i=1
sum=0
while i<=100:
    sum += i
    if (sum > 20):
        break
    i+=1


print(i)
