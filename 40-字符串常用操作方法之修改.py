"""
replace()：替换

语法:
    字符串序列.replace(旧⼦串, 新⼦串, 替换次数)
注意：替换次数可以不写，如果不写，则替换全部次数

# 2.split(): -- 按照指定字符分割字符串，分割返回一个列表

语法：
    字符串序列.split(分割字符, num)
注意：num表示分割的次数，将来返回数据个数为num+1个

3.join()
    用来连接的字符或⼦串.join(多字符串组成的序列)

"""

mystr = "hello world and itcast and itheima and Python"

# 1.replace()  把and换成he
new_str = mystr.replace('and', 'he')  # **说明replace函数有返回值，返回值是修改后的字符串
print(mystr)
print(new_str)
print(mystr.replace('world', '88'))
# 替换次数如果超出字串出现的次数，表示替换所有这个字串
print(mystr.replace('and', 'or', 100))
# 调用replace函数后，原有字符串的数据并没有得到修改，修改后的数据是replace函数的返回值
# ---说明 字符串是不可变数据类型
# 数据类型根据数据是否可以改变划分为两大类  分别为：可变类型 和 不可变类型

# 2.split() -- 分割，返回一个列表，丢失分割字符
# 分割后则丢失该⼦串。

list1 = mystr.split('and')
print(list1)

print(list1[1])  # 返回数据个数为num+1个

# 分割字符不在字符串中则不分割，但返回一个列表
print(mystr.split('牛逼', 2))

# 超过分割符出现的次数只分割字符串中分全部的割符符
a = mystr.split('and', 500000)


# 3.join() --合并列表里面的字符串数据为一个大字符串,将一列表返回一个字符串
mylist = ['aa', 'bb', 'cc']
"""

用来连接的字符或⼦串.join(多字符串组成的序列)
"""
# 将['aa', 'bb', 'cc']修改为aa...bb...cc
new_str2 = '...'.join(mylist)
print(new_str2)
