# @Version  : 1.0
# @Author   : Jun1999
# @Name     : house_service.py
# @Time     : 2024/9/1 下午10:29

"""
业务层：处理数据
1、编写HouseService
2、提供方法完成对房屋的各种操作-增删改查CRUD
3、
"""

from house import *


class HouseService:
    houses = []
    id_counter = 1

    def __init__(self):
        # 为了测试方便，给我们列表放入一个测试对象
        house = House(1, 'wjc', 132, '地址', 800, '未出租')
        self.houses.append(house)

    def get_houses(self):
        """
        返回房屋列表
        :return: 房屋列表
        """
        return self.houses

    def add(self, new_house: House):
        """
        将添加到的new_house，新增到houses中
        :param new_house:  新的房屋信息
        :return:
        """
        self.id_counter += 1
        new_house.id = self.id_counter
        self.houses.append(new_house)

    def find_by_id(self, find_id):
        """
        根据find_id返回对应的房屋信息
        :param find_id:
        :return:
        """
        for house in self.houses:
            if find_id == house.id:
                return house
        return None

    def del_by_id(self, del_id: int):
        """
        根据收到的id删除房屋信息
        :param del_id:
        :return:
        """
        house = self.find_by_id(del_id)
        if house:
            self.houses.remove(house)
            return True
        else:
            return False
