# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 03调用父类成员.py
# @Time     : 2024/8/31 下午8:41

"""
  如果子类和父类出现同名的成员，可以通过 父类名、super() 访问 父类的成员


方式一:
    --访问成员变量：父类名.成员变量
    --访问成员方法：父类民.成员方法(self)

方式二:
    --访问成员变量：super().成员变量
    --访问成员方法：super().成员方法()
    --⭐ super 是指直接父类

建议使用super方法，不受父类类名的影响
"""


class A:
    n1 = 100

    def run(self):
        print("A-run")


class B(A):
    n1 = 200

    def say(self):
        print(f"say-父类的n1:{A.n1} 本类的n1:{self.n1}")
        # 调用父类的run
        A.run(self)
        # 调用本类的run
        self.run()

    def hi(self):
        print(f"hi-父类的n1:{super().n1}")
        super().run()

    def run(self):
        print('B-run')


b = B()
b.say()
b.hi()