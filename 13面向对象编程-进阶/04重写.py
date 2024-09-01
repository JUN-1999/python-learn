# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 04重写.py
# @Time     : 2024/8/31 下午9:52


"""
重写又称覆盖，即子类继承父类的属性和方法后，根据业务需要，再重新定义【同名的属性或方法】

"""

class A:
    n1=100
    def hi(self):
        print('A-hi')


class B(A):
    # n1=200
    def hi(self):
        print('B-hi')

b=B()
print(b.n1)
b.hi()