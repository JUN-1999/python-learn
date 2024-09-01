# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 02对象传递机制.py
# @Time     : 2024/8/29 下午8:46


class Cat:
    name = None
    age = None

# cat1 = Cat()
# cat1.name = '小花'
# cat1.age = 12
# cat2 = cat1
# cat2.name = '小花2'
# print(cat1.name)  # 小花2
# print(cat2.name)  # 小花2
# print(id(cat1), id(cat2))  # 相同id

# cat1 = Cat()
# cat1.name = '小花'
# cat1.age = 12
# cat2 = cat1
# cat2.name = '小花2'
# cat2 = None
# print(cat1.name) # 小花2
# # print(cat2.name)  # 报错 没有cat2.name
# print(id(cat1), id(cat2))

# 总结：实例一个对象后为一个地址，相等赋值是赋值地址，内部元素是指向相同的
