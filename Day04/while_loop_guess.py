'''
猜数字游戏

@author: kakakeven
'''

import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    guess = int(input("请输入: "))
    if guess > answer:
        print("小一点！")
    elif guess < answer:
        print("大一点！")
    else:
        print("恭喜你，猜对了！")
        break
print('你一共猜了 %d 次' % counter)
if counter > 7:
    print("你的智商余额明显已不足！")
