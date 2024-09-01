# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 04课后练习.py
# @Time     : 2024/8/22 下午10:53
import random

# 随机生成十个整数（1-100）使用冒泡排序
arr = list()
for i in range(0, 10):
    arr.append(random.randint(1, 100))


def foo(px_list):
    # 完成排序
    for i in range(0, len(px_list)):
        for j in range(0, len(px_list) - i - 1):
            if px_list[j + 1] > px_list[j]:
                # 两个值替换
                px_list[j + 1], px_list[j] = px_list[j], px_list[j + 1]



print(foo(arr))
