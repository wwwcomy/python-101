import re
arr = []
try:
    with open("filtered_words.txt", "r") as htmlFile:
        arr = htmlFile.read().splitlines()
except IOError as err:
    print(str(err))
print (arr)

# index will throw exception if there's no match
inputStr = input()
tmpStr = inputStr;
for s in arr:
    if(inputStr.find(s)>-1):
        tmpStr = tmpStr.replace(s,'**')

print(tmpStr)
