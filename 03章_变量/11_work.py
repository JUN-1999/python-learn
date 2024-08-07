# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 11_work.py
# @Time     : 2024/7/23 下午11:37


name = '某某某'
age = 18
score = 99
sex = '男'
hobby = '唱跳rap'
# 拼接字符串
str = name + "\t" + str(age) + "\t\t" + str(score) + "\t\t" + sex + "\t\t" + hobby
print(f"姓名\t\t年龄\t\t成绩\t\t性别\t\t爱好\n{str}")

print(f"""
姓名  年龄  性别
{name}  {age}   {sex}
""")
