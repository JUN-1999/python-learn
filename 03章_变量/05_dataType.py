# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 05_dataType.py
# @Time     : 2024/7/22 下午11:26


# 数据类型
"""
整型 int
浮点数 float
布尔值 bool
字符串 string
"""

# type函数的使用
type_int = 1
type_float = 2.1
type_bool = True
type_string = "string"

print(
    type(type_int),
    type(type_float),
    type(type_bool),
    type(type_string),
)

# 可以直接查看字面量的类型
print(f"hello字面量的类型是{type("hello")}" )
