import uuid
arr=[]
for i in range(0,2):
    arr.append(str(uuid.uuid1()))
print(arr)