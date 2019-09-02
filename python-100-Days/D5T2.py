import math

# find the Perfect number 完全数

def getDivisor(s):
    result = []
    for i in range(1,s):
        if(s%i==0):
            result.append(i)
    return result

result = []
for i in range(1,10000):
    divisors = getDivisor(i)
    tmpAcc = 0
    for s in divisors:
        tmpAcc += s
    if tmpAcc == i:
        result.append(i)

print(result)