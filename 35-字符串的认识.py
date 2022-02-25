"""
认识字符串:
字符串是 Python 中最常⽤的数据类型。我们⼀般使⽤引号来创建字符串。创建字符串很简单，只要为
变量分配⼀个值即可。

"""
# 控制台显示结果为 <class 'str'> ， 即数据类型为str(字符串)。

# 字符串的书写方式
# 一、单引号
a = 'hello ' \
    'world'  # 中间加回车，代码换行输出的效果和不换行效果一样
print(a)
print(type(a))

# 二、双引号
b = "TO" \
    "M"  # 中间加回车，代码换行输出的效果和不换行效果一样
print(b)
print(type(b))

# 三、三引号
e = '''i 
am TOM'''  # 中间加回车，支持回车换行，并且不会添加任何的额外字符，但输出的字符是回车换行
print(e)
print(type(e))

f = """I 
AM TOM"""  # 中间加回车，支持回车换行，并且不会添加任何的额外字符，但输出的字符是回车换行
print(f)
print(type(f))

# I'm TOM
c = "I'm TOM"  # 双引号里面遇到双引号用转义字符，遇到单引号则不需要
print(c)
print(type(c))

# d = 'I'm TOM'  语法报错
d = 'I\'m TOM'  # 单引号里面遇到单引号用转义字符，遇到多引号则不需要
print(d)
print(type(d))

# 三引号里面可以有任何符号
k = '''I'm T'''
print(k)
print(type(k))

j = """I'm M"""
print(j)
print(type(j))


