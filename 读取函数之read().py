print()
"""
read():
    ⽂件对象.read(num)
    
num表示要从⽂件中读取的数据的⻓度（单位是字节），如果没有传⼊num，那么就表示读取⽂件中所有的数据。

readlines()

readlines可以按照⾏的⽅式把整个⽂件中的内容进⾏⼀次性读取，并且返回的是⼀个列表，其中每⼀⾏
的数据为⼀个元素。

readline()
readline()⼀次读取⼀⾏内容。



"""
f = open('读取函数测试.txt')

# print(f.read())    read()不写参数表示读取所有

print(f.read(10))  # 文件内容换行，底层有\n,会字节占位，导致read()书写参数读取出来的个数和和参数值不匹配

f.close()


w = open('读取函数测试.txt')

print(w.readlines())

w.close()

h = open('读取函数测试.txt')

print(h.readline())
print(h.readline())
print(h.readline())
h.close()
