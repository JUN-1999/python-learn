# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 03元组.py
# @Time     : 2024/8/18 下午11:28

"""
1、元组 tuple 可以存放多个不同类型数据，元组是不可变序列

元组的定义
创建一个元组，只要逗号分割不同的数据项，使用圆括号即可
tuple_a=(1,2,3,4,5)
tuple_b=('red',12,True)

元组的访问
print(tuple_a[2]) #3

tuple_b = ('red', 12, True)
# print(tuple_b[2])

# 编辑一个元组
print('while------')
index = 0
while index < len(tuple_b):
    print(tuple_b[index])
    index += 1

print('for-------')
for ele in tuple_b:
    print(ele)

print(tuple, type(tuple_b))

"""

"""
1、tuple 定义一个空元组 () 或 tuple()
2、元组的元素有多个，可以嵌套元组，元素类型不限制，并且是有序的
3、元组是不可变序列 [新建之后不能修改]
4、可以修改元组内的list里的内容（包括 修改、增加、删除 等）
5、⭐定义只有一个元素的元组，需要带上逗号，否则不是元组类型 
tuple=(100,)
6、已经有了列表为什么还需要元组
    1、数据的写保护
    2、内存更少
    3、在多线程的时候希望数据不能修改
"""

"""
元组的操作

"""
# 使用+是拼接操作
tuple_add = (1, 2, 3) + (4, 5, 6)
print(tuple_add)
