# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 03嵌套分支.py
# @Time     : 2024/8/6 下午8:47

"""
多个if...else...嵌套

if xx:
    if xx:
        zz
    elif xx:
        zz
    else:
        zz
else:
    zz

"""

#
# score = float(input('输入你的成绩：'))
#
# if score > 8.0:
#     sex = str(input('请入你的性别[男|女]：'))
#     if sex == '男':
#         print('男子组')
#     elif sex == '女':
#         print('女子组')
#     else:
#         print('输入正确的性别')
# else:
#     print('淘汰')


month = int(input('输入月份：'))
age = int(input('输入年龄：'))

if 4 <= month <= 10:
    # if 18 <= age <= 60:
    #     print(60)
    # elif age < 18:
    #     print('半价')
    # elif age > 60:
    #     print('1/3')

    if age > 60:
        print('1/3')
    elif age >= 18:
        print(60)
    else:
        print('半价')
else:
    if 18 <= age <= 60:
        print('40')
    else:
        print('20')
