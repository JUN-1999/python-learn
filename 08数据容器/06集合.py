# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 06集合.py
# @Time     : 2024/8/20 下午7:57


"""
集合是由 不重复元素组成的无序容器
不重复：不会有相同的元素
无序：取出的元素和存入的顺序不一致


"""
# 用一个大括号里面数据逗号分割
# set_1 = {100, 200, 300, 400, 500, 600}
# print(set_1, type(set_1))
# set_2 = {'apple', 'blenner', 'blenner', 'blenner', 'blenner', 'pear'}
# print(set_2)

"""
注意事项和使用细节
1、会自动去重
2、集合不支持索引
3、集合不支持while循环，只能使用for
4、创建空集合只能用set(),不能用{}，{}创建的是一个字典
"""
set_1 = {}  # 创建一个字典
set_2 = set()  # 创建一个空集合

print(f"set_1,{set_1}{type(set_1)}")
print(f"set_2,{set_2}{type(set_2)}")

"""
集合常用操作一览
1、len(集合)： 返回集合个数
2、x in s ： 检测s是否为s中的成员
3、add(ele)：将元素ele添加到元素中
4、remove(ele)：从集合中移除元素ele
5、pop()：从集合中移除并返回任意一个元素
6、clear()：从集合中移除所有元素
7、union(*others)
set | other | ...：返回一个新集合，对集合求并集 
8、intersection(*other)
set & other & ...：返回一个新集合，对集合求交集
9、difference(*other)
set-other-...：返回一个新集合，对集合求差集
"""


"""
集合生成式
{集合元素的表达式 for 自定义变量 in 可迭代对象}
"""
list1=[ele*2 for ele in range(1,5)]
print(list1)
set1={ele*2 for ele in range(1,5)}
print(set1)
set2={ele+ele for ele in "王1君2臣1"}
print(set2)