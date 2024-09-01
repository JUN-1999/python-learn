# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 02导入模块.py
# @Time     : 2024/8/27 下午9:35


# 1、多个模块导入，用 模块.xx使用
# import math
# import random
# random_num=random.random()*100
# print(random_num)
# print(math.floor(random_num))


# 2、导入模块的指定功能
# 直接使用功能名，不需要模块名
# from math import fabs
# print(fabs(-2.3269))

# 3、导入模块的全部功能
# 导入模块的全部功能、直接使用不需要带模块名(不直观，用于很熟悉的模块)
# from math import *
# print(fabs(-2.15))


# 4、给导入的模块或者功能取别名
# import 模块 as 别名
# import 模块 import 函数、类、变量...as 别名
# 1）import模块as别名：给导入的模块取别名，使用别名.xx
# 2）form 模块 import 函数、类、变量 ...as 别名：给导入的某个功能取别名，使用时直接用别名即可

import random as r
from math import floor as mfl,fabs as mfa
print(mfl(r.random()*100))
print(mfa(r.random()*-100))


