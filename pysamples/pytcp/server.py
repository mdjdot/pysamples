#!/usr/bin/env python3

from socket import socket
from socket import SOCK_STREAM
from socket import AF_INET
from datetime import datetime


def main():
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(("127.0.0.1", 8080))
    server.listen(512)
    print("Server started and listening")
    while True:
        conn, addr = server.accept()
        print(addr)
        conn.send(str(datetime.now()).encode("utf-8"))
        conn.close()


if __name__ == "__main__":
    main()
"""
telnet 127.0.0.1 8080

Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
2020-03-17 16:50:09.420835Connection closed by foreign host.
"""
