"""
==  判断相等。如果两个操作数的结果相等，则条件结         如a=3,b=3，则（a == b) 为 True
    果为真(True)，否则条件结果为假(False)

!=  不等于 。如果两个操作数的结果不相等，则条件为        如a=3,b=3，则（a == b) 为 True
    真(True)，否则条件结果为假(False)                如a=1,b=3，则(a != b) 为 True


>   运算符左侧操作数结果是否⼤于右侧操作数结果，         如a=7,b=3，则(a > b) 为 True
    如果⼤于，则条件为真，否则为假

<   运算符左侧操作数结果是否⼩于右侧操作数结果，        如a=7,b=3，则(a < b) 为 False
    如果⼩于，则条件为真，否则为假

>=  运算符左侧操作数结果是否⼤于等于右侧操作数结        如a=7,b=3，则(a < b) 为 False
    果，如果⼤于，则条件为真，否则为假                如a=3,b=3，则(a >= b) 为 True

<=  运算符左侧操作数结果是否⼩于等于右侧操作数结       如a=3,b=3，则(a <= b) 为 True
    果，如果⼩于，则条件为真，否则为假

"""

a = 7
b = 5
print(a == b)  # False
print(a != b)  # True
print(a < b)   # False
print(a > b)   # True
print(a <= b)  # False
print(a >= b)  # True
