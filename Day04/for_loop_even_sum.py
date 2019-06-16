'''
计算 100 以内奇数/偶数的和

@author kakakeven
'''
even_sum = 0
odd_sum = 0
for x in range(2, 101, 2):
    even_sum += x
for x in range(1,101,2):
    odd_sum += x
print("100 以内偶数的和: ", even_sum)
print("100 以内奇数的和: ", odd_sum)
