"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

@author: kakakeven
"""
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长： %f' % (a + b + c))
    # 海伦公式：https://zh.wikipedia.org/zh-hans/%E6%B5%B7%E4%BC%A6%E5%85%AC%E5%BC%8F
    # 使用边长计算面积
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积: %f' % area)
else:
    print('不能构成三角形')
