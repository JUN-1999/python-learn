# @Version  : 1.0
# @Author   : Jun1999
# @Name     : utility.py
# @Time     : 2024/9/1 下午10:35

"""
工具
编写 Utility类【工具类】
提供各种工具方法

"""


class Utility:
    @staticmethod
    def read_confirm_select():
        key = input("请输入你的选择(Y/N),请确认选择：")
        while key.lower() != 'y' and key.lower() != 'n':
            key = input("选择错误，重新输入：")
        return key.lower()

    @staticmethod
    def read_str(tip, default_value):
        str1 = input(tip)
        if len(str1) > 0:  # 如果用户有内容
            return str1
        else:
            return default_value
