import MySecond
MySecond.print1(['a','b'])
MySecond.print2()
try:
    with open('1.txt', encoding='utf-8') as theFile:
        print(theFile.readline(), end='')
        print(theFile.readline(), end='')
        theFile.seek(0)
        for line in theFile:
            print(line, end='')
except:
    print("Failed to open file")