# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 10综合练习.py
# @Time     : 2024/8/7 下午11:34


money = 100000
count = 0
while True:
    if money > 50000:
        money -= money * 0.05
    else:
        money -= 1000
    count += 1
    if money < 1000:
        break

print(count,money)
