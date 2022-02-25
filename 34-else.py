"""

循环可以和else配合使⽤，else下⽅缩进的代码指的是当循环正常结束之后要执⾏的代码

while...else... :
while 条件:
    条件成⽴重复执⾏的代码
else:
    循环正常结束之后要执⾏的代码
else指的是循环正常结束之后要执⾏的代码，即
如果是break终⽌循环的情况，else下⽅缩进的代码将不执⾏。

continue是退出当前⼀次循环，继续下⼀次循环，所以该循环在continue控制下是可以正常
结束的，当循环结束后，则执⾏了else缩进的代码


for...else... :
for 临时变量 in 序列:
    重复执⾏的代码
    ...
else:
    循环正常结束之后要执⾏的代码


    所谓else指的是循环正常结束之后要执⾏的代码，即如果是break终⽌循环的情况，else下⽅缩进
的代码将不执⾏。
    因为continue是退出当前⼀次循环，继续下⼀次循环，所以该循环在continue控制下是可以正常
结束的，当循环结束后，则执⾏了else缩进的代码。

"""

# for...else
str1 = 'itheima'
for i in str1:
    print(i)
else:
    print('循环正常结束之后执⾏的代码')
print()
# 退出循环的⽅式
# 1. break终⽌循环
str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        break
    print(i)
else:
    print('循环正常结束之后执⾏的代码')  # 没有执⾏else缩进的代码

print()
#  2. continue控制循环
str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        continue
    print(i)
else:
    print('循环正常结束之后执⾏的代码')
