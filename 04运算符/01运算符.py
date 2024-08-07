# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 01运算符.py
# @Time     : 2024/7/29 下午10:37


"""
算术运算符
赋值运算符
比较运算符
逻辑运算符
位运算符【需要二进制基础】
"""

"""

%   取模（取余） a % b = a - a // b * b
//  取整除-返回商的整数部分（向下取整）
**  返回x的y次幂 3 ** 2 = 9

"""

# 假如还有97天放假 计算 xx个星期零xx天
totalDay = 97
totalWeek = totalDay // 7
totalOneDay = totalDay % 7
print(f"假如还有{totalDay}天放假，还有{totalWeek}个星期{totalOneDay}天")
print(13 * 7 + 6)

# 定义一个变量保存华氏温度，华氏温度转摄氏度的公式为5/9*（华氏度-100）
hsd = 234.5
ssd = 5 / 9 * (hsd - 100)
print(f"华氏度{hsd}=摄氏度{ssd}")
print("华氏度%.2f=摄氏度%.2f" % (hsd, ssd))
