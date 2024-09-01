# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 06多态.py
# @Time     : 2024/8/31 下午10:31

"""
理解多态：
1、即多种状态，不同的对象调用相同的方法，表现出不同的状态，称为多态
2、多态通常作用在继承关系上

一个父类，具有多个子类，不同的子类对象调用相同的方法，执行的时候产生不同的状态，就是多态

"""

#
# # 动物类
# class Animal:
#     name = None
#
#     def __init__(self, name):
#         self.name = name
#
#
# class Cat(Animal):
#     pass
#
#
# class Dog(Animal):
#     pass
#
#
# # 食物类
# class Food:
#     name = None
#
#     def __init__(self, name):
#         self.name = name
#
#
# class Fish(Food):
#     pass
#
#
# class Meat(Food):
#     pass
#
#
# # 主人类-有一个喂食的方法feed
# class Master:
#     name = None
#
#     def __init__(self, name):
#         self.name = name
#
#     def feed(self, animal: Animal, food: Food):
#         print(f"主人{self.name}给{animal.name}喂{food.name}")
#
#
# # 创建动物
# cat = Cat('小花猫')
# dog = Dog('小黑狗')
# fish = Fish('鲤鱼')
# meat = Meat('五花肉')
# master=Master('王君臣')
#
# master.feed(cat,fish)
# master.feed(dog,meat)


"""
isinstance() 用于判断对象是否为某个类或者其子类的对象
isinstance(object,classinfo)
object:对象，实例对象
classinfo：可以是类名,基本类型或者它们组成的元组
"""

