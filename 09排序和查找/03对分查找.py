# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 03对分查找.py
# @Time     : 2024/8/22 下午10:40

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
find = 3


def find_value(list1, find):
    find_index = -1
    left_index, right_index = 0, len(list1) - 1

    while left_index <= right_index:
        # 中间数的下标
        mid_index = (left_index + right_index) // 2
        if list1[mid_index] > find:
            right_index = mid_index - 1
        elif list1[mid_index] < find:
            left_index = mid_index + 1
        else:
            find_index = mid_index
            break

    return find_index


out_find_index = find_value(list1, find)
print(out_find_index)
