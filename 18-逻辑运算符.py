"""

and   x and y   都真才真
布尔"与"：如果 x 为 False，x and y 返回False，否则它返回 y 的值.True and False， 返回False.

or    x or y    一真则真，都假才假
布尔"或"：如果 x 是 True，它返回 True，否则它返回 y 的值.False or True， 返回True.

not   not x    取反
布尔"⾮"：如果 x 为 True，返回 False. 如果 x为 False，它返回 True。not True 返回 False, not False 返回 True.


"""

a = 1
b = 2
c = 3
print((a < b) and (b < c))  # True
print((a > b) and (b < c))  # False
print((a > b) or (b < c))  # True
print(not (a > b))  # True

print(a)

# 这里你可以看到a b c 又被重新附上了新的值
a = 0
b = 1
c = 2
# and运算符，只要有⼀个值为0，则结果为0，否则结果为最后⼀个⾮0数字
print(a and b)  # 0
print(b and a)  # 0
print(a and c)  # 0
print(c and a)  # 0
print(b and c)  # 2
print(c and b)  # 1
# or运算符，只有所有值为0结果才为0，否则结果为第⼀个⾮0数字
print(a or b)  # 1
print(a or c)  # 2
print(b or c)  # 1