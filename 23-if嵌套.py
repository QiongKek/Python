"""
语法:
if 条件1：
    条件1成⽴执⾏的代码
    条件1成⽴执⾏的代码

    if 条件2：
        条件2成⽴执⾏的代码
        条件2成⽴执⾏的代码
注意：条件2的if也是出于条件1的缩进关系内部。

"""

"""
1. 如果有钱，则可以上⻋
2. 上⻋后，如果有空座，可以坐下
   上⻋后，如果没有空座，则站着等空座位
   如果没钱，不能上⻋
"""

"""
1. 如果有钱，则可以上⻋
 2. 上⻋后，如果有空座，可以坐下
 上⻋后，如果没有空座，则站着等空座位
如果没钱，不能上⻋
"""
# 假设⽤ money = 1 表示有钱, money = 0表示没有钱; seat = 1 表示有空座，seat = 0 表示没有空座
money = 0
seat = 0
ss = 1

if money == 1:
    print('⼟豪，不差钱，顺利上⻋')
    if seat == 1:
        print('有空座，可以坐下')
    else:
        print('没有空座，站等')
else:
    print('没钱，不能上⻋，追着公交⻋跑')
    if ss == 1:
        print('牛逼')
