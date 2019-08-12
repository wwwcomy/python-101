import re
import os

dict = {}
def loopDir(path,dict):
    files= os.listdir(path)
    for file in files: #遍历文件夹
        wholePath = path + "/" + file
        if os.path.isdir(wholePath):
            loopDir(wholePath, dict)
        else:
            analyzeJavaCode(wholePath, dict)

def analyzeJavaCode(wholePath, dict):
    if not wholePath.endswith(".java"):
        return
    try:
        with open(wholePath, "r") as article:
            innerDict = {}
            commentOutLine = 0
            code = 0
            blankLine = 0
            commentLine = 0
            commentStart = False
            for line in article:
                stripLine = line.strip()
                if commentStart and not stripLine.endswith("*/"):
                    commentLine += 1
                    continue;
                elif stripLine.endswith("*/"):
                    commentLine += 1
                    commentStart = False
                    continue

                if ''==stripLine:
                    blankLine+=1
                elif stripLine.startswith("//"):
                    commentOutLine+=1
                elif stripLine.startswith("/*"):
                    commentLine += 1
                    commentStart = True
                else:
                    code+=1
            dict[wholePath]={}
            dict[wholePath]['commentOutLine'] = commentOutLine
            dict[wholePath]['blankLine'] = blankLine
            dict[wholePath]['commentLine'] = commentLine
            dict[wholePath]['code'] = code
    except IOError as err:
        print(str(err))

path = "/Users/xingnliu/github/poi_test/src"
loopDir(path,dict)

print(dict)