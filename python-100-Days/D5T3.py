import math

# “百钱百鸡”问题。

for i in range(1,100):
    for j in range (1,100):
        if(i*5+3*j+(100-i-j)/3==100):
            print("i="+str(i)+",j="+str(j)+",res="+str((100-i-j)))
