# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 06_int_detail.py
# @Time     : 2024/7/23 下午9:37


"""
 int类型的细节
 在python中可以表示很大的数、
 整数可以有 十进制、十六进制、八进制、二进制
 十六进制：0X
 八进制：0O
 二进制：0B
"""
import sys

# 十六进制
# print(0x10)
# 八进制
# print(0o10)
# 二进制
# print(0b10)

# 一个int整型占多少字节
# 字节数随着数字增大而增大
# 增量是四个字节
# 在python中，可以通过sys.getsizeof 返回对象的大小（按照字节单位）
n1 = 0
n2 = 2 ** 15
n3 = 2 ** 30
n4 = 2 ** 60

print(f"n1 的大小是{sys.getsizeof(n1)} 类型是 {type(n1)}")
print(f"n2 的大小是{sys.getsizeof(n2)} 类型是 {type(n2)}")
print(f"n3 的大小是{sys.getsizeof(n3)} 类型是 {type(n3)}")
print(f"n4 的大小是{sys.getsizeof(n4)} 类型是 {type(n4)}")
