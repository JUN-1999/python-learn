# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 01断点调试.py
# @Time     : 2024/8/26 下午9:29

"""
  F7         跳入：跳入方法/函数内
  F8        跳过：逐行执行代码
  shift+F8  跳出：跳出方法/函数
  F9        resume：执行到下一个断点
"""

res = 0
for i in range(0, 10):
    res += i
    print(i, res)
