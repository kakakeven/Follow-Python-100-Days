'''
双重循环实现 9 * 9 乘法表

@author: kakakeven
'''

for x in range(1, 10):
    for y in (1, x + 1):
        print("%d * %d = %d" % (x, y, x * y),end='\t')
