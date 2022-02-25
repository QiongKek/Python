"""
ljust()：返回⼀个原字符串左对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度的新字符串。
语法:
    字符串序列.ljust(⻓度, 填充字符)

rjust()：返回⼀个原字符串右对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度的新字符串，
语法和ljust()相同。

center()：返回⼀个原字符串居中对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度的新字符串，
语法和ljust()相同。


"""
mystr = 'hello'
newstr = mystr.ljust(10, '.')
newstr2 = mystr.ljust(10)

print(newstr)
print(newstr2)