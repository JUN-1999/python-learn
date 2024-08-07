# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 04赋值运算符.py
# @Time     : 2024/7/30 下午9:48


"""
=   简单赋值
+=  复合加法赋值 类似 c+=a  c=c+a
"""

"""
有一个变量a 一个变量b 进行交换
正常的处理是取一个中间值，但是在python有个更简单的方法
a,b=b,a
"""

a = 10
b = 20
print('a=', a, ' b=', b)

a, b = b, a

print('a=', a, ' b=', b)

