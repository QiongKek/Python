# 字符串的常⽤操作⽅法有查找、修改和判断三⼤类。
"""
查找:
    所谓字符串查找⽅法即是查找⼦串在字符串中的位置或出现的次数。

find()：检测某个⼦串是否包含在这个字符串中，如果在返回这个⼦串开始的位置下标，否则则返回-1。
语法:
    字符串序列.find(⼦串, 开始位置下标, 结束位置下标)
注意：开始和结束位置下标可以省略，表示在整个字符串序列中查找。

index()：检测某个⼦串是否包含在这个字符串中，如果在返回这个⼦串开始的位置下标，否则则报异常。
语法:
    字符串序列.index(⼦串, 开始位置下标, 结束位置下标)
注意：开始和结束位置下标可以省略，表示在整个字符串序列中查找。

count()：返回某个⼦串在字符串中出现的次数
语法:
    字符串序列.count(⼦串, 开始位置下标, 结束位置下标)
注意：开始和结束位置下标可以省略，表示在整个字符串序列中查找。


rfind()： 和find()功能相同，但查找⽅向为右侧开始。
rindex()：和index()功能相同，但查找⽅向为右侧开始。


"""

mystr = "hello world and itcast and itheima and Python"  # 空格也要算上，第一个下标为0

# 1.find()
print(mystr.find('and'))  # 12        它只会找到第一个子串返回
print(mystr.find('and', 15, 30))  # 23
print(mystr.find('ands'))  # -1， ands子串不存在

# 2.index()
print(mystr.index('and'))  # 12
print(mystr.index('and', 15, 30))  # 23
# print(mystr.index('ands'))  # 如果index查找子串不存在，报错

# 3.count()
print(mystr.count('and'))  # 3
print(mystr.count('ands'))  # 0
print(mystr.count('and', 0, 20))  # 1

# 4.rfind()
print(mystr.rfind('and'))  # 35
print(mystr.rfind('and', 0, 20))  # 12  ：从右开始读，范围是（0——20）
print(mystr.rfind('ands'))  # -1

# 5.rindex
print(mystr.rindex('and'))  # 35
print(mystr.rindex('and', 0, 20))  # 12  ：从右开始读，范围是（0——20）
# print(mystr.rindex('ands'))  # 报错

str2 = '张 琼 珂  珂珂珂'
print(str2.find('张'))
print(str2.count('珂'))

print(str2.count(' '))
