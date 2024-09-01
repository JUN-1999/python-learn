# @Version  : 1.0
# @Author   : Jun1999
# @Name     : house.py
# @Time     : 2024/9/1 下午10:29

"""
数据层：存储数据
1、编写House类
2、一个House对象表示一个房屋信息
"""


class House:
    def __init__(self, id, name, phone, address, rent, state):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
        self.rent = rent
        self.state = state

    # 重写 __str__ 按照格式
    def __str__(self):
        return f"{self.id}\t\t{self.name}\t\t{self.phone}\t\t{self.address}\t\t{self.rent}\t\t{self.state}"
