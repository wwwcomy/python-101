import random


# Craps赌博游戏 - 两个色子
# 第一次摇色子
# 如果摇出了7点或11点 - 玩家胜
# 如果摇出了2点、3点或12点 - 庄家胜
# 如果摇出其他点数 - 游戏继续
# 继续
# 如果摇出了7点 - 庄家胜
# 如果摇出了第一次摇的点数 - 玩家胜
# 如果摇出了其他点数 - 游戏继续

def throwDice():
    return [random.randint(1, 6), random.randint(1, 6)]


def sum(arr):
    return arr[0] + arr[1]


firstResult = 0
while (True):
    a = input("Enter to play")
    dice = throwDice()
    sumResult = sum(dice)
    print(str(sumResult))
    if (firstResult == 0):
        if (sumResult == 7 or sumResult == 11):
            print("you win")
        elif (sumResult == 2 or sumResult == 3 or sumResult == 12):
            print("you lose")
        else:
            print('Next Round...')
            firstResult = sumResult
    else:
        if (sumResult == 7):
            print("you lose" + str(sumResult))
            firstResult = 0
        elif (firstResult == sumResult):
            print("you win" + str(sumResult))
            firstResult = 0
        else:
            print('Next Round...')
