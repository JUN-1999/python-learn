# @Version  : 1.0
# @Author   : Jun1999
# @Name     : __init__.py.py
# @Time     : 2024/8/27 下午10:21


# __init__.py 通过 __all__控制允许导入的模块
# 在__init__.py中增加__all__=[允许导入的模块列表]
# 针对 from 包 import * 方式生效，对 import xx 方式不生效


__all__=['module02','module01']