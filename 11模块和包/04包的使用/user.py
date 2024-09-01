# @Version  : 1.0
# @Author   : Jun1999
# @Name     : user.py
# @Time     : 2024/8/27 下午10:22
from math import fabs

# 1、导入包下的模块 import 包名.模块名
# import wjc_package.module01
# import wjc_package.module02
# 使用导入的模块
# wjc_package.module01.hi()

# 2、from 包名 import 模块名
# from wjc_package import module01,module02

# module01.hi()
# module02.ok()

# 3、from 包名.模块 import 函数、类、变量
#    from 包名.模块 import *
# from wjc_package.module01 import hi
# from wjc_package.module02 import ok
# hi()
# ok()


# 包中 __init__.py 使用 __all__ 可以限制使用的模块
# from wjc_package import *
#
# module02.ok()
# module01.hi()


# 包可以多个层级
# 方式一
# import wjc_package.wjc_package2.module03
# wjc_package.wjc_package2.module03.cal(1,2)

# 方式二
# from wjc_package.wjc_package2.module03 import cal as cal3
# cal3(1, 2)

# 方式三
# from wjc_package.wjc_package2 import  module03
# module03.cal(1, 2)


print(fabs(-90.8))