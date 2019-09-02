# 使用 Python 实现：对着电脑吼一声,自动打开浏览器中的默认网站。
#
# 例如，对着笔记本电脑吼一声“百度”，浏览器自动打开百度首页。
#
# 关键字：Speech to Text

# pip install sounddevice
# pip install numpy scipy matplotlib
# pip install requests

import sounddevice as sd
from scipy.io.wavfile import write
import requests
import hashlib
import urllib
import base64
import time
import json


def createRecording():
    fs = 16000  # Sample rate
    seconds = 3  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    print('StartRecording...')
    sd.wait()  # Wait until recording is finished
    print('Recording Done...')
    write('output.wav', fs, myrecording)  # Save as WAV file

def createRecording1():
    fs = 16000  # Sample rate
    seconds = 3  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    print('StartRecording...')
    sd.wait()  # Wait until recording is finished
    print('Recording Done...')
    write('output.wav', fs, myrecording)  # Save as WAV file

def md5(string):
    md = hashlib.md5()
    md.update(string)
    md5 = md.hexdigest().upper()
    return md5


def urlencode(args):
    tuples = [(k, args[k]) for k in sorted(args.keys()) if args[k]]
    query_str = urllib.parse.urlencode(tuples)
    print(query_str)
    return query_str


def signify(args, app_key):
    query_str = urlencode(args)
    query_str = query_str + '&app_key=' + app_key
    signature = md5(query_str.encode())
    print(signature)
    return signature


def getAudioData():
    try:
        with open("output.wav", "rb") as wav:
            return wav.read()
    except IOError as err:
        print(str(err))


def voiceRecognotionUsingTecent():
    # TODO set the app info
    appid = 1
    appkey = ''
    url = 'https://api.ai.qq.com/fcgi-bin/aai/aai_asr'
    audio_data = getAudioData()

    args = {
        'app_id': appid,
        'time_stamp': str(int(time.time())),
        'nonce_str': 'ttt',
        'format': 2,
        'rate': 16000,
        'speech': base64.b64encode(audio_data),
    }
    signiture = signify(args, appkey)
    args['sign'] = signiture

    response = requests.post(
        url,
        data=args
    )
    print(response.json())


def voiceRecognotionUsingBaidu():
    url = 'http://vop.baidu.com/server_api'
    audio_data = getAudioData()
    speech = base64.b64encode(audio_data).decode()
    args = {
        'format': 'wav',
        'rate': 16000,
        'channel': 1,
        'cuid': 'tttXX0088QQQ',
        'token': '24.3f0468a7e8bf15badadb90d2da109738.2592000.1568727317.282335-17037646',
        'speech': speech,
        'len': len(audio_data)
    }
    header = {'Content-Type': 'application/json'}
    jsonStr = json.dumps(args)
    #print(jsonStr)
    response = requests.post(
        url,
        data=jsonStr,
        headers=header
    )
    print(response.json())


def voiceRecognotionUsingBaidu2():
    url = 'http://vop.baidu.com/server_api?cuid=tttXX0088QQQ&token=24.3f0468a7e8bf15badadb90d2da109738.2592000.1568727317.282335-17037646'
    audio_data = getAudioData()

    header = {'Content-Type': 'audio/pcm;rate=16000'}
    response = requests.post(
        url,
        data=audio_data,
        headers=header
    )
    print(response.json())


#createRecording1()
# voiceRecognotionUsingTecent()
voiceRecognotionUsingBaidu()
voiceRecognotionUsingBaidu2()
