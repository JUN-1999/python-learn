# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 02列表.py
# @Time     : 2024/8/14 下午10:39

"""
创建一个列表，只要用逗号分隔的不同的数据项使用方括号起来即可
list1=[100,200,300,400]
list2=['red','green','black']
"""

# list1 = [1, 2, 3, 4, 5, 6]
# print(list1)  # 输出列表的所有数据项
# print(type(list1))  # 输出类型
#
# for item in list1:
#     print(item)
#
# i = 0
# while i < len(list1):
#     print(list1[i])
#     i += 1
# # 数字保留两位
# print(round(2.3456789, 2))


"""
1、注意事项 需要一个空列表，通过[]，或者list()
2、列表的元素可以有多个，并且数据类型没有限制，允许有重复元素，并且是有序的
3、下标从0开始
4、下班范围必须在指定范围内
5、索引也可以从尾部开始 最后一个为-1
6、往列表里添加、删除、修改数据
list[下标]=新值    # 修改指定下标得值
list.append(新值) # 添加数据
del list[下标]    # 删除第几个下标的值
7、修改列表内部值，列表地址不会有变化
"""

"""
列表常用方法
len(list)   :列表元素个数
max(list)   :返回列表元素最大值
min(list)   :返回列表元素最小值
list(seq)   :将元组转换为列表

列表常用操作
list.append(obj)    :在列表末尾添加新的对象
list.count(obj)     :统计某个元素在列表中出现的次数
list.extend(seq)    :在列表末尾一次性追加另一个序列中的多个值
list.index(obj)     :在列表中找出某个值第一个匹配项的索引位置
list.insert(index,obj) :将对象插入列表
list.pop([index=-1])   :移除列表中某个值的第一个匹配项
list.remove(obj)    ：移除列表中某个值的一个匹配项
list.reverse()      :反向列表中元素
list.sort(key=None,reverse=False)   ：对原列表进行排序
list.clear()        :清空列表
list.copy()         :复制列表（浅拷贝）
"""

print([1, 2, 3] + [4, 5, 6])

"""
列表生成式
[列表元素的表达式 for 自定义变量 in 可迭代对象]
"""
list=[ele * 2 for ele in range(1, 5)]
print(list)