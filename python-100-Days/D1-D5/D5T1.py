import math

# find the Narcissistic Number 水仙花数

result = []
for i in range(100,1000):
    tmpAcc = 0
    for s in str(i):
        tmpAcc += math.pow(int(s),3)
    if tmpAcc == i:
        result.append(i)

print(result)