# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 05类型注解.py
# @Time     : 2024/8/31 下午9:58


"""
type hint -- 类型注解：对类型的提示
"""


# a:str 给形参a进行类型注解，标注a的类型是str
def fun1(a: str):
    for ele in a:
        print(ele)


fun1('123')

"""
    基础数据类型注解
    变量：类型
 """
# 基础数据类型注解
n1: int = 10
n2: float = 10.1
is_pass: bool = True
name: str = 'xxx'


# 类类型注解
class Cat:
    pass


# 对cat进行类型注解 cat的类型为Cat类
cat: Cat = Cat()

# 容器类型注解
my_list: list = [1, 2, 3]  # 列表
my_tuple: tuple = (1, 2, 3)  # 元组
my_set: set = {1, 2, 3, 1}  # 集合
my_dict: dict = {'a': 1, 'b': 2}  # 字典

# 容器的详细类型注解
my_list2: list[int] = [1, 2, '3']
my_tuple2: tuple[str, int, str] = ('1', 2, '3')
my_set2: set[str] = {'2', 2, 3}
# my_dict2: dict[str, int] 类型注解的含义：
# key的类型是str，value是int
my_dict2: dict[str, int] = {'a': 1, 'b': '2'}
# my_dict2 = {'a': 'str'} # 会黄色警告提示，在重新赋值的时候生效


"""
在函数中的类型注解
def 函数/方法名(形参名：类型，形参名：类型。。。)->返回值类型：
    函数/方法体
"""


def fun1(name: str) -> str:
    str_like = ''
    for ele in name:
        print(ele)
        str_like += ele
    return str_like


print(fun1('wjc'))


def sum(num1: int, num2: int) -> int:
    return num1 + num2


print(sum(1, 2))

"""
    联合类型的使用：
    typing.Union:Union[x,y]等价于X|Y,意味着X或Y满足之一即可
    如果需要使用 Union 需要先导入 不然会报错
    from typing import Union
"""
from typing import Union

a: Union[int, str] = 1
my_list3: list[Union[int, str]] = []


def cal(
        num1: Union[float, int],
        num2: Union[float, int]
) -> Union[float, int]:
    return num1 + num2


print(cal(11, 2.2))
