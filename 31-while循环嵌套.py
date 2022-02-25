"""
while 条件1:
    条件1成⽴执⾏的代码
    ......
    while 条件2:
        条件2成⽴执⾏的代码
        ......

        所谓while循环嵌套，就是⼀个while⾥⾯嵌套⼀个while的写法，
        每个while和之前的基础语法是相同的。
"""
i = 0

while i < 7:
    print('早中晚饭')
    j = 0
    while j < 2:
        print('睡午觉')
        print('睡晚觉')
        j += 1
    print('一天结束')
    i += 1



