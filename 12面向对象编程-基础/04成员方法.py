# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 04成员方法.py
# @Time     : 2024/8/29 下午8:59


# 在类中定义的行为（函数），我们成为：成员方法

class Person:
    name = None
    age = None

    def hi(self):
        print(self.name, '在奔跑')

    def cal02(self, n):
        sum = 0
        i = 1
        while (i <= n):
            sum += i
            i += 1
        return sum

    def get_sum(self, num1, num2):
        return num1 + num2


person1 = Person()
person1.name = '王君臣'
person1.age = 18
person1.hi()
total = person1.cal02(12)
print('total', total)
sum = person1.get_sum(1, 2)
print('sum', sum)
