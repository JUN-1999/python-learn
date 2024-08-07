# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 06多重循环控制.py
# @Time     : 2024/8/7 下午8:32


"""
多重循环， 两个循环嵌套
"""
# 打印空心三角形
# total=5
# for i in range(total+1):
#     # 输出每行的空格
#     for k in range(total-i):
#         print(" ",end="")
#
#     for j in range(2*i-1):
#         if i == total:
#             print("*",end="")
#         else:
#             if j == 0 or j == 2*(i-1):
#                 # end="" 表示输出不换行
#                 print('*', end="")
#             else:
#                 print(" ",end="")
#     else:
#         print('')

# # 打印空心菱形
# total = 6
# for i in range(total + 1):
#     if i < total // 2:
#         for k in range(total // 2 - i):
#             print(" ", end="")
#         for j in range(i * 2 + 1):
#             if j == 0 or j == i * 2 + 1 - 1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         else:
#             print("")
#     else:
#         for k in range(i - total // 2):
#             print(" ", end="")
#         for j in range((total - i) * 2 + 1):
#             if j == 0 or j == (total - i) * 2 + 1 - 1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         else:
#             print("")


# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i}*{j}={i*j} ",end="")
#     else:
#         print("")
