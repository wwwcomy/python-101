import re
try:
    with open("test.html", "r") as htmlFile:
        lines = htmlFile.readlines()
        wholeTest = ' '.join(lines)
        #print (wholeTest)
        # Seems match only return the last match...
        #pattern = re.compile('.*href="(.+?)"', re.M|re.I|re.DOTALL)
        #matches = pattern.match(wholeTest)
        #if(matches):
        #    print (matches.groups())
        #else:
        #    print ("No Matches")

        result = re.findall('.*href="(.+?)"', wholeTest)
        print (result)
except IOError as err:
    print(str(err))

