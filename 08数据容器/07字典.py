# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 07字典.py
# @Time     : 2024/8/20 下午9:25


"""
字典dict 的基本使用
是一种映射类型 使用 key-value 的形式
"""
# tel = {
#     'jack': 408,
#     "tom": 122,
#     'obj': {
#         'name': '王君臣',
#         'age': 18,
#         'address': '浙江'
#     }
# }
# print(tel)
# print(type(tel))
# print(tel['obj'])

"""
字典dict 使用细节
1、键使用字符串和数字
2、字典不支持索引
3、不支持while循环，只能使用for循环 ，得到是key
4、创建一个空字典 {} 或者 dict()
"""

# dict_b = {'one': 1, 'two': 2, 'three': 3}
# 依次取出key
# for key in dict_b:
#     print(f"key:{key} value:{dict_b[key]}")

# 依次取出value
# for value in dict_b.values():
#     print(f"value:{value}")

# 依次取出key-value
# for key,value in dict_b.items():
#     print(f"key:{key} value:{value}")


"""
字典的常用操作 
1、len(d):返回字典d中的项数
2、d[key]：返回d中以key为键的项。
3、d[key]=value ：原本存在修改，不存在新增
4、del d[key]： 将d[key]从d中移除
5、pop(key[,default])：如果key存在于字典中，将其移除并返回其值
6、keys：返回字典所有的key
7、key in d：如果d中存在键key则 返回 True
8、clear():移除字典所有元素
"""

"""
字典生成式
{字典key的表达式：字典value的表达式 for 表示key的变量，表示value的变量 in zip(可迭代对象，可迭代对象)}
"""
book = ["红楼梦", "sgyy", '11']
authors = ['曹雪芹', '罗贯中', '22']
print(dict(zip(book,authors)))
dict_a = {key: value for key, value in zip(book, authors)}
print(dict_a)
