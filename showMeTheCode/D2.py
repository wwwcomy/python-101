import uuid
#0001
arr=[]
for i in range(0,200):
    print(i)
    arr.append(str(uuid.uuid1()))
print(arr)