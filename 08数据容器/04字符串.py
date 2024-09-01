# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 04字符串.py
# @Time     : 2024/8/19 下午9:36

"""
ord 返回单个字符对应的Unicode编码值
"""

"""
字符串常用方法
1、len(str) 字符串的长度
2、str.replace(old,new,[,count]) 返回字符串的副本，将所有的字符串old替换为new，如果给出可选参数，则使用固定次数
3、str.split(sep,maxsplit) 对字符串根据sep进行分割
4、str.count 统计指定字符串在字符串中出现的次数
5、str.index 从字符串中找出指定字符串的第一个匹配项
6、str.strip([chars]) 移除其中的前导和末尾字符
7、str.lower() 返回字符串小写的副本
8、str.upper() 返回字符串大写的副本
"""


"""
str_names="tom jack mary nono smith hsp"
1、统计一共多少个人名
2、如果有 ”hsp“ 替换为 "老韩"
3、如果人名是英文，则首字母改为大写
"""

str_names="tom jack mary nono smith hsp"
print(f'一共有 {len(str_names.split(' '))}个人名')
str_names_new=str_names.replace('hsp','老韩')
print(str_names_new)


