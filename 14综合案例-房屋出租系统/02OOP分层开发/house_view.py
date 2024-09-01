# @Version  : 1.0
# @Author   : Jun1999
# @Name     : house_view.py
# @Time     : 2024/9/1 下午10:29

"""
界面层 显示页面
1、编写类HouseView
2、显示界面
3、接受用户的输入
4、调用业务层的方法完成对房屋的各种操作
"""
from house_service import *
from house import *
from utility import *


class HouseView:
    house_operation: HouseService = HouseService()

    def main_menu(self):

        while True:
            print()
            print("房屋出租系统菜单".center(32, "="))
            print('\t\t\t 1、新增房源')
            print('\t\t\t 2、查找房屋')
            print('\t\t\t 3、删除房屋信息')
            print('\t\t\t 4、修改房屋信息')
            print('\t\t\t 5、房屋列表')
            print('\t\t\t 6、退出')
            key = int(input("请输入你的选择(1-6)"))
            if key in [1, 2, 3, 4, 5, 6]:
                if key == 1:
                    self.add_house()
                elif key == 2:
                    self.find_house()
                elif key == 3:
                    self.del_house()
                elif key == 4:
                    self.update_house()
                elif key == 5:
                    self.list_houses()
                elif key == 6:
                    if self.exit_sys():
                        break
            else:
                print('请输入范围内的数字')

    def list_houses(self):
        """
        显示房屋列表
        :return: 房屋列表
        """
        houses = self.house_operation.get_houses()
        print("房屋列表".center(32, "="))
        # 打印表头信息
        print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态")
        # 打印表格信息
        for house in houses:
            print(house)

        print("房屋列表显示完毕".center(32, "="))

    def add_house(self):
        """
           添加房屋信息
           :return:
           """
        print("添加房屋".center(32, "="))
        name = input("姓名：")
        phone = input("电话：")
        address = input("地址：")
        rent = int(input("租金："))
        state = input("状态：")

        new_house = House(0, name, phone, address, rent, state)
        self.house_operation.add(new_house)

    def del_house(self):
        print('删除房屋信息'.center(32, "="))
        del_id = int(input("请输入待删除的房屋编号(-1退出)："))
        if del_id == -1:
            print('放弃删除房屋信息')
            return

        key = Utility.read_confirm_select()

        if key == 'y':
            del_flag = self.house_operation.del_by_id(del_id)
            if del_flag:
                print('删除成功')
            else:
                print('错误的id，删除房屋信息失败')
        else:
            # 取消删除
            print("放弃删除房屋信息".center(32, "="))

    def exit_sys(self):
        """
        退出系统需要确认
        :return:
        """
        key = Utility.read_confirm_select()
        if key == 'y':
            return True
        else:
            return False

    def find_house(self):
        find_id = int(input('输入查询的房屋id'))

        house = self.house_operation.find_by_id(find_id)
        if house:
            # 打印表头信息
            print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态")
            print(house)
        else:
            print(f"房屋id{find_id}不正确")

    def update_house(self):
        """
            根据id修改房屋信息
            :return:
            """
        find_id = int(input('输入查询的房屋id（-1表示退出）'))

        if find_id == -1:
            print('放弃修改房屋信息')
            return
        house = self.house_operation.find_by_id(find_id)
        if not house:
            print(f"房屋id{find_id}不正确".center(32, '='))
            return

        # 对象修改值 对象.键   字典修改值 字典[键值]
        house.name = Utility.read_str(f"姓名({house.name})：", house.name)
        house.phone = Utility.read_str(f"电话({house.phone})：", house.phone)
        house.address = Utility.read_str(f"地址({house.address})：", house.address)
        house.rent = int(Utility.read_str(f"月租({house.rent})：", house.rent))
        house.state = Utility.read_str(f"地址({house.state})：", house.state)
