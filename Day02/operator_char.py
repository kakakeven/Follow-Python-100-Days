"""
运算符的使用

@author: kakakeven
"""
a = 5
b = 10
c = 3
d = 4
e = 5
a += b  # a = 15
a -= c  # a = 12
a *= d  # a = 48
a /= e  # a = 9.6
print("a = ", a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)  # True
print("flag2 = ", flag2)  # False
print("flag3 = ", flag3)  # False
print("flag4 = ", flag4)  # True
print("flag5 = ", flag5)  # True
print(flag1 is True)  # True
print(flag2 is not False)  # False
