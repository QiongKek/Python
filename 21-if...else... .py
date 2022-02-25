# if...else...
# 作⽤：条件成⽴执⾏if下⽅的代码; 条件不成⽴执⾏else下⽅的代码。
"""
if 条件:
 条件成⽴执⾏的代码1
 条件成⽴执⾏的代码2
 ......
else:
 条件不成⽴执⾏的代码1
 条件不成⽴执⾏的代码2
 ......

"""

# 实⽤版：⽹吧上⽹

age = int(input('请输⼊您的年龄：'))
if age >= 18:
    print(f'您的年龄是{age},已经成年，可以上⽹')
else:
    print(f'您的年龄是{age},未成年，请⾃⾏回家写作业')

print('系统关闭')

# 注意：如果某些条件成⽴执⾏了相关的代码，那么其他的情况的代码解释器根本不会执⾏。
