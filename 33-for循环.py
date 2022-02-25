"""
语法：

for 临时变量 in 序列:
    重复执⾏的代码1
    重复执⾏的代码2
    ......

"""

str1 = 'itheima'
for i in str1:
    print(i)

str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e跳过')
        continue
    print(i)


str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e结束打印')
        break
    print(i)
