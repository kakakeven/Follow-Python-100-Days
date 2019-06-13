"""
1 使用 type() 来检查变量的类型
2 使用 chr() 将整数转换成对应的字符
3 使用 ord() 将字符转换成对应的整数
@author: kakakeven
"""

a = 100
b = 12.345
c = 1 + 5j
d = 'hello,world'
e = True
f = 89
g = 'A'

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>
print(type(d))  # <class 'str'>
print(type(e))  # <class 'bool'>
print(type(f), chr(f))  # <class 'int'> Y
print(type(g), ord(g))  # <class 'str'> 65
