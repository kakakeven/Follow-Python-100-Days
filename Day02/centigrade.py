"""
华氏温度转摄氏温度
F = 1.8C + 32

@author: kakakeven
"""
f = float(input("请输入华氏温度: "))
c = (f - 32) / 1.8
print('%.1f 华温度 = %.1f 摄氏度' % (f, c))
