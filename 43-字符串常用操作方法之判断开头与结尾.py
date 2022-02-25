"""
startswith()：检查字符串是否是以指定⼦串开头，是则返回 True，否则返回 False。
            如果设置开始和结束位置下标，则在指定范围内检查。
语法：
    字符串序列.startswith(⼦串, 开始位置下标, 结束位置下标)

endswith()：检查字符串是否是以指定⼦串结尾，是则返回 True，否则返回 False。
            如果设置开始和结束位置下标，则在指定范围内检查。
语法：
    字符串序列.endswith(⼦串, 开始位置下标, 结束位置下标)
"""

mystr = "hello world and itcast and itheima and Python "
# 结果：True
print(mystr.startswith('hello'))
# 结果False
print(mystr.startswith('hello', 0, 4))  # 注意结果为false
