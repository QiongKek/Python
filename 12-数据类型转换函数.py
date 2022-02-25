# 1.float() -- 将数据转换成浮点类型
num1 = 1
str1 = '10'

print(type(float(num1)))  # 转换为float类型

print(num1)  # 1
print(float(num1))  # 1.0

print(float(str1))  # 10.0

# 2.str() -- 将数据转换成字符串型
print(type(str(num1)))  # 转换为str类型


"""
序列指的是数据依次排列的数据结构，包括列表、元组、集合、字典
"""
# 3.tuple() -- 将一个序列转换成元组
list1 = [10, 20, 300]  # 列表序列
print(tuple(list1))

# 4.list() -- 将一个序列转换成列表
t1 = (100, 200, 300)  # 元组序列
print(list(t1))

# 5.eval() --计算字符串中的有效python表达式，并返回一个对象
str2 = '1'
str3 = '1.1'
str4 = '(1000,2000,3000)'
str5 = '[1000,2000,3000]'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))

# eval的作用就是把字符串里面的数据转换成它原本的类型

print(eval(str2))
print(eval(str3))

print(str2)
print(str3)


"""
总结：
    int()   转换为整型
    float() 转换为浮点型
    str()   转换为字符串类型
    list()  转换为列表类型
    tuple() 转换为元组类型
    eval()  转换为它原本的类型
"""
