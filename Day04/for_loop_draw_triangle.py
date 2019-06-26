"""
打印各种三角形图案

@author: kakakeven
"""

row = int(input("请输入行数: "))

for i in range(row):
    for _ in range(i+1):
        print('*',end='')
    print()


for i in range(row):
    pass