# print默认是打印一行，结尾加换行。end=' '意思是末尾不换行，加空格。
for i in range(3):
    print(i, end=",")
print("----------")
for i in range(3):
    print(i)
print("----------")
for i in range(2):
    print(i, end="")
else:
    print(0)
print("----------")

