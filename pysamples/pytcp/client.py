#!/usr/bin/env python3
from socket import socket

def main():
    client = socket() # 默认使用IPV4和TCP协议
    client.connect(("127.0.0.1", 8080))
    print(client.recv(1024).decode("utf-8"))
    client.close()

if __name__ == "__main__":
    main()