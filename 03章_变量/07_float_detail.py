# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 07_float_detail.py
# @Time     : 2024/7/23 下午10:01
import sys

# 浮点数的类型
# 表示形式 1、小数  2、科学计数法
n5 = 5.12e2  # 5.12乘以 【10的2次方】
n6 = 5.12e-2  # 5.12除以 【10的2次方】

# 浮点数的最大和最小值
print('浮点数最大值：', sys.float_info.max)
print('浮点数最小值 ', sys.float_info.min)


# 浮点数计算存在进度缺失，可以使用Decimal类，需要导入使用
print(0.1+0.2)
# 导入 Decimal 类
from decimal import Decimal
print(Decimal("0.1")+Decimal("0.2"))
