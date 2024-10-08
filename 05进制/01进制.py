# @Version  : 1.0
# @Author   : Jun1999
# @Name     : 01进制.py
# @Time     : 2024/8/1 下午8:52


"""
2进制     0B
8进制     0O
10进制
16进制    0X
"""

"""
进制转换 基本功

第一组
1、二进制转十进制
从右到左，取出每个数字，位数从0开始，乘2的位数几次方
0B1011 = (1*2^3)+(0*2^2)+(1*2^1)+(1*2^0)
       = 8+0+2+1
       = 11
2、八进制转十进制
从右到左，取出每个数字，位数从0开始，乘8的位数几次方
0O234 = (2*8^2)+(3*8^1)+(4*8^0)
      = 128+24+4
      = 156
3、十六进制转十进制
从右到左，取出每个数字，位数从0开始，乘16的位数几次方
0X23A = (2*16^2)+(3*16^1)+(10*16^0)
      = 512+48+10
      = 570
      
课后练习：
0B110001100 = 1*2^8+1*2^7+1*2^3+1*2^2
            = 256+128+8+4
            = 396
0O2456 = 2*8^3+4*8^2+5*8^1+6*8^0
       = 1024+256+40+6
       = 1326
0XA45 = 10*16^2+4*16^1+5*16^0
      = 2560+64+5
      = 2629

第二组
1、十进制转二进制
将数不断除以2，直到商为0为止，然后将每步得到的余数倒过来，就是对应的二进制
34/2=17...0
17/2=8...1
8/2=4...0
4/2=2...0
2/2=1...0
1/2=0...1
34 = OB100010

使用内置函数 bin(num) num为十进制数，可以输出为0B开头的二进制 

2、十进制转八进制
将数不断除以8，直到商为0为止，然后将每步得到的余数倒过来，就是对应的二进制
131/8=16...3
16/8=2...0
2/8=0...2
131 = 0O203

使用内置函数 oct(num) num为十进制数，可以输出为0O开头的八进制 

3、十进制转十六进制
将数不断除以16，直到商为0为止，然后将每步得到的余数倒过来，就是对应的十六进制
237/16=14...13-D
14/16=0...14-E

237=0XED

使用内置函数 hex(num) num为十进制数，可以输出为0X开头的八进制 


课后练习：
123 => 二进制 bin
123/2=61...1
61/2=30...1
30/2=15...0
15/2=7...1
7/2=3...1
3/2=1...1
1/2=0...1
0B1111011

678 => 八进制 oct
678/8=84...6
84/8=10...4
10/8=1...2
1/8=0...1
0O1246

8912 => 十六进制 hex
8912/16=557...0
557/16=34...13-D
34/16=2...2
2/16=0...2
0X22D0

第三组、
1、二进制转八进制
从低位开始，将二进制数每三位一组，转为对应的八进制数即可
0B11010101 = 11 010 101
           = 1*2^1+1*2^0 1*2^1 1*2^2+1*2^0
           = 3 2 5
           = 0O325
           
2、二进制转十六进制
从低位开始，将二进制数每四位一组，转为对应的八进制数即可
0B11010101 = 1101 0101
           = 1*2^3+1*2^2+1*2^0 1*2^2+1*2^0
           = 8+4+1 4+1
           = 13 5
           = 0XD5
           
课后练习：
0B11100101 = 11 100 101
           = 3 4 5
           = 0O345
0B1110010110 = 11 1001 0110
             = 3 9 6
             = 0X396

第四组
1、八进制转二进制
将八进制的每一位转为三位的二进制数即可
0O237 = 010 011 111
      = 0B010011111

2、十六进制转二进制
将十六进制的每一位转为四位的二进制数即可
0X23B = 0010 0011 1011
      = 0B001000111011
      
      
课后练习：
0O1230转为二进制
0O1230 = 001 010 011 000
       = 0B1010011000
       
0XAB29转为二进制
0XAB29 = 1010 1011 0010 1001
       = 0B1010101100101001
"""

# 作业一：进制转为十进制
# print(0B110001100) # 396
# print(0O2456) # 1326
# print(0XA45) # 2629

# 作业二：十进制转为各个进制
# print(bin(123))  # 0B1111011
# print(oct(678))  # 0O1246
# print(hex(8912))  # 0X22D0

# 作业三：二进制转为八进制和十六进制
# print(oct(0B11100101))
# print(hex(0B1110010110))

# 作业四：八进制和十六进制转为二进制
# print(bin(0O1230))
# print(bin(0XAB29))
