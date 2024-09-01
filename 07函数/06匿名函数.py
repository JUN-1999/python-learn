# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 06匿名函数.py
# @Time     : 2024/8/9 下午9:13


"""
lambda 匿名函数

1、函数的定义
def关键字，可以定义带【有名称】的函数。可以重复使用
lambda关键字，可以定义【匿名函数】（无名称），匿名函数只能使用一次
匿名函数用于临时创建一个函数，【只使用一次】的场景
2、基本语法
lambda 形参列表：函数体（一行代码）
"""


def get_max_val(fun, n1, n2):
    return fun(n1, n2)


ref = get_max_val(lambda a, b: a if a > b else b, 2, 3)
print(ref)
