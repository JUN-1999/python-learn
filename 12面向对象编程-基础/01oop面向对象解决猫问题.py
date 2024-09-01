# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 01oop面向对象解决猫问题.py
# @Time     : 2024/8/28 下午11:31

"""
class 类名：
    属性。。。
    行为。。。

# 实例化
对象名=类名()

"""

class Cat:
    age = None  # 年龄
    name = None  # 名字
    color = None  # 颜色


# 通过类 创建一个实例
cat1 = Cat()
cat1.name = '小白'
cat1.age = 2
cat1.color = '白色'

# 通过对象名.属性名可以访问到属性值
print(f'cat1的信息：名字为{cat1.name} 年龄为{cat1.age} 颜色为{cat1.color}')
