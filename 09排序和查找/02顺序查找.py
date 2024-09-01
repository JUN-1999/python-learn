# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 02顺序查找.py
# @Time     : 2024/8/22 下午10:21

find=3218
list1=[15,678,121,5484,321,3218,84,0]
for i in range(0,len(list1)):
    if list1[i] == find :
        print(list1[i],i)