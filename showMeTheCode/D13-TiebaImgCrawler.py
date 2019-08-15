# TODO use URL lib and re
import urllib.request
import urllib.error as error
import re
import uuid

def openAndGetPic(urlSeg):
    url = "http://tieba.baidu.com" + urlSeg
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    try:
        response = urllib.request.urlopen(request)
    except error.URLError as e:
        print(str(e))
    responseTxt = response.read().decode('utf-8')
    pattern = re.compile('<img\s.*?src="(http://img.*?)"', re.M | re.I)
    picUrls = pattern.findall(responseTxt)
    print(picUrls)
    for picUrl in picUrls:
        request = urllib.request.Request(url=url, headers=headers)
        try:
            urllib.request.urlretrieve(picUrl, './img/'+str(uuid.uuid1())+'.jpg')
        except error.URLError as e:
            print(str(e))

url = "http://tieba.baidu.com/p/2166231880"
#url = "https://tieba.baidu.com/f?kw=%E5%9B%BD%E6%BC%AB&ie=utf-8&tab=main"

#mode 1
#response = urllib.request.urlopen(url)
#print(response.read().decode('UTF8'))

#mode 2, use Request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
try:
    response = urllib.request.urlopen(request)
except error.URLError as e:
    print(str(e))
responseTxt = response.read().decode('utf-8')

pattern = re.compile('<a\s.*href="(/p/\d+)"',re.M|re.I)

matches = pattern.findall(responseTxt)
print(matches)
for urlSeg in matches:
    openAndGetPic(urlSeg)