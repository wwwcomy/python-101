import re
arr = []
try:
    with open("filtered_words.txt", "r") as htmlFile:
        arr = htmlFile.read().splitlines()
except IOError as err:
    print(str(err))
print (arr)

inputStr = input()
for s in arr:
    if(s in inputStr):
        print('Freedom')
        exit(1)

print('Human Right')
