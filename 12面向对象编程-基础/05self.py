# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 05self.py
# @Time     : 2024/8/29 下午9:33


# self 表示当前对象本身，简单地说就是哪个对象调用，self就代表哪个对象

class Dog:
    name=None
    age=None

    # 2、使用@staticmethod 可以定义一个静态方法，不需要self
    # 2、可以实例调用也可以直接类调用
    @staticmethod
    def run():
        print('run')


dog1=Dog()
dog1.run()
Dog.run()