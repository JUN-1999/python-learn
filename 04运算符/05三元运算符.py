# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 05三元运算符.py
# @Time     : 2024/7/30 下午10:05


"""
max = a if a>b else b
"""

a = 10
b = 20
c = 30
max1 = b if b > c else c
max = a if a > max1 else max1
print(max)
