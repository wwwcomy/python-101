#import requests
#import xml.etreeElementTree as ET

# s = 'I love China!   '
# arr_s = s.split(' ')
# print(arr_s)
# output=[]
# for seg in arr_s:
#     output.insert(0,seg)
# print(' '.join(output))

s = 'I love China!   '
arr_s = s.split(' ')
print(arr_s)
output=[]
for seg in range(len(arr_s)-1,-1,-1):
    output.append(arr_s[seg])
print(' '.join(output))

import math
result = []
for i in range(3,100,2):
    match = True
    for j in range (3, int(math.sqrt(i)+1)):
        if(i%j==0):
            match=False
    if(match):
        result.append(i)
print(result)


def func(x,y,z=3,d=4,s=8,e=7):
    return x,y,z,d,s,e;
print(func(1,2,e=6,s=12))

print('-------')
def func1(a,b,*c):
    if(not c):
        return a,b
    else:
        return a,b,c
print(func1(1,2))
print(func1(1,2,3))

def hanoi(n,a,b,c):
    if(n==1):
        print(a+'-->'+b)
    else:
        hanoi(n-1,a,c,b)
        print(a+'-->'+b)
        hanoi(n-1,c,b,a)

hanoi(4,'a','b','c')