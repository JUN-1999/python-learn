# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 04for循环.py
# @Time     : 2024/8/6 下午9:43


"""
基本语句
for 变量 in 范围/序列:
    循环操作语句
"""

# 定义一个列表
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(type(nums))
# for i in nums:
#     print(i,'hello world')


# 使用内置函数生成一个需要的数列 range(start,stop,[step]) 开始和结束：前闭后开
#                           range(开始的值：默认为0，结束的值，步长：默认为1)
# r1 = range(5)  # 单个参数是指stop的值
# print(list(r1))
#
# r2 = range(1, 10, 2)
# print(list(r2))
#
# for i in range(3):
#     print(i, 'list')


"""
for 可以和 else 配合使用

语法格式：
for 变量 in 可遍历数列
    执行语句
else:
    执行语句
    
什么情况下会执行else下的执行语句：就是for循环正常的完成遍历，在遍历的过程中，没有打断（解释：比如break语句）
"""

for i in range(3):
    # if i==2:
    #     break
    print(i)
else:
    print('正常循环')
