# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 02继承.py
# @Time     : 2024/8/30 下午11:08

"""
继承：当多个类存在相同的属性和方法，可以抽象到父类


class 子类(父类):
    子类的其他属性、方法


派生类会自动拥有基类定义的属性和方法
基类习惯上也叫父类
派生类也叫子类
"""


class Stduent:
    name = None
    age = None
    __score = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

    def get_info(self):
        print(f"姓名：{self.name},成绩：{self.__score}")


class pupil(Stduent):
    def do(self):
        print('小学生在考试-小学数学', self.get_score())


class undergraduate(Stduent):
    def do(self):
        print('大学生在考试-高数', self.get_score())


p = pupil('小学生', 8)
p.set_score(80)
p.get_info()
p.do()

u = undergraduate('大学生', 18)
u.set_score(48)
u.get_info()
u.do()

# 子类可以访问到父类的公共属性和方法
# 子类不可以访问到父类的私有属性和方法【如果需要访问父类的私有，需要提供公共的方法返回私有】
# ctrl+h 可以查看继承关系

# ⭐在多重继承中，如果有同名的成员，遵守从左到右的继承优先级
# 即：写在左边的父类优先级高，写在右边的父类优先级低

# super().__init__(xx1,xx2,xx3)
# 可以通过super访问父类的构造器
