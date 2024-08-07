# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 09键盘输入语句.py
# @Time     : 2024/7/30 下午10:53


"""
input(text) text为输入的提示信息
接收到的信息是字符串
"""

"""
    name = input('请输入姓名 ')
    age = input('请输入年龄 ')
    score = input('请输入成绩 ')
    
    print('姓名是', name, '年龄是', age, '成绩是', score)
    
    # 如果需要进行算术运算-需要进行类型转换
    print(10 + int(score))
"""

# 当然也可以在接受的时候直接转为需要的类型
age = int(input('请输入年龄 '))
print(type(age))
print(age + 10)
