"""
1 使用 input 函数获取输入
2 使用 int() 进行类型转换
3 使用占位符格式化输出

@author kakakeven
"""
a = int(input('a = '))
b = int(input('b = '))

print('%d + %d = %d' % (a, b, (a + b)))  # 运行结果: 3  + 4 = 7
print('%d - %d = %d' % (a, b, (a - b)))
print('%d * %d = %d' % (a, b, (a * b)))
print('%d / %d = %d' % (a, b, (a / b)))
print('%d // %d = %d' % (a, b, (a // b)))
print('%d %% %d = %d' % (a, b, (a % b)))
print('%d ** %d = %d' % (a, b, (a ** b)))
