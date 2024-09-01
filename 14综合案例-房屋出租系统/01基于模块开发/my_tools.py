# @Version  : 1.0
# @Author   : Jun1999
# @Name     : my_tools.py
# @Time     : 2024/9/1 下午5:34

"""
 说明：编写工具函数，供程序员使用
"""


def read_confirm_select():
    """
     确认用户输入的是（Y/N）,不区分大小写
     如果用户输入的不是Y/N,就循环反复输入
    :return:
    """
    key = input("请输入你的选择(Y/N),请确认选择：")
    while key.lower() != 'y' and key.lower() != 'n':
        key = input("选择错误，重新输入：")
    return key.lower()


def read_str(tip, default_value):
    """
    读取用户的输入,如果用户没有输入内容，则返回default_value
    :param tip: 提示信息
    :param default_value: 默认值
    :return: 新的值
    """
    str = input(tip)
    if len(str) > 0:  # 如果用户有内容
        return str
    else:
        return default_value
