# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 09_str_detail.py
# @Time     : 2024/7/23 下午10:39


"""
字符串 str 的说明


"""

# 单引号和双引号的区别
str1 = "tom说'123'"
str2 = 'jack说"456"'

print(str1)
print(str2)
print(type(str1))
print(type(str2))
# 通过加号可以连接字符串
print(str1 + ' ' + str2)

# 注意事项
"""
python 不支持单字符类型，单字符在python中也是作为一个字符串使用
用三个单引号或者三个双引号 可以将内容保留格式原样输出
在字符串前面加‘r’可以使整个字符串不会被转义
"""

print("""
 什么东西
 真的 可以吗？？
 hello world
""")

str4 = r"jack\ntom\tking"
print(str4)

# 字符串的驻留机制
string1 = "Hello"
string2 = "Hello"
string3 = "Hello"
# id 返回对象的内存地址
print('string1',id(string1))
print('string2',id(string2))
print('string3',id(string3))
