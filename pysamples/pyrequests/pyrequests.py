#!/usr/bin/env python3
import json
import requests

if __name__ == "__main__":
    resp = requests.get(
        "https://dncapi.bqiapp.com/api/config/ad?appid=1&channelcode=daohang&webp=0")
    dataDict = json.loads(resp.text)
    for ad in dataDict["data"][0]["ads"]:
        print(ad)
