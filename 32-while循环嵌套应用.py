# 应用一：
# ⼀⾏输出5个星号，重复打印5⾏
"""

*****
*****
*****
*****
*****

"""
j = 0
while j < 5:
    # ⼀⾏星星的打印
    i = 0
    while i < 5:
        print('*', end=' ')  # ⼀⾏内的星星不能换⾏，取消print默认结束符\n
        i += 1
    # 每⾏结束要换⾏，这⾥借助⼀个空的print，利⽤print默认结束符换⾏
    print(end='\n')
    j += 1

# 应用二：打印星号(三⻆形
"""

*
**
***
****
*****

"""
j = 0
while j < 5:
    i = 0
    while i <= j:
        print('*', end=' ')
        i += 1
    print()
    j += 1

# 九九乘法表
j = 0
while j < 9:
    i = 0
    while i <= j:
        print(f'{i + 1}*{j + 1}={(i + 1) * (j + 1)}', end='\t')
        i += 1
    print()
    j += 1
