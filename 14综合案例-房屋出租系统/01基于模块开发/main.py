# @Version  : 1.0
# @Author   : Jun1999
# @Name     : main.py
# @Time     : 2024/9/1 上午9:39

"""
    说明：出租系统的主程序
"""

from house_operation import *
from my_tools import *


def main():
    while True:
        main_menu()
        key = int(input("请输入你的选择(1-6)"))
        if key in [1, 2, 3, 4, 5, 6]:
            if key == 1:
                add_house()
            elif key == 2:
                find_house()
            elif key == 3:
                del_house()
            elif key == 4:
                update_house()
            elif key == 5:
                list_house()
            elif key == 6:
                if exit_sys():
                    break
        else:
            print('请输入范围内的数字')


if __name__ == '__main__':
    main()
    print('退出系统，欢迎再次使用...')
