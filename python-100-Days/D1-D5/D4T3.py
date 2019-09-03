#coding=utf-8
"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
"""

def print1(n):
    for i in range(1,n):
        for j in range(n,n-i,-1):
            print("*", end="")
        print("")
print1(6)
print("")


def print2(n):
    for i in range(1,n):
        for j in range(1,n):
            if((n-j)>i):
                print(' ', end="")
            else:
                print('*', end="")
        print("")
print2(6)
print("")

def print3(n):
    for i in range(1,n):
        for j in range(1,2*n-1):
            if(j<=n-i):
                print(' ', end="")
            elif(j>=n+i):
                continue
            else:
                print('*', end="")
        print("")
print3(6)