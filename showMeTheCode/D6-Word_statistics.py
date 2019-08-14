import re
arr=[]
dict = {}
try:
    with open("Article.txt","r") as article:
        for line in article:
            arr=re.split('\W+', line.strip())
            #arr=line.strip().split('\\W+')
            for str in arr:
                stripStr = str.strip().lower()
                if(''==stripStr):
                    continue
                if(dict.get(stripStr) is None):
                    dict[stripStr] = 1
                else:
                    dict[stripStr] = dict[stripStr] +1
except IOError as err:
    print(str(err))

print(dict)
sortedDict = sorted(dict.items(),key=lambda item:item[1],reverse=True)
print(sortedDict)