print()
"""

r 以只读⽅式打开⽂件。⽂件的指针将会放在⽂件的开头。这是默认模式。
rb 以⼆进制格式打开⼀个⽂件⽤于只读。⽂件指针将会放在⽂件的开头。这是默认模式。
r+ 打开⼀个⽂件⽤于读写。⽂件指针将会放在⽂件的开头。
rb+ 以⼆进制格式打开⼀个⽂件⽤于读写。⽂件指针将会放在⽂件的开头。
w
打开⼀个⽂件只⽤于写⼊。如果该⽂件已存在则打开⽂件，并从开头开始编辑，即原有内
容会被删除。如果该⽂件不存在，创建新⽂件。
wb 以⼆进制格式打开⼀个⽂件只⽤于写⼊。如果该⽂件已存在则打开⽂件，并从开头开始编
辑，即原有内容会被删除。如果该⽂件不存在，创建新⽂件。
w+
打开⼀个⽂件⽤于读写。如果该⽂件已存在则打开⽂件，并从开头开始编辑，即原有内容
会被删除。如果该⽂件不存在，创建新⽂件。
wb+ 以⼆进制格式打开⼀个⽂件⽤于读写。如果该⽂件已存在则打开⽂件，并从开头开始编
辑，即原有内容会被删除。如果该⽂件不存在，创建新⽂件。
a
打开⼀个⽂件⽤于追加。如果该⽂件已存在，⽂件指针将会放在⽂件的结尾。也就是说，
新的内容将会被写⼊到已有内容之后。如果该⽂件不存在，创建新⽂件进⾏写⼊。
ab
以⼆进制格式打开⼀个⽂件⽤于追加。如果该⽂件已存在，⽂件指针将会放在⽂件的结
尾。也就是说，新的内容将会被写⼊到已有内容之后。如果该⽂件不存在，创建新⽂件进
⾏写⼊。
a+
打开⼀个⽂件⽤于读写。如果该⽂件已存在，⽂件指针将会放在⽂件的结尾。⽂件打开时
会是追加模式。如果该⽂件不存在，创建新⽂件⽤于读写。
ab+ 以⼆进制格式打开⼀个⽂件⽤于追加。如果该⽂件已存在，⽂件指针将会放在⽂件的结
尾。如果该⽂件不存在，创建新⽂件⽤于读写

"""

# r:只读   如果文件不存在，报错;且不支持写入
f = open("test.xls", 'r')
f.close()

# w:只写  如果文件不存在，则新建文件   执行写入后会覆盖原有内容
w = open('test1.xls', 'w')
w.write('bbb')
w.close()

# a:追加   如果文件不存在，则新建文件  执行写入后在原有基础上，追加新内容
g = open('test2.txt', 'a')
g.write('xdf')
g.close()

# 访问模式参数是否可以省略，如果省略表示访问模式为r
h = open('test2.txt')
h.close()
