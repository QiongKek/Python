# 应⽤⼀：计算1 - 100累加和
# 1-100的累加和，即1 + 2 + 3 + 4 +….，即前两个数字的相加结果 + 下⼀个数字( 前⼀个数字 +1).

# 方法1：
i = 1
result = 0

while i <= 100:
    result += i
    i += 1
print(result)  # 5050

# 应⽤⼆：计算1-100偶数累加和

j = 1
result2 = 0
while j <= 100:
    if j % 2 == 0:
        result2 += j
    j += 1
print(result2)  # 2250

# 方法2

k = 0  # 若从1开始是奇数的和
result3 = 0
while k <= 100:
    result3 += k
    k += 2
print(result3)
