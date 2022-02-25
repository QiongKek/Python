"""
1. input
2. 检测input数据类型str
3. int()转换数据类型
4. 检测是否转换成功
"""
num = input("请输入数字：")
print(num)

print(type(num))  # str数据类型

print(type(int(num)))  # 转换为int类型
