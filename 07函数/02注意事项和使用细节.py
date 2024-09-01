# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 02注意事项和使用细节.py
# @Time     : 2024/8/8 下午9:33

"""
1、函数的参数列表可以是多个，也可以没有
2、函数的命名遵循标识符命名规则和规范
3、同名函数最近执行
4、传递的实参和定义的形参顺序和个数必须一直，否则报错
5、函数可以返回多个值，返回类型不受限制
def f2(n1,n2):
    return n1+n2,n1-n2

r1,r2=f2(10,20)
6、函数支持关键字参数：即函数调用通过 形参名=实参值，
    这样子不受顺序的限制

def book_info(name,price,author):
    print(name,price,author)

book_info(name='xxx',price=16,author='mmm')

7、函数支持默认参数/缺省参数 默认值需要在参数列表后
def book_info(name='xxx',price=16,author='mmm')
    print(name,price,author)

book_info('aaa')

8、函数支持可变参数/不定长参数
当不确定函数有多少个函数，多个参数会变为元组

def sum(*args):
    total=0
    for ele in args:
        total += ele
    return total

sum(1,2,3,34)

9、函数的可变参数/不定长参数，还支持多个关键字参数，也就是多个 “参数名=实参值”
多个关键字参数会变为字典(对象)

def sum(**args):
    for arg_key in args:
        print(f"{arg_key}-{args[arg_key]}")

10、 python 调用 另一个.py中的函数
f1.py
def add(x,y)
 print(x+y)

f2.py
import f1
f1.add(1,2)


sum(name='xxx',age=18,email='2@qq.com')

"""
