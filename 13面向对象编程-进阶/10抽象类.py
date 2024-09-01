# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 10抽象类.py
# @Time     : 2024/9/1 上午12:00
from abc import ABC, abstractmethod


# 主要着重于设计

# Animal就是一个抽象类：
# 注意：抽象类（含有抽象方法），不能被实例化
# 抽象类需要继承ABC，并且至少要有一个抽象方法
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    # 这时 cry 就一个抽象方法
    @abstractmethod
    def cry(self):
        pass


class Dog(Animal):

    def cry(self):
        print('汪汪叫')


dog = Dog('小虎')
print(dog.name)
dog.cry()
