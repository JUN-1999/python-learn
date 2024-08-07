# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 03逻辑运算符.py
# @Time     : 2024/7/29 下午11:06


"""

and x and y     布尔与：如果 x为 false，x and y 返回x的值，否则返回y的值
or  x or y      布尔或：如果 x 为 true，返回x的值，或者返回y的值
not not x       布尔非：取反，


0 值为假 非0为真
"""

a = 10
b = 0
print(a and b)
print(a or b)
print(not (a and b))

"""
and 逻辑运算符 ，第一个true，返回第二个值
                第一个false，返回第一个值
"""
# 判断一个成绩是否在 60-80之间
score = 40
if (score >= 60) and (score <= 80):
    print('在60-80氛围内')
elif (score > 80):
    print('在90分以上')
else:
    print('低于60分')

"""
or 逻辑运算符
短路运算符，只有第一个为true，直接返回第一个值
            第一个为false，则返回第二个值
"""

# 判断一个成绩是否小于等于60或者大于等于80
score = 81
if score <= 60 or score >= 80:
    print('是的')


"""
not 运算符
对一个值对反 返回true 或者 false
"""
