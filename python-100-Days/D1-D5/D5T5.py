import math

# 生成“斐波拉切数列”。

def fibonacci(i):
    if(i==0):
        return 0
    if(i==1):
        return 1
    if(i==2):
        return 1
    return fibonacci(i-1)+fibonacci(i-2)

def f(i):
    for i in range (1,i+1):
        print(fibonacci(i))

def f2(i):
    arr = []
    if(i==0):
        return 0
    if(i==1):
        return 1
    if(i==2):
        return 1
    arr.append(1)
    arr.append(1)
    for j in range (3,i+1):
        tmpResult = arr[j-2]+arr[j-3]
        print(tmpResult)
        arr.append(tmpResult)
    return arr[i-1]
f(10)
print(f2(10))