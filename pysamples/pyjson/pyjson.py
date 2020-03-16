#!/usr/bin/env python3
import json
import requests

"""
dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象
"""


def loadsAndDump():
    resp = requests.get(
        "https://dncapi.bqiapp.com/api/config/ad?appid=1&channelcode=daohang&webp=0")
    dataDict = json.loads(resp.text)
    for ad in dataDict["data"][0]["ads"]:
        print(ad)

    with open("./ads.json", "w", encoding="utf-8") as f1:
        json.dump(dataDict, f1)


def loadAndDumps():
    with open("./ads.json", "r", encoding="utf-8") as f1:
        dataDict = json.load(f1)
        print(dataDict["data"][0]["ads"][0])
        dataStr = json.dumps(dataDict)
        print(dataStr)


if __name__ == "__main__":
    loadsAndDump()
    loadAndDumps()
