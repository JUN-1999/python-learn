# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 11模板代码设计模式.py
# @Time     : 2024/9/1 上午12:23


"""
模板代码设计模式：
    使用抽象类规范需要实现的方法和公共抽象的部分
    由子类的实现抽象方法
    子类的实例去调用抽象类的普通方法，实现公共功能，在


"""
import time
from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def job(self):
        pass

    def job_time(self):
        start_time = time.time()
        print(start_time)
        self.job()
        end_time = time.time()
        print(end_time)
        print(f"工作时间为{end_time - start_time}秒")


class Work(Base):
    def job(self):
        i = 0
        for ele in range(1, 999999):
            i += ele
        print(i)

class Work2(Base):
    def job(self):
        i = 0
        for ele in range(1, 999999):
            i -= ele
        print(i)

w1=Work()
w1.job_time()
w2=Work2()
w2.job_time()