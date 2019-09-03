
import math
'''
Is Prime Number
'''
def is_prime(input):
    if(input==2):
        return True
    if(input%2==0):
        return False
    for i in range (3,int(math.sqrt(input))+1,2):
        if(input%i==0):
            return False
    return True

for i in range (2,100):
    if(is_prime(i)):
        print i