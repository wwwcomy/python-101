
import math

def do(input1, input2):
    minNum = min(input1,input2)
    for i in range(minNum,2,-1):
        if(input1%i==0 and input2%i==0):
            print("Great common divisor:" + str(i))
            break

    maxNum = max(input1,input2)
    while True:
        maxNum +=1
        if(maxNum%input1==0 and maxNum%input2==0):
            print("Least common multiple:" + str(maxNum))
            break;



do(4,5)
do(111,334)
do(128,64)
do(772,96)