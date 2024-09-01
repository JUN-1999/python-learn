# @Version  : 1.0
# @Author   : Jun1999
# @Name     : house_operation.py.py
# @Time     : 2024/9/1 上午9:40

"""
    说明：提供房屋出租的所有操作
"""
from my_tools import *

# 房屋信息-全局变量
houses: list[dict] = [
    {
        "id": 1,
        "name": "wjc",
        "phone": 132123,
        "address": "浙江",
        "rent": 1800,
        "state": "已出租"
    }
]
# 自增id-全局变量
id_counter = 1


def main_menu():
    """
    显示主菜单
    :return:
    """
    print()
    print("房屋出租系统菜单".center(32, "="))
    print('\t\t\t 1、新增房源')
    print('\t\t\t 2、查找房屋')
    print('\t\t\t 3、删除房屋信息')
    print('\t\t\t 4、修改房屋信息')
    print('\t\t\t 5、房屋列表')
    print('\t\t\t 6、退出')


def list_house():
    """
    显示房屋列表
    :return:
    """
    print("房屋列表".center(32, "="))
    # 打印表头信息
    print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态")
    # 打印表格信息
    for house in houses:
        for value in house.values():
            print(value, end="\t\t")
        print()
    print("房屋列表显示完毕".center(32, "="))


def add_house():
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
    # 由系统分配房屋id
    global id_counter
    id_counter += 1

    houses.append({
        "id": id_counter,
        "name": name,
        "phone": phone,
        "address": address,
        "rent": rent,
        "state": state
    })


def del_house():
    """
    根据id删除房屋信息
    :return:
    """
    print('删除房屋信息'.center(32, "="))
    del_id = int(input("请输入待删除的房屋编号(-1退出)："))
    if del_id == -1:
        print('放弃删除房屋信息')
        return

    key = read_confirm_select()

    if key == 'y':
        # 根据del_id 去house列表查找是否存在该房屋
        house = find_by_id(del_id)
        if house:
            print(f"完成删除房源{del_id}")
            houses.remove(house)
        else:
            print('输入错误id，删除错误'.center(32, "="))
    else:
        # 取消删除
        print("放弃删除房屋信息".center(32, "="))


def find_by_id(find_id):
    """
    根据输入的find_id返回对应的房屋信息（字典），如果没有就返回None
    :param find_id:
    :return:
    """
    # 遍历houses列表
    for house in houses:
        if house["id"] == find_id:
            return house
    return None


def exit_sys():
    """
    完成退出系统，并完成
    :return:如果是确认退出返回True，否则返回False
    """
    choice = read_confirm_select()
    if choice == 'y':
        return True
    else:
        return False


def find_house():
    """
    根据id查找到房屋信息
    :return:
    """
    find_id = int(input('输入查询的房屋id'))

    house = find_by_id(find_id)
    if house:
        # 打印表头信息
        print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态")
        for value in house.values():
            print(value, end="\t\t")
        print()
    else:
        print(f"房屋id{find_id}不正确")


def update_house():
    """
    根据id修改房屋信息
    :return:
    """
    find_id = int(input('输入查询的房屋id（-1表示退出）'))

    if find_id == -1:
        print('放弃修改房屋信息')
        return
    house = find_by_id(find_id)
    if not house:
        print(f"房屋id{find_id}不正确".center(32, '='))
        return

    # 先按照简单的方式完成

    #  name = input(f"姓名({house['name']})：")
    #  if len(name) > 0:  # 如果用户有内容
    #     house['name'] = name
    house['name'] = read_str(f"姓名({house['name']})：", house['name'])
    house['phone'] = read_str(f"电话({house['phone']})：", house['phone'])
    house['address'] = read_str(f"地址({house['address']})：", house['address'])
    house['rent'] = int(read_str(f"月租({house['rent']})：", house['rent']))
    house['state'] = read_str(f"地址({house['state']})：", house['state'])
