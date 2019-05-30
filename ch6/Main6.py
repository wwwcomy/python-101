def sanitize(arr):
    result={}
    result['name']=arr.pop(0)
    result['dob']=arr.pop(0)
    speed=[]
    for s in arr:
        clean_txt = str(s).replace(':','.').replace('-','.');
        if(clean_txt not in speed):
            speed.append(clean_txt)
    speed.sort()
    result['speed']=speed
    return result

arr={}
try:
    with open("james2.txt","r") as james:
        arr=james.readline().strip().split(",")
except IOError as err:
    print(str(err))
arr1 = sanitize(arr)
print(arr1)

