# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 06构造方法.py
# @Time     : 2024/8/29 下午10:13

# 在创建类的对象时，直接指定这个对象的属性


class Person:
    name = None
    age = None

    # 构造方法，在初始化实例的时候会自动执行
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print(self.name,self.age)


p1=Person('wjc',18)
p1.get_info()