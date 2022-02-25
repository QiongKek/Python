"""
两个print为什么换行输出
print('输出内容'，end="\n")

在python中，print(),默认自带end="\n"这个换行结束符，所以导致每两个print直接会换行展示，用户可以按需求更改结束符

"""
# print('ss')print('ss') 错误，一行中出现两个print


print('hello', end="\n")  # ctrl 加 d 直接复制此行
print('world', end="\t")
print('hello', end="...")  # end="", 可以去写这些转义字符作为结束符号，也可以去写任意的我们需求的标点去做结束链接符号
print('Python')


