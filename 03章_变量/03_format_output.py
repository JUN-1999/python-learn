# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 03_format_output.py.py
# @Time     : 2024/7/16 下午10:49


# 格式化输出案例
age = 80
score = 77.5
gender = '男'
name = "某某某"

# %占位符 s字符串 d整数型 f浮点数
print("个人信息:%s-%d岁-%s-%.2f分" % (name, age, gender, score))

# format()函数
print("个人信息:{}-{}岁-{}-{}分".format(name, age, gender, score))

# f-string 【推荐】
print(f"个人信息:{name}-{age}岁-{gender}-{score}分")
