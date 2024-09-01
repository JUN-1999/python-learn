# @Version  : 1.0
# @Author   : Jun1999
# @Name     : wjc_module1.py
# @Time     : 2024/8/27 下午9:48

# 在from xx import * 的时候 指定哪些模块可以对外使用
# 注意：import 模块 不受__all__影响
__all__ = ['ok', 'hi']


def hi():
    print("wjc hi")


def ok():
    print("wjc ok")


if __name__ == '__main__':
    hi()
