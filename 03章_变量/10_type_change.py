# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 10_type_change.py
# @Time     : 2024/7/23 下午11:10


# 数据类型转换

# python 根据该变量使用的上下文（当前值），在运行时决定类型
# var1 = 10
# print(type(var1))
# var1 = 1.1
# print(type(var1))
# var1 = "smdx"
# print(type(var1))

# 在运算的时候，数据类型会向高精度自动转换
"""

num1 = 10
num2 = 1.2
num3 = num1 + num2
print("num3", num3, type(num3))
num1 = num1 + 0.1
print("num1", num1, type(num1))

"""

# n1 = 100
# result = "n1的值是" + n1


# 显示类型转换
i = 10
print(i, type(i))
j = float(i)
print(j, type(j))
k = str(i)
print(k, type(k))

"""
注意事项
1、无论什么值的int、float 都可以转为str str(x)将对象转为字符串
2、int转float会增加小数、float转int时会去掉小数部分
3、str转int，float使用int(x)/float(x)将对象x转换为int/float
4、将str类型转为int时候，需要确保可以成功转为int，不然会报错
5、对一个变量进行强制转换，会返回一个数据/值，并且这个值对原数据没有影响
"""
