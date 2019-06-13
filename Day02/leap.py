"""
输入年份，判断是否为闰年

@author: kakakeven
"""
year = int(input("请输入年份: "))
is_leap = ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 3200 != 0))
print(is_leap)
