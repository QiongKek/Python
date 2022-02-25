"""
三⽬运算符也叫三元运算符或三元表达式。
语法如下：
    条件成⽴执⾏的表达式 if 条件 else 条件不成⽴执⾏的表达式



"""
a = 1
b = 2
c = a if a > b else b
print(c)

# 需求：有两个变量，比较大小，如果变量1 大于 变量2 执行 变量1 - 变量2；否则 变量2 - 变量1
print('请输入变量1:')
aa = int(input())
print('请输入变量2:')
bb = int(input())
cc = aa - bb if aa > bb else bb-aa
print(cc)

