# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 05函数作为参数调用.py
# @Time     : 2024/8/9 下午8:57


"""



"""


def get_max_val(num1, num2):
    max_val = num1 if num1 > num2 else num2
    return max_val


def f1(fun, num1, num2):
    return fun(num1, num2)


def f2(fun, num1, num2):
    return num1 + num2, fun(num1, num2)


print(f1(get_max_val, 1, 2))
sum_val, max_val = f2(get_max_val, 2, 3)
print(sum_val, max_val)
