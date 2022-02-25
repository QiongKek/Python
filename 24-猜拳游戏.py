# 导⼊random模块
import random

fist = 0  # 拳头
scissors = 1  # 剪刀
cloth = 2  # 布

computer = random.randint(0, 2)
print('请玩家出拳：0-拳头、1-剪刀、2-布')
player = int(input())
if player == fist:
    if computer == fist:
        print(f'{computer} 平局')
    elif computer == scissors:
        print(f'{computer} 玩家获胜')
    elif computer == cloth:
        print(f'{computer} 电脑获胜')
elif player == scissors:
    if computer == fist:
        print(f'{computer} 电脑获胜')
    elif computer == scissors:
        print(f'{computer} 平局')
    elif computer == cloth:
        print(f'{computer} 玩家获胜')
elif player == cloth:
    if computer == fist:
        print(f'{computer} 玩家获胜')
    elif computer == scissors:
        print(f'{computer} 电脑获胜')
    elif computer == cloth:
        print(f'{computer} 平局')
else:
    print('输入错误')

"""
提示：0-⽯头，1-剪⼑，2-布
1. 出拳
玩家输⼊出拳
电脑随机出拳
2. 判断输赢
玩家获胜
平局
电脑获胜
"""

# 计算电脑出拳的随机数字
computer1 = random.randint(0, 2)
player1 = int(input('请出拳：0-⽯头，1-剪⼑，2-布：'))
print(computer1)
# 玩家胜利 p0:c1 或 p1:c2 或 p2:c0
if ((player1 == 0) and (computer1 == 1)) or ((player1 == 1) and (computer1 == 2)) or (
        (player1 == 2) and (computer1 == 0)):
    print('玩家获胜')
# 平局：玩家 == 电脑
elif player1 == computer1:
    print('平局')
else:
    print('电脑获胜')
