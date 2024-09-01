# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 09Class对象和静态方法.py
# @Time     : 2024/8/31 下午11:53

class A:
    name = 'www'

    def hi(self):
        print('输出')

    # 将方法转换为静态方法，
    # 静态方法不会接受隐式的第一个参数，要声明一个静态方法
    # 静态方法既可以类调用 A.f() 也可以实例调用 A().f()
    @staticmethod
    def f(arg1,arg2):
        print(arg1,arg2)


print(A)
print(f"类的name:{A.name}")
# 通过类名如何调用非静态成员方法，需要显示的传入self的值
A.hi(A)
