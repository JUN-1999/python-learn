# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 08_bool_detail.py
# @Time     : 2024/7/23 下午10:18


# bool 布尔值 使用 True 和 False 【区分大小写，关键字】

num1 = 100
num2 = 200

# 把比较的结果赋值给result 为 bool 类型
result = num1 > num2
print('result的类型是', result)
if num1 < num2:
    print("num1<num2")

""" bool 的使用细节
1、布尔类型只有两个值： True 和 False
2、布尔类型可以和其他类型进行比较，比如数字、字符串等，在比较的时候python会把True当作1，False当作0
3、在python中，非0被视为真值，0值被是为假值

"""
