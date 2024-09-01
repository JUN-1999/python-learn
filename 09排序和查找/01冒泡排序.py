# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 01冒泡排序.py
# @Time     : 2024/8/22 下午9:04


list1 = [24, 69, 80, 57, 13, 99, 77, 88, 66]

for i in range(0, len(list1)):
    for j in range(0, len(list1) - i - 1):
        if list1[j + 1] < list1[j]:
            list1[j + 1], list1[j] = list1[j], list1[j + 1]

print(list1)
