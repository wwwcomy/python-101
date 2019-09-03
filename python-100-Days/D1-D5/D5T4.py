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

f(10)