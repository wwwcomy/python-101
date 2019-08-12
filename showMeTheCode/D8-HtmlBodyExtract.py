import re
try:
    with open("test.html", "r") as htmlFile:
        lines = htmlFile.readlines()
        wholeTest = ' '.join(lines)
        print(re.sub('\n\s+\n+','\n',re.sub('<.*?>','',wholeTest)))
except IOError as err:
    print(str(err))

