# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 07练习.py
# @Time     : 2024/8/31 下午11:11


class A:
    i = 10

    def sum(self):
        # 这里的self指向B 谁调用指向谁
        # 当调用对象成员的时候，会和对象本身动态关联
        return self.getI() + 10

    def sum1(self):
        return self.i + 10

    def getI(self):
        return self.i


class B(A):
    i = 20

    def getI(self):
        return self.i


b = B()
print(b.sum())
print(b.sum1())

"""
编程题
"""


class Employee:
    __name = None
    __month_salary = None

    def __init__(self, name, month_salary):
        self.__name = name
        self.__month_salary = month_salary

    def get_annual(self):
        pass

    def get_month_salary(self):
        return self.__month_salary

    def get_name(self):
        return self.__name

    def get_annual(self):
        return self.get_month_salary() * 12


class Worker(Employee):
    def __init__(self, name, month_salary):
        super().__init__(name, month_salary)

    def work(self):
        print('普通员工-'+self.get_name()+'-work')


class Manager(Employee):
    bonus = None

    def __init__(self, name, month_salary, bonus):
        super().__init__(name, month_salary)
        self.bonus = bonus

    def get_annual(self):
        return super().get_annual() + self.bonus

    def manage(self):
        print('经理-'+self.get_name()+'-manage')


# 获得任何员工对象的年工资
def show_emp_annual(e: Employee):
    print(e.get_annual())


def work(e: Employee):
    if isinstance(e, Worker):
        e.work()
    elif isinstance(e, Manager):
        e.manage()
    else:
        print('无法确认工作状态')

word = Worker('小王', 8000)
manager = Manager('小李', 10000, 20000)
show_emp_annual(word)
show_emp_annual(manager)
work(word)
work(manager)
