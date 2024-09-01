# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 04函数的递归.py
# @Time     : 2024/8/9 下午7:12

"""
递归的重要规则
1、执行一个函数时，就创建一个新的空间
2、函数的变量是独立的
3、递归必须向退出递归的条件逼近，否则就是无限递归
4、当一个函数执行完毕，或者遇到return 就会返回，遵守谁调用，就将结果返回给谁
"""


# 求出第n个斐波那契数列的值
# def fbn(n):
#     """
#     功能：返回n对应的斐波那契数
#     :param n: 接受一个整数 n>=1
#     :return: 返回一个整数
#     """
#     if n < 1:
#         print('请输入正确的整数')
#         return
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fbn(n - 1) + fbn(n - 2)
#
#
# print(fbn(35))


# def ctz(n):
#     """
#     功能：计算猴子刚开始有几个桃子
#     :param n: 天数-整数>=0
#     :return: 返回桃子数
#     """
#     if n == 10:
#         return 1
#     else:
#         return (ctz(n + 1) + 1) * 2
#
#
# print(ctz(1))


def f3(n):
    if n == 1:
        return 3
    else:
        return 2 * f3(n - 1) + 1


print(f3(3))
