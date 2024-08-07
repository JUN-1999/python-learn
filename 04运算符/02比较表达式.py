# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 02比较表达式.py
# @Time     : 2024/7/29 下午10:59

"""
==      等于
！=      不等于
<       小于
>       大于
<=      小于等于
>=      大于等于
is      判断两个变量引用对象是否为同一个
is not  判断来个变量引用对象是否不同
"""

a = 'www123'
b = 'www1232'
if a is b:
    print('相同空间')
else:
    print('不同空间')
