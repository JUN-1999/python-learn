# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 01封装.py
# @Time     : 2024/8/30 下午9:36

"""
静态的方法：可以直接类去调用，不用实例也可以
公有的方法：在类的内部和外部都可以访问
私有的方法：使用双下划线__开头命名，只能在类的内部使用，
"""


# 创建职员类（Clerk），属性有 name，job，salary
# 不能随便查看职员的职位和工资等隐私
# 提供公共方法，对职位和工资进行操作

class Clerk:
    name = None
    __job = None
    __salary = None

    def __init__(self, name, job, slalry):
        self.name = name
        self.__job = job
        self.__slalry = slalry

    def get_job(self):
        return self.__job

    def set_name(self, new_job):
        self.__job = new_job


c1 = Clerk('王君臣', '前端', 15000)
print(c1.get_job())
c1.set_name('全干工程师')
print(c1.get_job())
