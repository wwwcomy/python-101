def sanitize(time_string):
    arr = []
    for s in time_string:
        clean_txt = str(s).replace(':','.').replace('-','.');
        if(clean_txt not in arr):
            arr.append(clean_txt)
    return arr


def sanitize1(time_arr):
    return [str(s).replace(':','.').replace('-','.') for s in time_arr]

arr=[]
try:
    with open("james.txt","r") as james:
        arr=james.readline().strip().split(",")
except IOError as err:
    print(str(err))
arr1 = sanitize(arr)
print(sorted(arr1))
arr1.sort()
print(arr1[0:100])


