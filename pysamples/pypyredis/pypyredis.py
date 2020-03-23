#!/usr/bin/env python3

import redis


def getConn():
    conn = redis.Redis(
        host="127.0.0.1",
        port=6379,
        decode_responses=True,
        password="roottest",
    )
    return conn


def setKey(key, value):
    conn = getConn()
    conn.set(key, value)


def getKey(key):
    conn = getConn()
    value = conn.get(key)
    return value


if __name__ == "__main__":
    setKey("张三", "管理员")
    print(getKey("张三"))
